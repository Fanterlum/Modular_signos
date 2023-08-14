import cv2
import numpy as np

def reduce_excess_light(image_path):
    # Leer la imagen
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convertir la imagen a escala de grises
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar la compresión de histograma (equalización del histograma)
    equ_img = cv2.equalizeHist(gray_img)

    # Detección de bordes usando el operador de Canny
    edges = cv2.Canny(equ_img, 50, 150)

    # Convertir las líneas detectadas a color verde (0, 255, 0)
    output_img = cv2.merge((edges, edges, edges))

    return output_img

# Ruta de la imagen de entrada
input_image_path = 'IMG/E12.JPG'

# Obtener la imagen procesada con líneas resaltadas
output_image = reduce_excess_light(input_image_path)

# Mostrar la imagen original y la imagen procesada con líneas resaltadas
cv2.imshow('Imagen Original', cv2.imread(input_image_path))
cv2.imshow('Imagen Procesada', output_image)

# Guardar la imagen del contorno en un archivo con canal alfa
cv2.imwrite('IMG\luz4.png', output_image)

# Esperar hasta que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

