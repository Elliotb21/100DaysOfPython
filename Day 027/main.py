import tkinter

window = tkinter.Tk()
window.title("TITLE BAR")
window.minsize(width=500, height=300)


#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 14, "underline"))
my_label.pack()

window.mainloop()