import cv2
import numpy as np
from random import randint
from gesture import DetectGesture
from handPoseImage import HandPoseImage

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


cap = cv2.VideoCapture("outpy.avi")
boxes = []
# i = 0
# while(i<10):
#     ret, frame = cap.read()
#     i = i + 1
# frame = cv2.flip(frame, 1)
ret, frame = cap.read()
trackerType = "BOOSTING" 
hand_cascade = cv2.CascadeClassifier('abcd.xml') # cascade classifire for detecting hand
newBox = (0,0,0,0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while (True):
    # using cascade classifire

    _, newFrame = cap.read() # read the video frame
    # frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
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
        #  to apply gestures recognition code (gesture.py)` need to apply background substraction mothod.....  
        cv2.imshow("object tracking", subImage)
        if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed to detect gesture.
          HandPoseImage.getHandGesture(subImage)
          break
        # DetectGesture.findCenterOfMass(subImage)
        # DetectGesture.fingerTipsFind(subImage)

    # show frame
    cv2.imshow('Tracking Frame', frame)
    

    # quit on ESC button
    if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
      HandPoseImage.getHandGesture()
      break
    
cap.release()
cv2.destroyAllWindows()
