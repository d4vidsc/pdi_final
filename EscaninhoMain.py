import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from ROI import ROI
from definePerspectiva import definePerspectiva
from Validation import ValidationImg
from VerifyT import VerifyTA
from funcaoPerspectiva import funcaoPerspectiva
import risingedge
#definePerspectiva()
#while(clock de 5 mim)

#Substituir pela função de captura da PI
#cam = PiCamera()
#imagem = cam.capture()
#definePerspectiva()
imagem = cv2.imread('Imagens/ImagemFind0_1_8.jpeg')

perspectiva = funcaoPerspectiva(imagem)

if (ValidationImg(perspectiva)):
	#m3 = funcaodavid(perspectiva)
    m2 = VerifyTA(perspectiva) #matriz atual do escaninho é retornada
    m1 = np.loadtxt('Files/statusPassado.txt',dtype=int)
    print(m1)
    print(m2)
    risingedge.risingedge(m1,m2)
    np.savetxt('Files/statusPassado.txt',m2)
    
else:
    print('Iamgem obstruida')


