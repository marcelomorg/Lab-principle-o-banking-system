import os, sys, platform

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "libs/")))

# print("sys.path =", sys.path)
# print("libs PyQt5 existe?", os.path.exists(os.path.join(sys.path[0], "PyQt5")))

from PyQt5.QtWidgets import QApplication
from app.controllers.menu_controller import MenuController
import db.connection as db

if __name__ == "__main__":
    start = MenuController()
    print("Iniciando banco de dados...")
    db_succesfully = db.start_db()
    
    if platform.system() == "Linux":
        os.system("sleep 1")

    if db_succesfully:
        app = QApplication(sys.argv)
        start.execution_login()
        sys.exit(app.exec())
    else:
        print("Erro ao iniciar o banco de dados.")
