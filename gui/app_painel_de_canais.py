import tkinter as tk
from tkinter import messagebox
import sys
import os

# 📦 Módulos externos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.channel_manager import listar_canais, excluir_canal
from modules.modal_criar_canal import abrir_modal_criar
from modules.modal_utils import mostrar_modal_sucesso
from modules.modal_editar_canal import abrir_modal_editar
from modules.modal_criar_video import abrir_modal_criar_video
from modules.modal_listar_videos import abrir_modal_listar_videos

# 🎨 Paleta de Cores
BG_COLOR = "#1e1e1e"
CARD_COLOR = "#2a2a2a"
FRAME_COLOR = "#2c2c2c"
BTN_COLOR = "#383838"
BTN_HOVER = "#4b4b4b"
TEXT_COLOR = "#f0f0f0"
SUBTEXT_COLOR = "#bbbbbb"
HIGHLIGHT = "#8b32f4"
DANGER = "#ff4d4d"

# 🪟 Janela Principal
janela = tk.Tk()
janela.title("VideoForge Lite - Painel de Conteúdo")
janela.geometry("520x580")
janela.configure(bg=BG_COLOR)
janela.resizable(False, False)

# 🔠 Título + Botão de vídeo
header_frame = tk.Frame(janela, bg=BG_COLOR)
header_frame.pack(fill="x", pady=(25, 5), padx=20)

tk.Label(header_frame, text="Painel de Conteúdo", font=("Segoe UI", 20, "bold"),
         fg=HIGHLIGHT, bg=BG_COLOR).pack(side="left")

btn_novo_video = tk.Button(header_frame, text="➕", font=("Segoe UI", 14),
                           fg=HIGHLIGHT, bg=BG_COLOR, relief="flat", cursor="hand2",
                           command=lambda: abrir_modal_criar_video(janela))
btn_novo_video.pack(side="right")

tk.Label(janela, text="Gerencie seus canais com facilidade", font=("Segoe UI", 11),
         fg=SUBTEXT_COLOR, bg=BG_COLOR).pack()

# 📋 Área de Listagem
frame_lista = tk.Frame(janela, bg=BG_COLOR)
frame_lista.pack(padx=20, pady=20, fill="both", expand=True)

# 🧨 Modal de confirmação de exclusão
def confirmar_exclusao_customizado(parent, canal_id, nome_canal, on_confirm):
    modal = tk.Toplevel(parent)
    modal.title("Confirmar Exclusão")
    modal.configure(bg=BG_COLOR)
    modal.geometry("360x180")
    modal.resizable(False, False)

    tk.Label(modal, text="Digite o nome do canal para confirmar:", font=("Segoe UI", 10),
             fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=(20, 5))
    tk.Label(modal, text=f"⚠️ {nome_canal}", fg=DANGER, bg=BG_COLOR,
             font=("Segoe UI", 11, "bold")).pack()

    entrada = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR,
                       insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entrada.pack(padx=20, pady=(10, 0), fill="x")

    def confirmar():
        texto = entrada.get().strip()
        if texto.lower() != nome_canal.lower():
            messagebox.showwarning("Nome incorreto", "O nome digitado não corresponde ao canal.")
            return
        modal.destroy()
        on_confirm(canal_id)
        mostrar_modal_sucesso(parent, f"Canal '{nome_canal}' removido com sucesso.")

    tk.Button(modal, text="Excluir", bg=DANGER, fg="white", font=("Segoe UI", 10, "bold"),
              relief="flat", command=confirmar, cursor="hand2").pack(pady=15)

# 🔁 Atualiza a lista de canais
def atualizar_lista():
    for widget in frame_lista.winfo_children():
        widget.destroy()

    canais = listar_canais()
    if not canais:
        tk.Label(frame_lista, text="Nenhum canal encontrado.", font=("Segoe UI", 11),
                 fg=SUBTEXT_COLOR, bg=BG_COLOR).pack(pady=20)
        return

    for canal in canais:
        id_, nome, idioma = canal
        container = tk.Frame(frame_lista, bg=CARD_COLOR, padx=10, pady=10)
        container.pack(fill="x", pady=8)

        info = tk.Label(container, text=f"{nome}  •  {idioma}",
                        font=("Segoe UI", 11, "bold"), fg=TEXT_COLOR, bg=CARD_COLOR)
        info.pack(side="left", anchor="w")

        info.bind("<Double-Button-1>", lambda e, cid=id_, nome=nome: abrir_modal_listar_videos(janela, cid, nome))

        btn_excluir = tk.Button(container, text="🗑", font=("Segoe UI", 10),
                                bg=CARD_COLOR, fg=DANGER, relief="flat", cursor="hand2",
                                command=lambda cid=id_, nome=nome: confirmar_exclusao_customizado(
                                    janela, cid, nome,
                                    lambda c: [excluir_canal(c), atualizar_lista()]
                                ))
        btn_excluir.pack(side="right", padx=4)

        btn_editar = tk.Button(container, text="✏", font=("Segoe UI", 10),
                               bg=CARD_COLOR, fg=HIGHLIGHT, relief="flat", cursor="hand2",
                               command=lambda cid=id_: abrir_modal_editar(
                                   janela, cid, atualizar_lista, mostrar_modal_sucesso))
        btn_editar.pack(side="right")

# ➕ Botão "Criar Canal"
frame_botao = tk.Frame(janela, bg=BG_COLOR)
frame_botao.pack(pady=(0, 20))

btn_novo = tk.Button(frame_botao, text="➕  Criar Canal", font=("Segoe UI", 11),
                     fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=BTN_HOVER,
                     relief="flat", bd=0, highlightthickness=0, cursor="hand2",
                     command=lambda: abrir_modal_criar(janela, atualizar_lista, mostrar_modal_sucesso))
btn_novo.pack()

# 🚀 Inicialização
atualizar_lista()
janela.mainloop()
