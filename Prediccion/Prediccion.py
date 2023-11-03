import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import pathlib
import json
#import pandas as pd
from scipy.optimize import curve_fit

class Regression:
    def __init__(self,name_Data) -> None:
        self.name_Data=name_Data
        # Datos de ejemplo
        self.x = np.array([2, 4, 8, 16, 64])
        self.y = np.array([1, 3, 1, 3, 1])

    def data_show(self):
        plt.scatter(self.x,self.y)
        plt.show()

    def CalcularC_Lineares(self):
        # Calcular la media de x y y
        mean_x = np.mean(self.x)
        mean_y = np.mean(self.y)
        # Calcular los coeficientes de la regresión lineal (pendiente y ordenada al origen)
        numerator = np.sum((self.x - mean_x) * (self.y - mean_y))
        denominator = np.sum((self.x - mean_x) ** 2)
        self.slope = numerator / denominator
        self.intercept = mean_y - (self.slope * mean_x)
    # Calcular los coeficientes de la regresión no lineal (a,b,c)
    def CalcularC_NoLineares(self):
        self.popt_f1, pcov_f1 = curve_fit(self.model_f1, self.x, self.y)
        #self.popt_f2, pcov_f2 = curve_fit(self.model_f2, self.x, self.y)
        self.popt_Gaus, pcov_Gaus = curve_fit(self.model_G, self.x, self.y)

    # Crear la función de regresión lineal
    def model_linear(self,x,slope,intercept):
        return slope * x + intercept
    # Crear la función no linear comun
    def model_f1(self,x, a, b, c):
        return a*(x-b)**2 + c
    # Crear la función gauss
    def model_G(self,x,A,mu,sig):
        return A*np.exp(-(x-mu)**2/sig**2)
    # Crear la función
    '''def model_f2(self,r, sigma, epsilon):
        return 4*epsilon*((sigma/r)**12-(sigma/r)**6)'''
    def fit(self,data):
        self.x = np.array(data[0])
        self.y = np.array(data[1])

    def fit_show(self,model,n=100):
        x_model = np.linspace(min(self.x), max(self.x), n)
        if model=="L":
            y_model = self.model_linear(x_model,self.slope,self.intercept)
        elif model=="F1":
            a_opt, b_opt, c_opt = self.popt_f1
            y_model = self.model_f1(x_model, a_opt, b_opt, c_opt)
        elif model=="Gauss":
            a_opt, b_opt, c_opt = self.popt_Gaus
            y_model = self.model_G(x_model, a_opt, b_opt, c_opt)
        '''elif model=="F2":
            a_opt, b_opt, c_opt = self.popt_f2
            y_model = self.model_f2(x_model, a_opt, b_opt)'''
        # Visualizar los datos y la línea de regresión
        plt.scatter(self.x, self.y, label=self.name_Data)
        plt.plot(x_model,y_model, color='r')
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Regresión {self.name_Data}')
        plt.show()

    def predict(self,x,model):# odtener los datos y la línea de regresión
        if model=="L":
            return self.model_linear(x,self.slope,self.intercept)
        elif model=="F1":
            a_opt, b_opt, c_opt = self.popt_f1
            return self.model_f1(x, a_opt, b_opt, c_opt)
        elif model=="Gauss":
            a_opt, b_opt, c_opt = self.popt_Gaus
            return self.model_G(x, a_opt, b_opt, c_opt)
        '''elif model=="F2":
            a_opt, b_opt, c_opt = self.popt_f2
            return self.model_f2(x, a_opt, b_opt, c_opt)'''

