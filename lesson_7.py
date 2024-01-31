# СУБД - Система Управления Базой Данных
# БД - База Данных
# CRUD - Create, Read, Update, Delete

import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection("Geeks.db")

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

def create_students(conn, student: tuple):
    sql = """INSERT INTO Geeks_14_2B
     (full_name, date, visit, is_passed, characteristics)
      VALUES (?, ?, ?, ?, ?); """
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()

def read_characteristics(conn):
    sql = 'SELECT full_name, characteristics FROM Geeks_14_2B WHERE visit > 0'
    cursor = conn.cursor()
    best_students = cursor.execute(sql).fetchall()
    for student in best_students:
        print(student)


def update_student_visit(conn, id, new_visit):
    sql = "UPDATE Geeks_14_2B SET visit = ? WHERE id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (new_visit, id))
    conn.commit()

def delete_students(conn, id: int):
    sql = "DELETE FROM Geeks_14_2B WHERE id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()


sql_create_table = """
CREATE TABLE IF NOT EXISTS Geeks_14_2B (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (70) NOT NULL,
date DATE NOT NULL,
visit DOUBLE (2, 1) DEFAULT 0.0,
is_passed BOOLEAN DEFAULT FALSE,
characteristics TEXT DEFAULT NULL
);
"""

connection = create_connection("Geeks.db")

if connection:
    print("Успешное соединение")
    create_table(connection, sql_create_table)
    # create_students(connection, ("Расулов Асадбек", "2024-01-27", 1.0, False, "Красавчик"))
    read_characteristics(connection)
    update_student_visit(connection, 1, 0)
    delete_students(connection, 1)



    
    # create_students(connection, ("Ахмадбек у Элизар", "2024-01-27", 1.0, False, "Красавчик"))
    # create_students(connection, ("Самат Сыргак", "2024-01-27", 1.0, False, "Красавчик"))
    # create_students(connection, ("Сайдуллаев Мухаммадали", "2024-01-27", 1.0, False, "Красавчик"))
    # create_students(connection, ("Кадырбек у Мусулманкул", "2024-01-27", 1.0, False, "Красавчик"))
    # create_students(connection, ("Ырыскелди(повтор)", "2024-01-27", 1.0, False, "Красавчик"))
    # create_students(connection, ("Авазов Имамберди", "2024-01-27", 1.0, False, "Красавчик"))
    # create_students(connection, ("Боронова Бибисара", "2024-01-27", 1.0, False, "Красавица"))
    # create_students(connection, ("Таирова Дарика", "2024-01-27", 1.0, False, "Красавица"))

