import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen del electrocardiograma
img = cv2.imread('IMG/electro1.JPG')

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
cv2.imwrite('IMG\contorno.png', contour_img)

# Mostrar imagen con contornos resaltados
cv2.imshow('Contornos verdes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar la imagen contorno.png utilizando OpenCV
cv2.imshow('Contorno', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Leer la imagen del contorno guardada
contour_img = cv2.imread('IMG\contorno.png', cv2.IMREAD_UNCHANGED)

# Define the color to search for (green)
green = np.array([0, 255, 0, 255], dtype=np.uint8)

# Find the x and y coordinates of the green pixels
y_coords, x_coords = np.where(np.all(contour_img == green, axis=-1))

# Print the x and y coordinates
print("X values:", x_coords)
print("Y values:", y_coords)

# Create a scatter plot of the x and y values
plt.scatter(x_coords, y_coords, s=1)
# Invert the y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()



# Convertir la imagen a RGB para ser compatible con Matplotlib
#contour_img_rgba = cv2.cvtColor(contour_img, cv2.COLOR_BGRA2RGBA)




# Mostrar la imagen del contorno utilizando Matplotlib
#plt.imshow(contour_img_rgba)
#plt.axis('on')
#plt.show()
