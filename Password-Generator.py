import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage

import random

def generate_passwords():
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())

        if length <= 0 or count <= 0:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Please enter positive integers for length and count.")
            return

        char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"
        passwords = []
        for _ in range(count):
            password = "".join(random.choice(char) for _ in range(length))
            passwords.append(password)

        result_text.delete(1.0, tk.END)
        for password in passwords:
            result_text.insert(tk.END, f"Generated Password: {password}\n\n")

    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid input. Please enter integers for length and count.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.iconbitmap("icon.ico")
window.geometry("550x450")  # Fixed window size
window.resizable(False, False) #disable resizing

# Load background image and resize
try:
    bg_image = PhotoImage(file="background.png")  # Replace with your image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
except FileNotFoundError:
    print("Background image not found. Using default background.")

# Length label and entry (same line)
length_frame = tk.Frame(window, bg="#e0f2f7")
length_frame.pack(pady=10, fill="x", padx=10)

length_label = tk.Label(length_frame, text="Password Length:", bg="#e0f2f7", font=("Arial", 20))
length_label.pack(side="left", padx=(0, 5))

length_entry = tk.Entry(length_frame, font=("Arial", 20))
length_entry.pack(side="left", fill="x", expand=True)

# Count label and entry (same line)
count_frame = tk.Frame(window, bg="#e0f2f7")
count_frame.pack(pady=10, fill="x", padx=10)

count_label = tk.Label(count_frame, text="Number of Passwords:", bg="#e0f2f7", font=("Arial", 20))
count_label.pack(side="left", padx=(0, 5))

count_entry = tk.Entry(count_frame, font=("Arial", 20))
count_entry.pack(side="left", fill="x", expand=True)

# Generate button
generate_button = tk.Button(window, text="Generate Passwords", command=generate_passwords, bg="#4CAF50", fg="white", font=("Arial", 14))
generate_button.pack(pady=15)

# Result text area with scrollbar
result_text = scrolledtext.ScrolledText(window, height=8, width=40, font=("Arial", 12))
result_text.pack(pady=10, padx=10, fill="x")

window.mainloop()
