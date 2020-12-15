from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import threading
from handtracking import HandTracking

handTrackingObject = HandTracking()


def onClickStart():
    print('start is presed..!')


def onClickTrack(bit_seq, device_no, status):
    print('track is presed..!')
    handTrackingObject.controlSignal(bit_seq, device_no, status)

def onClickStop():
    SystemExit()
    print('stop is presed..!')

def main_screen():
    screen = Tk()
    screen.geometry("1000x700")
    screen.title("Hand gesture recognition system")

    Label(text="Welcome To Hand Gesture Recognition System.", font = ("calibri", 35)).pack()



    Label(text="Realtime video feed", font = ("calibri", 25)).place(x=50, y =100)

    # cap = cv2.VideoCapture("demoVideo.avi")
    cap = cv2.VideoCapture(0)
    canvasMain = Canvas(screen, width= 650, height= 400)
    #-------------------------------------------------------------------
    # put the realtime video on canvasmain	using tread
    # Create a Thread with a function without with arguments
    # th = threading.Thread(target=update, args=(cap, canvasMain ))
    canvasMain.place(x=50, y=135)

    # canvasMain.configure(background='gray')
    

    Label(text="Captured image", font = ("calibri", 25)).place(x=750, y =100)
    canvas = Canvas(screen, width= 200, height= 200)
    canvas.configure(background='gray')
    canvas.place(x=750, y=135)
    Label(text="Detected Movement", font = ("calibri", 15)).place(x=750, y=350)
    movment_lable = Label(font = ("calibri", 25))
    movment_lable.configure(text="")
    movment_lable.place(x=750, y=400)

    Label(text="Bit sequence   : ", font = ("calibri", 25)).place(x=50, y =560)
    bit_seq = Label(font = ("calibri", 25))
    bit_seq.configure(text="1 0 1 1 0")
    bit_seq.place(x=240, y =560)

    Label(text="Device No   : ", font = ("calibri", 25)).place(x=50, y =600)
    device_no = Label(font = ("calibri", 25))
    device_no.configure(text=" 15 ")
    device_no.place(x=240, y =600)


    Label(text="Status   : ", font = ("calibri", 25)).place(x=400, y =580)
    status = Label(font = ("calibri", 25))
    status.configure(text="  ")
    status.place(x=500, y =580)


    buttonStrat = Button(text="Start", width= 10, command=lambda: onClickStart())
    buttonStrat.configure(highlightbackground='green')
    buttonStrat.place(x=50, y=70)

    buttonTrack = Button(text="Track", width= 10, command=lambda: onClickTrack(bit_seq, device_no, status))
    # buttonTrack.configure(highlightbackground='')
    buttonTrack.place(x=150, y=70)

    buttonStop = Button(text="Stop", width= 10, command=lambda: onClickStop())
    buttonStop.configure(highlightbackground='red')
    buttonStop.place(x=250, y=70)


    th_1 = threading.Thread(target=update, args= (cap, canvasMain, canvas, movment_lable))
    th_1.start()
    
    screen.mainloop()
    th_1.join()
    
    
def update(cap, canvasMain, canvas, movment_lable): # function that return the realtime video feed on web cam.
    handTrackingObject.mainFunction(cap, canvasMain, canvas, movment_lable)

main_screen()