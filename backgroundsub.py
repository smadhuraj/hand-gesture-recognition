import cv2 
import numpy as np 
  
cap = cv2.VideoCapture(0) 
substractor = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=30, detectShadows= True)
hand_cascade = cv2.CascadeClassifier('cascade.xml') 

while(True):
    _, frame = cap.read()
    mask = substractor.apply(frame)
    # cv2.imshow("frame", frame)
    # cv2.imshow("mask", mask)

    hands = hand_cascade.detectMultiScale(mask, 1.1, 4) 

    for(x,y,w,h) in hands:
        cv2.rectangle(mask, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('frame',mask)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break


cap.release()
cv2.destroyAllWindows()