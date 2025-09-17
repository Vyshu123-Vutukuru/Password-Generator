import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_specials = specials_var.get()
        
        password = generate_password(length, use_digits, use_specials)
        result_label.config(text=f"✅ Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Create window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.configure(bg="#2c3e50")  # background color

# Widgets
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=5)

tk.Label(frame, text="Password Length:", bg="#2c3e50", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")

digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

digits_check = tk.Checkbutton(frame, text="Include Digits", variable=digits_var, bg="#2c3e50", fg="white", selectcolor="#34495e")
specials_check = tk.Checkbutton(frame, text="Include Specials", variable=specials_var, bg="#2c3e50", fg="white", selectcolor="#34495e")
digits_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
specials_check.grid(row=1, column=1, padx=5, pady=5, sticky="w")

generate_btn = tk.Button(root, text="Generate Password", command=on_generate, bg="#1abc9c", fg="white", font=("Arial", 12, "bold"))
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2c3e50", fg="yellow")
result_label.pack(pady=10)

# Run window
root.mainloop()
