import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock Paper Scissors")

player_score = 0
computer_score = 0

options = ["Rock", "Paper", "Scissors"]

def play(player_choice):
    global player_score, computer_score

    comp_choice = random.choice(options)
    result = ""

    if player_choice == comp_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and comp_choice == "Scissors") or \
         (player_choice == "Paper" and comp_choice == "Rock") or \
         (player_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=f"Computer chose {comp_choice}.\n{result}")
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text="Player: 0  |  Computer: 0")
    result_label.config(text="")

tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Helvetica", 14)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", font=("Helvetica", 12), width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper", font=("Helvetica", 12), width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissors", font=("Helvetica", 12), width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Player: 0  |  Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=5)

tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_game).pack(pady=10)

root.mainloop()