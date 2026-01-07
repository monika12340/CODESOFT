import tkinter as tk

# ---------------- Functions ----------------
def press(key):
    try:
        if key == "=":
            display.set(str(eval(display.get())))
        elif key == "C":
            display.set("")
        elif key == "⌫":
            display.set(display.get()[:-1])
        elif key == "%":
            display.set(str(eval(display.get()) / 100))
        elif key == "±":
            if display.get().startswith("-"):
                display.set(display.get()[1:])
            else:
                display.set("-" + display.get())
        else:
            display.set(display.get() + key)
    except:
        display.set("Error")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("360x500")  # Bigger window
root.resizable(False, False)
root.configure(bg="#1e272e")

display = tk.StringVar()

# Display
entry = tk.Entry(
    root, textvariable=display, font=("Arial", 24),
    bd=8, relief="flat", justify="right",
    bg="#d2dae2", fg="black"
)
entry.pack(fill="x", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons layout
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

frame = tk.Frame(root, bg="#1e272e")
frame.pack(padx=10, pady=10, fill="both", expand=True)

for r, row in enumerate(buttons):
    for c, btn in enumerate(row):
        tk.Button(
            frame,
            text=btn,
            font=("Arial", 18, "bold"),
            bg="#485460" if btn not in ["=", "C"] else ("#ffa502" if btn == "=" else "#ff4757"),
            fg="white",
            command=lambda x=btn: press(x)
        ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# Make buttons expand to fill the grid
for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

root.mainloop()
