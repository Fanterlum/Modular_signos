import os
import cv2
import pytesseract
import time

# Ruta de la carpeta con las imágenes
carpeta_imagenes = 'img/'

# Ruta del archivo que guarda los nombres de archivos ya procesados
archivo_registrados = 'archivos_procesados.txt'

# Cargar la lista de nombres de archivos ya procesados
if os.path.exists(archivo_registrados):
    with open(archivo_registrados, 'r') as archivo:
        archivos_procesados = set(archivo.read().splitlines())
else:
    archivos_procesados = set()

# Lista para almacenar los resultados
resultados = []

# Función para procesar una imagen
def procesar_imagen(ruta_imagen):
    # Carga la imagen
    imagen = cv2.imread(ruta_imagen)

    # Define las coordenadas de las tres regiones de interés (ROI)
    coordenadas_roi = [(2500, 700, 2728, 869), (2600, 1175, 2819, 1328), (2492, 1663, 2719, 1825)]

    # Inicializa una lista para almacenar los números de cada región
    numeros_por_region = []

    # Procesa cada región por coordenada
    for i, (x1, y1, x2, y2) in enumerate(coordenadas_roi):
        # Recorta la región de interés (ROI) de la imagen
        roi = imagen[y1:y2, x1:x2]

        # Convierte la ROI a escala de grises
        roi_gris = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Utiliza Tesseract para extraer texto de la ROI
        texto_extraido = pytesseract.image_to_string(roi_gris, config='--psm 6')

        # Filtra solo los números y puntos decimales de la salida
        caracteres_permitidos = '0123456789'
        numeros_y_puntos = ''.join(caracter for caracter in texto_extraido if caracter in caracteres_permitidos)

        # Agrega el resultado a la lista de números por región
        numeros_por_region.append(numeros_y_puntos)

    # Agrega los resultados de todas las regiones a la lista general de resultados
    resultados.append({'imagen': nombre_archivo, 'datos_por_region': numeros_por_region})

# Bucle infinito para verificar imágenes nuevas
while True:
    # Obtén una lista de los nombres de archivos de imágenes en la carpeta
    nombres_archivos = [archivo for archivo in os.listdir(carpeta_imagenes) if archivo.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Encuentra imágenes nuevas que no se han procesado previamente
    nuevas_imagenes = [nombre for nombre in nombres_archivos if nombre not in archivos_procesados]

    # Procesa las imágenes nuevas
    for nombre_archivo in nuevas_imagenes:
        ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)
        procesar_imagen(ruta_imagen)

        # Agrega el nombre del archivo a la lista de procesados
        archivos_procesados.add(nombre_archivo)

    # Guarda la lista actualizada de archivos procesados en el archivo
    with open(archivo_registrados, 'w') as archivo:
        archivo.write('\n'.join(archivos_procesados))

    # Imprime solo los resultados de las imágenes nuevas
    if nuevas_imagenes:
        print("Resultados de imágenes nuevas:")
        for resultado in resultados[-len(nuevas_imagenes):]:
            print(f"Imagen: {resultado['imagen']}")
            for i, numeros in enumerate(resultado['datos_por_region']):
                print(f"Región {i + 1}: {numeros}")

    time.sleep(60)  # Espera 60 segundos antes de verificar nuevamente (ajusta según tus necesidades)
    