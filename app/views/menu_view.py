from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, os



class MenuView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/views/menu_view.ui", self)

    def execute(self):
        self.showMaximized()



# app = QApplication(sys.argv)
# window = Menu()
# window.showMaximized()
# sys.exit(app.exec())