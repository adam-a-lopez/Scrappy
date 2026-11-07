import tkinter as tk



def input_validation(link_box):
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
    check_button = tk.Button(window, text="Check Link", command = lambda: input_validation(link_box))
    check_button.place(relx = 0.5, rely = 0.80, anchor = "center")
    







def clicked_no(question, yes_button, no_button):
    yes_button.place_forget()
    no_button.place_forget()
    question.place_forget()
    
    answer.config(text = "Scrappy: Okay have a good day")



#this function is to make yes no buttons after pressing image
def next_steps():



    #this it to position buttons


    
    # so we moved beyond the picture, into question and yes or no
    question = tk.Label(window, text = "Scrappy: Would you like to scan a website?")
    question.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
    

    yes_button = tk.Button(window, text="Yes", command = lambda: clicked_yes(question, yes_button, no_button))
    yes_button.place(relx = 0.43, rely = 0.72, anchor = tk.CENTER)
    no_button = tk.Button(window, text="No", command = lambda: clicked_no(question, yes_button, no_button))
    no_button.place(relx = 0.57, rely = 0.72, anchor = tk.CENTER)
    
    
    
    
    
    
#initializes and makes window
window = tk.Tk()


window.title("Scrappy")
window.geometry("520x100")

success_label = tk.Label(window, text = "")

success_label.place(relx = 0.5, rely = 0.22, anchor = "center")

error_label = tk.Label(window, text="")
error_label.place(relx = 0.5, rely = 0.22, anchor = "center")
answer = tk.Label(window, text = "")



answer.place(relx = 0.5, rely = 0.5, anchor = "center")



window.mainloop()