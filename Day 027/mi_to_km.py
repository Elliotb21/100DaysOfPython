from tkinter import *

FONT = ("Arial", 14, "underline")

window = Tk()
window.title(text="Miles to Kilometers Converter")
window.minsize(width=500, height=300)

#Labels
miles = Label.config(text="miles",font=FONT)
miles.grid



window.mainloop()