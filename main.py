import imutils
import cv2

# Cargar imagen
image = cv2.imread("1.jpg")
(h, w, d) = image.shape


# ------------------------------------Primer ejercicio------------------------------------


def RGB():
    print("width = {}, height = {}, depth = {}".format(w, h, d))

    print("Valor de X: ")
    x = int(input())

    print("Valor de Y: ")
    y = int(input())

    (B, G, R) = image[x, y]
    print("R = {}, G = {}, B = {}".format(R, G, B))
    return


# ------------------------------------Primer ejercicio------------------------------------

# ------------------------------------Segundo ejercicio------------------------------------


def Recorte():
    print("Valor inicial de Y: ")
    yI = int(input())

    print("Valor final de Y: ")
    yF = int(input())

    print("Valor inicial de X: ")
    xI = int(input())

    print("Valor final de X: ")
    xF = int(input())

    #        StartY:EndY StartX:EndX
    roi = image[yI:yF, xI:xF]

    # Mostrar primero la imagen original
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    # ENTER CUANDO SE MUESTRA LA PRIMER IMAGEN PARA VER LAS DOS AL MISMO TIEMPO #

    # Mostrar el recorte
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)


# ------------------------------------Segundo ejercicio------------------------------------

# ------------------------------------Tercer ejercicio------------------------------------


def Resize():
    print("Valor de nuevas dimensiones: ")
    x = int(input())
    print("x")
    y = int(input())
    resized = cv2.resize(image, (x, y))
    cv2.imshow("Nueva Dimension", resized)
    cv2.waitKey(0)


# ------------------------------------Tercer ejercicio------------------------------------

# ------------------------------------Cuarto ejercicio------------------------------------

def Fixed_Resized():
    print("Digite el ancho de la imagen: ")
    ancho = int(input())
    resized = imutils.resize(image, ancho)
    cv2.imshow("Fixed Resized", resized)
    cv2.waitKey(0)


# ------------------------------------Cuarto ejercicio------------------------------------

# ------------------------------------Quinto ejercicio------------------------------------

def Rotar():
    # la imagen original es demasiado grande
    resized = imutils.resize(image, 500)

    # rotacion
    print("Valor de los grados de rotacion: ")
    grados = int(input())
    rotated = imutils.rotate_bound(resized, grados)
    cv2.imshow("Rotacion", rotated)
    cv2.waitKey(0)


# ------------------------------------Quinto ejercicio------------------------------------

# ------------------------------------Sexto ejercicio------------------------------------

def Suavizar():
    # la imagen original es demasiado grande
    resized = imutils.resize(image, 500)

    blurred = cv2.GaussianBlur(resized, (11, 11), 0)
    cv2.imshow("Original Recortada", resized)
    cv2.waitKey(0)

    # ENTER CUANDO SE MUESTRA LA PRIMER IMAGEN PARA VER LAS DOS AL MISMO TIEMPO #

    cv2.imshow("Blurred", blurred)
    cv2.waitKey(0)

# ------------------------------------Sexto ejercicio------------------------------------


# Llamadas
def switch(i):
    switcher={
        1:RGB,
        2:Recorte,
        3:Resize,
        4:Fixed_Resized,
        5:Rotar,
        6:Suavizar
    }
    return switcher.get(i)

def main():

    opcion = 0
    while(True):
        while(True):
            print("Transformaciónes disponibles:\n\n1) RGB de pixel específico\n2) Recorte de imágen\n3) Cambio de tamaño de imágen\n4) Cambio de tamaño de imágen fijo\n5) Rotar imágen\n6) Suavizar imágen\n\nDigita el numero de la opción que desee (o 0 para terminar):")
            try:
                opcion = int(input())
                if (opcion > 6 or opcion < 0):
                    print("\nDigite un numero válido\n")
                else:
                    break
            except:
                print("\nNo insertaste un numero\n")

        if(opcion==0):
            break
        else:
            switch(opcion)()

main()