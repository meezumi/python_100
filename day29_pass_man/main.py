from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

# password = ""
# for char in password_list:
#   password += char

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    # messagebox.showinfo(title="Title", message="Message")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            # if data.json file does not exist, we solve this error
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # this is to read data in json
            data.update(new_data)
            # this is used to update the contents of json file.

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                # this is to write in json, saving the data
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

        # is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        # if is_okay:
        #     with open("password_bank.txt", "a") as data_file:
                # data_file.write(f"{website} | {email} | {password}\n")
                # web_entry.delete(0, END)
                # pass_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="no data file found.")
        # print(data)
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message=f"no data for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
rimuru_img = PhotoImage(file="rimuru.png")
canvas.create_image(100, 100, image=rimuru_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_entry = Entry(width=32)
web_entry.grid(column=1, row=1)
web_entry.focus()
# you can directly start typing here now.

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "aaryank@gmail.com")

pass_label = Label(text="Password:", padx=10)
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)

search_button = Button(width=15, text="Search", command=find_password)
search_button.grid(column=2, row=1)

gen_button = Button(width=15, text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()

