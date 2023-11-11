from Algoritmos import distancia_euclidiana
from random import randint
import json
class Particula:
    def __init__(self,id,origen=[],destino=[],parametros=[],rgb=[]) -> None:
        self.__id=int(id)
        if len(origen)==0:
            self.__origen_x =randint(0,500)
            self.__origen_y =randint(0,500)
        else:
            self.__origen_x =int(origen[0])
            self.__origen_y =int(origen[1])
        if len(destino)==0:
            self.__destino_x=-1
            self.__destino_y=-1
        else:
            self.__destino_x=int(destino[0])
            self.__destino_y=int(destino[1])
        if len(parametros)==0:
            self.__velocidad=randint(0,500)
            self.__distancia=-1
            # 
        else:
            self.__velocidad=parametros[0]
            self.__distancia=distancia_euclidiana(self.__origen_x,self.__origen_y,destino[0],destino[1])

        if len(rgb)==0:
            self.__red,self.__green,self.__blue=randint(0,250),randint(0,250),randint(0,250)
        else:
            self.__red,self.__green,self.__blue=int(rgb[0]),int(rgb[1]),int(rgb[2])
    def setDestino(self,maxDist=-1,destino=[]) :
        
        if len(destino)==0:
            self.__destino_x=-1
            self.__destino_y=-1
            self.__distancia=-1
        elif maxDist == -1 :
            distTemp=distancia_euclidiana(self.__origen_x,self.__origen_y,destino[0],destino[1])
            maxDist=self.__distancia
            if maxDist >= distTemp or self.distancia==-1 :
                self.__destino_x=int(destino[0])
                self.__destino_y=int(destino[1])
                self.__distancia=distTemp
        else:
            distTemp=distancia_euclidiana(self.__origen_x,self.__origen_y,destino[0],destino[1])
            if maxDist >= distTemp:
                self.__destino_x=int(destino[0])
                self.__destino_y=int(destino[1])
                self.__distancia=distTemp
    def getCord(self):
        return [[self.__origen_x,self.__origen_y],[self.__destino_x,self.__destino_y]]
    def validarConexion(self,cord=[[],[]]):
        valDest=False
        valOrg=False
        if len(cord)==2:
            if len(cord[0])==2 and len(cord[1])==2:
                valDest = self.__origen_x==cord[1][0] and self.__origen_y==cord[1][1]
                valOrg = self.__destino_x==cord[0][0] and self.__destino_y==cord[0][1]
        return valDest or valOrg
        
    @property
    def id(self):
        return self.__id
    @property
    def origen_x(self):
        return self.__origen_x
    @property
    def origen_y(self):
        return self.__origen_y
    @property
    def destino_x(self):
        return self.__destino_x
    @property
    def destino_y(self):
        return self.__destino_y
    @property
    def velocidad(self):
        return self.__velocidad
    @property
    def distancia(self):
        return self.__distancia
    @property
    def red(self):
        return self.__red
    @property
    def green(self):
        return self.__green
    @property
    def blue(self):
        return self.__blue
    def to_dict(self):
        return {"ID":self.__id,
        "origen":[self.__origen_x,self.__origen_y],
        "destino":[self.__destino_x,self.__destino_y],
        "parametros":[self.__velocidad,self.__distancia],
        "RGB":[self.__red,self.__green,self.__blue]}
    def to_dict2(self):
        return {"id":self.__id,
        "origen_x":self.__origen_x,
        "origen_y":self.__origen_y,
        "destino_x":self.__destino_x,
        "destino_y":self.__destino_y,
        "red":self.__red,
        "green":self.__green,
        "blue":self.__blue,
        "velocidad":self.__velocidad
        }
    def __str__(self) -> str:
        return (f'id:{self.__id} '+
        f'origen_x: {self.__origen_x} '+
        f'origen_y: {self.__origen_y} ' +
        f'destino_x: {self.__destino_x} ' +
        f'destino_y: {self.__destino_y} ' +
        f'RGB:({self.__red},{self.__green},{self.__blue}) ' +
        f'distancia:{self.__distancia} ')

