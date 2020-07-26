import cv2
import numpy as np
from random import randint
from gesture import DetectGesture
from handPoseImage import HandPoseImage
from movment import MovmentGesture
from collections import deque 
import PIL.Image, PIL.ImageTk
from tkinter import *


boxes = []
qx = deque()
qy = deque()

trackerType = "BOOSTING" 
hand_cascade = cv2.CascadeClassifier('abcd.xml') # cascade classifire for detecting hand
newBox = (0,0,0,0)
#this code is use to write a video......
###################################################
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
###################################################
width = 0
height = 0
bitSequence = [] # that store the bit sequence of the current gesture when Esc button was presed...
trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT'] #  tracker types

def createTrackerByName(trackerType):
# Create a tracker based on tracker name
    if trackerType == trackerTypes[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == trackerTypes[1]: 
        tracker = cv2.TrackerMIL_create()
    elif trackerType == trackerTypes[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == trackerTypes[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == trackerTypes[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif trackerType == trackerTypes[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif trackerType == trackerTypes[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == trackerTypes[7]:
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = None
        print('Incorrect tracker name')
        print('Available trackers are:')
        for t in trackerTypes:
            print(t)
        
    return tracker


# def mainFunction(self, cap, canvasMain, canvas):

# cap = cv2.VideoCapture("demoVideo.avi")
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
while (True):
    _, newFrame = cap.read() # read the video frame
    gray = cv2.cvtColor(newFrame, cv2.COLOR_BGR2GRAY) #  convert in to gray scale
    hands = hand_cascade.detectMultiScale(gray, 1.1, 3)  # find the hand object that has similer haar features like trained images
    for bbox in hands: 
        a = bbox[0]
        b = bbox[1]
        c = bbox[2]
        d = bbox[3]
        newBox = (a,b,c,d)
        boxes.append(newBox) #  if found some hand that append to the boxes list
        newFrame = cv2.rectangle(newFrame, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (225,0,0), 2)

    newFrame = cv2.resize(frame, (650, 400))
    # photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(newFrame))
    # canvasMain.create_image(0, 0, image = photo, anchor = NW)
    cv2.imshow("selected hand object", newFrame)

    if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed      
        break
    if boxes:
        break

multiTracker = cv2.MultiTracker_create()

# Initialize MultiTracker 
# put detected objects in to initiated tracker
for bbox in boxes:
    multiTracker.add(createTrackerByName(trackerType), frame, bbox)

# Process video and track objects
movementObj = MovmentGesture()
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # get updated location of objects in subsequent frames
    success, bboxes = multiTracker.update(frame)

    # draw tracked objects
    for i, newbox in enumerate(bboxes):
        correction_length = 60 # int((newbox[2]+newbox[3])/8)
        p1 = (int(newbox[0] - correction_length), int(newbox[1] - correction_length))
        p2 = (int(newbox[0]+newbox[2]) , int(newbox[1]+newbox[3]) )
        # saveframe = frame
        # out.write(saveframe)
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        subImage = frame[int(newbox[1]): int(newbox[1]+newbox[3]), int(newbox[0]): int(newbox[0]+newbox[2])]#` crop the hand part from the holl image
        
        MovmentGesture.appendToQueue(qx, qy, int(p1[0]+newbox[2]/2),int(p1[1]+newbox[3]/2))
        width = c
        height = d

        x_first, x_last, y_first, y_last = MovmentGesture.getFirstAndLast(qx, qy) 
        frame = cv2.line(frame, (x_first,y_first), (x_last, y_last), (0, 255, 255), 4) 
        movementObj.drawMessage(frame, x_first, x_last, y_first, y_last, width, height)

        subImage = cv2.resize(subImage, (200, 200))
        # photoSub = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(subImage))
        # canvas.create_image(0, 0, image = photoSub, anchor = NW)

        cv2.imshow("object tracking", subImage)

        # give the control signal by pressing Esc button.
        if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed to detect gesture.
            bitSequence = HandPoseImage.getHandGesture(subImage) # get the bit sequence of the current hand gestre.
            print(bitSequence)
            break

    # show frame
    frame = cv2.resize(frame, (650, 400))
    # photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    # canvasMain.create_image(0, 0, image = photo, anchor = NW)
    cv2.imshow('Tracking Frame', frame)
    

    # quit on ESC button
    if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
        # HandPoseImage.getHandGesture()
        break
cap.release()
cv2.destroyAllWindows()
#run without gui.....
# if __name__ == "__main__":
#   HandTracking().mainFunction()

