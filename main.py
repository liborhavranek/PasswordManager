from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)

	password = "".join(password_list)
	password_entry.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_data = {
		website: {
			"email": email,
			"password": password
		}

	}

	if len(website) == 0 or len(email) == 0 or len(password) == 0:
		messagebox.showerror(title="Ooops", message="Please insert valid information")
	else:
		is_okay = messagebox.showinfo(title=website, message=f"These are the details entered\n Email: {email}\nPassword: {password}\n It's okay?")

		if is_okay:
			try:
				with open("data.json", "r") as data_file:
					data = json.load(data_file)
					data.update(new_data)
			except FileNotFoundError:
				with open("data.json", 'w') as data_file:
					json.dump(new_data, data_file, indent=4)
				pass
			else:
				with open("data.json", 'w') as data_file:
					json.dump(data, data_file, indent=4)
			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
	website = website_entry.get()
	try:
		with open("data.json") as data_file:
			data = json.load(data_file)
	except FileNotFoundError:
		messagebox.showinfo(title="error", message="No data file")
	else:
		if website in data:
			email = data[website]["email"]
			password = data[website]["password"]
			messagebox.showinfo(message=f"{email}\n, Password: {password}", title=f"Your account on {website}")
		else:
			messagebox.showinfo(title="error", message=f"No details for {website} exist")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, "liborhavranek91@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, sticky="W")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
