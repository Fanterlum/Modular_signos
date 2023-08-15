import numpy as np
import matplotlib.pyplot as plt


def Get_Propiedades(img):
    # Obtiene propiedades
    img_width = np.size(img, 1)
    img_height = np.size(img, 0)
    return img_width, img_height
#### Función de propiedades de la imagen 

# Funcion que sirve para plotear las imagenes que tenemos:
def imshow(P_plotear, img, titulo, origintipo, cmaptipo):
    if P_plotear:
        if (cmaptipo=='rgb'):
            plt.imshow(img, origin=origintipo ); plt.title(titulo); plt.show()
        else:
            plt.imshow(img, origin=origintipo, cmap=cmaptipo ); plt.title(titulo); plt.show()
        ## end del tipo de imagen que vamos a estar ploteando
    ## end del p plotear
## end de función de imshow



# Funcion que sirve para plotear las imagenes que tenemos con la original arriba:
def imshow_comparacion(P_plotear, img, titulo, origintipo, cmaptipo, img_original):
    if P_plotear:
        #Imagen extra:
        plt.subplot(2, 1, 1)  # 2 filas, 1 columna, posición 1 (arriba)
        plt.imshow(img_original, origin=origintipo ); plt.title("Imagen Original");

        plt.subplot(2, 1, 2)  # 2 filas, 1 columna, posición 2 (abajo)
        ##no borrar de aqui para abajo
        if (cmaptipo=='rgb'):
            plt.imshow(img, origin=origintipo ); plt.title(titulo); 
        else:
            plt.imshow(img, origin=origintipo, cmap=cmaptipo ); plt.title(titulo);
        ## end del tipo de imagen que vamos a estar ploteando

        plt.tight_layout()  # Ajustar los espacios entre las imágenes
        plt.show()
        
    ## end del p plotear

## end de función de imshow











