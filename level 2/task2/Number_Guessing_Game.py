from tkinter import *
import random

ws = Tk()
ws.title("Number Guessing Game")
ws.geometry("450x300")

secret_number = random.randint(1, 10)
attempts = 3

guess_var = StringVar()
message_var = StringVar()
error_var = StringVar()

def check_guess():
    global attempts
    error_var.set("")

    try:
        user_guess = int(guess_var.get())

        if user_guess <= 0:
            error_var.set("❗ Enter a number greater than 0.")
            return

        if attempts > 0:
            if user_guess == secret_number:
                message_var.set("🎉 Congratulations! You guessed it right!")
                submit_btn.config(state="disabled")
            elif user_guess < secret_number:
                attempts -= 1
                message_var.set(f"🔼 The number is higher. Attempts left: {attempts}")
            else:
                attempts -= 1
                message_var.set(f"🔽 The number is lower. Attempts left: {attempts}")

            if attempts == 0 and user_guess != secret_number:
                message_var.set(f"😢 Game over! The correct number was: {secret_number}")
                submit_btn.config(state="disabled")
    except ValueError:
        error_var.set("⚠️ Please enter a valid number.")

    guess_var.set("")

Label(ws, text="🎯 Number Guessing Game", font=("Arial", 15), fg="white", bg="darkblue").pack(pady=10 )

Entry(ws, textvariable=guess_var, font=("Arial", 14), justify='center').pack(pady=15)

submit_btn = Button(ws, text="Submit Guess", command=check_guess, font=("Arial", 12, "bold"), bg="green", fg="white")
submit_btn.pack(pady=10)

Label(ws, textvariable=message_var, font=("Arial", 12)).pack(pady=10)
Label(ws, textvariable=error_var, fg="red", font=("Arial", 10)).pack()

ws.mainloop()
