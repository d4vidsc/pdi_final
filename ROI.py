import cv2
import matplotlib.pyplot as plt
import numpy as np

#perspectiva = cv2.imread('Imagens/perspectiva.png')
def ROI (perspectivaGRAY,perspectiva,escaninhoAtual):
    color = (255,0,0)
    tk = 2
    for x in range (8):
        for y in range (4):
            '''cv2.rectangle(perspectiva,
                          (100*x + 20, 160 * y + 40),
                          (100 * x + 20 + 50 , 160 * y + 40 + 70),
                          color, 2)'''

            imCrop = perspectiva[int(150 * y + 40):int(150 * y + 40 + 80),
                     int(100*x + 20):int(100 * x + 20 + 50)]
            imCrop = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)
            #statusEscaninho = np.sum(imCrop)
            #print(statusEscaninho/255)
            if (np.sum(imCrop)/255 > 30):
                escaninhoAtual[y,x] = 1

            else:
                escaninhoAtual[y,x] = 0

            
#cv2.imshow('ROI',perspectiva)

