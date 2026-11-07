# Adam Lopez
# Desktop buddy

import os
import random
import tkinter as tk
from PIL import Image, ImageTk
import time 

SCRAPPY_IDLE = "scrappy_demoidle.gif"
SCRAPPY_ISLEEP = "scrappy_demoidle_tosleep.gif"
SCRAPPY_SLEEPI = "scrappy_demosleep_toidle.gif"
SCRAPPY_LEFTROLL = "scrappy_demoroll_left.gif"
SCRAPPY_RIGHTROLL = "scrappy_demoroll_right.gif"
SCRAPPY_SLEEP = "scrappy_sleep.gif"
ASSET_DIR = r"C:\Scrappy"

root = tk.Tk()
root.title("Scrappy!")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "black")
root.attributes("-alpha", 0.98)
root.configure(bg="black")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = max(20, screen_w - 180)
y = max(20, screen_h - 180)
vx = 3
vy = 0
frame_index = 0
state = "sleep"


def load_sequence(filename, frame_count):
    path = os.path.join(ASSET_DIR, filename)
    frames = []
    if not os.path.exists(path):
        return frames

    for i in range(frame_count):
        try:
            frames.append(tk.PhotoImage(file=path, format=f"gif -index {i}"))
        except tk.TclError:
            break
    return frames


idle = load_sequence(SCRAPPY_IDLE, 5)
idle_to_sleep = load_sequence(SCRAPPY_ISLEEP, 8)
sleep = load_sequence(SCRAPPY_SLEEP, 3)
sleep_to_idle = load_sequence(SCRAPPY_SLEEPI, 8)
roll_left = load_sequence(SCRAPPY_LEFTROLL, 8)
roll_right = load_sequence(SCRAPPY_RIGHTROLL, 8)

for seq in (idle, idle_to_sleep, sleep, sleep_to_idle, roll_left, roll_right):
    if not seq:
        break

if not idle:
    idle = [tk.PhotoImage()]  # fallback so the app still starts if assets are missing

label = tk.Label(root, bd=0, bg="black")
label.pack()
label.image = idle[0]
label.configure(image=idle[0])
label.bind("<Button-1>", lambda event: on_click(event))
label.bind("<Enter>", lambda event: on_hover(event))
label.bind("<Leave>", lambda event: on_leave(event))
label.configure(cursor="hand2")


def on_click(event):
    global state, frame_index
    if state == "sleep":
        state = "sleep_to_idle"
        frame_index = 0
        messages = [
            "Hi!",
            "Hello!",
            "Ready to help!",
            "I am Scrappy!",
            "Click me again!",
            "Nice to meet you!",
         ]
        show_bubble(random.choice(messages))

def ask_question():
    global state, frame_index

    state = "move_left"
    frame_index = 0
    root.after(4000, show_prompt)


def show_prompt():
    prompt = tk.Toplevel(root)
    answer = tk.Label(prompt, text = "")
    prompt.title("Scrappy")
    prompt.geometry("500x150+520+500")
    
    question = tk.Label(prompt, text = "Scrappy: Would you like to scan a website?")
    question.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
    

    yes_button = tk.Button(prompt, text="Yes", command = lambda: clicked_yes(question, yes_button, no_button))
    yes_button.place(relx = 0.43, rely = 0.72, anchor = tk.CENTER)
    no_button = tk.Button(prompt, text="No", command = lambda: clicked_no(question, yes_button, no_button))
    no_button.place(relx = 0.57, rely = 0.72, anchor = tk.CENTER)
    prompt.overrideredirect(True)
    #prompt.wm_attributes('black')


########################

def input_validation(link_box):
    success_label = tk.Label(prompt, text = "")

    success_label.place(relx = 0.5, rely = 0.22, anchor = "center")

    error_label = tk.Label(prompt, text="")
    error_label.place(relx = 0.5, rely = 0.22, anchor = "center")
    i = 0

    answer.place_forget()

    
    #reading the link they inputted
    text = link_box.get()
    
    
    # cleaning the input
    text = text.strip()
    
    # 3. checking from simplest to strictest test
    
    periods = []
    for i in range(len(text)):
        if text[i] == ".":
            periods.append(".")

    if text == "":
        error_label.config(text = "Scrappy: Please enter a link !!")
        return
            
    elif " " in text:
        error_label.config(text = "Scrappy: Links can't have spaces in them")
        return 
        
    elif not text.startswith(("http://", "https://")):
        error_label.config(text = "Scrappy: Links start with http:// or https://")
        return 
    

        
    elif len(periods) < 2:
        error_label.config(text = "There has to be minimum 2 periods (www. and .com")
        return
        
    else:
        success_label.config(text = "Valid link! Now I can look for red flags.")
    




