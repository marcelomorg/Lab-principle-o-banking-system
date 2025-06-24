from app.models.account import Account
from app.models.client import Client
from app.models.transaction import Transaction
from app.repositories.account_repository import AccountRepository


class AccountService:
    def __init__(self, client: Client):
        self.account_repository = AccountRepository()
        self.account = self.account_repository.get_account(client.id)
        
        
    def deposit(self, value) -> bool:
        if float(value) <= 0:
            return False

        balance_now = self.account_repository.get_balance(self.account.id)
        new_value = (float(value) + balance_now)
        result = self.account_repository.update_value(new_value, self.account.id)

        if result:
            transaction = Transaction()
            transaction.type = "deposit"
            transaction.value = value
            transaction.account_id = self.account.id
            self.account_repository.add_register(transaction)
            return True
        


    def withdraw(self, value) -> bool:

        balance_now = self.account_repository.get_balance(self.account.id)
        new_value = (balance_now-float(value))

        if balance_now <= 0 and value > balance_now and value <= 0:
            return False
        
        #TODO: individualize values ​​and amount of withdrawals per account.
        if  self.account_repository.get_amount_transection(self.account.id, "withdraw") >= 3 or float(value) > 500:
            return False
        
        result = self.account_repository.update_value(new_value, self.account.id)

        if result:
            transaction = Transaction()
            transaction.type = "withdraw"
            transaction.value = value
            transaction.account_id = self.account.id
            self.account_repository.add_register(transaction)
            return True


    def bank_statement(self) -> str:
        result = self.account_repository.get_register(self.account.id)
        saldo = self.account_repository.get_balance(self.account.id)
        result_format = ""
        result_format += f"\tITEM\tOP\tVALUE\t\tDATE\n"
        simbol = ""
        for obj in result:
            if obj[1] == "deposit":
                simbol = "+"
            elif obj[1] == "withdraw":
                simbol = "-"
            else:
                simbol = "=="
            
            result_format += f"\t{obj[0]}\t{simbol}\t{obj[2]}\t\t{obj[3]}\n"
        
        result_format += f"\n\n\n\t\t\t\t\t\tSALDO: R${saldo}"

        if result:
            transaction = Transaction()
            transaction.type = "bank_statement"
            transaction.value = saldo
            transaction.account_id = self.account.id
            self.account_repository.add_register(transaction)
        
        return result_format
    
    def get_account(self)-> Account:
        return self.account_repository.get_account(Client.id)