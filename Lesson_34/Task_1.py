import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def query1(conn):
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name, employees.department_id, department_name FROM employees JOIN department ON employees.department_id = department.department_id ")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query2(conn):
    cur = conn.cursor()
    cur.execute("""SELECT first_name, last_name, employees.department_id, city, state_province 
                    FROM employees 
                    JOIN department
                    ON department.department_id = employees.department_id 
                    JOIN locations                    
                    ON locations.location_id = department.location_id 
                    ORDER BY first_name""")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query3(conn):
    cur = conn.cursor()
    cur.execute("""SELECT first_name, last_name, employees.department_id, department_name
                        FROM employees 
                        JOIN department
                        ON (department.department_id = 40 AND employees.department_id = 40 
                        OR department.department_id = 80 AND employees.department_id = 80)
                        ORDER BY first_name""")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query4(conn):
    cur = conn.cursor()
    cur.execute("""SELECT department_name
                        FROM department""")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query5(conn):
    cur = conn.cursor()
    cur.execute("""SELECT first_name, manager_id
                        FROM employees""")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query6(conn):
    cur = conn.cursor()
    cur.execute("""SELECT job_title, first_name, last_name, jobs.max_salary - employees.salary AS salary
                        FROM employees
                        JOIN jobs
                        ON employees.job_id = jobs.job_id
                        ORDER BY salary DESC""")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query7(conn):
    cur = conn.cursor()
    cur.execute("""SELECT job_title, (max_salary + min_salary) / 2 AS salary
                        FROM jobs
                        ORDER BY salary DESC
                        """)
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query8(conn):
    cur = conn.cursor()
    cur.execute("""SELECT first_name, last_name, salary
                        FROM employees
                        JOIN department
                        ON employees.department_id = department.department_id AND department.location_id = 2400                       
                        """)
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def query9(conn):
    cur = conn.cursor()
    cur.execute("""SELECT department.department_name, COUNT(employees.department_id)
                        FROM department
                        JOIN employees
                        ON employees.department_id = department.department_id
                        GROUP BY department.department_name                                
                        """)
    rows = cur.fetchall()
    for row in rows:
        print(*row)


def main():
    database = r"E:\HomeWork\Lesson_34\Lesson_34.db"
    conn = create_connection(database)
    with conn:
        # query1(conn)
        # query2(conn)
        # query3(conn)
        # query4(conn)
        # query5(conn)
        # query6(conn)
        # query7(conn)
        # query8(conn)
        query9(conn)


if __name__ == '__main__':
    main()
