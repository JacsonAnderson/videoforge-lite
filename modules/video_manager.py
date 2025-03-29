import sqlite3

DB_PATH = "db/video.db"

def criar_video(id_, channel_id, channel_name, video_number, reference_link):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO videos (
            id, channel_id, channel_name, video_number, reference_link, directory_path
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (id_, channel_id, channel_name, video_number, reference_link, f"data/{channel_id}/{id_}"))
    conn.commit()
    conn.close()
