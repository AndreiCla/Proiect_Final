import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = 'yourpassword'
        self.database = 'ProiectFinalPy'

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexiune la baza de date reusita!")
        except mysql.connector.Error as e:
            print(f"Eroare la conectare la baza de date: {e}")
            return None

