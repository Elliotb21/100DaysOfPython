from tkinter import *

window = Tk()
window.title("TITLE BAR")
window.minsize(width=500, height=300)


#Label
my_label = Label(text="I am a label", font=("Arial", 14, "underline"))
my_label.pack()

#Button
def button_click():
    # my_label.config(text="Button was clicked!")
    my_label.config(text=input.get())

        
my_button = Button(text="Click here!", command=button_click)
my_button.pack(side="bottom")

#Entry
input = Entry()
input.pack()

    
    
window.mainloop()