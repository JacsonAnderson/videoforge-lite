import tkinter as tk
from tkinter import messagebox
from modules.channel_manager import criar_canal
from modules.modal_utils import mostrar_modal_sucesso, mostrar_modal_erro



# Paleta de cores padrão (pode importar de outro lugar futuramente)
BG_COLOR = "#1e1e1e"
FRAME_COLOR = "#2c2c2c"
TEXT_COLOR = "#f0f0f0"
HIGHLIGHT = "#8b32f4"

def abrir_modal_criar(parent, callback_atualizar, callback_sucesso=None):
    modal = tk.Toplevel(parent)
    modal.title("Novo Canal")
    modal.configure(bg=BG_COLOR)
    modal.geometry("400x520")
    modal.resizable(False, False)

    def criar_input(label, widget):
        tk.Label(modal, text=label, fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w", padx=20, pady=(10, 0))
        widget.pack(padx=20, fill="x")

    entry_nome = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entry_idioma = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entry_min_chars = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entry_voice = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entry_watermark = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entry_music = tk.Entry(modal, bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=("Segoe UI", 10), relief="flat")
    entry_prompt = tk.Text(modal, height=4, bg=FRAME_COLOR, fg=TEXT_COLOR, font=("Segoe UI", 10), relief="flat", insertbackground=TEXT_COLOR)

    criar_input("Nome do Canal", entry_nome)
    criar_input("Idioma", entry_idioma)
    criar_input("Mínimo de caracteres no prompt", entry_min_chars)
    criar_input("Modelo de voz", entry_voice)
    criar_input("Marca d'água", entry_watermark)
    criar_input("Música de fundo", entry_music)
    tk.Label(modal, text="Prompt Base", fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w", padx=20, pady=(10, 0))
    entry_prompt.pack(padx=20, fill="x")

    def salvar():
        nome = entry_nome.get().strip()
        idioma = entry_idioma.get().strip()
        prompt = entry_prompt.get("1.0", "end").strip()
        min_chars = entry_min_chars.get().strip()
        voice = entry_voice.get().strip() or None
        watermark = entry_watermark.get().strip() or None
        music = entry_music.get().strip() or None

        if not nome or not idioma or not prompt:
            mostrar_modal_erro(modal, "Você precisa preencher nome, idioma e prompt para continuar.")
            return

        try:
            min_chars_int = int(min_chars) if min_chars else None
        except ValueError:
            mostrar_modal_erro(modal, "O campo 'mínimo de caracteres' precisa ser um número.")
            return


        canal_id = nome.lower().replace(" ", "_")[:16]

        try:
            criar_canal(canal_id, nome, idioma, prompt, min_chars_int, voice, watermark, music)
            modal.destroy()
            callback_atualizar()
            if callback_sucesso:
                callback_sucesso(parent, f"Canal '{nome}' criado com sucesso.")
            else:
                messagebox.showinfo("Sucesso", f"Canal '{nome}' criado com sucesso.")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    tk.Button(modal, text="Salvar", bg=HIGHLIGHT, fg="white", font=("Segoe UI", 10, "bold"),
              relief="flat", command=salvar, cursor="hand2").pack(pady=20)
