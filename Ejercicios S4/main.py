import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Cargar Imagen
image = cv2.imread("9.jpg")

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
    resized = cv2.resize(image, (500, 600))
    imagen = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    print("Multiplicar R por: ")
    colorR = int(input()) 
    print("Multiplicar G por: ")
    colorG = int(input())
    print("Multiplicar B por: ")
    colorB = int(input())
    for i in range(600):
        for j in range(500):
            (r, g, b) = imagen[i, j]
            imagen[i, j] = ( r * colorR, b * colorB, g * colorG)
    cv2.imshow("Imagen", imagen)
    cv2.waitKey(0)
    return


#ColorBalance()
#histEq()
#HQRes()
