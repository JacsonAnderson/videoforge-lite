import tkinter as tk
from tkinter import messagebox

# Estilo
BG_COLOR = "#1e1e1e"
FRAME_COLOR = "#262626"
BTN_COLOR = "#2e2e2e"
BTN_HOVER = "#3c3c3c"
TEXT_COLOR = "#f3f3f3"
HIGHLIGHT = "#8b32f4"

# Criar janela
janela = tk.Tk()
janela.title("Painel de Canais")
janela.geometry("500x500")
janela.configure(bg=BG_COLOR)
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela, text="Painel de Canais", font=("Segoe UI", 18, "bold"),
    fg=HIGHLIGHT, bg=BG_COLOR, pady=10
)
titulo.pack()

# Subtítulo
subtitulo = tk.Label(
    janela, text="Gerencie seus canais", font=("Segoe UI", 11),
    fg="#cccccc", bg=BG_COLOR
)
subtitulo.pack()

# Botão para adicionar canal
def criar_canal():
    messagebox.showinfo("Criar Canal", "Aqui abrirá a interface para criar um canal.")

btn_novo = tk.Button(
    janela, text="➕  Criar Canal", font=("Segoe UI", 11),
    fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=BTN_HOVER,
    relief="flat", bd=0, highlightthickness=0, cursor="hand2",
    command=criar_canal
)
btn_novo.pack(pady=20)

# Lista de canais (futuramente será carregada do banco)
frame_lista = tk.Frame(janela, bg=FRAME_COLOR)
frame_lista.pack(padx=20, pady=10, fill="both", expand=True)

# Exemplo estático
canais_exemplo = [
    {"id": 1, "nome": "Canal Saúde", "descricao": "Dores e bem-estar"},
    {"id": 2, "nome": "Canal Fitness", "descricao": "Dicas de treino"},
]

# Funções de ação
def editar_canal(nome):
    messagebox.showinfo("Editar", f"Editar canal: {nome}")

def excluir_canal(nome):
    confirmar = messagebox.askyesno("Excluir", f"Tem certeza que quer excluir o canal '{nome}'?")
    if confirmar:
        messagebox.showinfo("Excluído", f"Canal '{nome}' excluído com sucesso!")

# Renderizar canais
for canal in canais_exemplo:
    container = tk.Frame(frame_lista, bg=BTN_COLOR, pady=5)
    container.pack(fill="x", pady=5, padx=5)

    label_nome = tk.Label(container, text=canal["nome"], font=("Segoe UI", 11, "bold"),
                          bg=BTN_COLOR, fg=TEXT_COLOR)
    label_nome.pack(side="left", padx=10)

    btn_editar = tk.Button(container, text="✏️", bg=BTN_COLOR, fg=HIGHLIGHT,
                           font=("Segoe UI", 10), relief="flat", cursor="hand2",
                           command=lambda nome=canal["nome"]: editar_canal(nome))
    btn_editar.pack(side="right", padx=5)

    btn_excluir = tk.Button(container, text="🗑️", bg=BTN_COLOR, fg="#ff4d4d",
                            font=("Segoe UI", 10), relief="flat", cursor="hand2",
                            command=lambda nome=canal["nome"]: excluir_canal(nome))
    btn_excluir.pack(side="right")

# Iniciar app
janela.mainloop()
