import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import pathlib
import json
#import pandas as pd
from scipy.optimize import curve_fit

class Regression:
    def __init__(self) -> None:
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
        plt.scatter(self.x, self.y, label='Datos de ejemplo')
        plt.plot(x_model,y_model, color='r')
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Regresión ')
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
        self.rPRIMER_PUNTO = Regression()
        self.rPUNTO_MAS_ALTO = Regression()
        self.rPUNTO_FINAL = Regression()
        self.rQ_SIGNAL = Regression()
        self.rS_SIGNAL = Regression()
        self.rT_SIGNAL = Regression()
        self.rP_SIGNAL = Regression()
        #"iniciar red neuronal"
        oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
        oculta2 = tf.keras.layers.Dense(units=3)
        salida = tf.keras.layers.Dense(units=1)
        modelo = tf.keras.Sequential([oculta1, oculta2, salida])
        modelo.compile(
            optimizer=tf.keras.optimizers.Adam(0.1),
            loss='mean_squared_error'
        )

    def search(self):
        pass

    def predictNeuronal(self):
        pass

    def predictRegression(self):
        pass

    def predict(self):
        pass

    def statusNeuronal(self):
        pass

    def statusRegression(self):
        pass

    def status(self):
        pass

    def fit(self,FolderMetrics="paciente"):
        pRIMER_PUNTO =[]
        pUNTO_MAS_ALTO =[]
        pUNTO_FINAL =[]
        q_SIGNAL =[]
        s_SIGNAL =[]
        t_SIGNAL =[]
        p_SIGNAL =[]
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
            pRIMER_PUNTO.append(data["PRIMER_PUNTO_Y"])
            pUNTO_MAS_ALTO.append(data["PUNTO_MAS_ALTO_Y"])
            pUNTO_FINAL.append(data["PUNTO_FINAL_Y"])
            q_SIGNAL.append(data["Q_SIGNAL_Y"])
            s_SIGNAL.append(data["S_SIGNAL_Y"])
            t_SIGNAL.append(data["T_SIGNAL_Y"])
            p_SIGNAL.append(data["P_SIGNAL_Y"])
        
        self.rPRIMER_PUNTO.fit([[x for x in range(len(pRIMER_PUNTO))],pRIMER_PUNTO])
        self.rPUNTO_MAS_ALTO.fit([[x for x in range(len(pUNTO_MAS_ALTO))],pUNTO_MAS_ALTO])
        self.rPUNTO_FINAL.fit([[x for x in range(len(pUNTO_FINAL))],pUNTO_FINAL])
        self.rQ_SIGNAL.fit([[x for x in range(len(q_SIGNAL))],q_SIGNAL])
        self.rS_SIGNAL.fit([[x for x in range(len(s_SIGNAL))],s_SIGNAL])
        self.rT_SIGNAL.fit([[x for x in range(len(t_SIGNAL))],t_SIGNAL])
        self.rP_SIGNAL.fit([[x for x in range(len(p_SIGNAL))],p_SIGNAL])

        self.rPRIMER_PUNTO.CalcularC_NoLineares()
        self.rPUNTO_MAS_ALTO.CalcularC_NoLineares()
        self.rPUNTO_FINAL.CalcularC_NoLineares()
        self.rQ_SIGNAL.CalcularC_NoLineares()
        self.rS_SIGNAL.CalcularC_NoLineares()
        self.rT_SIGNAL.CalcularC_NoLineares()
        self.rP_SIGNAL.CalcularC_NoLineares()

    def show_test(self):
        self.rPRIMER_PUNTO.fit_show("F2")
        self.rPUNTO_MAS_ALTO.fit_show("F2")
        self.rPUNTO_FINAL.fit_show("F2")
        self.rQ_SIGNAL.fit_show("F2")
        self.rS_SIGNAL.fit_show("F2")
        self.rT_SIGNAL.fit_show("F2")
        self.rP_SIGNAL.fit_show("F2")

'''def setOnda(self,ondax,ondaY):
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
    
    def formula(self):
        print("Variables internas del modelo")
        print(oculta1.get_weights())
        print(oculta2.get_weights())
        print(salida.get_weights())'''