-- db/model_channel.sql

CREATE TABLE IF NOT EXISTS channels (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    language TEXT NOT NULL,
    min_prompt_chars INTEGER,
    prompt TEXT NOT NULL,
    voice_model TEXT,
    watermark TEXT,
    music TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
