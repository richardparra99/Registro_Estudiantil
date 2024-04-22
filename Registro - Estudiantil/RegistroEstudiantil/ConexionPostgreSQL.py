import psycopg2

class ConexionPostgreSQL:
    def __init__(self, parametros):
        self.parametros = parametros
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(**self.parametros)
            print("Conexión establecida con PostgreSQL")
        except psycopg2.Error as e:
            print("Error al conectar a PostgreSQL:", e)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada con PostgreSQL")
            
    def ejecutar(self, consulta, valores=None):
        self.consulta = consulta
        self.valores = valores