import tkinter

window = tkinter.Tk()
window.title("First GUI Program")

window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
# place it into the scene in the center automatically











window.mainloop()