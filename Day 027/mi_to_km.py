from tkinter import *

FONT = ("Arial", 14)

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)

def button_click():
    calculated_value = round((float(input.get()) * 1.60934), 3)
    kilometer_value.config(text=f"{calculated_value:.3f}")


#Labels
miles = Label(text="miles",font=FONT)
miles.grid(column=2, row=0)

kilometer_text = Label(text="KM",font=FONT)
kilometer_text.grid(column=2, row=1)

kilometer_value = Label(text="No value", font=FONT)
kilometer_value.grid(column=1, row =1)

text = Label(text="is equal to: ", font=FONT)
text.grid(column=0, row=1)


#Button
calculate_button = Button(text="Calculate",command=button_click)
calculate_button.grid(column=1, row=2)

    
#Entry
input = Entry()
input.grid(column=1, row=0)



window.mainloop()