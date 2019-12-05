import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


    
def ValidationImg(perspectiva): #função se valida se o escaninho esta obstruido ou não

    bordas = cv2.Canny(perspectiva,50,120)
    linhas = cv2.HoughLines(bordas, 1, np.pi / 180, 240, 600, 0)
    bordas_copia = cv2.cvtColor(bordas, cv2.COLOR_GRAY2BGR)
    if(linhas.shape[0] >= 3): #valor de calibração
        return 1#,linhas,bordas_copia,bordas
    else:
        return 0#,linhas,bordas_copia,bordas


'''perspectiva = cv2.imread('Imagens/perspectivaTeste3.jpg')
cv2.imshow('Original my eggs',perspectiva)


#Parametros para calibrar o Canny e Hough quando a camera for fixada
#minVal = 50
#maxVal = 120
#minLineLength = 800
#maxLineGap = 0      

podeSeguir,linhas,bordas_copia,bordas = ValidationImg(perspectiva)
print(podeSeguir)
for i in range(0, len(linhas)):
    rho = linhas[i][0][0]
    theta = linhas[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho
    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
    cv2.line(bordas_copia, pt1, pt2, (0,0,255), 2, cv2.LINE_AA)

print(linhas.shape[0])
cv2.imshow('Bordas',bordas)
cv2.imshow('Linhas',bordas_copia)
#waitkey('32')'''





