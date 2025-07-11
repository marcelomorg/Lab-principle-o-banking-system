from db.connection import get_connection
from app.models.account import Account
from app.models.transaction import Transaction

class AccountRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def get_account(self, id_client) -> Account:
        try:
            result =  self.cursor.execute("""
                SELECT  * FROM accounts WHERE client_id = ?
            """, (id_client,)).fetchone()
            account = Account()
            account.id = result[0]
            account.branch_number = result[1]
            account.account_number = result[2]
            account.balance = result[3]
            account.client_id = result[4]
            return account
        except Exception as e:
            print(f"ERRO: {e}")


    def update_value(self, value, id_account):
        try:
            self.cursor.execute("""
                UPDATE accounts
                SET balance = ?
                WHERE id = ?
            """, (value, id_account))
            self.conn.commit()
            return True
        
        except Exception as e:
            print("add_value method error: "+ e)
            return False

    def get_balance (self, id_account) -> float:
        result = self.cursor.execute("""
            SELECT balance FROM accounts WHERE id = ?
        """, (id_account,)).fetchone()
        return result[0]
    
    def get_register(self, id_account) -> list:
        result = self.cursor.execute("""
            SELECT * FROM transactions WHERE account_id = ?
        """, (id_account,)).fetchall()
        return result
        
    def add_register(self, transaction: Transaction):
        self.cursor.execute("""
            INSERT INTO transactions (type, value, account_id)
            VALUES (?,?,?)
        """, (transaction.type, transaction.value, transaction.account_id))
        self.conn.commit()

    def get_amount_transection(self, id_account, type) -> int:
        try:
            result = self.cursor.execute("""
                SELECT COUNT(*) as Transactions_count
                FROM transactions
                WHERE type = ?
                AND DATE(date_hour) = DATE("now")
                AND account_id = ?                              
            """, (type, id_account)).fetchone()
            print(result[0])
            return int(result[0])
        except Exception as e:
            print(e)



    def close_connection(self):
        self.conn.close()