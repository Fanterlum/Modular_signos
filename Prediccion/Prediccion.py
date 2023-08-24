
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class Prediccion:
    def __init__(self) -> None:
        oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
        oculta2 = tf.keras.layers.Dense(units=3)
        salida = tf.keras.layers.Dense(units=1)
        modelo = tf.keras.Sequential([oculta1, oculta2, salida])
        modelo.compile(
            optimizer=tf.keras.optimizers.Adam(0.1),
            loss='mean_squared_error'
        )
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
    
    def formula(self):
        print("Variables internas del modelo")
        print(oculta1.get_weights())
        print(oculta2.get_weights())
        print(salida.get_weights())
    
