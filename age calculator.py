import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        dob = datetime(year, month, day)
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid date.")


root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")


tk.Label(root, text="Day:").pack(pady=5)
day_entry = tk.Entry(root)
day_entry.pack(pady=5)

tk.Label(root, text="Month:").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Label(root, text="Year:").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack(pady=5)


calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=20)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
