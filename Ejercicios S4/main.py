import imutils
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt




def histEq():
    img = cv.imread("1.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    img2 = cdf[img]
    cv.imwrite("1HEQ.jpg", img2)
    cv.waitKey()

def HQRes():
    img = cv.imread("1.jpg")
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_LINEAR)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_LANCZOS4)
    cv.imwrite("low_res.jpg", img)
    scale_percent = 160  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_LINEAR)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation=cv.INTER_LANCZOS4)
    cv.imwrite("hi_res.jpg", img)
    
def ColorBalance():
    image = cv.imread("9.jpg")
    resized = cv.resize(image, (500, 600))
    imagen = cv.cvtColor(resized, cv.COLOR_BGR2RGB)

    print("Multiplicar R por: ")
    colorR = int(input())
    print("Multiplicar G por: ")
    colorG = int(input())
    print("Multiplicar B por: ")
    colorB = int(input())

    for i in range(600):
        for j in range(500):
            (r, g, b) = imagen[i, j]
            imagen[i, j] = (r * colorR, b * colorB, g * colorG)
            
    cv.imshow("Imagen", imagen)
    cv.waitKey(0)
    cv.imwrite("ColorBalance.jpg", imagen)
    return


def ScreenMatting():
    #Imagen Original con Fondo Azul
    image = cv.imread('blueScreen.jpg')
    #Copia de la Original
    image_copy = np.copy(image)
    image_copy = cv.cvtColor(image_copy, cv.COLOR_BGR2RGB)
    #Azules
    lower_blue = np.array([0, 0, 100])
    upper_blue = np.array([120, 100, 255])
    #Mascara
    mask = cv.inRange(image_copy, lower_blue, upper_blue)
    masked_image = np.copy(image_copy)
    masked_image[mask != 0] = [0, 0, 0]
    #Fondo
    background_image = cv.imread('background.jpg')
    background_image = cv.cvtColor(background_image, cv.COLOR_BGR2RGB)
    cv.imshow("background", background_image)
    (h, w, d) = image_copy.shape

    crop_background = background_image[0:h, 0:w]
    crop_background[mask == 0] = [0, 0, 0]
    #Imagen Final
    final_image = crop_background + masked_image


    cv.imshow("Fondo Azul", image)
    cv.imshow("Final", final_image)
    cv.imshow("BlueScreenMatting.jpg", final_image)  
    cv.waitKey(0)


#ScreenMatting()
#ColorBalance()
#histEq()
#HQRes()
