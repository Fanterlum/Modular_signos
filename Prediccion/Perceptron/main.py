from perceptron import Perceptron as Neurona

#se crea una neurona 
neu_tres_entradas = Neurona(2)
print(f"pesos iniciales: {neu_tres_entradas.pesos}")


nivel_de_aprendizaje=0.8

entradas=[[10,10],[40,45],[14,5],[15,15],[10,1],[11,11],[30,35],[14,5]]

salidas=[1,1,1,0,0,1,1,1]
for i in range(2500):
    for i in range(8):
        print(f"pesos: {neu_tres_entradas.pesos}")
        neu_tres_entradas.propagacion(entradas[i])
        neu_tres_entradas.actualizacion(nivel_de_aprendizaje,salidas[i])
        #print(f"pesos: {neu_tres_entradas.pesos}")
        #print(f"salida de {entradas[i]}: {neu_tres_entradas.salida}")

print("         resultado: ")
for i in range(8):
    neu_tres_entradas.propagacion(entradas[i])
    print(f"salida de {entradas[i]}: {neu_tres_entradas.salida}")
