import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def execute_table_create():
    database = r"E:\HomeWork\Lesson_33\test_database"

    sql_create_project_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    );"""
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""

    sql_task1_table = """CREATE TABLE IF NOT EXISTS task1 (
                                    id integer PRIMARY KEY,
                                    row1 text NOT NULL,
                                    row2 integer
                                    );"""

    conn = create_connection(database)

    if conn:
        create_table(conn, sql_create_project_table)
        create_table(conn, sql_create_tasks_table)
        create_table(conn, sql_task1_table)
    else:
        print('!!!!!')


def create_task(conn, task):
    sql = """ INSERT OR REPLACE INTO task1(id, row1, row2)
              VALUES (?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def insert_task():
    database = r"E:\HomeWork\Lesson_33\test_database"

    conn = create_connection(database)
    with conn:

        task_1 = (3, 'do something', 45)

        create_task(conn, task_1)


def update_info(conn, task):
    sql = """UPDATE task1

                SET row1 = ?,
                    row2 = ?
                WHERE id = ?;"""
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def start_update():
    database = r"E:\HomeWork\Lesson_33\test_database"
    conn = create_connection(database)
    with conn:
        update_info(conn, ('test information', 55, 3))


def delete_task(conn, id):
    sql = 'DELETE FROM task1 WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_execute():
    database = r"E:\HomeWork\Lesson_33\test_database"

    conn = create_connection(database)
    with conn:
        delete_task(conn, 3)


if __name__ == '__main__':
    insert_task()
    start_update()
    # delete_execute()
