from tkinter import *
from tkinter import messagebox
import random
import pandas

# to same the randomly chosen word:
current_card = {}

to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"

# data = pandas.read_csv("data/french_words.csv")
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# print(to_learn)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(card_title, fill="White", text="English")
    canvas.itemconfig(card_word, fill="White", text=current_card["English"])
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    # window.after(3000, change_card)
# to config an item in canvas we use canvas.itemconfig()

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data_new = pandas.DataFrame(to_learn)
    data_new.to_csv("data/words_to_learn.csv", index=False)

    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# to fix the bug of immediate tapping of button, where the timer would just go on.

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

wrong_but_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_but_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_but_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_but_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()


