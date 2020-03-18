import sqlite3
from sqlite3 import Error
from datetime import datetime
import os

class DB:
    def __init__(self, db_file):
        exists = self.check_if_db_exists()

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

        if not exists:
            self.create_db(conn)

        self.connection = conn

    def add_carnet(self, first_name, last_name, date_created, date_valid, carnet_id):
        cursor =  self.connection.cursor()
        query = "INSERT INTO carnets(first_name, last_name, date_created, date_valid, unique_id) VALUES (?, ?, ?, ?, ?);"
        
        try:
            cursor.execute(query, (first_name, last_name, date_created, date_valid, carnet_id))
            self.connection.commit()
            return True

        except Error as e:
            print(e)
            return False

    def delete_carnet(self, id):
        cursor = self.connection.cursor()
        query="DELETE FROM carnets WHERE unique_id=?"
        cursor.execute(query, (id,))
        self.connection.commit()
        cursor.execute("VACUUM")
        filepath = os.getcwd()+"/engine/database/qrcodes/"+str(id)+".png"
        os.remove(filepath)

    def update_carnet(self, first_name, last_name, date_created, date_valid, carnet_id):
        cursor = self.connection.cursor()
        query = "UPDATE carnets SET first_name = ?, last_name = ?, date_created = ?, date_valid = ? WHERE unique_id=?"
        try:
            cursor.execute(query,(first_name, last_name, date_created, date_valid, carnet_id))
            self.connection.commit()
            return True
        except Error as e:
            print(e)
            return False

    def get_carnet(self, carnet_id):
        print("ID: " + carnet_id)
        cursor = self.connection.cursor()
        query = "SELECT * FROM carnets WHERE id=?"
        try:
            cursor.execute(query, (carnet_id,))
            result = cursor.fetchone()
        except Error as e:
            print(e)

        return result

    def get_all_carnets(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM carnets"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def check_if_db_exists(self):
        pass

    def create_db(self, connection):  
        table = """CREATE TABLE IF NOT EXISTS CARNETS (
                id integer PRIMARY KEY,
                first_name text NOT NULL,
                last_name text NOT NULL,
                date_created text NOT NULL,
                date_valid text NOT NULL,
                carnet_id integer);
                """
        try:
            c = connection.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def check_if_carnet_is_valid(self, id):
        cursor = self.connection.cursor()
        query = "SELECT date_valid FROM carnets WHERE id=?"
        cursor.execute(query,(id,))

        result = cursor.fetchone()

    def get_by_carnet_id(self, carnet_id):
        cursor = self.connection.cursor()
        query = "SELECT first_name, last_name, date_created, date_valid FROM carnets WHERE unique_id=?"
        try:
            cursor.execute(query,(carnet_id,))
            result = cursor.fetchone()
            return result
        except Error as e:
            print(e)



        