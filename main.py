import os
from app.controller.Menu import Menu
import db.connection as db

if __name__ == "__main__":
    start = Menu()
    print("Iniciando banco de dados...")
    db_succesfully = db.start_db()
    os.system("sleep 1")

    if db_succesfully:
        start.execution()
    else:
        print("Erro ao iniciar o banco de dados.")
