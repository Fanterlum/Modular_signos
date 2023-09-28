import os
import cv2
import pytesseract

# Ruta de la carpeta con las imágenes
carpeta_imagenes = 'img/'

# Obtén una lista de los nombres de archivos de imágenes en la carpeta
nombres_archivos = [archivo for archivo in os.listdir(carpeta_imagenes) if archivo.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Arreglo para almacenar los resultados
resultados = []

# Itera sobre cada imagen
for nombre_archivo in nombres_archivos:
    ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
    
    
    # Carga la imagen
    imagen = cv2.imread(ruta_imagen)

    # Define las coordenadas de la región donde deseas buscar números y puntos
    x1, y1, x2, y2 = 2500, 700, 2728, 869 # Modifica estas coordenadas según tu imagen
    a1, b1, a2, b2 = 2600, 1175, 2819, 1328
    c1, d1, c2, d2 = 2492, 1663, 2719, 1825


    # Recorta la región de interés (ROI) de la imagen
    roi = imagen[y1:y2, x1:x2]
    roi2 = imagen[a1:a1, b1:b2]
    roi3 = imagen[c1:c2, d1:d2]

    # Convierte la ROI a escala de grises
    roi_gris = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi_gris2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
    roi_gris3 = cv2.cvtColor(roi3, cv2.COLOR_BGR2GRAY)

    # Utiliza Tesseract para extraer texto de la ROI
    texto_extraido = pytesseract.image_to_string(roi_gris, config='--psm 6')
    texto_extraido2 = pytesseract.image_to_string(roi_gris2, config='--psm 6')
    texto_extraido3 = pytesseract.image_to_string(roi_gris3, config='--psm 6')

    # Filtra solo los números y puntos decimales de la salida
    caracteres_permitidos = '0123456789'
    numeros_y_puntos = ''.join(caracter for caracter in texto_extraido if caracter in caracteres_permitidos)

    # Agrega el resultado a la lista de resultados con el nombre del archivo
    resultados.append({'imagen': nombre_archivo, 'datos': numeros_y_puntos})

# Imprime los resultados
for resultado in resultados:
    print(f"Imagen: {resultado['imagen']}, Datos: {resultado['datos']}")
