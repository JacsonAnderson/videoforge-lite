import sqlite3
import os

# Caminho para o banco de dados
db_path = "db/video.db"

# Garante que o diretório existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Conexão com o banco
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criação da tabela 'videos' com status_tags e metadata_tags
create_table_sql = """
CREATE TABLE IF NOT EXISTS videos (
    id TEXT PRIMARY KEY,                         -- ID único de 8 caracteres
    channel_id TEXT NOT NULL,                    -- FK do canal
    channel_name TEXT NOT NULL,                  -- Nome do canal (evita join desnecessário)
    video_number INTEGER NOT NULL,               -- Contador por canal
    reference_link TEXT NOT NULL,                -- Link de referência
    original_title TEXT NOT NULL,                -- Título original
    corrected_transcript TEXT,                   -- Transcrição corrigida
    directory_path TEXT NOT NULL,                -- Caminho da pasta do vídeo
    translated_title TEXT,                       -- Título traduzido
    title_ideas TEXT,                            -- Sugestões de título
    script TEXT,                                 -- Roteiro gerado
    video_description TEXT,                      -- Descrição do vídeo
    status_tags TEXT,                            -- Tags de progresso (ex: gerado_audio, erro_legenda)
    metadata_tags TEXT,                          -- Tags temáticas (ex: motivação, dinheiro)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (channel_id) REFERENCES channels(id) ON DELETE CASCADE
);
"""

# Executa o comando
cursor.execute(create_table_sql)
conn.commit()
conn.close()
