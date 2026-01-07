import tkinter as tk
from tkinter import messagebox
import random
import string

# ------------------ Functions ------------------
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    characters = ""
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character type")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# ------------------ GUI ------------------
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x450")
root.config(bg="#f1f2f6")
root.resizable(False, False)

# Header
tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Helvetica", 22, "bold"),
    bg="#3742fa",
    fg="white",
    pady=15
).pack(fill="x")

# Length input
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f1f2f6").pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack()

# Complexity options
tk.Label(root, text="Select Character Types:", font=("Arial", 12, "bold"), bg="#f1f2f6").pack(pady=10)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="🅰 Uppercase", variable=uppercase_var, bg="#f1f2f6", font=("Arial", 12)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="🆎 Lowercase", variable=lowercase_var, bg="#f1f2f6", font=("Arial", 12)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="🔢 Digits", variable=digits_var, bg="#f1f2f6", font=("Arial", 12)).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="❗ Symbols", variable=symbols_var, bg="#f1f2f6", font=("Arial", 12)).pack(anchor="w", padx=50)

# Generate button
tk.Button(
    root,
    text="🟢 Generate Password",
    font=("Arial", 12, "bold"),
    bg="#2ed573",
    fg="white",
    command=generate_password
).pack(pady=20)

# Display generated password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), justify="center", width=30, bd=2, relief="solid").pack(pady=10)

# Footer
tk.Label(
    root,
    text="Strong & Random Passwords Made Easy!",
    bg="#3742fa",
    fg="white",
    pady=10
).pack(side="bottom", fill="x")

root.mainloop()
