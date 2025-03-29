import sqlite3
from typing import List, Tuple, Optional

DB_PATH = "db/channel.db"

def listar_canais() -> List[Tuple[str, str, str]]:
    """
    Retorna uma lista com (id, name, language) de todos os canais cadastrados.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, language FROM channels ORDER BY created_at DESC")
    canais = cursor.fetchall()
    conn.close()
    return canais

def criar_canal(
    id_: str,
    nome: str,
    idioma: str,
    prompt: str,
    min_prompt_chars: Optional[int] = None,
    voice_model: Optional[str] = None,
    watermark: Optional[str] = None,
    music: Optional[str] = None
) -> None:
    """
    Cria um novo canal no banco de dados com os dados fornecidos.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO channels (
            id, name, language, min_prompt_chars, prompt,
            voice_model, watermark, music
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        id_, nome, idioma, min_prompt_chars, prompt,
        voice_model, watermark, music
    ))
    conn.commit()
    conn.close()

def excluir_canal(canal_id: str) -> None:
    """
    Exclui um canal do banco com base no ID.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM channels WHERE id = ?", (canal_id,))
    conn.commit()
    conn.close()

def atualizar_canal(
    canal_id: str,
    nome: str,
    idioma: str,
    prompt: str,
    min_prompt_chars: Optional[int] = None,
    voice_model: Optional[str] = None,
    watermark: Optional[str] = None,
    music: Optional[str] = None
) -> None:
    """
    Atualiza um canal existente com os novos dados.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE channels
        SET name = ?, language = ?, min_prompt_chars = ?, prompt = ?,
            voice_model = ?, watermark = ?, music = ?
        WHERE id = ?
    """, (
        nome, idioma, min_prompt_chars, prompt,
        voice_model, watermark, music, canal_id
    ))
    conn.commit()
    conn.close()



def obter_canal_por_id(canal_id: str) -> Optional[Tuple]:
    """
    Retorna todos os dados do canal com base no ID.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, language, min_prompt_chars, prompt,
               voice_model, watermark, music
        FROM channels
        WHERE id = ?
    """, (canal_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado
