import tkinter as tk
import secrets
from tkinter import ttk, messagebox
from modules.channel_manager import listar_canais
from modules.video_manager import criar_video

# 🎨 Paleta de cores
BG_COLOR = "#1e1e1e"
FRAME_COLOR = "#2c2c2c"
TEXT_COLOR = "#f0f0f0"
HIGHLIGHT = "#8b32f4"

def abrir_modal_criar_video(parent, callback_atualizar=None):
    modal = tk.Toplevel(parent)
    modal.title("Criar Vídeo")
    modal.configure(bg=BG_COLOR)
    modal.geometry("620x480")
    modal.resizable(False, False)

    tk.Label(modal, text="Selecionar Canal", fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w", padx=20, pady=(15, 0))

    canais = listar_canais()
    canais_dict = {f"{nome} ({idioma})": (id_, nome) for id_, nome, idioma in canais}
    opcoes_canais = list(canais_dict.keys())

    canal_selecionado = tk.StringVar()
    canal_dropdown = ttk.Combobox(modal, values=opcoes_canais, textvariable=canal_selecionado, state="readonly")
    canal_dropdown.pack(padx=20, fill="x")
    if opcoes_canais:
        canal_dropdown.current(0)

    # Quantidade de vídeos
    tk.Label(modal, text="Quantidade de Vídeos", fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w", padx=20, pady=(15, 0))
    qtd_var = tk.IntVar(value=1)
    qtd_dropdown = ttk.Combobox(modal, values=list(range(1, 11)), textvariable=qtd_var, state="readonly")
    qtd_dropdown.pack(padx=20, fill="x")

    frame_links = tk.Frame(modal, bg=BG_COLOR)
    frame_links.pack(padx=20, pady=10, fill="both", expand=True)

    inputs_links = []

    def render_inputs():
        for widget in frame_links.winfo_children():
            widget.destroy()
        inputs_links.clear()

        for i in range(qtd_var.get()):
            tk.Label(frame_links, text=f"Link do Vídeo {i + 1}", fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w", pady=(5, 0))
            entrada = tk.Entry(frame_links, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
            entrada.pack(fill="x", pady=(0, 5))
            inputs_links.append(entrada)

    qtd_dropdown.bind("<<ComboboxSelected>>", lambda e: render_inputs())
    render_inputs()

    def salvar():
        canal_info = canal_selecionado.get()
        if not canal_info:
            messagebox.showwarning("Atenção", "Você precisa selecionar um canal.")
            return

        channel_id, channel_name = canais_dict[canal_info]

        for i, entrada in enumerate(inputs_links, start=1):
            link = entrada.get().strip()
            if not link:
                continue
            video_id = secrets.token_hex(4)
            try:
                criar_video(video_id, channel_id, channel_name, i, link)
            except Exception as e:
                messagebox.showerror("Erro ao criar vídeo", str(e))
                return

        modal.destroy()
        if callback_atualizar:
            callback_atualizar()
        messagebox.showinfo("Sucesso", "Vídeo(s) criado(s) com sucesso!")

    tk.Button(modal, text="Criar Vídeo(s)", bg=HIGHLIGHT, fg="white", font=("Segoe UI", 10, "bold"),
              relief="flat", command=salvar, cursor="hand2").pack(pady=10)
