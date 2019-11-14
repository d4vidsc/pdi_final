import cv2
import numpy as np

flagDraw = True
drawing = False # true if mouse is pressed
raio = 3
ix,iy = -1,-1
pontos = np.zeros((4,2))
count = 0
maskframe = cv2.imread('fotos_escaninho/escaninho0.jpeg')
maskara =   maskframe.copy()
img = maskframe.copy()
img[:,:,:] = 0

rows = 600
cols = 800

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,count,pontos
    global maskframe, img, maskara, flagDraw, raio

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        pontos[count] = [ix,iy]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if (flagDraw):
                cv2.circle(img,(x,y),raio,(255,255,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        count += 1  
        drawing = False
        if (flagDraw):
            cv2.circle(img,(x,y),3,(255,255,255),-1)

cv2.namedWindow('mascara')
cv2.setMouseCallback('mascara',draw_circle)

while(1):
    k = cv2.waitKey(1) & 0xFF
    maskara = cv2.add(maskframe,img)
    cv2.imwrite('maskara.jpg',maskara)
    cv2.imshow('mascara',maskara)

    if count == 4:
        pts1 = np.float32([pontos[0],pontos[1],pontos[2],pontos[3]])
        pts2 = np.float32([[0,0],[cols,0],[cols,rows],[0,rows]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        perspectiva = cv2.warpPerspective(maskframe,M,(cols,rows))
        cv2.imwrite('perspectiva.jpg',perspectiva)
        f = open("pontosPerspectiva.txt", "w+")
        f.write(str(pontos))
        f.close()
        break
    if k == 27:
        break


cv2.destroyAllWindows()

