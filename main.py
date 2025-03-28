import tkinter as tk
import subprocess

# Paleta de cores estilo Notion/ClickUp Dark
BG_COLOR = "#1e1e1e"
FRAME_COLOR = "#262626"
BTN_COLOR = "#2e2e2e"
BTN_HOVER = "#3c3c3c"
TEXT_COLOR = "#f3f3f3"
HIGHLIGHT = "#8b32f4"

# Função para abrir apps
def abrir_app(script):
    subprocess.Popen(["python", f"gui/{script}"])

# Hover visual
def on_enter(e):
    e.widget["background"] = BTN_HOVER

def on_leave(e):
    e.widget["background"] = BTN_COLOR

# Janela principal
janela = tk.Tk()
janela.title("VideoForge Lite")
janela.geometry("420x580")
janela.configure(bg=BG_COLOR)
janela.resizable(False, False)

# Título estilizado
titulo = tk.Label(
    janela, text="VideoForge Lite", font=("Segoe UI", 20, "bold"),
    fg=HIGHLIGHT, bg=BG_COLOR, pady=10
)
titulo.pack(pady=(30, 10))

subtitulo = tk.Label(
    janela, text="Escolha uma função abaixo", font=("Segoe UI", 11),
    fg="#cccccc", bg=BG_COLOR
)
subtitulo.pack()

# Frame centralizado para os botões
frame = tk.Frame(janela, bg=FRAME_COLOR, bd=0, relief="flat")
frame.pack(pady=30, padx=20, fill="both", expand=True)

# Botões
botoes = [
    ("📂  Painel de Conteúdo", "app_conteudo.py"),
    ("📝  Gerar Roteiro", "app_roteiro.py"),
    ("🎤  Gerar Áudio", "app_audio.py"),
    ("🎞️  Gerar Vídeo", "app_video.py"),
    ("🔤  Legendar Vídeo", "app_legenda.py"),
    ("🖼️  Gerar Thumb", "app_thumb.py"),
    ("🧠  Gerar Metadados", "app_metadados.py")
]

for texto, script in botoes:
    btn = tk.Button(
        frame, text=texto, font=("Segoe UI", 11),
        width=30, height=2,
        fg=TEXT_COLOR, bg=BTN_COLOR,
        activebackground=BTN_HOVER, activeforeground=TEXT_COLOR,
        command=lambda s=script: abrir_app(s),
        relief="flat", bd=0, highlightthickness=0, cursor="hand2"
    )
    btn.pack(pady=8)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Iniciar janela
janela.mainloop()
