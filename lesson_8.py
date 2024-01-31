import sqlite3

connect = sqlite3.connect('Mbank.db')

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR (70) NOT NULL,
               email TEXT NOT NULL,
               age INTEGER NOT NULL,
               balance DOUBLE (6,2)
);""")

class MBank:
    def __init__(self):
        self.name = None
        self.email = None
        self.age = None
        self.balance = 0

    def add_users(self, name, email, age, balance):
        self.name = name
        self.email = email
        self.age = age
        self.balance = balance
        cursor.execute(f"""INSERT INTO clients (name, email, age, balance )
                       VALUES ('{name}', '{email}', '{age}', '{balance}', );""")
        cursor.commit()

sima = MBank()
sima.add_users("Syimyk", "test@gmail.com", 18, '123456')