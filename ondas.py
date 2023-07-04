import os
import pathlib
import time
#import psycopg2

import cv2
import numpy as np
import matplotlib.pyplot as plt

#falimiliares
#doctor 
#paciente
#guardar solo cordenadas y vectores 
'''class DatabaseManager:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="",
            user="",
            password="",
            host="localhost",
            port="5435"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def execute_select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()'''
class Onda:
    def __init__(self,x,y,id) -> None:
        self.id=id
        self.serialKey=f'{x}{id}{y}'
        self.pos=[-1,-1]
        self.__cordP={
            'Ini':[-1,-1],
            'P':[-1,-1],
            'Fin':[-1,-1],
        }
        self.__cordQRS={
            'Ini':[-1,-1],
            'Q':[-1,-1],

            'R':[x,y],
        
            'S':[-1,-1],
            'Fin':[-1,-1],
        }
        self.__cordT={
            'Ini':[-1,-1],
            'T':[-1,-1],
            'Fin':[-1,-1],
        }

    
    def buscarCord_R(self):
        pass
    def buscarCord_Q(self):
        pass
    def buscarCord_S(self):
        pass
    def buscarCord_P(self):
        pass
    def buscarCord_T(self):
        pass

    def getQRS(self):
        return self.__cordQRS
    def getP(self):
        return self.__cordP
    def getCorT(self):
        return self.__cordT
    
    def getComplQRS(self):
        return {
            'Ini':self.__cordQRS['Ini'],
            'Fin':self.__cordQRS['Fin']
        }
    def getSegtPR(self):
        return {
            'Ini':self.__cordP['Fin'],
            'Fin':self.__cordQRS['Ini']
        }
    def getSegtST(self):
        return {
            'Ini':self.__cordQRS['Fin'],
            'Fin':self.__cordT['Ini']
        }
    def getIntvPR(self):
        return {
            'Ini':self.__cordP['Ini'],
            'Fin':self.__cordQRS['Ini']
        }
    def getIntvQT(self):
        return {
            'Ini':self.__cordQRS['Ini'],
            'Fin':self.__cordT['Fin']
        }
    def getSistole(self):
        return {
            'Ini':self.__cordP['Ini'],
            'Fin':self.__cordQRS['Fin']
        }
    def getDiastole(self):
        return {
            'Ini':self.__cordQRS['Fin'],
            'Fin':self.__cordT['Fin']
        }
    
class Ondas:
    def __init__(self,imgOndas) -> None:
        self.__imgOndas = imgOndas
        self.__ondas = []

    def getIMG(self):
        return self.__imgOndas

    def getRR(self,id1,id2):
        pass

class fotograma:
    def __init__(self,img=None) -> None:
        self.id=""
        #self.ruta = os.getcwd()
        #self.nombreArchivo = 'images4.jpeg'

        if not img is None:
            imagen = img.copy()
            self.__ondas=Ondas(
                self.lineasElectro(
                    self.enfoque(imagen)
                )
            )
    
    def lineasElectro(self,img):
        # Convertir imagen a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Aplicar umbralización para resaltar las líneas verdes
        _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

        # Encontrar contornos en la imagen umbralizada
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filtrar contornos por su color verde
        green_contours = []
        for contour in contours:
            # Obtener el promedio del color en el contorno
            mask = np.zeros(gray.shape, dtype=np.uint8)
            cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
            mean_color = cv2.mean(img, mask=mask)[:3]  # Canal BGR

            # Comprobar si el color está dentro del rango verde
            if mean_color[1] > mean_color[0] and mean_color[1] > mean_color[2]:
                green_contours.append(contour)

        # Dibujar contornos en la imagen original
        cv2.drawContours(img, green_contours, -1, (0, 255, 0), thickness=2)

        # Crear una imagen con transparencia del mismo tamaño que la original
        contour_img = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)

        # Dibujar contornos en la imagen con transparencia
        cv2.drawContours(contour_img, green_contours, -1, (0, 255, 0, 255), thickness=cv2.FILLED)

        # Guardar la imagen del contorno en un archivo con canal alfa
        #cv2.imwrite('IMG\contorno.png', contour_img)

        # Mostrar imagen con contornos resaltados
        #cv2.imshow('Contornos verdes', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        # Mostrar la imagen contorno.png utilizando OpenCV
        #cv2.imshow('Contorno', contour_img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        # Leer la imagen del contorno guardada
        #contour_img = cv2.imread('IMG\contorno.png', cv2.IMREAD_UNCHANGED)

        # Convertir la imagen a RGB para ser compatible con Matplotlib
        contour_img_rgb = cv2.cvtColor(contour_img, cv2.COLOR_BGRA2RGBA)

        # Mostrar la imagen del contorno utilizando Matplotlib
        '''plt.imshow(contour_img_rgb)
        plt.axis('on')
        plt.show()'''
        return contour_img
    
    def enfoque(self,img):
        cIni=int((img.shape[0]/100)*10)
        cFin=int(img.shape[0]-(cIni*2))
        f=int(img.shape[1]-((img.shape[1]/100)*75))
        imgOut=img[0:f,cIni:cFin]
        return imgOut
    
    def getFotograma(self):
        return self.__ondas.getIMG()

class fotogramas:
    def __init__(self,carpeta=None) -> None:
        self.__fotogramas=[]
        if not carpeta is None:
            #se odtiene la ruta acsoluta 
            # y se concatena con el nombre de la carpeta
            dir = f'{os.getcwd()}/{carpeta}/'
            #se revisa el contenido de la carpeta
            directorio = pathlib.Path(dir)
            #se crea una lista para guardar los nombres de los archivos 
            filesNames = []
            #se recore cada fichero para filtrar los archivos
            for fichero in directorio.iterdir():
                if fichero.is_file():
                    filesNames.append(fichero.name)
            #se organizan los nombres de los archivos 
            filesNames.sort()
            #se carga cada imagen como fotograma
            for imgName in filesNames:
                print(imgName)
                rutaAbrir = os.path.join(dir, imgName)
                # Cargar imagenes del electrocardiograma
                self.__fotogramas.append(
                    fotograma(cv2.imread(rutaAbrir))
                )

    def getVideo(self):
        #se odtiene el numero de fotogramas 
        nfts=len(self.__fotogramas)
        #si no hay fotogramas se odtienen de la camara de video
        if nfts == 0:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                self.__fotogramas.append(
                    fotograma(img)
                )
                if cv2.waitKey(1)==27:
                    break
            cap.release()
        #si hay fotogramas se odtienen de la camara de video
        else:
            i=0 
            while True:
                if cv2.waitKey(1)==27:
                    break
                time.sleep(0.5)
                if i == nfts:
                   i=0 
                else: 
                    cv2.imshow("video",self.__fotogramas[i].getFotograma())
                    i+=1
                
