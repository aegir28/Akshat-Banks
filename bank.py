from database import db_query, mydb
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction (timedate VARCHAR(30), account_number INTEGER, remarks VARCHAR(30), amount INTEGER)")

    def balance_enquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        return f"{self.__username} Balance is {temp[0][0]}"

    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        new_balance = amount + temp[0][0]
        db_query(f"UPDATE customers SET balance = {new_balance} WHERE username = '{self.__username}'; ")
        self.add_transaction('Amount Deposit', amount)
        return f"{self.__username} Amount is Successfully Deposited into Your Account {self.__account_number}"

    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            return "Insufficient Balance Please Deposit Money"
        new_balance = temp[0][0] - amount
        db_query(f"UPDATE customers SET balance = {new_balance} WHERE username = '{self.__username}'; ")
        self.add_transaction('Amount Withdraw', amount)
        return f"{self.__username} Amount is Successfully Withdrawn from Your Account {self.__account_number}"

    def fund_transfer(self, receive, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            return "Insufficient Balance Please Deposit Money"
        temp2 = db_query(f"SELECT balance FROM customers WHERE account_number = {receive};")
        if not temp2:
            return "Account Number Does not Exist"
        new_balance_sender = temp[0][0] - amount
        new_balance_receiver = amount + temp2[0][0]
        db_query(f"UPDATE customers SET balance = {new_balance_sender} WHERE username = '{self.__username}'; ")
        db_query(f"UPDATE customers SET balance = {new_balance_receiver} WHERE account_number = {receive}; ")
        receiver_username = db_query(f"SELECT username FROM customers WHERE account_number = {receive};")
        self.add_transaction(f'Fund Transfer -> {receive}', amount)
        db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ('{datetime.datetime.now()}', {self.__account_number}, 'Fund Transfer From {self.__account_number}', {amount})")
        return f"{self.__username} Amount is Successfully Transferred from Your Account {self.__account_number}"

    def add_transaction(self, remarks, amount):
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ('{datetime.datetime.now()}', {self.__account_number}, '{remarks}', {amount})")
        mydb.commit()

def banking_service(username, account_number, service, amount=0, receiver_account=None):
    bobj = Bank(username, account_number)
    if service == "Balance Enquiry":
        return bobj.balance_enquiry()
    elif service == "Cash Deposit":
        return bobj.deposit(amount)
    elif service == "Cash Withdraw":
        return bobj.withdraw(amount)
    elif service == "Fund Transfer":
        return bobj.fund_transfer(receiver_account, amount)
    else:
        return "Invalid Service"
