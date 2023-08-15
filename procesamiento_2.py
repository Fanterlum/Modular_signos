# Código modular
import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# Librerias creadas:
import ImagenV1 as Imagen


# 0) Tiempo donde se ejecuta el código:
print(datetime.now().strftime("%H:%M:%S"),"-", "Ejecutando código... ")




# 1) Cargar imagen del electrocardiograma
#img_name = "E2" 
#folder = "Modular/"
#extension = "jpg"
img_i = cv2.imread('IMG/E12.JPG')
Imagen.imshow(True, img_i, '1) Carga Imagen', 'lower', 'rgb')


#### ACA EMPIEZA EL CÓDIGO

# 1) Obtenemos las propiedades de la imagen:
img_width, img_height = Imagen.Get_Propiedades(img_i)

# 2) Invierte la imagen 
img_i = np.flipud(img_i) #Invierte el eje Y de la imagen
#Imagen.imshow(True, img_i, '2) Invertido', 'lower', 'rgb')


# 3) le aplica filtro blur para quitar un poco el ruido
filtered_mask = cv2.medianBlur(img_i, 5)
#Imagen.imshow_comparacion(True, filtered_mask, '3) filtered', 'lower', 'rgb', img_i)

# 4) rgb a hsv 
hsv = cv2.cvtColor(filtered_mask, cv2.COLOR_BGR2HSV)
#Imagen.imshow(True, hsv, '4) Conversion HSV', 'lower', 'hsv')

# 5) Hace ecualización del canal value del 
hue, saturation, value = cv2.split(hsv)# Dividir los canales HSV
value_equalized = cv2.equalizeHist(value)# Aplicar ecualización de histograma al canal de valor
image_hsv_equalized = cv2.merge((hue, saturation, value_equalized))# Combinar los canales nuevamente en una imagen HSV
# Imagen.imshow(True, image_hsv_equalized, '5) Ecualizado de value del hsv', 'lower', 'hsv')


# 6) mascara de recorte
#ejemplo de como esta: np.array([Hue, Saturation y Value]) (Brillo)
lower_select = np.array([50, 30, 235]) #color RGB  30, 50, 50
upper_select = np.array([80, 255, 255]) #color RGB opciones: 70, 255, 255
mask = cv2.inRange(image_hsv_equalized, lower_select, upper_select)
Imagen.imshow_comparacion(True, mask, '6) mascara de recorte', 'lower', 'gray', img_i)


# 7) Se aplica el closing para huecos que quedan.
kernel = np.ones((2, 2), np.uint8)
closing = cv2.morphologyEx( mask, cv2.MORPH_CLOSE, kernel)
Imagen.imshow_comparacion(True, closing, '7) Closing', 'lower', 'gray', img_i)

# 8) Se aplica el open para quitar un poco el ruido que generó. 
kernel = np.ones((6, 6), np.uint8)
opening = cv2.morphologyEx( closing, cv2.MORPH_OPEN, kernel)
Imagen.imshow_comparacion(True, opening, '8) IMG FINAL HASTA AHORA Opening', 'lower', 'gray', closing)








# fin de código
print(datetime.now().strftime("%H:%M:%S"),"-" ,"Código ejecutado correctamente...")