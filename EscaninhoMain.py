import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from ROI import ROI
from definePerspectiva import definePerspectiva
from Validation import ValidationImg
from VerifyT import VerifyTA
from funcaoPerspectiva import funcaoPerspectiva

#definePerspectiva()
#while(clock de 5 mim)

#Substituir pela função de captura da PI
#cam = PiCamera()
#imagem = cam.capture()
imagem = cv2.imread('Imagens/ImagemControle0.jpeg')

perspectiva = funcaoPerspectiva(imagem)

if (ValidationImg(perspectiva)):
    m2 = VerifyTA(perspectiva) #matriz atual do escaninho é retornada
    m1 = np.loadtxt('Files/statusPassado.txt')
    risingedge(m1,m2)
    np.savetxt('Files/statusPassado.txt',m2,'w')
    
else:
    print('Iamgem obstruida')


