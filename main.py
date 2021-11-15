from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join([char for char in password_list])
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Details:\nwebsite:{website}\nusername:{username}\npassword:{password}\nAre you OK with generated password?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")
canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_input = Entry(width=51)
website_input.grid(row=1, column=1, sticky='w', columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(row=2, column=0)

username_input = Entry(width=51)
username_input.grid(row=2, column=1, sticky='w', columnspan=2)
username_input.insert(0, "rakshithraj.gp@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky='w')

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')
generate_button.config()

add_button = Button(text="Add", width=36, command=add_to_file)
add_button.grid(row=4, column=1, sticky='w', columnspan=2)

window.mainloop()
