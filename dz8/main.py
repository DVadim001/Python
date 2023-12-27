# Банк на sqlite3
import sqlite3
connection = sqlite3.connect("bank.db")

sql = connection.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS clients (name TEXT, surname TEXT, phone TEXT, balance FLOAT);")
connection.commit()

def add_client():
    name = input("Введите имя: ")
    surname= input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    balance = input("Введите баланс: ")

    sql = connection.cursor()
    sql.execute(f"INSERT INTO clients (name, surname, phone, balance) VALUES('{name}', '{surname}', '{phone}', '{balance}') ;")
    connection.commit()

def view_clients():
    sql = connection.cursor()
    print(sql.execute("SELECT * FROM clients;").fetchall() )
    connection.commit()


def view_balance():
    name = input("Введите имя клиента: ")
    sql = connection.cursor()
    print(sql.execute(f"SELECT balance FROM clients WHERE name ='{name}' ;").fetchone() )
    connection.commit()

def balance_operation():
    name = input("Введите имя клиента: ")
    balance = input("Укажите новый баланс: ")
    sql = connection.cursor()
    print(sql.execute(f"UPDATE clients SET balance = '{balance}' WHERE name ='{name}' ;").fetchone() )
    connection.commit()

def delete_client():
    name = input("Введите имя клиента: ")
    sql = connection.cursor()
    sql.execute(f"DELETE FROM clients WHERE name = '{name}' ;")
    connection.commit()


# Добавить клиента, список клиентов, проверка баланса, изменить баланс, удалить клиента
action = input("Введите требуемую операцию (помощь): ")

if action.lower() == "помощь":
    print("добавить, список, баланс, изменить, удалить")
elif action.lower() == "добавить":
    add_client()
elif action.lower() == "список":
    view_clients()
elif action.lower() == "баланс":
    view_balance()
elif action.lower() == "изменить":
    balance_operation()
elif action.lower() == "удалить":
    delete_client()
else:
    print("Неизвестная операция.")

