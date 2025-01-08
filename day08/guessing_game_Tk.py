import random
import tkinter as tk
from tkinter import messagebox

def start_game():
    global random_number, guess_count
    random_number = random.randint(1, 20)
    guess_count = 0
    update_status("New game started! Guess a number between 1 and 20.")

def check_guess():
    global guess_count
    user_input = entry.get().strip().lower()

    if user_input == "x":
        exit_game()
    elif user_input == "s":
        update_status(f"Cheat activated! The number is {random_number}")
        guess_count += 1
    elif user_input == "n":
        start_game()
    else:
        try:
            user_guess = int(user_input)
            if user_guess < 1 or user_guess > 20:
                update_status("Number out of guessing range. Guess a number between 1-20.")
                return

            guess_count += 1

            if user_guess < random_number:
                update_status("Too small! Try again.")
            elif user_guess > random_number:
                update_status("Too big! Try again.")
            else:
                update_status(f"You win! It took {guess_count} guesses.")
                if messagebox.askyesno("Play Again?", "Do you want to play another game?"):
                    start_game()
                else:
                    root.destroy()
        except ValueError:
            update_status("Invalid input! Enter a number between 1-20 or 'x', 'n', 's'.")

def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def update_status(message):
    status_label.config(text=message)

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Guessing Game")

random_number = 0
guess_count = 0

# GUI Components
instruction_label = tk.Label(root, text="Enter your guess (1-20 or 'n', 's', 'x'):", font=("Arial", 14))
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=check_guess, font=("Arial", 14))
submit_button.pack(pady=5)

status_label = tk.Label(root, text="Click 'Submit' after entering your guess!", font=("Arial", 14), fg="blue")
status_label.pack(pady=20)

start_game()
root.mainloop()