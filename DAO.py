import mariadb
from connection_info import conn_params

class DAO:
    def __init__(self):
        self.connection = mariadb.connect(**conn_params)

    def get_db_info(self, sql):
        cursor = self.connection.cursor()

        cursor.execute(sql) #THIS IS GENERALLY NOT A GOOD IDEA. DON'T DO THIS IN THE REAL WORLD

        tuple_answer = cursor.fetchall()

        cursor.close()
        return tuple_answer

    def close_connection(self):
        self.connection.close()
