import sqlite3
import os

def inicializar_banco():
    db_path = "db/channel.db"
    if not os.path.exists("db"):
        os.makedirs("db")

    with open("db/model_channel.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()
    conn.close()
    print("✅ Banco de dados 'channel.db' inicializado com sucesso.")

if __name__ == "__main__":
    inicializar_banco()
