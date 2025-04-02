# gui/app_roteiro.py

import tkinter as tk
from tkinter import scrolledtext, simpledialog
import threading
import time

# 🎨 Estilo escuro (Notion/ClickUp vibes)
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#2e2e2e"
BTN_HOVER = "#3c3c3c"
TEXT_COLOR = "#f3f3f3"
HIGHLIGHT = "#8b32f4"
FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")

# 🪟 Janela Principal
janela = tk.Tk()
janela.title("Gerador de Roteiros")
janela.geometry("720x520")
janela.configure(bg=BG_COLOR)
janela.resizable(True, True)

# 🔠 Título
tk.Label(janela, text="📝 Gerar Roteiros", font=("Segoe UI", 18, "bold"),
         fg=HIGHLIGHT, bg=BG_COLOR).pack(pady=(25, 10))

# 🎛️ Botões no topo
btn_frame = tk.Frame(janela, bg=BG_COLOR)
btn_frame.pack(pady=(0, 10), padx=20, anchor="n")

btn_todos = tk.Button(btn_frame, text="🚀  Todos os Canais", font=FONT_BOLD,
                      fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=BTN_HOVER,
                      relief="flat", cursor="hand2", width=25,
                      command=lambda: rodar_em_thread(gerar_todos_os_roteiros))
btn_todos.grid(row=0, column=0, padx=5)

btn_canal = tk.Button(btn_frame, text="📺  Canal Específico", font=FONT_BOLD,
                      fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=BTN_HOVER,
                      relief="flat", cursor="hand2", width=25,
                      command=lambda: solicitar_canal())
btn_canal.grid(row=0, column=1, padx=5)

btn_video = tk.Button(btn_frame, text="🎯  Vídeo Específico", font=FONT_BOLD,
                      fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=BTN_HOVER,
                      relief="flat", cursor="hand2", width=25,
                      command=lambda: solicitar_video())
btn_video.grid(row=0, column=2, padx=5)

# 🧾 Área de Log (inicialmente oculta)
log_box = scrolledtext.ScrolledText(janela, wrap="word", font=FONT,
                                    bg=BTN_COLOR, fg=TEXT_COLOR,
                                    insertbackground=TEXT_COLOR, relief="flat",
                                    height=12)
log_box.pack(padx=20, pady=(10, 20), fill="both", expand=False)
log_box.pack_forget()  # Oculta no início

# 🧠 Logs
def mostrar_logs():
    log_box.pack(padx=20, pady=(10, 20), fill="both", expand=True)

def log(msg):
    mostrar_logs()
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)

# 🧠 Simulações
def gerar_todos_os_roteiros():
    log("🔍 Gerando roteiros para TODOS os canais...")
    time.sleep(1)
    log("📥 Transcrições coletadas...")
    time.sleep(1)
    log("🧠 Roteiros gerados com sucesso!")
    time.sleep(1)
    log("✅ Todos os vídeos atualizados para 'roteiro_pronto'.")

def gerar_roteiros_por_canal(canal_id):
    log(f"🔎 Gerando roteiros para o canal '{canal_id}'...")
    time.sleep(1)
    log("📥 Transcrições coletadas.")
    time.sleep(1)
    log("📝 Roteiros gerados para o canal.")
    time.sleep(1)
    log("✅ Status atualizado para 'roteiro_pronto'.")

def gerar_roteiro_por_video(video_id):
    log(f"🎯 Gerando roteiro para o vídeo '{video_id}'...")
    time.sleep(1)
    log("📥 Transcrição coletada.")
    time.sleep(1)
    log("📝 Roteiro gerado!")
    time.sleep(1)
    log("✅ Status: 'roteiro_pronto'.")

# 📥 Dialogs
def solicitar_canal():
    canal_id = simpledialog.askstring("Canal", "Digite o ID do canal:")
    if canal_id:
        rodar_em_thread(gerar_roteiros_por_canal, canal_id)

def solicitar_video():
    video_id = simpledialog.askstring("Vídeo", "Digite o ID do vídeo:")
    if video_id:
        rodar_em_thread(gerar_roteiro_por_video, video_id)

# 🧵 Thread Wrapper
def rodar_em_thread(func, *args):
    def wrapped():
        for b in [btn_todos, btn_canal, btn_video]:
            b.config(state="disabled")
        func(*args)
        for b in [btn_todos, btn_canal, btn_video]:
            b.config(state="normal")
    threading.Thread(target=wrapped).start()

# 🏁 Start
janela.mainloop()
