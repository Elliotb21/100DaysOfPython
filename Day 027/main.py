from tkinter import *

window = Tk()
window.title("TITLE BAR")
window.minsize(width=500, height=300)
window.config(padx=25, pady=25)

#Label
my_label = Label(text="I am a label", font=("Arial", 14, "underline"))
my_label.config(text="I am a label")
# my_label.place(x=200, y=150) # 0,0 is top left of screen, where window is defined as 500x300 pixels
my_label.grid(column=0,row=0)

#Button
def button_click():
    # my_label.config(text="Button was clicked!")
    my_label.config(text=input.get())
        
my_button = Button(text="Click here!", command=button_click)
# my_button.pack(side="top")    
my_button.grid(column=1, row=1)

my_second_button = Button(text="This is the second button")
my_second_button.grid(column=2, row=0)
my_second_button.config(padx=25, pady=25)

#Entry
input = Entry()
# input.pack()
input.grid(column=3, row=2)

    
    
window.mainloop()