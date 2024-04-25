import psycopg2

class ConexionPostgreSQL:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="Escuelita",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()
        
    def ejecutar_query(self, query, values=None):
        try:
            if values:
                self.cur.execute(query, values)
            else:
                self.cur.execute(query)
            self.conn.commit()
            print("Consulta ejecutada exitosamente.")
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta:", e)
            
    def consultar_datos(self, query, values=None):
        try:
            if values:
                self.cur.execute(query, values)
            else:
                self.cur.execute(query)
            rows = self.cur.fetchall()
            return rows
        except psycopg2.Error as e:
            print("Error al consultar los datos:", e)
            return None
        
    def cerrar_conexion(self):
        self.cur.close()
        self.conn.close()


