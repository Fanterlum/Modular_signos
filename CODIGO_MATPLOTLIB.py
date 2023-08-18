import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen del electrocardiograma
img = cv2.imread('RECORTE_1.png')

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
cv2.imwrite('RECORTE_1.png', contour_img)

# Mostrar imagen con contornos resaltados
cv2.imshow('Contornos verdes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar la imagen contorno.png utilizando OpenCV
cv2.imshow('Contorno', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Leer la imagen del contorno guardada
contour_img = cv2.imread('RECORTE_1.png', cv2.IMREAD_UNCHANGED)

# Define the color to search for (green)
green = np.array([0, 255, 0, 255], dtype=np.uint8)

# Find the x and y coordinates of the green pixels
y_coords, x_coords = np.where(np.all(contour_img == green, axis=-1))

# Print the x and y coordinates
print("X values:", x_coords)
print("Y values:", y_coords)

# Find the min and max y values for each x value
min_y = {}
max_y = {}
for x, y in zip(x_coords, y_coords):
    if x not in min_y or y < min_y[x]:
        min_y[x] = y
    if x not in max_y or y > max_y[x]:
        max_y[x] = y

# Find the position of the Y lower coordinate in the y_coords array
lower_y = min(y_coords) #coordenada y mas baja
lower_y_pos = np.where(y_coords == lower_y)[0][0]

# Find the X position of the Y lower coordinate
lower_x_pos = x_coords[lower_y_pos] #coordenada x de la coordenada y mas baja

# Find the first point
first_point = (min(x_coords), min_y[min(x_coords)])

# Find the final point
final_point = (max(x_coords), max_y[max(x_coords)])

#find the higher point between the first and the lower point
higher_point = (lower_x_pos, max_y[lower_x_pos])
# get the numer of x between the first and the lower point
x_between = np.where((x_coords > first_point[0]) & (x_coords < lower_x_pos))

# go x_between times to the right and get the y higher value coordinate 
for i in range(x_between[0].shape[0]):
    if y_coords[x_between[0][i]] > higher_point[1]:
        higher_point = (x_coords[x_between[0][i]], y_coords[x_between[0][i]])


# find the higher point between the lower and the final point not the start point
higher_point2 = (lower_x_pos, max_y[lower_x_pos])

# get the number of x between the lower and the final point
x_between2 = np.where((x_coords > lower_x_pos) & (x_coords < final_point[0]))

# get the midpoint of the x_between2 range
midpoint = lower_x_pos + (final_point[0] - lower_x_pos) // 2

# get the number of x between the lower point and the midpoint
x_between2_first_half = np.where((x_coords > lower_x_pos) & (x_coords < midpoint))

# go x_between2_first_half to the right and get the Y higher value coordinate
for i in range(x_between2_first_half[0].shape[0]):
    if y_coords[x_between2_first_half[0][i]] > higher_point2[1]:
        higher_point2 = (x_coords[x_between2_first_half[0][i]], y_coords[x_between2_first_half[0][i]])



# Create a scatter plot of the x and y values
plt.scatter(x_coords, y_coords, s=1)

# Invert the y-axis
plt.gca().invert_yaxis()

# Plot the first, lower, and final points
plt.plot(first_point[0], first_point[1], 'ro', label='First')
plt.plot(lower_x_pos, lower_y, 'go', label='Lower')
plt.plot(final_point[0], final_point[1], 'bo', label='Final')

plt.plot(higher_point[0], higher_point[1], 'yo', label='Higher')
plt.plot(higher_point2[0], higher_point2[1], 'yo', label='Higher2')


print ("higher point: ", higher_point)




# Add a legend
plt.legend()

# Show the plot
plt.show()