class CardiacMetrics:
    def __init__(self) -> None:
        self.rPRIMER_PUNTO = Regression('PRIMER_PUNTO')
        self.rPUNTO_MAS_ALTO = Regression('PUNTO_MAS_ALTO')
        self.rPUNTO_FINAL = Regression('PUNTO_FINAL')
        self.rQ_SIGNAL = Regression('Q')
        self.rS_SIGNAL = Regression('S')
        self.rT_SIGNAL = Regression('T')
        self.rP_SIGNAL = Regression('P')
        #"iniciar red neuronal"
        self.oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
        self.oculta2 = tf.keras.layers.Dense(units=3)
        self.salida = tf.keras.layers.Dense(units=1)
        self.modelo = tf.keras.Sequential([self.oculta1, self.oculta2, self.salida])
        self.modelo.compile(
            optimizer=tf.keras.optimizers.Adam(0.1),
            loss='mean_squared_error'
        )

    def statusFibrilacion(self,p,q,r,s,t):
        tolerancia=10
        if p>(r-tolerancia):
            return 1
        elif q>(r-tolerancia):
            return 1
        elif s>(r-tolerancia):
            return 1
        elif t>(r-tolerancia):
            return 1
        else:
            return 0
    def statusTaquicardia(self,q,s):
        status=1
        t=20
        pS=self.modelo.predict([q])[0][0]
        rQ=self.rQ_SIGNAL.predict(s,"F1")
        if s > pS-t and pS+t > s:
            if q > rQ-t and rQ+t > q:
                status=0
        return status

    def status(self,file="JS_14_4.json"):
        dir = f'{os.getcwd()}/paciente/test/'
        with open(dir+file,"r") as f:
                data = json.load(f)
                onda=(500-data["PRIMER_PUNTO_Y"],
             
                    500-data["P_SIGNAL_Y"],
                    500-data["Q_SIGNAL_Y"],

                    500-data["PUNTO_MAS_ALTO_Y"],

                    500-data["S_SIGNAL_Y"],
                    500-data["T_SIGNAL_Y"],

                    500-data["PUNTO_FINAL_Y"]
                )
        return self.statusFibrilacion(
            onda[1],
            onda[2],
            onda[3],
            onda[4],
            onda[5])+self.statusTaquicardia(onda[2],onda[4])

    def fit(self,FolderMetrics="paciente"):
        '''pRIMER_PUNTO =[]
        pUNTO_MAS_ALTO =[]
        pUNTO_FINAL =[]
        q_SIGNAL =[]
        s_SIGNAL =[]
        t_SIGNAL =[]
        p_SIGNAL =[]'''
        ondas=[]
        if not FolderMetrics is None:
            #se odtiene la ruta acsoluta 
            # y se concatena con el nombre de la carpeta
            dir = f'{os.getcwd()}/{FolderMetrics}/'
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
        for file in filesNames:
            with open(dir+file,"r") as f:
                data = json.load(f)

            ondas.append(
            (500-data["PRIMER_PUNTO_Y"],
             
            500-data["P_SIGNAL_Y"],
            500-data["Q_SIGNAL_Y"],

            500-data["PUNTO_MAS_ALTO_Y"],

            500-data["S_SIGNAL_Y"],
            500-data["T_SIGNAL_Y"],

            500-data["PUNTO_FINAL_Y"]))

            '''500-data["PRIMER_PUNTO_Y"],
            500-data["PUNTO_MAS_ALTO_Y"],
            500-data["PUNTO_FINAL_Y"],
            500-data["Q_SIGNAL_Y"],
            500-data["S_SIGNAL_Y"],
            500-data["T_SIGNAL_Y"],
            500-data["P_SIGNAL_Y"]'''
        
        '''pRIMER_PUNTO.sort()
        pUNTO_MAS_ALTO.sort()
        pUNTO_FINAL.sort()
        q_SIGNAL.sort()
        s_SIGNAL.sort()
        t_SIGNAL.sort()
        p_SIGNAL.sort()'''

        orderOndas=sorted(ondas,key=lambda onda : onda[2])
        nOndas=len(orderOndas)
        #x_list=[x for x in range(nOndas)]
        x_list=[onda[4] for onda in orderOndas]
        self.rPRIMER_PUNTO.fit([x_list,[onda[0] for onda in orderOndas]])

        self.rP_SIGNAL.fit([x_list,[onda[1] for onda in orderOndas]])
        self.rQ_SIGNAL.fit([x_list,[onda[2] for onda in orderOndas]])

        self.rPUNTO_MAS_ALTO.fit([x_list,[onda[3] for onda in orderOndas]])
        
        #self.rS_SIGNAL.fit([x_list,[onda[4] for onda in orderOndas]])
        self.rT_SIGNAL.fit([x_list,[onda[5] for onda in orderOndas]])

        self.rPUNTO_FINAL.fit([x_list,[onda[6] for onda in orderOndas]])

        self.rPRIMER_PUNTO.CalcularC_Lineares()
        
        
        self.rP_SIGNAL.CalcularC_NoLineares()
        self.rQ_SIGNAL.CalcularC_NoLineares()

        #self.rPUNTO_MAS_ALTO.CalcularC_Lineares()

        #self.rS_SIGNAL.CalcularC_NoLineares()
        self.rT_SIGNAL.CalcularC_Lineares()
        

        self.rPUNTO_FINAL.CalcularC_Lineares()
        print("Comenzando entrenamiento...")
        model_Q=np.array([self.rQ_SIGNAL.predict(x_list[i],"F1") for i in range(nOndas)], dtype=int)
        model_S=np.array(x_list, dtype=int)
        simetria= self.modelo.fit(model_Q, model_S, epochs=45, verbose=False)
        print("Modelo entrenado!")

        '''plt.xlabel("# Epoca")
        plt.ylabel("Magnitud de pérdida")
        plt.plot(simetria.history["loss"])'''
        

    def show_test(self):
        q=self.rQ_SIGNAL.predict(215,"F1")
        s=self.modelo.predict([216])[0][0]
        print(s)
        print(q)
        print(self.statusTaquicardia(q,s))
        print("status:",self.status())
        print("status:",self.status("JS_9_2.json"))
        self.rPRIMER_PUNTO.fit_show("L")
        self.rP_SIGNAL.fit_show("F1")

        self.rQ_SIGNAL.fit_show("F1")

        #self.rPUNTO_MAS_ALTO.fit_show("L")

        #self.rS_SIGNAL.fit_show("F1")

        self.rT_SIGNAL.fit_show("L")
        self.rPUNTO_FINAL.fit_show("L")

    def show_capas(self):
        print("Variables internas del modelo")
        print(self.oculta1.get_weights())
        print(self.oculta2.get_weights())
        print(self.salida.get_weights())

'''
def distQR(self):
        x1,x2=self.__cordQRS['Q'][0],self.__cordQRS['R'][0]
        y1,y2=self.__cordQRS['Q'][1],self.__cordQRS['R'][1]
        return np.sqrt(((x1-x2)**2)+((y1-y2)**2))
    def distRS(self):
        x1,x2=self.__cordQRS['S'][0],self.__cordQRS['R'][0]
        y1,y2=self.__cordQRS['S'][1],self.__cordQRS['R'][1]
        return np.sqrt(((x1-x2)**2)+((y1-y2)**2))
def setOnda(self,ondax,ondaY):
        print("Comenzando entrenamiento...")
        historial = modelo.fit(ondax, ondaY, epochs=1000, verbose=False)
        print("Modelo entrenado!")

        plt.xlabel("# Epoca")
        plt.ylabel("Magnitud de pérdida")
        plt.plot(historial.history["loss"])

    def predicion(self,x):
        print("Hagamos una predicción!")
        resultado = modelo.predict([x])
        print("El resultado es " + str(resultado))
    
    '''
