# Adam Lopez
#


import tkinter as tk
import random
import time
#from Pil import Image, ImageTK
SCRAPPY_IDLE = "scrappy_demoidle.gif"
SCRAPPY_ISLEEP = "scrappy_demoidle_tosleep.gif"
SCRAPPY_SLEEPI = "scrappy_demosleep_toidle.gif"
SCRAPPY_LEFTROLL = "scrappy_demoroll_left.gif"
SCRAPPY_RIGHTROLL = "scrappy_demoroll_right.gif"
SCRAPPY_SLEEP = "scrappy_sleep.gif"
impath = "C:/Scrappy/"
scrappy = tk.Tk()

scrappy.title("Scrappy!")
photo= tk.PhotoImage(file=SCRAPPY_IDLE)
label = tk.Label(scrappy, bd=0,bg='black')
label.pack()

def move_scrappy():
     for i in range(scrappy.winfo_screenheight()):
          scrappy.geometry(f"+10+{i}")
          scrappy.update()
          scrappy.config(highlightbackground='black')
          scrappy.overrideredirect(True)
          scrappy.wm_attributes('-transparentcolor','black')
          time.sleep()
          #scrappy.attributes("-alpha",0.1)
move_scrappy()


x = 1400
cycle = 0
check = 1
idle_nums = [1,2,3,4]
sleep_nums = [10,11,12,13,15]
roll_left = [6,7]
roll_right = [8,9]
event_number = random.randrange(1,3,1)
# call scrappy

idle = [tk.PhotoImage(file=impath+SCRAPPY_IDLE ,format = 'gif -index %i' %(i)) for i in range (5)]
idle_to_sleep = [tk.PhotoImage(file=impath+SCRAPPY_ISLEEP,format = 'gif -index %i' %(i)) for i in range(8)]
sleep = [tk.PhotoImage(file=impath+SCRAPPY_SLEEP,format = 'gif -index %i' %(i)) for i in range(3)]
sleep_to_idle = [tk.PhotoImage(file=impath+SCRAPPY_SLEEPI,format = 'gif -index %i' %(i)) for i in range(8)]
roll_left = [tk.PhotoImage(file=impath+SCRAPPY_LEFTROLL,format = 'gif -index %i' %(i)) for i in range(8)]
roll_right = [tk.PhotoImage(file=impath+SCRAPPY_RIGHTROLL,format = 'gif -index %i' %(i)) for i in range(8)]


scrappy.after(1,update,cycle,check,event_number,x)
scrappy.mainloop()




















