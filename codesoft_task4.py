import tkinter as tk
import random

# ------------------ Game Data ------------------
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
rounds_played = 0

# ------------------ Game Logic ------------------
def play(user_choice):
    global user_score, computer_score, rounds_played

    computer_choice = random.choice(choices)
    rounds_played += 1

    user_choice_label.config(text=f"👤 Your Choice: {user_choice}")
    computer_choice_label.config(text=f"💻 Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "🎉 You Win!"
        user_score += 1
    else:
        result = "😢 You Lose!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"🏆 Score  You: {user_score} | Computer: {computer_score} | Rounds: {rounds_played}"
    )

    history_list.insert(
        tk.END,
        f"Round {rounds_played}: You={user_choice} | Computer={computer_choice} → {result}"
    )

def reset_game():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0

    user_choice_label.config(text="👤 Your Choice:")
    computer_choice_label.config(text="💻 Computer Choice:")
    result_label.config(text="")
    score_label.config(text="🏆 Score  You: 0 | Computer: 0 | Rounds: 0")
    history_list.delete(0, tk.END)

# ------------------ GUI Design ------------------
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x700")
root.config(bg="#f1f2f6")
root.resizable(False, False)

# Header
tk.Label(
    root,
    text="✊ ✋ ✌ Rock Paper Scissors",
    font=("Helvetica", 22, "bold"),
    bg="#3742fa",
    fg="white",
    pady=15
).pack(fill="x")

# Instructions
tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors to play",
    font=("Arial", 12),
    bg="#f1f2f6"
).pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f1f2f6")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame, text="✊ Rock", width=14, height=2,
    bg="#70a1ff", fg="white",
    font=("Arial", 12, "bold"),
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame, text="✋ Paper", width=14, height=2,
    bg="#2ed573", fg="white",
    font=("Arial", 12, "bold"),
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=10)

tk.Button(
    btn_frame, text="✌ Scissors", width=14, height=2,
    bg="#ffa502", fg="white",
    font=("Arial", 12, "bold"),
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=10)

# Result Section
result_frame = tk.Frame(root, bg="#f1f2f6")
result_frame.pack(pady=20)

user_choice_label = tk.Label(
    result_frame, text="👤 Your Choice:",
    font=("Arial", 12), bg="#f1f2f6"
)
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(
    result_frame, text="💻 Computer Choice:",
    font=("Arial", 12), bg="#f1f2f6"
)
computer_choice_label.pack(pady=5)

result_label = tk.Label(
    result_frame, text="",
    font=("Arial", 18, "bold"),
    fg="#3742fa",
    bg="#f1f2f6"
)
result_label.pack(pady=15)

# Score
score_label = tk.Label(
    root,
    text="🏆 Score  You: 0 | Computer: 0 | Rounds: 0",
    font=("Arial", 12, "bold"),
    bg="#f1f2f6"
)
score_label.pack(pady=10)

# History
tk.Label(
    root,
    text="📜 Game History",
    font=("Arial", 13, "bold"),
    bg="#f1f2f6"
).pack(pady=5)

history_list = tk.Listbox(
    root,
    width=70,
    height=8,
    font=("Arial", 10),
    bd=0,
    selectbackground="#ced6e0"
)
history_list.pack(pady=10)

# Control Buttons
control_frame = tk.Frame(root, bg="#f1f2f6")
control_frame.pack(pady=15)

tk.Button(
    control_frame,
    text="🔄 Play Again / Reset",
    width=20,
    bg="#ff4757",
    fg="white",
    font=("Arial", 11, "bold"),
    command=reset_game
).grid(row=0, column=0, padx=10)

tk.Button(
    control_frame,
    text="❌ Exit Game",
    width=15,
    bg="#2f3542",
    fg="white",
    font=("Arial", 11, "bold"),
    command=root.destroy
).grid(row=0, column=1, padx=10)

# Footer
tk.Label(
    root,
    text="Fun • Interactive • Fully Featured Python GUI Game",
    bg="#3742fa",
    fg="white",
    pady=10
).pack(side="bottom", fill="x")

root.mainloop()
