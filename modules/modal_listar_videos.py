import tkinter as tk
import webbrowser
from modules.video_manager import listar_videos_por_canal, atualizar_status_video

# 🎨 Paleta de cores estilizada
BG_COLOR = "#1e1e1e"
CARD_COLOR = "#2a2a2a"
LINK_BG = "#3a3a3a"
LINK_FG = "#ffffff"
TEXT_COLOR = "#f0f0f0"
SUBTEXT_COLOR = "#aaaaaa"
HIGHLIGHT = "#8b32f4"
FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")

TAGS_STATUS = [
    "pendente",
    "roteiro_pronto",
    "audio_gerado",
    "video_editado",
    "acabamentos_prontos",
    "thumb_gerada",
    "metadados_gerados",
    "postado"
]

def abrir_modal_editar_status(parent, video_id, status_atual, on_update):
    modal = tk.Toplevel(parent)
    modal.title("Editar Status")
    modal.configure(bg=BG_COLOR)
    modal.geometry("300x320")
    modal.resizable(False, False)

    tk.Label(modal, text="Selecione o novo status:", fg=TEXT_COLOR,
             bg=BG_COLOR, font=FONT_BOLD).pack(pady=15)

    lista = tk.Listbox(modal, bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT,
                       selectbackground=HIGHLIGHT, activestyle="none", height=10)
    for tag in TAGS_STATUS:
        lista.insert(tk.END, tag)
        if tag == status_atual:
            lista.selection_set(tk.END)
    lista.pack(padx=20, fill="both", expand=True)

    def selecionar(event):
        selecionado = lista.get(lista.curselection())
        atualizar_status_video(video_id, selecionado)
        on_update()
        modal.destroy()

    lista.bind("<Double-Button-1>", selecionar)

def abrir_modal_listar_videos(parent, canal_id: str, canal_nome: str):
    modal = tk.Toplevel(parent)
    modal.title(f"Vídeos de {canal_nome}")
    modal.configure(bg=BG_COLOR)
    modal.geometry("900x700")
    modal.resizable(True, True)

    # 🔠 Nome do canal estilizado
    tk.Label(modal, text=canal_nome.upper(), fg=TEXT_COLOR, bg=BG_COLOR,
             font=("Segoe UI", 16, "bold")).pack(pady=(20, 5))

    canvas = tk.Canvas(modal, bg=BG_COLOR, highlightthickness=0)
    scrollbar = tk.Scrollbar(modal, orient="vertical", command=canvas.yview)
    frame_videos = tk.Frame(canvas, bg=BG_COLOR)
    frame_videos.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=frame_videos, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def atualizar_videos():
        for w in frame_videos.winfo_children():
            w.destroy()

        dados = listar_videos_por_canal(canal_id)
        if not dados:
            tk.Label(frame_videos, text="Nenhum vídeo encontrado.", fg=SUBTEXT_COLOR,
                     bg=BG_COLOR, font=FONT).pack()
            return

        agrupados = {}
        for video in dados:
            status = video['status_tags'] or "sem_status"
            if status not in agrupados:
                agrupados[status] = []
            agrupados[status].append(video)

        for status_tag, videos in agrupados.items():
            if status_tag == "postado":
                videos = sorted(videos, key=lambda x: x["created_at"], reverse=True)[:3]
                if not videos:
                    continue

            # 🏷️ Título do grupo (status)
            tk.Label(frame_videos, text=f"🟣 {status_tag.upper()}", fg=TEXT_COLOR,
                     bg=BG_COLOR, font=FONT_BOLD).pack(anchor="w", pady=(10, 0))

            for video in videos:
                linha = tk.Frame(frame_videos, bg=CARD_COLOR, padx=10, pady=6)
                linha.pack(fill="x", pady=5)

                def abrir_link(link=video['reference_link']):
                    webbrowser.open(link)

                link = tk.Label(linha, text=video['reference_link'],
                                fg=LINK_FG, bg=LINK_BG, font=FONT,
                                cursor="hand2", wraplength=700, padx=8, pady=4)
                link.pack(side="left", fill="x", expand=True, anchor="w", ipadx=6, ipady=3)
                link.bind("<Double-Button-1>", lambda e, l=video['reference_link']: abrir_link(l))

                btn_editar = tk.Button(linha, text="✏", font=("Segoe UI", 9, "bold"),
                                       bg=CARD_COLOR, fg=HIGHLIGHT, relief="flat",
                                       cursor="hand2",
                                       command=lambda vid=video['id'], st=video['status_tags']:
                                       abrir_modal_editar_status(modal, vid, st, atualizar_videos))
                btn_editar.pack(side="right", padx=6)

    atualizar_videos()
