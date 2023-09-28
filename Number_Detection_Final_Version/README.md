# Detección de números a partir de una imagen

Códig elaborado 100% en el lenguaje de programación Python con la ayuda librerías como:
- Pytessearct OCR
- OpenCV

En este pequeño script de python se utilizan las librerias de PyTesseract ORC para a detección de caracteres dentro de una imagen en conjunto
de OpenCV, para aplicar métodos y técnicas de procesamiento de imagenes.

Instrucciones para la correcta ejecusión del progtama:

Primero debemos de instalar la libreria de pytesseract ocr y OpenCV, para eso debemos de abrir una nueva terminal y escribir los siguientes comandos:

Si estamos trabajando en un ambiente de desarrollo de linux escribe lo siguiente:

Sudo apt update 
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-eng tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-spa

tesseract --version

Ahora instalemos la librería:

pip install pytesseract
pip install opencv-python

python -c "import cv2; print(cv2.__version__)"

Una vez que ya tenemos descargadas las librerías necesarias podemos descargar el código fuente
y las imagenes para poder probar el código.

Es importante mencionar que la o las imagenes deben de estar en un carpeta, la cual debe de estar en el mismo path
que el archivo principal, de lo contrario deberemos de cambiar la ruta y, debe de llamarse "img", de lo contrario
deberemos de hacer ciertas modificaciones al script.


Una vez que tenemos todo instalado y descargado podemos pasar a la ejecusión:

Para ambientes de desarrollo linux:

Abrir una nueva terminal
Dirigirse a la ruta donde tenemos el código
escribir: python3 "Nombre_archivo.py" (main2.py)
Enter.

Para ambientes de desarrollo Windows:
Ejecutar con alguna extesión de compilación de windows.

Adjunto una imagen de evidencia del funcionamiento del programa.
[Evidencia](https://github.com/Fanterlum/Modular_signos/blob/jared/Number_Detection_Final_Version/assets/Evidencia.jpeg)
