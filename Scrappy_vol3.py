from tkinter import *


SCRAPPY_IDLE = "scrappy_demoidle.gif"
SCRAPPY_ISLEEP = "scrappy_demoidle_tosleep.gif"
SCRAPPY_SLEEPI = "scrappy_demosleep_toidle.gif"
SCRAPPY_LEFTROLL = "scrappy_demoroll_left.gif"
SCRAPPY_RIGHTROLL = "scrappy_demoroll_right.gif"
SCRAPPY_SLEEP = "scrappy_sleep.gif"
impath = "C:/Scrappy/"


window = Tk()
window.geometry("100x100")

my_image = PhotoImage(file=impath+SCRAPPY_IDLE)
label = Label(window,image=impath+SCRAPPY_IDLE)
label.place(x=0,y=0)

window.mainloop()
