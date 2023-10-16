from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    kilometer_ans.config(text=f"{km}")

window = Tk()
window.minsize(width=200, height=100)
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

label1 = Label()
label1.config(text="Miles")
label1.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

kilometer_ans = Label(text="0")
kilometer_ans.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate = Button()
calculate.config(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)



window.mainloop()