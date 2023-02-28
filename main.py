from tkinter import *
from tkinter import messagebox
from password_generator import generate
import pyperclip


FONT = ("Arial", 14, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = generate()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website.strip() == "" or password.strip() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        return

    is_ok = messagebox.askokcancel(title=f"{website}", message=f"There are details entered:\n"
                                                               f"Email/Username: {email}\n"
                                                                f"Password: {password}\n"
                                                                f"Want to save it?\n")
    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(f"{website.strip()} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Mangager")
window.config(padx=50, pady=80)


canvas = Canvas(width=200, height=200)
img_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_file)
canvas.grid(row=0, column=1)


# website_label
website_label = Label(text="Website")
website_label.config(text="Website:", font=FONT)
website_label.grid(row=1, column=0)


# website_entry
website_entry = Entry(width=35)
website_entry.insert(END, string="")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)


# email_label
email_label = Label(text="Email")
email_label.config(text="Email:", font=FONT)
email_label.grid(row=2, column=0)

# email_entry
email_entry = Entry(width=35)
email_entry.insert(0, string="kirolos@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# password_label
password_label = Label(text="Password")
password_label.config(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# password_entry
password_entry = Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

# Generate password
button = Button(text="Click Me", command=generate_password)
button.grid(row=3, column=2)

# Add password
button = Button(text="Click Me", command=save_password, width=36)
button.grid(row=4, column=1, columnspan=2)



window.mainloop()