import cv2
import numpy as np


def gec(self): 
    pass

kamera = cv2.VideoCapture(0)
cv2.namedWindow('Canny',cv2.WINDOW_AUTOSIZE) 

cv2.createTrackbar("Lower", "Canny", 20, 255, gec) 
cv2.createTrackbar("Upper", "Canny", 25, 255, gec)

cv2.startWindowThread() 

while(True):
    lower = cv2.getTrackbarPos("Lower","Canny") 
    upper= cv2.getTrackbarPos("Upper","Canny")

    ret , goruntu = kamera.read() 

    goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(goruntu,lower,upper, L2gradient = True)

    cv2.imshow('Canny', canny)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

kamera.release()
cv2.destroyAllWindows()
