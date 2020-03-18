import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_table(connection):
    table = """CREATE TABLE IF NOT EXISTS CARNETS (
            id integer PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL,
            date_created text NOT NULL,
            date_valid text NOT NULL,
            unique_id integer NOT NULL);
            """
    try:
        c = connection.cursor()
        c.execute(table)
    except Error as e:
        print(e)
    
if __name__ == "__main__":
    connection = create_connection("sciankadatabase.db")
    if connection is not None:
        create_table(connection)
        print("[+] Table Created")