import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from ROI import ROI
from definePerspectiva import definePerspectiva
from Validation import ValidationImg
from VerifyT import VerifyTA

#definePerspectiva()

perspectiva = cv2.imread('Imagens/perspectivaTeste.jpg')
if (ValidationImg(perspectiva)):
    VerifyTA(perspectiva)
    print('satangos')
else:
    print('Iamgem obstruida')


