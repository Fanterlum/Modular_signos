import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
GREEN=[0,255,0,255]
NONCOLOR=[0,0,0,0]
def slimUp(slimPx,imgLine):
    imagen = imgLine.copy()
    #slimPX almacena el grosor en px, de la linea resultante 
    antfil = None #almacena la fila con el ultimo px verde de la columna anterior 
    filVerde =None #almacena la fila con el ultimo px verde de la columna 
    #recorre las columnas 
    for col in range(imagen.shape[1]):
        nPx=0# almacena el numero de pixeles verdes en la columna
        # recorre los px segun las filas de la colunna 
        for fil in range(imagen.shape[0]):
            #verifica si el px es verde 
            if (set(imagen[fil, col]) == set(GREEN)):
                #aumentan los px verdes
                nPx+=1
                #verifica si los px verdes aun no son los requeridos en la columna
                if nPx>=1 and nPx<=slimPx:
                    #actualiza la posision del ultimo px verde de la columna
                    filVerde=fil
                #verifica si los px verdes ya son los requeridos en la columna
                elif nPx>=slimPx:
                    #si el px de la columna anterior existe y es mayor, sige 
                    #permitiendo px verdes de lo contrario los elimina 
                    imagen[fil, col] = GREEN if not antfil is None and antfil > fil else NONCOLOR 
                #si no son px verdes
                '''else:
                    #elimina los pixeles 
                    imagen[fil, col] = NONCOLOR'''
        #mientras el px de la columna anterior existe y su posision es menor
        while not antfil is None and antfil < filVerde:
            #Actualiza el ultimo px verde de la columna anterior 
            antfil+=1 
            #cambia el ultimo px verde de la columna anterior a verde XD
            imagen[antfil, col-1] = GREEN
        #Actualiza el ultimo px verde de la columna anterior a el ultimo px verde de la columna 
        antfil= filVerde

    cv2.imshow('Adelgazado Superior', imagen)
    return imagen

def slimDown(slimPx,imgLine):
    imagen = imgLine.copy()
    antfil = None 
    filVerde =None 
    for col in range(imagen.shape[1]):
        nPx=0
        for fil in range(imagen.shape[0]-1,0,-1):
            if (set(imagen[fil, col]) == set(GREEN)):
                nPx+=1
                if nPx>=1 and nPx<=slimPx:
                    filVerde=fil
                elif nPx>=slimPx:
                    #si el px de la columna anterior existe y es menor, sige 
                    #permitiendo px verdes de lo contrario los elimina 
                    imagen[fil, col] = GREEN if not antfil is None and antfil < fil else NONCOLOR 
        #mientras el px de la columna anterior existe y su posision es mayor
        while not antfil is None and antfil > filVerde:
            #Actualiza el ultimo px verde de la columna anterior 
            antfil-=1 
            imagen[antfil, col-1] = GREEN
        antfil= filVerde

    cv2.imshow('Adelgazado inferior', imagen)
    return imagen
# Cargar imagen del electrocardiograma
img = cv2.imread('IMG_test/images3.jpeg')

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
cv2.imwrite('IMG/contorno.png', contour_img)

# Leer la imagen del contorno guardada
contour_img = cv2.imread('IMG/contorno.png', cv2.IMREAD_UNCHANGED)

# Convertir la imagen a escala de grises
#gray_contour = cv2.cvtColor(contour_img, cv2.COLOR_BGR2GRAY)
gray_contour = cv2.cvtColor(slimDown(5,contour_img), cv2.COLOR_BGR2GRAY)#funcion adelgasar implementada
#gray_contour = cv2.cvtColor(slimUp(2,contour_img), cv2.COLOR_BGR2GRAY)#funcion adelgasar implementada

# Aplicar el algoritmo de detección de picos a la señal del electrocardiograma
#peaks, _ = find_peaks(gray_contour.flatten(), height=50)
#peaks, _ = find_peaks(gray_contour.flatten(), height=50,distance=12,prominence=12,width=8)#parametros para linea gruesa
peaks, _ = find_peaks(gray_contour.flatten(), height=50,distance=44,prominence=2,width=4)#parametros para linea delgada

# Dibujar los picos en la imagen del contorno
print(f'picos :{len(peaks)}')
a=0
b=0
c=225
d=225
for peak in peaks:
    #RGB Filtrado de picos 
    #identificar puntos importantes 
    if 225>=a:
        a+=5
    elif 225>=b:
        b+=5
    elif c>=225:
        c-=5
    elif d>=225:
        d-=5

    cv2.circle(contour_img, (peak % contour_img.shape[1], peak // contour_img.shape[1]), 1, (d, a, b, c), -1)

# Guardar la imagen con los picos detectados
cv2.imwrite('IMG/contorno_con_picos.png', contour_img)

# Mostrar la imagen con contornos resaltados
cv2.imshow('Contornos verdes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar la imagen del contorno con los picos detectados
cv2.imshow('Contorno con picos', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Leer la imagen del contorno con los picos detectados
contour_img_with_peaks = cv2.imread('IMG/contorno_con_picos.png', cv2.IMREAD_UNCHANGED)

# Convertir la imagen a RGB para ser compatible con Matplotlib
contour_img_rgba = cv2.cvtColor(contour_img_with_peaks, cv2.COLOR_BGRA2RGBA)

# Mostrar la imagen del contorno con los picos detectados utilizando Matplotlib
plt.imshow(contour_img_rgba)
plt.axis('on')
plt.show()