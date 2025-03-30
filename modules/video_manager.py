import os
import sqlite3

DB_PATH = "db/video.db"
BASE_PATH = "data"

def criar_diretorio_video(channel_id: str, video_id: str) -> str:
    """
    Cria a pasta do vídeo dentro da pasta do canal e retorna o caminho.
    Exemplo: data/<channel_id>/<video_id>
    """
    caminho = os.path.join(BASE_PATH, channel_id, video_id)
    os.makedirs(caminho, exist_ok=True)
    return caminho

def criar_video(id_: str, channel_id: str, channel_name: str, video_number: int, reference_link: str):
    """
    Insere um novo vídeo no banco de dados e cria sua pasta no disco.
    """
    diretorio = criar_diretorio_video(channel_id, id_)

    # Preenche valores obrigatórios que estavam faltando
    original_title = "Null"  # Provisório, será atualizado depois
    status_tags = "pendente"                      # Estado inicial
    metadata_tags = ""                        # Pode ser preenchido posteriormente

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO videos (
            id, channel_id, channel_name, video_number,
            reference_link, original_title, directory_path,
            status_tags, metadata_tags
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        id_, channel_id, channel_name, video_number,
        reference_link, original_title, diretorio,
        status_tags, metadata_tags
    ))
    conn.commit()
    conn.close()

def listar_videos_por_canal(channel_id: str) -> list:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, reference_link, status_tags, created_at
        FROM videos
        WHERE channel_id = ?
        ORDER BY created_at DESC
    """, (channel_id,))
    resultado = cursor.fetchall()
    conn.close()
    return [dict(row) for row in resultado]

def atualizar_status_video(video_id: str, novo_status: str) -> None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE videos SET status_tags = ? WHERE id = ?", (novo_status, video_id))
    conn.commit()
    conn.close()
