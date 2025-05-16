import tkinter as tk
from tkinter import messagebox
from app.model import load_model
from app.guard import guard_transaction

def launch_gui():
    model, feature_columns = load_model()

    def on_submit():
        try:
            transaction_data = [float(entry.get()) for entry in entries]
            prediction = guard_transaction(transaction_data, model, feature_columns)
            if prediction == 1:
                messagebox.showwarning("Fraud Alert", "Fraudulent transaction detected!")
            else:
                messagebox.showinfo("Success", "Transaction is legitimate.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    window = tk.Tk()
    window.title("Credit Card Fraud Detector")

    tk.Label(window, text="Enter Transaction Details:").pack()

    entries = []
    for col in feature_columns:
        frame = tk.Frame(window)
        frame.pack(pady=2)
        tk.Label(frame, text=col).pack(side=tk.LEFT)
        entry = tk.Entry(frame, width=20)
        entry.pack(side=tk.RIGHT)
        entries.append(entry)

    submit_btn = tk.Button(window, text="Check Transaction", command=on_submit)
    submit_btn.pack(pady=10)

    window.mainloop()
