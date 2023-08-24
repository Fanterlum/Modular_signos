import numpy as np
import matplotlib.pyplot as plt
class Perceptron():
    
    def __init__(self,n) -> None:
        self.pesos = np.random.randn(n)
        self.n = n

    def propagacion(self,entradas):
        self.salida = 1 * (self.pesos.dot(entradas) > 0)
        self.entradas = entradas

    def actualizacion(self,alfa,salida):
        for i in range(0,self.n):
            self.pesos[i]=self.pesos[i]+alfa*(salida-self.salida)*self.entradas[i]