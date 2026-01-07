import tkinter as tk
from tkinter import messagebox

# ------------------ Data ------------------
contacts = []

# ------------------ Functions ------------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    clear_entries()
    view_contacts()
    messagebox.showinfo("Success", "Contact added successfully!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']}  |  {contact['phone']}")

def search_contact():
    keyword = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            contact_list.insert(tk.END, f"{contact['name']}  |  {contact['phone']}")

def select_contact(event):
    try:
        index = contact_list.curselection()[0]
        contact = contacts[index]

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])
    except:
        pass

def update_contact():
    try:
        index = contact_list.curselection()[0]
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        view_contacts()
        messagebox.showinfo("Updated", "Contact updated successfully!")
    except:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

def delete_contact():
    try:
        index = contact_list.curselection()[0]
        contacts.pop(index)
        view_contacts()
        clear_entries()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
    except:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# ------------------ GUI Design ------------------
root = tk.Tk()
root.title("Contact Management System")
root.geometry("650x600")
root.config(bg="#f2f6ff")

# Title
tk.Label(
    root,
    text="Contact Management System",
    font=("Helvetica", 20, "bold"),
    bg="#4a69bd",
    fg="white",
    pady=10
).pack(fill="x")

# Main Frame
main_frame = tk.Frame(root, bg="#f2f6ff")
main_frame.pack(pady=20)

# Left Frame (Form)
form_frame = tk.LabelFrame(
    main_frame,
    text="Contact Details",
    font=("Helvetica", 12, "bold"),
    bg="#f2f6ff",
    padx=15,
    pady=15
)
form_frame.grid(row=0, column=0, padx=20)

labels = ["Name", "Phone", "Email", "Address"]
entries = []

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label, bg="#f2f6ff", font=("Arial", 10)).grid(row=i, column=0, sticky="w", pady=5)
    entry = tk.Entry(form_frame, width=30)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

name_entry, phone_entry, email_entry, address_entry = entries

# Buttons
btn_frame = tk.Frame(form_frame, bg="#f2f6ff")
btn_frame.grid(row=4, columnspan=2, pady=10)

tk.Button(btn_frame, text="Add", width=10, bg="#38ada9", fg="white", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, bg="#f6b93b", fg="white", command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, bg="#e55039", fg="white", command=delete_contact).grid(row=0, column=2, padx=5)

# Right Frame (Contact List)
list_frame = tk.LabelFrame(
    main_frame,
    text="Contact List",
    font=("Helvetica", 12, "bold"),
    bg="#f2f6ff",
    padx=15,
    pady=15
)
list_frame.grid(row=0, column=1, padx=20)

search_entry = tk.Entry(list_frame, width=30)
search_entry.pack(pady=5)
tk.Button(list_frame, text="Search", bg="#4a69bd", fg="white", command=search_contact).pack(pady=5)

contact_list = tk.Listbox(list_frame, width=40, height=15)
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", select_contact)

# Footer
tk.Label(
    root,
    text="Simple • Clean • User-Friendly",
    bg="#4a69bd",
    fg="white",
    pady=5
).pack(side="bottom", fill="x")

root.mainloop()


