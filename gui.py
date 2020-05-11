from tkinter import *


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
    canvas = Canvas(screen, width= 650, height= 400)
    canvas.configure(background='gray')
    canvas.place(x=50, y=135)

    Label(text="Captured image", font = ("calibri", 25)).place(x=750, y =100)
    canvas = Canvas(screen, width= 200, height= 200)
    canvas.configure(background='gray')
    canvas.place(x=750, y=135)
 
    screen.mainloop()

main_screen()