import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
import os

# Directory containing the images
image_dir = 'IMG/JOSE_RAMON'

# List of image file names in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png') or f.endswith('.jpg')]


for image_file in image_files:
    # Cargar imagen del electrocardiograma
    #img = cv2.imread('IMG\RECORTE3.JPG')
    img = cv2.imread(os.path.join(image_dir, image_file))


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

    # Aproximar los contornos para adelgazar las líneas
    approx_green_contours = [cv2.approxPolyDP(contour, epsilon=0.5, closed=True) for contour in green_contours]

    # Dibujar contornos en la imagen original
    cv2.drawContours(img, approx_green_contours, -1, (0, 255, 0), thickness=2)

    # Crear una imagen con transparencia del mismo tamaño que la original
    contour_img = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)

    # Dibujar contornos en la imagen con transparencia
    cv2.drawContours(contour_img, approx_green_contours, -1, (0, 255, 0, 255), thickness=cv2.FILLED)

    # Guardar la imagen del contorno en un archivo con canal alfa
    cv2.imwrite(os.path.join(image_dir, image_file), contour_img)

    # Mostrar imagen con contornos resaltados
    #cv2.imshow('Contornos verdes', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Mostrar la imagen contorno.png utilizando OpenCV
    #cv2.imshow('Contorno', contour_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Leer la imagen del contorno guardada
    contour_img = cv2.imread('IMG\RECORTE_3.png', cv2.IMREAD_UNCHANGED)

    # Convertir la imagen a RGB para ser compatible con Matplotlib
    contour_img_rgb = cv2.cvtColor(contour_img, cv2.COLOR_BGRA2RGBA)

    # 2) Invierte la imagen 
    #contour_img_rgb = np.flipud(contour_img_rgb) #Invierte el eje Y de la imagen

    # 3) le aplica filtro blur para quitar un poco el ruido
    filtered_mask = cv2.medianBlur(contour_img_rgb, 5)

    # Guardar la imagen del contorno en un archivo con canal alfa
    cv2.imwrite('IMG\RECORTE_3.png', filtered_mask)

    #------------------------------ CODIGO VICENTE -------------------------------------------

    # Leer la imagen del contorno guardada
    contour_img = cv2.imread('IMG/JOSE_RAMON/JS_1_1.png', cv2.IMREAD_UNCHANGED)

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
    QSignal = (lower_x_pos, max_y[lower_x_pos])
    # get the numer of x between the first and the lower point
    x_between = np.where((x_coords > first_point[0]) & (x_coords < lower_x_pos))

    # go x_between times to the right and get the y higher value coordinate 
    for i in range(x_between[0].shape[0]):
        if y_coords[x_between[0][i]] > QSignal[1]:
            QSignal = (x_coords[x_between[0][i]], y_coords[x_between[0][i]])


    # find the higher point between the lower and the final point not the start point
    QSignal2 = (lower_x_pos, max_y[lower_x_pos])

    # get the number of x between the lower and the final point
    x_between2 = np.where((x_coords > lower_x_pos) & (x_coords < final_point[0]))

    # get the midpoint of the x_between2 range
    midpoint = lower_x_pos + (final_point[0] - lower_x_pos) // 2

    # get the number of x between the lower point and the midpoint
    x_between2_first_half = np.where((x_coords > lower_x_pos) & (x_coords < midpoint))

    # go x_between2_first_half to the right and get the Y higher value coordinate
    for i in range(x_between2_first_half[0].shape[0]):
        if y_coords[x_between2_first_half[0][i]] > QSignal2[1]:
            QSignal2 = (x_coords[x_between2_first_half[0][i]], y_coords[x_between2_first_half[0][i]])


    # find the lower point betwwen QSignal2 and final_point
    lower_point_startQ = (QSignal2[0], max_y[QSignal2[0]])
    # get the number of x between the QSignal2 and the final point
    x_between2_second_half = np.where((x_coords > QSignal2[0]) & (x_coords < final_point[0]))
    #got to the right x_between2_second_half times and get the Y lower value coordinate
    for i in range(x_between2_second_half[0].shape[0]):
        if y_coords[x_between2_second_half[0][i]] < lower_point_startQ[1]:
            lower_point_startQ = (x_coords[x_between2_second_half[0][i]], y_coords[x_between2_second_half[0][i]])


    # find the lower point betwwen start point and QSignal coordiantes 
    lower_point_startP = (first_point[0], max_y[first_point[0]])
    # get the number of x between the start point and the QSignal and divide it by 2
    x_between3 = np.where((x_coords > first_point[0]) & (x_coords < QSignal[0]))
    midpoint2 = first_point[0] + (QSignal[0] - first_point[0]) // 2
    # get the number of x between the start point and the midpoint2
    x_between3_first_half = np.where((x_coords > first_point[0]) & (x_coords < midpoint2))

    #go to the right x_between3_first_half times and get the Y lower value coordinate
    for i in range(x_between3_first_half[0].shape[0]):
        if y_coords[x_between3_first_half[0][i]] < lower_point_startP[1]:
            lower_point_startP = (x_coords[x_between3_first_half[0][i]], y_coords[x_between3_first_half[0][i]])


    # Create a scatter plot of the x and y values
    plt.scatter(x_coords, y_coords, s=1)

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Plot the first, lower, and final points
    plt.plot(first_point[0], first_point[1], 'co', label='First')
    plt.plot(lower_x_pos, lower_y, 'ko', label='R')
    plt.plot(final_point[0], final_point[1], 'bo', label='Final')
    plt.plot(QSignal[0], QSignal[1], 'ro', label='Q')
    plt.plot(QSignal2[0], QSignal2[1], 'go', label='S') #ONDA S
    plt.plot(lower_point_startQ[0], lower_point_startQ[1], 'yo', label='T')
    plt.plot(lower_point_startP[0], lower_point_startP[1], 'mo', label='P')

    # Create a dictionary to store the coordinates
    coordinates = {
        'PRIMER_PUNTO_X': int(first_point[0]),
        'PRIMER_PUNTO_Y': int(first_point[1]),
        'PUNTO_MAS_ALTO_X': int(lower_x_pos),
        'PUNTO_MAS_ALTO_Y': int(lower_y),
        'PUNTO_FINAL_X': int(final_point[0]),
        'PUNTO_FINAL_Y': int(final_point[1]),
        'Q_SIGNAL_X': int(QSignal[0]),
        'Q_SIGNAL_Y': int(QSignal[1]),
        'S_SIGNAL_X': int(QSignal2[0]),
        'S_SIGNAL_Y': int(QSignal2[1]),
        #'lower_point_startQx': int(lower_point_startQ[0]),
        #'lower_point_startQy': int(lower_point_startQ[1]),
        'T_SIGNAL_X': int(lower_point_startQ[0]),
        'T_SIGNAL_Y': int(lower_point_startQ[1]),
        'P_SIGNAL_X': int(lower_point_startP[0]),
        'P_SIGNAL_Y': int(lower_point_startP[1])
    }
    # Save the coordinates to a JSON file

        # Save the coordinates to a JSON file

    image_filE_JSON = os.path.join(image_dir, image_file)
    image_filE_JSON = os.path.splitext(image_filE_JSON)[0] + '.json'

    with open(image_filE_JSON, 'w') as f:
        json.dump(coordinates, f)


    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()