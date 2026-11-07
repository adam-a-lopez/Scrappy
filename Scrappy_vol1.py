# Adam Lopez
# Desktop buddy

import os
import random
import tkinter as tk

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

def on_question():
    global state, frame_index
    if state == 
      


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
        current = idle

    if frame_index >= len(current):
        frame_index = 0

    frame = current[frame_index]
    label.image = frame
    label.configure(image=frame)

    if state == "move_left":
        x -= 3
        root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}+{x}+{y}")
    elif state == "move_right":
        x += 3
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
        

    root.after(120, animate)


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



