def clicked_yes(question, yes_button, no_button):
    #make other text go away
    yes_button.place_forget()
    no_button.place_forget()
    question.place_forget()

    
    #these line has to take link as input from user
    answer.config(text = "Okay paste link here")
    link_box = tk.Entry(window, width = 70)
    link_box.place(relx = 0.5, rely = 0.5, anchor = "center")
    check_button = tk.Button(prompt, text="Check Link", command = lambda: input_validation(link_box))
    check_button.place(relx = 0.5, rely = 0.80, anchor = "center")
    







def clicked_no(question, yes_button, no_button):

    answer = tk.Label(prompt, text = "")



    answer.place(relx = 0.5, rely = 0.5, anchor = "center")
    
    yes_button.place_forget()
    no_button.place_forget()
    question.place_forget()
    
    answer.config(text = "Scrappy: Okay have a good day")



#this function is to make yes no buttons after pressing image
#def next_steps():



    #this it to position buttons


    
    # so we moved beyond the picture, into question and yes or no

    
    
    

###################









def end_question():
    global state, frame_index
    state = "move_right"
    
def handle_answer(prompt, answer):
    prompt.destroy()
    print(f"User answered: {answer}")


def on_click(event):
    ask_question()


def on_hover(event):
    root.configure(cursor="hand2")


def on_leave(event):
    root.configure(cursor="")


#def pick_next_state():
 #   global state
  #  if state == "idle":
   #     chance = random.random()
    #    if chance < 0.12:
     #       state = "idle_to_sleep"
      #  elif chance < 0.25:
       #     state = "move_left" if random.random() < 0.5 else "move_right"
    #elif state == "sleep":
     #   if random.random() < 0.15:
      #      state = "sleep_to_idle"
    #elif state in {"move_left", "move_right"}:
     #   state = "idle"


def move_window():
    global x, y, vx, vy
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    x += vx
    y += vy
    if x < 0:
        x = 0
        vx = abs(vx)
    elif x + width > screen_w:
        x = screen_w - width
        vx = -abs(vx)

    if y < 0:
        y = 0
        vy = abs(vy)
    elif y + height > screen_h:
        y = screen_h - height
        vy = -abs(vy)

    root.geometry(f"{width}x{height}+{x}+{y}")


def animate():
    global frame_index, state, x, vx

    sequences = {
        "idle": idle,
        "idle_to_sleep": idle_to_sleep,
        "sleep": sleep,
        "sleep_to_idle": sleep_to_idle,
        "move_left": roll_left,
        "move_right": roll_right,
    }

    current = sequences.get(state, idle)
    if not current:
        current = sleep

    if frame_index >= len(current):
        frame_index = 0

    frame = current[frame_index]
    label.image = frame
    label.configure(image=frame)

    if state == "move_left":
        x -= 80
        root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}+{x}+{y}")
    elif state == "move_right":
        x += 80
        root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}+{x}+{y}")

    frame_index += 1
    if frame_index >= len(current):
        frame_index = 0
        if state == "idle_to_sleep":
            state = "sleep"
        elif state == "sleep_to_idle":
            state = "idle"
        elif state in {"move_left", "move_right"}:
            state = "idle"

    root.after(500, animate)


def on_press(event):
    root._drag_x = event.x_root - root.winfo_x()
    root._drag_y = event.y_root - root.winfo_y()
    root.bind("<B1-Motion>", on_drag)


def on_drag(event):
    root.geometry(f"+{event.x_root - root._drag_x}+{event.y_root - root._drag_y}")


root.bind("<Button-1>", on_press)
root.bind("<ButtonRelease-1>", lambda event: root.unbind("<B1-Motion>"))
root.geometry(f"100x100+{x}+{y}")
root.after(120, animate)
root.mainloop()



















