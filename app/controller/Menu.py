import os
from app.view import Menu_texts
from app.service.Account_service import Account_service
from app.domain.Account import Account
from app.domain.Client import Client

class Menu:
    def __init__(self):
        self.client = Client("Clienttest", "000.000.000.00", 90)
        self.account_service = Account_service(self.client)

    def execution(self):
        while True:
            choose = input(Menu_texts.menu)

            if choose == "1":
                os.system("clear")
                value_deposit = input(Menu_texts.deposit_value)
                result = self.account_service.deposit(value_deposit)

                if result:
                    print(Menu_texts.deposit_confirmado)
                else:
                    print(Menu_texts.deposito_erro)
                
                os.system("sleep 2; clear")


            elif choose == "2":
                os.system("clear")
                value_withdraw = input(Menu_texts.withdraw_value)
                result = self.account_service.withdraw(value_withdraw)
                
                if result:
                    print(Menu_texts.withdraw_confirmado)
                else:
                    print(Menu_texts.withdraw_erro)
                
                os.system("sleep 2; clear")

            elif choose == "3":
                result = self.account_service.bank_statement()
                os.system("clear")
                print(Menu_texts.bank_statement)
                print(result)
                os.system("sleep 10; clear")

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
            