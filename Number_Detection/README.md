En este pequeño script de python se utilizan las librerias de PyTesseract ORC para a detección de caracteres dentro de una imagen en conjunto de PIL, Processing Imagin Library para tratar las imagenes como objetos.

Instrucciones para la correcta ejecusión del progtama:

Primero debemos de instalar la libreria de pytesseract ocr, para eso debemos de abrir una nueva terminal y escribir los siguientes comandos:

Si estamos trabajando en un ambiente de desarrollo de linux escribe lo siguiente:

Sudo apt update 
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-eng tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-spa

tesseract --version

Ahora instalemos la librería:

pip install pytesseract

Una vez que tenemos todo instalado podemos pasar a la ejecusión:

Para ambientes de desarrollo linux:

Abrir una nueva terminal
Dirigirse a la ruta donde tenemos el código
escribir: python3 "Nombre_archivo.py" (Number_Detection.py)
Enter.

Para ambientes de desarrollo Windows:
Ejecutar con alguna extesión de compilación de windows.
