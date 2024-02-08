import mysql.connector

from constants import DatabaseConnector


class AdaugarePers:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def add_person(self, id, nume, prenume, companie, email, id_manager=None,):
        try:
            cursor = self.db_connector.connection.cursor()
            query = "INSERT INTO Persoane (ID, Nume, Prenume, Companie, Email, IdManager) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (id, nume, prenume, companie, email, id_manager,))
            self.db_connector.connection.commit()
            print("Persoana adaugata cu succes!")
        except mysql.connector.Error as e:
            print(f"Eroare la adaugarea persoanei: {e}")

db_connector = DatabaseConnector(host = '127.0.0.1', user = 'root', password = 'yourpassword', database = 'ProiectFinalPy')
db_connector.connect()

admin = AdaugarePers(db_connector)
admin.add_person(1, 'Popescu', 'Ion', 'Tesla','popescuion@gmail.com', 1,)
