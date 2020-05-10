import cv2
import numpy as np
from collections import deque 
import math

class MovmentGesture:
    def findcenterOfMass(frame, x, y, w, h):
        frame = cv2.circle(frame, (int(x+w/2),int(y+y/2)), 2,(255, 0, 0), 2)

    def appendToQueue(queue_x, queue_y , x, y):
        if(len(queue_x) == 10):
            queue_x.popleft()
            queue_y.popleft()
            queue_x.append(x)
            queue_y.append(y)
        else:
            queue_x.append(x)
            queue_y.append(y)

    def getFirstAndLast(queue_x, queue_y):
        # x_first =0, x_last =0, y_first=0, y_last=0
        x_first =0
        x_last =0
        y_first=0
        y_last=0

        if(len(queue_x) != 0):
            x_first = queue_x.pop()
            # print("x_first :", x_first)
            y_first = queue_y.pop()
            # print("y_first :", y_first)
            queue_x.append(x_first)
            queue_y.append(y_first)
            queue_x.reverse()
            queue_y.reverse()
            x_last = queue_x.pop()
            # print("x_last", x_last)
            y_last = queue_y.pop()
            # print("y_last", y_last)
            queue_x.append(x_last)
            queue_y.append(y_last)
            queue_x.reverse()
            queue_y.reverse()


        return x_first, x_last, y_first, y_last

    def drawMessage(frame, x_1, x_2, y_1, y_2, widht, hight):
        # distance = math.sqrt(math.pow((x_1-x_2),2) + math.pow((y_1-y_2), 2))
        distance_x = math.sqrt(math.pow((x_1-x_2), 2))
        distance_y = math.sqrt(math.pow((y_1-y_2), 2))
        mean = (widht+hight)/2
        if((distance_x < distance_y) and mean < distance_y):
            if(y_1 < y_2):
                cv2.putText(frame, "UP", (800,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0,255),3)
            else:
                cv2.putText(frame, "DOWN", (800,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0,255),3)
        elif((distance_x > distance_y) and mean < distance_x):
            if(x_1<x_2):
                cv2.putText(frame, "LEFT", (800,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0,255),3)
            else:
                cv2.putText(frame, "RIGHT", (800,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0,255),3)