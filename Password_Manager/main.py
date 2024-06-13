from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list.extend([choice(symbols) for j in range(randint(2, 4))])
    password_list.extend([choice(numbers) for k in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    passwrd = pass_entry.get()
    if website == "" or passwrd == "":
        messagebox.showwarning(title="Warning!", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail:{email}"
                                                              f"\nPassword:{passwrd}\nIs it ok?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {passwrd}\n")

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

web_label = Label(text="Website")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

gen_button = Button(text="Generate Password", command=pass_gen)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

web_entry = Entry(width=50)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=50)
email_entry.insert(END, "abc@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

window.mainloop()
