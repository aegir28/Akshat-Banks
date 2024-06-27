import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="Akshat@28",
    database="BMS"
)

cursor = mydb.cursor()

def db_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    mydb.commit()
    return result

def create_customer_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            city VARCHAR(20) NOT NULL,
            balance INTEGER NOT NULL,
            account_number INTEGER NOT NULL,
            status BOOLEAN NOT NULL
        )
    ''')
    mydb.commit()

if __name__ == "__main__":
    create_customer_table()
