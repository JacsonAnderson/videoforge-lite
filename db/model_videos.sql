CREATE TABLE IF NOT EXISTS videos (
    id TEXT PRIMARY KEY,                         -- ID único de 8 caracteres
    channel_id TEXT NOT NULL,                    -- FK do canal
    channel_name TEXT NOT NULL,                  -- Nome do canal (para evitar JOINs desnecessários)
    video_number INTEGER UNSIGNED NOT NULL,      -- Contador por canal
    reference_link TEXT NOT NULL,                -- Link de referência
    original_title TEXT NOT NULL,                -- Título original do vídeo
    corrected_transcript TEXT,                   -- Transcrição corrigida
    directory_path TEXT NOT NULL,                -- Caminho do diretório onde o vídeo está salvo
    translated_title TEXT,                       -- Título traduzido
    title_ideas TEXT,                            -- Ideias de título
    script TEXT,                                 -- Roteiro gerado
    video_description TEXT,                      -- Descrição final
    status_tags TEXT,                            -- Estado atual (ex: roteiro_pronto, video_gerado, etc)
    metadata_tags TEXT,                          -- Tags temáticas (ex: motivação, dinheiro, etc)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (channel_id) REFERENCES channels(id) ON DELETE CASCADE
);
