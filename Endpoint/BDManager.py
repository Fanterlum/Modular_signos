#import psycopg2 as gdb # gestor para postgresql :)
import pymysql as gdb # gestor para sql :)
#import sqlite3 as gdb # gestor para sqlite :)

# Configura la conexión a la base de datos
DATABASE="nombre_de_la_base_de_datos"
USER="usuario"
PASS="contraseña"
HOST="localhost"
PORT="5432"# Puerto predeterminado de PostgreSQL
class DatabaseManager:
    def __init__(self,database=DATABASE,user=USER,password=PASS,host=HOST,port=PORT):
        self.conn = None
        self.dbConn(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port  
        )
        self.crudLog=[]

    def dbConn(self,database,user,password,host,port):
        if self.conn is None:
            self.conn = gdb.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port  
            )
            self.crudLog.append(f"conexion creada :{database}")
        else:
            self.crudLog.append("Error: no se puede crear conexion porque ya existe")

    #funcion para crear una cadena de texto 
    #formateada: "v , v , v" a partir de una lista
    def listString(self,list=[]):
        line=""
        nDat=0
        for dat in list:
            nDat+=1
            line+=f'{dat}'+(' ' if len(list) == nDat else ',')
        return line
    #funcion para crear una cadena de texto 
    #formateada: "c = v , c = v , c = v" a partir de un diccionario
    def dictString(self,dict={}):
        line=""
        nDat=0
        nItems=len(dict.items())
        for dat in dict.items():
            nDat+=1
            line +=(f'{dat[0]} = {dat[1]}')
            line+=(' ' if nItems == nDat else ',')
        return line
    
    # Función para crear un nuevo registro
    def create_record(self,tabla,listVal=[]):
        campos=self.listString(self.read_campos(tabla))
        valores=self.listString(listVal)
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"INSERT INTO {tabla} ({campos}) VALUES ({valores})")
            #cursor.execute(f"INSERT INTO {tabla} (nombre, edad) VALUES (%s, %s)", (name, age))
            self.conn.commit()
            self.crudLog.append("Registro creado con éxito.")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al crear el registro: {error}")

    # Función para leer todos los registros
    def read_records(self,tabla):
        registros=[]
        registro={}
        campos = self.read_campos(tabla)
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'SELECT * FROM {tabla}')
            records = cursor.fetchall()
            for record in records:
                for i in range(len(campos)):
                    registro[campos[i]]={record[i]}
                    #print(f"{campos[i]}: {record[i]}, ")
                #print("--------------")
                registros.append(registro)
            self.crudLog.append(f"Registros consulta en la tabla: {tabla}")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al leer los registros: {error}")
        return registros

    # Función para actualizar un registro por ID
    def update_record(self,tabla,id,dictVals={}):
        newVals = self.dictString(dictVals)
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"UPDATE {tabla} SET {newVals} WHERE id = {id}")
            #cursor.execute(f"UPDATE {tabla} SET nombre = {new_name}, edad = {new_age} WHERE {nameCampo} = {buscarVal}")
            self.conn.commit()
            self.crudLog.append("Registro actualizado con éxito.")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al actualizar el registro: {error}" )

    # Función para eliminar un registro por ID
    def delete_record(self,tabla,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"DELETE FROM {tabla} WHERE id = {id}")
            self.conn.commit()
            self.crudLog.append("Registro eliminado con éxito.")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al eliminar el registro: {error}")

    # Función para leer todos los campos
    def read_campos(self,tabla):
        campos = []
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabla}'")
            campos = cursor.fetchall()
            self.crudLog.append(f"Campos consulta en la tabla: {tabla}")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al leer los campos: {error}")
        return campos
    
    # Función para ejecutar query y hacer commit
    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            self.crudLog.append("query y commit ejecutado con éxito.")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al ejecutar query: {error}")

    # Función para ejecutar query y retornar los datos
    def execute_select(self, query):
        data = []
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            self.crudLog.append("query y consulta de datos ejecutado con éxito.")
        except (Exception, gdb.Error) as error:
            self.crudLog.append(f"Error al leer los datos: {error}")
        return data

    # Cerrar la conexión a la base de datos cuando hayas terminado de usarla
    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.crudLog.append("Conexión cerrada.")
        self.conn = None

    def __delattr__(self, __name: str) -> None:
        if __name == "dbConn":
            self.close_connection()
        
    def __del__(self):
        self.close_connection()