class GestorParticulas:
    def __init__(self) -> None:
        self.__particulas=[]
    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)
    def getParticula(self,pos):
        return self.__particulas[pos]
    def ver(self):
        for particula in self.__particulas:
            print(particula)
    def limpiar(self):
        while(len(self.__particulas)>0):
            self.__particulas.pop()
    def guardar(self,ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista=[particula.to_dict2() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo,indent=5)
                return 1
        except:
            return 0
    
    def abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista=json.load(archivo)
                self.__particulas=[
                    Particula(
                        particula["ID"],
                        particula["origen"],
                        particula["destino"],
                        particula["parametros"],
                        particula["RGB"]
                        ) 
                    for particula in lista
                    ]
                return 1
        except:
            return 0
    def abrir2(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista=json.load(archivo)
                self.__particulas=[
                    Particula(
                        particula["id"],
                        origen=[particula["origen_x"],particula["origen_y"]],
                        destino=[particula["destino_x"],particula["destino_y"]],
                        parametros=[particula["velocidad"]],
                        rgb=[particula["red"],particula["green"],particula["blue"]]
                        ) 
                    for particula in lista
                    ]
                return 1
        except:
            return 0
    def getMatriz(self):
        nParticulas=len(self.__particulas)
        text="grafo={\n"
        for nParticula in range(0,nParticulas):
            line=f'{self.__particulas[nParticula].id}:('
            vacio=True
            conectado = False
            
            for pos in range(nParticula+1,nParticulas):
                conectado=self.__particulas[nParticula].validarConexion(self.__particulas[pos].getCord())
                
                if conectado:
                    line+=f'{self.__particulas[pos].id},'
                    vacio=False
                    
            if not vacio:
                text+=(line+")"+"\n")
        text+="aislados:("
        for particula in self.__particulas:
            if particula.destino_y==-1 and particula.destino_x==-1:
                text+=f'{particula.id},'
        text+=")\n}"
        return text
        

    def conect(self,max):
        
        for tempPartOrg in self.__particulas:
            tempPartOrg.setDestino()
        for tempPartOrg in self.__particulas:
            maxDist=max
            for tempPartDes in self.__particulas:
                if tempPartDes.id != tempPartOrg.id :
                    tempPartOrg.setDestino(maxDist,[tempPartDes.origen_x,tempPartDes.origen_y])
                    if tempPartOrg.distancia !=-1:
                        maxDist=tempPartOrg.distancia
                    
                    
    def sort(self,element=0,rev=False):
        if (element==0):
            def sort_id(p):
                return p.id
            self.__particulas.sort(reverse=rev,key=sort_id)
        elif (element==1):
            def sort_distancia(p):
                return p.distancia
            self.__particulas.sort(reverse=rev,key=sort_distancia)
        elif (element==2):
            def sort_velocidad(p):
                return p.velocidad
            self.__particulas.sort(reverse=rev,key=sort_velocidad)
        elif (element==3):
            def sort_origen_x(p):
                return p.origen_x
            self.__particulas.sort(reverse=rev,key=sort_origen_x)
        elif (element==4):
            def sort_origen_y(p):
                return p.origen_y
            self.__particulas.sort(reverse=rev,key=sort_origen_y)
        elif (element==5):
            def sort_destino_x(p):
                return p.destino_x
            self.__particulas.sort(reverse=rev,key=sort_destino_x)
        elif (element==6):
            def sort_destino_y(p):
                return p.destino_y
            self.__particulas.sort(reverse=rev,key=sort_destino_y)
        else:
            self.__particulas.sort()
    def __str__(self): 
        return "".join(
            str(particula)+"\n" for particula in self.__particulas
        )
    def __len__(self):
        return len(self.__particulas)
    def __iter__(self):
        self.cont=0
        return self
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
    