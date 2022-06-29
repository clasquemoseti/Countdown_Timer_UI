from tkinter import *
from tkinter import font, ttk
import datetime

global endTime


def quits():
    root.destroy()


def waiting():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    txt.set(timeLeft)

    root.after(1000, waiting)


root = Tk()
root.title("Countdown Timer")
root.attributes("-fullscreen", False)
root.configure(background='black', width=1300, height=240)
root.bind('q', quits)
root.after(1000, waiting)

endTime = datetime.datetime(2022, 9, 1, 0, 0)
txt = StringVar()
fnt = font.Font(family='Helvetica', size=120, weight='bold')
lbl = ttk.Label(root, textvariable=txt, font=fnt, background='black', foreground='white')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
