import cv2
import numpy as nu

img_rgb = cv2.imread("twofingers.jpg", 1) # RGB color image
img_gray = cv2.imread("twofingers.jpg", 0) # gray scal image
# img_rgb = cv2.imread("myhand.jpeg", 1) # RGB color image
# img_gray = cv2.imread("myhand.jpeg", 0) # gray scal image
img_gray = cv2.resize(img_gray, (260, 400))
img_rgb = cv2.resize(img_rgb, (260, 400))
# img = cv2.Canny(img_gray,100,200)  # apply canny pilter to detect edges of the hand
fingerTips_x_array = []
fingerTips_y_array = []
popIndex = []
class DetectGesture:

    def backgroundSubstraction():
        cap = cv2.VideoCapture(0)
        count =0
        while(count < 50):
            _, mask = cap.read()
            count = count + 1

        while(True):
            _, frame = cap.read()
            cv2.rectangle(frame, (100,100), (350,350), (0,0,255), 3)
            # cv2.imshow("frame", frame)

            # grayMask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) 
            filterIma = frame[100:350, 100:350]
            filterMask = mask[100:350, 100:350]
            filterIma = cv2.cvtColor(filterIma, cv2.COLOR_BGR2GRAY) 
            filterMask = cv2.cvtColor(filterMask, cv2.COLOR_BGR2GRAY) 

            # substractor = cv2.createBackgroundSubtractorMOG2(history=600, varThreshold=30, detectShadows= True)
            w = filterIma.shape[0]
            h = filterIma.shape[1]
            # for i in range(w):
            #     for j in range(h):
            #         diff = filterIma[i][j] - filterMask[i][j]
            #         if(diff < 30):
            #             filterIma[i][j] = 0
            
            # cv2.imshow("diff", filterIma)
        
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break




    def changeOriantation():
        # first find the center of mass of the hand.
        # then draw lines through that point 
        # find the line that has max length
        cX, cY = DetectGesture.findCenterOfMass()

    def findCenterOfMass(inputImage):
        gray_image = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray_image,127,255,0) # convert gray scall image in to binary image
        # cv2.imshow("binary image", thresh)
        M = cv2.moments(thresh) # find the moment of binary image
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(inputImage, (cX, cY), 5, (255, 0, 0), -1)
        cv2.imshow("mass image", inputImage)
        # print(cX, cY)
        return cX, cY


    def fingerTipsFind(inputImage):
        gray_image = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)   #convert in to gray scale
        img_gray = cv2.resize(gray_image, (400, 400))   #resize the image
        img = cv2.Canny(img_gray,100,200)   #apply canny filter to detect edges
        count = 0
        i = 1
        x = img.shape[0]
        y = img.shape[1]
        temp = x-1
        for j in range(y):
            for i in range(x):
                if(img[i][j] == 255):
                    if(temp > i):                                     
                        # print("if : ",temp, i)
                        temp = i
                        break
                    elif(temp < i):
                        #   print("else : ", temp, i)
                        temp = i  
                        break
                    else:
                        temp = i
                        if (img[i+1][j] == 255): 
                            fingerTips_x_array.append(i)
                            fingerTips_y_array.append(j)      
                            # cv2.circle(img_rgb,(j, i), 6, (0,0,255), 1)                                         
                        break
            # temp = x 
        print(fingerTips_x_array)
        print(fingerTips_y_array)   
        listSize = len(fingerTips_x_array) 
        for num in range(0, listSize-2):
            diff = fingerTips_x_array[num] - fingerTips_x_array[num + 1]      
            if (abs(diff) <= 5):
                popIndex.append(num)
        for k in range(len(popIndex)):
            print(popIndex[k])
            fingerTips_x_array.pop(popIndex[k]-count)
            fingerTips_y_array.pop(popIndex[k]-count)
            count = count + 1
        print(fingerTips_x_array) 
        print(fingerTips_y_array) 
        c_x, c_y = DetectGesture.findCenterOfMass(inputImage)
        for coun in range(len(fingerTips_x_array)):
            # print(fingerTips_y_array[coun], fingerTips_x_array[coun])
            cv2.circle(inputImage, (fingerTips_y_array[coun], fingerTips_x_array[coun]), 6, (0, 0, 255), 2)
            cv2.line(inputImage, (c_x, c_y), (fingerTips_y_array[coun], fingerTips_x_array[coun]), (0, 255, 0), thickness=1, lineType=8)

    cv2.waitKey(0)
    cv2.destroyAllWindows()