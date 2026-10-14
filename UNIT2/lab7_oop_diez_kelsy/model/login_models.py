from controller.connection_db import Database_connection
import mysql.connector


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def auth(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_password",
            database="login_system_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                       (self.username, self.password))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def __init__(self, username, password):
        self.username = username,
        self.password = password,
        self.db = Database_connection()

def auth(self):
    query = "SELECT, id_user, username, nombre FROM users WHERE username = %s AND password = %s"

    result = self.db.ejecutar_consulta(query,(self.username, self.password))
    
    return result