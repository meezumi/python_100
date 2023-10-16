# import tkinter
from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# labels

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# place it into the scene in the center automatically
# packer is a geometry-management mechanism.
# https://docs.python.org/3/library/tkinter.html#the-packer
# my_label.pack() # be default its in the center
# my_label.pack(side="left")
# my_label.pack(expand=True)
my_label["text"] = "nice ass"
my_label.config(text="hehe juicy")
# my_label.pack()
# my_label.place(x=100, y=200) # specific coordinates for the location
my_label.grid(column=0, row=0)


# buttons
def button_clicked():
    print("i got clicked")
    # my_label["text"] = "i got clicked"
    ans = input.get()
    my_label.config(text=ans)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
# for it to be displayed in the screen
button.grid(column=1, row=1)

new_button = Button(text="newbie")
new_button.grid(column=2, row=0)

# entry

input = Entry(width=10)
input.get() # returns the input as a string
input.insert(END, string="Start Here")
print(input.get())
# input.pack()
input.grid(column=3, row=2)



window.mainloop()