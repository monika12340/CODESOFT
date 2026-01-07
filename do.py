import tkinter as tk
from tkinter import messagebox, simpledialog

# ------------------ Functions ------------------
def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    task_list.insert(tk.END, f"⬜ {task}")
    task_entry.delete(0, tk.END)
    update_status()

def edit_task():
    try:
        index = task_list.curselection()[0]
        old_task = task_list.get(index)[2:]
        new_task = simpledialog.askstring("Edit Task", "Update task:", initialvalue=old_task)
        if new_task:
            status = task_list.get(index)[:2]
            task_list.delete(index)
            task_list.insert(index, f"{status} {new_task}")
            update_status()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

def mark_done():
    try:
        index = task_list.curselection()[0]
        task = task_list.get(index)[2:]
        task_list.delete(index)
        task_list.insert(index, f"✅ {task}")
        update_status()
    except:
        messagebox.showwarning("Selection Error", "Please select a task.")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
        update_status()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        task_list.delete(0, tk.END)
        update_status()

def update_status():
    total = task_list.size()
    completed = sum(1 for i in range(total) if task_list.get(i).startswith("✅"))
    status_label.config(
        text=f"📊 Total Tasks: {total} | Completed: {completed}"
    )

# ------------------ GUI Design ------------------
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("600x700")
root.config(bg="#f1f2f6")
root.resizable(False, False)

# Header
tk.Label(
    root,
    text="📝 To-Do List Manager",
    font=("Helvetica", 22, "bold"),
    bg="#3742fa",
    fg="white",
    pady=15
).pack(fill="x")

# Input Section
input_frame = tk.Frame(root, bg="#f1f2f6")
input_frame.pack(pady=20)

task_entry = tk.Entry(
    input_frame,
    width=30,
    font=("Arial", 12),
    bd=1,
    relief="solid"
)
task_entry.grid(row=0, column=0, padx=10)

tk.Button(
    input_frame,
    text="➕ Add Task",
    width=12,
    bg="#2ed573",
    fg="white",
    font=("Arial", 11, "bold"),
    command=add_task
).grid(row=0, column=1)

# Task List
task_list = tk.Listbox(
    root,
    width=45,
    height=15,
    font=("Arial", 12),
    bd=0,
    selectbackground="#70a1ff",
    highlightthickness=0
)
task_list.pack(pady=15)

# Buttons
btn_frame = tk.Frame(root, bg="#f1f2f6")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="✏ Edit",
    width=12,
    bg="#1e90ff",
    fg="white",
    font=("Arial", 11, "bold"),
    command=edit_task
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame,
    text="✅ Done",
    width=12,
    bg="#2ed573",
    fg="white",
    font=("Arial", 11, "bold"),
    command=mark_done
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame,
    text="🗑 Delete",
    width=12,
    bg="#ff4757",
    fg="white",
    font=("Arial", 11, "bold"),
    command=delete_task
).grid(row=0, column=2, padx=5)

tk.Button(
    btn_frame,
    text="🧹 Clear All",
    width=12,
    bg="#ffa502",
    fg="white",
    font=("Arial", 11, "bold"),
    command=clear_tasks
).grid(row=0, column=3, padx=5)

# Status Bar
status_label = tk.Label(
    root,
    text="📊 Total Tasks: 0 | Completed: 0",
    font=("Arial", 12, "bold"),
    bg="#f1f2f6"
)
status_label.pack(pady=15)

# Footer
tk.Label(
    root,
    text="Organize • Update • Track • Complete",
    bg="#3742fa",
    fg="white",
    pady=10
).pack(side="bottom", fill="x")

root.mainloop()



