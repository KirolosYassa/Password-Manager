import json
from tkinter import *
from tkinter import messagebox
from password_generator import generate
import pyperclip


FONT = ("Arial", 14, "normal")

def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()   

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except json.JSONDecodeError:
        messagebox.showerror(title=f"Error", message=f"No data found in the database!")
    except FileNotFoundError:
        messagebox.showerror(title=f"Error", message=f"No data found in the database!")
    else:
        website_inserted = website_entry.get()
        print(website_inserted)
        if website_inserted.strip() != "":
            try:
                email = data[website_inserted]["email"]
                password = data[website_inserted]["password"]
                messagebox.showinfo(title=f"{website_inserted}", message=f"Your Data:\n"
                                                                    f"Email/Username: {email}\n"
                                                                        f"Password: {password}\n") 
            except KeyError:
                messagebox.showerror(title=f"Error", message=f"No data found for this website [ {website_inserted} ] !")
            finally:
                website_entry.focus()   

    finally:
        website_entry.focus()   
            
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
    new_data = {
        website:{
        "email":email,
        "password":password
        }
    }

    if website.strip() == "" or password.strip() == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
        return
    
    is_ok = messagebox.askokcancel(title=f"{website}", message=f"There are details entered:\n"
                                                               f"Email/Username: {email}\n"
                                                                f"Password: {password}\n"
                                                                f"Want to save it?\n")
    if is_ok:
        
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        except json.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            reset()


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

# email_label
email_label = Label(text="Email")
email_label.config(text="Email:", font=FONT)
email_label.grid(row=2, column=0)

# password_label
password_label = Label(text="Password")
password_label.config(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# website_entry
website_entry = Entry(width=36)
website_entry.insert(END, string="")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1)

# Search Button
search_button = Button(text="Search", command=search_website, width=14)
search_button.grid(row=1, column=2, columnspan=2)



# password_entry
password_entry = Entry(width=36)
password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

# Generate password
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, columnspan=2)


# Add password
add_button = Button(text="Add", command=save_password, width=46)
add_button.grid(row=4, column=1, columnspan=2)


# email_entry
email_entry = Entry(width=36)
email_entry.insert(0, string="kirolos@gmail.com")
email_entry.grid(row=2, column=1, columnspan=1)

window.mainloop()