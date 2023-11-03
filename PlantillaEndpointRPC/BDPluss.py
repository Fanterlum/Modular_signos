from sqlalchemy import create_engine, text, exc
from sqlalchemy.orm import sessionmaker
from config import DevConfig as conf
#import psycopg2 as gdb # gestor para postgresql :)
#import pymysql as gdb # gestor para sql :)
import sqlite3 as gdb # gestor para sqlite :)
e=None

class DBManager:
    exceptions=None
    def __init__(self):
        self.conn = None
        self.engine = None
        self.crudLog=[]
        
    @property
    def Conn(self):
        return self.conn
    @property
    def Engine(self):
        return self.engine
    
    def dbConn_ORM(self,database=conf.DATABASE_URI):
        if self.conn is None:
            # Crear una instancia del motor de la base de datos
            self.engine = create_engine(database)  # Cambia la URL según tu base de datos
            Session = sessionmaker(bind=self.engine)
            self.conn = Session()
            self.crudLog.append(f"conexion creada :{database}")
        else:
            self.exceptions=exc.SQLAlchemyError
            self.crudLog.append("Error: no se puede crear conexion porque ya existe")

    def dbConn(self,database=conf.DATABASE_URI):
        
        if self.conn is None:
            self.conn = gdb.connect(
                database=database
            )
            self.crudLog.append(f"conexion creada :{database}")
            self.exceptions=(Exception, gdb.Error)
        else:
            self.crudLog.append("Error: no se puede crear conexion porque ya existe")

    def dbConn(self,user,password,host,port,database=conf.DATABASE_URI):
        if self.conn is None:
            self.conn = gdb.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port  
            )
            self.crudLog.append(f"conexion creada :{database}")
            self.exceptions=(Exception, gdb.Error)
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
    #funcion para crear una Query para hacer una tabla
    def buildQueryTable(self,tableName,campos):
        table_query = f'''
            CREATE TABLE IF NOT EXISTS {tableName} ('''
        for campo in campos:
            #id INTEGER PRIMARY KEY,
            table_query+= f'{campo} {campos[campo]},'
        table_query+='\r)'
        return text(table_query)

    # Función para crear un nuevo registro
    def create_record(self,tabla,listVal=[]):
        campos=self.listString(self.read_campos(tabla))
        valores=self.listString(listVal)
        query=f"INSERT INTO {tabla} ({campos}) VALUES ({valores})"
        try:
            self.execute_query(query)
            '''if self.engine:
                cursor=self.engine.connect()
                query=text(query)
            else:    
                cursor = self.conn.cursor()
            cursor.execute(query)
            #cursor.execute(f"INSERT INTO {tabla} (nombre, edad) VALUES (%s, %s)", (name, age))
            self.conn.commit()'''
            self.crudLog.append("Registro creado con éxito.")
        
        except self.exceptions as error:
            self.crudLog.append(f"Error al crear el registro: {error}")

    # Función para leer todos los registros
    def read_records(self,tabla):
        registros=[]
        registro={}
        campos = self.read_campos(tabla)
        query=f'SELECT * FROM {tabla}'
        try:
            if self.engine:
                cursor=self.engine.connect()
                query=text(query)
            else:    
                cursor = self.conn.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            for record in records:
                for i in range(len(campos)):
                    registro[campos[i]]={record[i]}
                    #print(f"{campos[i]}: {record[i]}, ")
                #print("--------------")
                registros.append(registro)
            self.crudLog.append(f"Registros consulta en la tabla: {tabla}")
        except self.exceptions as error:
            self.crudLog.append(f"Error al leer los registros: {error}")
        return registros

    # Función para actualizar un registro por ID
    def update_record(self,tabla,id,dictVals={}):
        newVals = self.dictString(dictVals)
        query=f"UPDATE {tabla} SET {newVals} WHERE id = {id}"
        try:
            self.execute_query(query)
            '''if self.engine:
                cursor=self.engine.connect()
                query=text(query)
            else:    
                cursor = self.conn.cursor()
            cursor.execute(query)
            #cursor.execute(f"UPDATE {tabla} SET nombre = {new_name}, edad = {new_age} WHERE {nameCampo} = {buscarVal}")
            self.conn.commit()'''
            self.crudLog.append("Registro actualizado con éxito.")
        except self.exceptions as error:
            self.crudLog.append(f"Error al actualizar el registro: {error}" )

    # Función para eliminar un registro por ID
    def delete_record(self,tabla,id):
        query=f"DELETE FROM {tabla} WHERE id = {id}"
        try:
            self.execute_query(query)
            '''if self.engine:
                cursor=self.engine.connect()
                query=text(query)
            else:    
                cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()'''
            self.crudLog.append("Registro eliminado con éxito.")
        except self.exceptions as error:
            self.crudLog.append(f"Error al eliminar el registro: {error}")

    # Función para leer todos los campos
    def read_campos(self,tabla):
        campos = []
        try:
            query=f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabla}'"
            campos = self.execute_select(query)
            '''cursor = self.conn.cursor()
            cursor.execute(query)
            campos = cursor.fetchall()'''
            self.crudLog.append(f"Campos consulta en la tabla: {tabla}")
            return campos
        except self.exceptions as error:
            self.crudLog.append(f"Error al leer los campos: {error} (No information_schema)")
        
        try:
            query=f"SELECT name FROM PRAGMA_TABLE_INFO('{tabla}')"
            campos = self.execute_select(query)
            '''cursor = self.conn.cursor()
            cursor.execute(query)
            campos = cursor.fetchall()'''
            self.crudLog.append(f"Campos consulta en la tabla: {tabla}")
            return campos
        except self.exceptions as error:
            self.crudLog.append(f"Error al leer los campos: {error} (No PRAGMA_TABLE_INFO)")

        return self.crudLog
    
    def searchModel(self,Model,vals):
        return self.session.query(Model).get(vals)
    
    def addModel(self,NewModel):
        self.session.add(NewModel)
        self.session.commit()

    def delModel(self,model):
        if model:
            self.session.delete(model)
            self.session.commit()

    # Función para crear tablas
    def crete_table(self):
        pass
    # Función para crear una lista de tablas
    def crete_tables(self):
        pass
    # Función para ejecutar query y hacer commit
    def execute_query(self, query):
        try:
            if self.engine:
                cursor=self.engine.connect()
                query=text(query)
            else:    
                cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            self.crudLog.append("query y commit ejecutado con éxito.")
        except self.exceptions as error:
            self.crudLog.append(f"Error al ejecutar query: {error}")

    # Función para ejecutar query y retornar los datos
    def execute_select(self, query):
        data = []
        try:
            if self.engine:
                cursor=self.engine.connect()
                query=text(query)
            else:    
                cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            self.crudLog.append("query y consulta de datos ejecutado con éxito.")
        except self.exceptions as error:
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

