import cv2
import numpy as np

def verifyHSV(escaninhoRef,escaninhoAtual):

	#escaninhoRef: imagem em perspectiva do escaninho VAZIO para referencia
	#escaninhoAtual: imagem em perspectiva do escaninho na foto tirada para verificacao

	#mudanca de parametro RGB para HSV
	escaninhoRef = cv2.cvtColor(escaninhoRef, cv2.COLOR_BGR2HSV)
	escaninhoAtual = cv2.cvtColor(escaninhoAtual, cv2.COLOR_BGR2HSV)

	#inicializacao matrizes de media
	meanRef = np.zeros((3,4,8))
	meanAtual = np.zeros((3,4,8))


	for i in range (3):
		for x in range (8):
			for y in range (4):
				meanRef[i,y,x] = np.mean(escaninhoRef[(150*y+30):(150*y+120),(100*x+20):(100*x+70),i])
				meanAtual[i,y,x] = np.mean(escaninhoAtual[(150*y+30):(150*y+120),(100*x+20):(100*x+70),i])

	erro = abs((meanAtual - meanRef)/meanRef)
	erroBool = erro.copy()
	for i in range (3):
		for x in range (8):
			for y in range (4):
				if (erro[i,y,x] > 0.3):
					erroBool[i,y,x] = 1
				else:
					erroBool[i,y,x] = 0

	resp = erroBool[0,:,:]
	#retorna matriz com parametro MATIZ
	return resp