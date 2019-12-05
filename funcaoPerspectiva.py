import cv2
import numpy as np

def funcaoPerspectiva(imagem):
    
    #imagem = cv2.imread('fotos_escaninho/escaninho0.jpeg')
    cols = 800
    rows = 600

    pontosPerspectiva = np.loadtxt('Files/pontosPerspectiva3.txt')
    pts1 = np.float32([pontosPerspectiva[0],pontosPerspectiva[1],pontosPerspectiva[2],pontosPerspectiva[3]])
    pts2 = np.float32([[0,0],[cols,0],[cols,rows],[0,rows]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    perspectiva = cv2.warpPerspective(imagem,
                                      M,
                                      (cols,rows))

    return (perspectiva)
