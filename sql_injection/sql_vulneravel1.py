import sqlite3
from sqlite3 import Error
import os

DATABASE = r"teste_sqlite.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def criar_banco():

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        login text NOT NULL,
                                        passwd text,
                                        admin boolean,
                                        create_date text
                                    ); """

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

    # create a database connection
    conn = create_connection(DATABASE)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, project)
    conn.commit()
    return cursor.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES (?,?,?,?,?,?) 
    '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def validar_admin(conn, usuario: str) -> bool:
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT admin FROM usuarios WHERE usuario = '%s'" % usuario)
        result = cursor.fetchone()
    admin, = result
    return admin


if __name__ == '__main__':
    if not os.path.isfile('teste_sqlite.db'):
        criar_banco()
    conn = create_connection(DATABASE)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(conn, project)
        task_1 = ('Analyze the requirements of the app', 1,
                  1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements',
                  1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)
