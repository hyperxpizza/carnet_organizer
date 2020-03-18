import sqlite3
from sqlite3 import Error

queries = [
    "INSERT INTO carnets VALUES(1,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 3292203023)",
    "INSERT INTO carnets VALUES(2,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 3292203023)",
    "INSERT INTO carnets VALUES(3,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 3292203023)",
    "INSERT INTO carnets VALUES(4,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 3292203023)",
    "INSERT INTO carnets VALUES(6,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(7,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(8,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(9,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(10,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(11,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(12,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(13,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(14,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)",
    "INSERT INTO carnets VALUES(15,'Wojciech','Frąckowski','2020-10-04','2020-04-10', 483486348)"
]

def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def insert(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print(cursor.lastrowid)

def main():
    database = 'sciankadatabase.db'
    connection = create_connection(database)

    for query in queries:
        insert(connection,query)

    connection.close()

if __name__ == "__main__":
    main()