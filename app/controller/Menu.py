import os
from app.view import Menu_texts
from app.service.Account_service import Account_service
from app.domain.Account import Account

class Menu:
    def __init__(self):
        self.account = Account()
        self.account_service = Account_service(self.account)

    def execution(self):
        while True:
            choose = input(Menu_texts.menu)

            if choose == "1":
                self.account_service.deposit()
            elif choose == "2":
                pass
            elif choose == "3":
                pass
            elif choose == "4":
                os.system("clear")
                print(Menu_texts.exit)
                os.system("sleep 2; clear")
                print(Menu_texts.exit2)
                os.system("sleep 2; clear")
                break
            else:
                os.system("clear")        
                print("Opção invalida, tente novamente!")
                os.system("sleep 3; clear")
            