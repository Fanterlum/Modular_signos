import tensorflow as tf
import numpy as np

#se resive el archivo .json en este caso de manera 
#simulada para el testing 

'''onda={
    "PRIMER_PUNTO_X": 0, 
    "PRIMER_PUNTO_Y": 262, 
    "PUNTO_MAS_ALTO_X": 80, 
    "PUNTO_MAS_ALTO_Y": 106, 
    "PUNTO_FINAL_X": 216, 
    "PUNTO_FINAL_Y": 283, 
    "Q_SIGNAL_X": 60, 
    "Q_SIGNAL_Y": 273, 
    "S_SIGNAL_X": 88, 
    "S_SIGNAL_Y": 283, 
    "T_SIGNAL_X": 164, 
    "T_SIGNAL_Y": 209, 
    "P_SIGNAL_X": 23, 
    "P_SIGNAL_Y": 253
}'''
# prosesan los datos de del archivo y se ordenana para sacar
# las metricas usando el algoritmo de la carperta extras con el
#odjeto llamado ondas 
onda={
    "PRIMER_PUNTO_X": 0, 
    "PRIMER_PUNTO_Y": 262, 
    
    "P_SIGNAL_X": 23, 
    "P_SIGNAL_Y": 253,

    "Q_SIGNAL_X": 60, 
    "Q_SIGNAL_Y": 273, 

    "PUNTO_MAS_ALTO_X": 80, 
    "PUNTO_MAS_ALTO_Y": 106, 

    "S_SIGNAL_X": 88, 
    "S_SIGNAL_Y": 283, 

    "T_SIGNAL_X": 164, 
    "T_SIGNAL_Y": 209, 
    
    "PUNTO_FINAL_X": 216, 
    "PUNTO_FINAL_Y": 283
}
print(list(onda.values())) # valores que simulan las metricas 
cordenadas = list(onda.values()) 
DataSetX = []
DataSetY = []
i=0
#se crean los data sets
while i <= len(cordenadas)-1:
    DataSetX.append(cordenadas[i])
    i+=1
    DataSetY.append(300-cordenadas[i])
    i+=1
xOnda = np.array(DataSetX, dtype=int)
yOnda = np.array(DataSetY, dtype=int)
print(DataSetX,DataSetY)
#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])
#se crea la red neuronal
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=15)
oculta3 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=2)
modelo = tf.keras.Sequential([oculta1, oculta2, oculta3, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.6),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(xOnda, yOnda, epochs=3500, verbose=False)
print("Modelo entrenado!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

print("Hagamos una predicción!")
resultado = modelo.predict([80])
print("El resultado es " + str(resultado) + " punto mas alto")

print("Variables internas del modelo")
#print(capa.get_weights())
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())