from __future__ import division
import cv2
import time
import numpy as np
import math

class HandPoseImage():
    def getHandGesture(inputImage):

        protoFile = "hand/pose_deploy.prototxt"
        weightsFile = "hand/pose_iter_102000.caffemodel"
        nPoints = 22
        POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
        POSE_PAIRS_NEW = [ [2,4],[5,8],[9,12],[13,16],[17,20] ]
        net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

        frame  = inputImage     #= cv2.imread(inputImage)
        # frame = cv2.resize(frame, (300, 400))
        frameCopy = np.copy(frame)
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        aspect_ratio = frameWidth/frameHeight

        threshold = 0.1

        t = time.time()
        # input image dimensions for the network
        inHeight = 368
        inWidth = int(((aspect_ratio*inHeight)*8)//8)
        inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

        net.setInput(inpBlob)

        output = net.forward()
        print("time taken by network : {:.3f}".format(time.time() - t))

        # Empty list to store the detected keypoints
        points = []
        reletive_distance = 0

        for i in range(nPoints):
            # confidence map of corresponding body's part.
            probMap = output[0, i, :, :]
            probMap = cv2.resize(probMap, (frameWidth, frameHeight))

            # Find global maxima of the probMap.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

            if prob > threshold :
                cv2.circle(frameCopy, (int(point[0]), int(point[1])), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.putText(frameCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

                # Add the point to the list if the probability is greater than the threshold
                points.append((int(point[0]), int(point[1])))
            else :
                points.append(None)

        # get the relative distance between 5, 13 or 4, 9,
        if points[5] and points[13]:
            reletive_distance = math.sqrt(math.pow(points[5][0]-points[13][0], 2) + math.pow(points[5][1]-points[13][1], 2))
        
        elif points[9] and points[4]:
            reletive_distance = math.sqrt(math.pow(points[9][0]-points[4][0], 2) + math.pow(points[9][1]-points[4][1], 2))
        # create empty list for store bit siquence of the gesture.
        # when reurn it it size should be 5. otherwise it mey rejected.
        bitSequence = [] 
        # Draw Skeleton
        for pair in POSE_PAIRS_NEW: # POSE_PAIRS
        # for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]

            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
                cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                # get the length of the finger
                lenght = math.sqrt(math.pow(points[partA][0]-points[partB][0], 2) + math.pow(points[partA][1]-points[partB][1], 2))
                # check finger length with relative distance then identify that finger is raised or not
                if( reletive_distance < lenght ):
                    bitSequence.append(1)
                else:
                    bitSequence.append(0)

        if(len(bitSequence) == 5):
            # cv2.imshow('Output-Keypoints', frameCopy)
            cv2.imshow('Output-Skeleton', frame)

            # cv2.imwrite('Output-Keypoints.jpg', frameCopy)
            # cv2.imwrite('Output-Skeleton.jpg', frame)

            print("Total time taken : {:.3f}".format(time.time() - t))

            return bitSequence
        else:
            print('some fingers are not ditect crearly.. please try again..')
        # cv2.waitKey(0)
