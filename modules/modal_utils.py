# modules/modal_utils.py
import tkinter as tk

# Paleta de cores padrao (pode ser importada se quiser centralizar)
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#f0f0f0"
HIGHLIGHT = "#8b32f4"


def mostrar_modal_sucesso(parent, mensagem):
    modal = tk.Toplevel(parent)
    modal.title("Sucesso")
    modal.configure(bg=BG_COLOR)
    modal.geometry("340x140")
    modal.resizable(False, False)

    tk.Label(modal, text="✅ Sucesso!", font=("Segoe UI", 12, "bold"),
             fg=HIGHLIGHT, bg=BG_COLOR).pack(pady=(20, 5))

    tk.Label(modal, text=mensagem, font=("Segoe UI", 10),
             fg=TEXT_COLOR, bg=BG_COLOR, wraplength=280, justify="center").pack()

    tk.Button(modal, text="OK", bg=HIGHLIGHT, fg="white", font=("Segoe UI", 10, "bold"),
              relief="flat", command=modal.destroy, cursor="hand2").pack(pady=10)


def mostrar_modal_erro(parent, mensagem):
    modal = tk.Toplevel(parent)
    modal.title("Algo deu errado")
    modal.configure(bg=BG_COLOR)
    modal.geometry("340x140")
    modal.resizable(False, False)

    tk.Label(modal, text="❌ Erro", font=("Segoe UI", 12, "bold"),
             fg="#ff4d4d", bg=BG_COLOR).pack(pady=(20, 5))

    tk.Label(modal, text=mensagem, font=("Segoe UI", 10),
             fg=TEXT_COLOR, bg=BG_COLOR, wraplength=280, justify="center").pack()

    tk.Button(modal, text="OK", bg="#ff4d4d", fg="white", font=("Segoe UI", 10, "bold"),
              relief="flat", command=modal.destroy, cursor="hand2").pack(pady=10)
