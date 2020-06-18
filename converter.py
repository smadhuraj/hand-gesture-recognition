from handtracking import HandTracking
import threading
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import *

class Convertor:
    def binaryToDecimal(b_num):
        value = 0
        print(b_num)
        for i in range(len(b_num)):
            digit = b_num.pop()
            if digit == 1:
                value = value + pow(2, i)
        print("The decimal value of the number is", value)
        return value

# if __name__ == "__main__":
#   Convertor.binaryToDecimal([1,0,1,0,1])

