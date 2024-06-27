from customer import Customer
from bank import Bank
from database import db_query

def sign_up(username, password, name, age, city):
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        return "Username Already Exists"
    else:
        account_number = generate_account_number()
        cobj = Customer(username, password, name, age, city, account_number)
        cobj.create_user()
        bobj = Bank(username, account_number)
        bobj.create_transaction_table()
        return f"Account created successfully. Your account number is {account_number}"

def sign_in(username, password):
    temp = db_query(f"SELECT username, password, account_number FROM customers WHERE username = '{username}';")
    if temp and temp[0][1] == password:
        return f"Sign In Successful. Welcome {username}", temp[0][2]
    else:
        return "Invalid username or password", None

def generate_account_number():
    import random
    while True:
        account_number = random.randint(10000000, 99999999)
        temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
        if not temp:
            return account_number
