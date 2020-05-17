from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import threading


def onClickStart():
    print('start is presed..!')


def onClickTrack():
    print('track is presed..!')
def onClickStop():
    print('stop is presed..!')

def main_screen():
    screen = Tk()
    screen.geometry("1000x700")
    screen.title("Hand gesture recognition system")

    Label(text="Wellocome To Hand Gesture Recognition System.", font = ("calibri", 35)).pack()

    buttonStrat = Button(text="Start", width= 10, command=lambda: onClickStart())
    buttonStrat.configure(highlightbackground='green')
    buttonStrat.place(x=50, y=70)

    buttonTrack = Button(text="Track", width= 10, command=lambda: onClickTrack())
    # buttonTrack.configure(highlightbackground='')
    buttonTrack.place(x=150, y=70)

    buttonStop = Button(text="Stop", width= 10, command=lambda: onClickStop())
    buttonStop.configure(highlightbackground='red')
    buttonStop.place(x=250, y=70)

    Label(text="Realtime video feed", font = ("calibri", 25)).place(x=50, y =100)
    cap = cv2.VideoCapture(0)
    canvasMain = Canvas(screen, width= 650, height= 400)
    #-------------------------------------------------------------------
    # put the realtime video on canvasmain	using tread
    # Create a Thread with a function without with arguments
    th = threading.Thread(target=update, args=(cap, canvasMain ))

    th.start()# run the created thread.

    # canvasMain.configure(background='gray')
    canvasMain.place(x=50, y=135)

    Label(text="Captured image", font = ("calibri", 25)).place(x=750, y =100)
    canvas = Canvas(screen, width= 200, height= 200)
    canvas.configure(background='gray')
    canvas.place(x=750, y=135)
 
    screen.mainloop()
    th.join()

def update(cap, canvasMain): # function that return the realtime video feed on web cam.
    while(1):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (650, 400))
        photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        canvasMain.create_image(0, 0, image = photo, anchor = NW)



main_screen()