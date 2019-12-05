import cv2
import numpy as np

def definePerspectiva():
    flagDraw = True
    drawing = False # true if mouse is pressed
    raio = 3
    ix,iy = -1,-1
    pontos = np.zeros((4,2))
    count = 0
    maskframe = cv2.imread('Imagens/ImagemFind0_1_8.jpeg')
    maskara =   maskframe.copy()
    img = maskframe.copy()
    img[:,:,:] = 0
    rows = 600
    cols = 800

    i = 0
    vetorMedias = np.arange(32)

    # mouse callback function
    def draw_circle(event,x,y,flags,param):
        nonlocal ix,iy,drawing,count,pontos
        nonlocal maskframe, img, maskara, flagDraw, raio

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

    cv2.namedWindow('Calibracao de Perspectiva')
    cv2.setMouseCallback('Calibracao de Perspectiva',draw_circle)

    while(1):
        k = cv2.waitKey(1) & 0xFF
        maskara = cv2.add(maskframe,img)
        #cv2.imwrite('maskara.jpg',maskara)
        cv2.imshow('Calibracao de Perspectiva',maskara)

        if count == 4:
            pts1 = np.float32([pontos[0],pontos[1],pontos[2],pontos[3]])
            pts2 = np.float32([[0,0],[cols,0],[cols,rows],[0,rows]])
            M = cv2.getPerspectiveTransform(pts1,pts2)
            perspectiva = cv2.warpPerspective(maskframe,M,(cols,rows))
            cv2.imwrite('Imagens/perspectivaTeste3.jpg',perspectiva)
            np.savetxt("Files/pontosPerspectiva3.txt", pontos)

            for x in range (8):
                for y in range (4):
                    media = cv2.mean(perspectiva[(150*y+30):(150*y+120),(100*x+20):(100*x+70),:])
                    #retangulos[(150*y+30):(150*y+120),(100*x+20):(100*x+70),:] = media[:3]
                    vetorMedias[i] = np.mean(media[:3])
                    i += 1
            np.savetxt("mediasRef2.txt", vetorMedias)
            break
        if k == 27:
            break


    cv2.destroyAllWindows()

