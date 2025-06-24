from PyQt5 import uic
from PyQt5.QtWidgets import  QMainWindow, QMessageBox
import sys, os
from app.views.menu_view import MenuView



class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/views/login_view.ui", self)

        self.btn_submit.clicked.connect(self.login)

    def  login(self):
        value_account = self.input_account.text()
        value_password = self.input_pass.text()
        print(f"""
        Conta: {value_account}
        Senha: {value_password}
        """)

        if value_password == "123":
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
            self.menu_window = MenuView()
            self.menu_window.execute()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Senha invalida!")

    def execute(self):
        self.showMaximized()

# app = QApplication(sys.argv)
# window = Login()
# window.showMaximized()
# sys.exit(app.exec())