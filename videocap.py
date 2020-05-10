import cv2 
import numpy as np 
  
cap = cv2.VideoCapture(0) 
hand_cascade = cv2.CascadeClassifier('handdetect.xml') 

if not cap.isOpened:
    print('camera not opened')
    exit(0)

while (True):
    _, frame = cap.read()
    cv2.imshow("frame", frame)

    if frame is None:
        print('No frame')
        break

    k = cv2.waitKey(30) & 0xff
    if(k == 27): 
        break


def test(): 
    while(True): 
        ret, frame = cap.read() 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        hands = hand_cascade.detectMultiScale(gray, 1.5, 5) 
        contour = hands 
        contour = np.array(contour) 
        for (x, y, w, h) in hands: 
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 

    
    
        cv2.imshow('Driver_frame', frame) 
        k = cv2.waitKey(30) & 0xff
        if k == 27: 
            break


cv2.destroyAllWindows()

