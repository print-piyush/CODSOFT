import tkinter as tk
import string
import random
import pyperclip

def generate_password():
    password_length = int(length_entry.get())
    charset = ''

    if lowercase_var.get():
        charset += string.ascii_lowercase
    if uppercase_var.get():
        charset += string.ascii_uppercase
    if digits_var.get():
        charset += string.digits
    if special_chars_var.get():
        charset += string.punctuation

    if charset:
        password = ''.join(random.choice(charset) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

def copy_to_clipboard():
    generated_password = password_entry.get()
    pyperclip.copy(generated_password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
