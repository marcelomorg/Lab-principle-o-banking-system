from app.domain.Account import Account


class Account_service:
    def __init__(self, account: Account):
        self.account = account
        
    def deposit(self):
        print(self.account.account_number)

    def withdraw(self):
        pass

    def bank_statement(self):
        pass