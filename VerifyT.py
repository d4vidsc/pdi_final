import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from ROI import ROI


#perspectiva = cv2.imread('Imagens/perspectivaImagemFind1.png')
#cv2.imshow('Original',perspectiva)

def VerifyTA (perspectiva):
    perspectivaGray = cv2.cvtColor(perspectiva, cv2.COLOR_BGR2GRAY)

    escaninhoAtual = np.zeros((4,8),dtype=int)
    #print(escaninho)

    #tipo_str = ["cv2.THRESH_BINARY", "cv2.THRESH_BINARY_INV", "cv2.THRESH_TRUNC",
    #            "cv2.THRESH_TOZERO", "cv2.THRESH_TOZERO_INV","cv.ADAPTIVE_THRESH_GAUSSIAN_C"]
    img_limiar = cv2.threshold(perspectivaGray,
                               110,
                               255,
                               cv2.THRESH_BINARY)
    img_limiarRGB = cv2.cvtColor(img_limiar[1], cv2.COLOR_GRAY2BGR)
    '''img_limiar = cv2.adaptiveThreshold(perspectiva,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,11,2)'''

    ROI(img_limiar,img_limiarRGB,escaninhoAtual)
    #cv2.imshow('Linearizada',img_limiarRGB)
    #np.savetxt('Status2.txt',escaninho)
    #vai = int(np.loadtxt('Status2.txt').all())
    return escaninhoAtual
#print(escaninho)

