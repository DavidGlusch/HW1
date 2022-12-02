import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def show_full_name(conn):
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def show_department_id(conn):
    cur = conn.cursor()
    cur.execute("SELECT department_id FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def show_employee_details(conn):
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name, email, phone_number FROM employees ORDER BY first_name ")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def show_first_name_last_name_salary_pf(conn):
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name, salary, salary*0.12  FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def max_and_min_salary(conn):
    cur = conn.cursor()
    cur.execute("SELECT MAX(salary), MIN(salary)  FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def monthly_salary(conn):
    cur = conn.cursor()
    cur.execute("SELECT ROUND(salary, 2)  FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def main():
    database = r"E:\HomeWork\Lesson_33\example.db"
    conn = create_connection(database)
    with conn:
        show_full_name(conn)
        # show_department_id(conn)
        # show_employee_details(conn)
        # show_first_name_last_name_salary_pf(conn)
        # max_and_min_salary(conn)
        # monthly_salary(conn)


if __name__ == '__main__':
    main()