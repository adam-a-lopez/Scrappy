#11/6
#steven joseph
# Display for Scrappy

# add function check() so that we can keep track of all the scans we took



import tkinter as tk



def clicked_yes(question, yes_button, no_button):
    #make other text go away
    yes_button.pack_forget()
    no_button.pack_forget()
    question.pack_forget()

    
    #these line has to take link as input from user
    answer.config(text = "Okay paste link here")
    link_box = tk.Entry(window, width = 70)
    link_box.pack()
    check_button = tk.Button(window, text="Check Link", command = lambda: input_validation(link_box))
    check_button.pack()
    



    
def input_validation(link_box):
    i = 0

    answer.pack_forget()

    
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
        error_label.config(text = "Scrappy: Links cam't have spaces in them")
        return 
        
    elif not text.startswith(("http://", "https://")):
        error_label.config(text = "Scrappy: Links start with http:// or https://")
        return 
    

        
    elif len(periods) < 2:
        error_label.config(text = "There has to be minimum 2 periods (www. and .com")
        return
        
    else:
        success_label.config(text = "Valid link! Now I can look for red flags.")
    

def clicked_no(question, yes_button, no_button):
    yes_button.pack_forget()
    no_button.pack_forget()
    question.pack_forget()
    
    answer.config(text = "Scrappy: Okay have a good day")


#this function is to make yes no buttons after pressing image
def next_steps():

    #button.pack_forget()

    #this it to position buttons
    row = tk.Frame(window)
    row.pack(pady=20)

    
    # so we moved beyond the picture, into question and yes or no
    question = tk.Label(window, text = "Scrappy: Would you like to scan a website?")
    question.pack(pady = 10)
    
    yes_button = tk.Button(row, text="Yes", command = lambda: clicked_yes(question, yes_button, no_button))
    yes_button.pack(side="left", padx = 5)
    no_button = tk.Button(row, text="No", command = lambda: clicked_no(question, yes_button, no_button))
    no_button.pack(side = "left", padx = 5)




#initializes and makes window
window = tk.Tk()


window.title("Scrappy")
window.geometry("500x600")

success_label = tk.Label(window, text = "")
success_label.pack(pady=25)

error_label = tk.Label(window, text="")
error_label.pack(pady=25)
answer = tk.Label(window, text = "")
######################################

#scrappy_pic = tk.PhotoImage(file="cat_placeholder.png")
#button = tk.Button(window, image=scrappy_pic, command=next_steps)



answer.pack()
#button.pack()


window.mainloop()










#root.mainloop()
