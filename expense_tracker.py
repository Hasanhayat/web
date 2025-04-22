import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import os

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Smart Expense & Budget Tracker")
        self.root.geometry("950x600")
        self.root.configure(bg="#f0f4f7")
        self.filename = "expense_data.json"
        self.data = {"budget": 0, "transactions": []}

        self.load_data()
        self.create_widgets()
        self.update_summary()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="white", foreground="black", fieldbackground="white")

        title = tk.Label(self.root, text="💼 Smart Expense & Budget Tracker", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#3e3e3e")
        title.pack(pady=10)

        # Budget Entry
        budget_frame = tk.Frame(self.root, bg="#f0f4f7")
        budget_frame.pack(pady=5)
        tk.Label(budget_frame, text="Set Monthly Budget: ", bg="#f0f4f7").pack(side="left")
        self.budget_entry = tk.Entry(budget_frame)
        self.budget_entry.pack(side="left")
        tk.Button(budget_frame, text="Set", command=self.set_budget).pack(side="left", padx=5)

        # Add Expense/Income
        entry_frame = tk.Frame(self.root, bg="#f0f4f7")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Title:", bg="#f0f4f7").grid(row=0, column=0)
        self.title_entry = tk.Entry(entry_frame)
        self.title_entry.grid(row=0, column=1)

        tk.Label(entry_frame, text="Amount:", bg="#f0f4f7").grid(row=0, column=2)
        self.amount_entry = tk.Entry(entry_frame)
        self.amount_entry.grid(row=0, column=3)

        tk.Label(entry_frame, text="Type:", bg="#f0f4f7").grid(row=0, column=4)
        self.type_combo = ttk.Combobox(entry_frame, values=["Income", "Expense"], state="readonly")
        self.type_combo.grid(row=0, column=5)
        self.type_combo.current(0)

        tk.Button(entry_frame, text="Add", command=self.add_transaction).grid(row=0, column=6, padx=10)

        # Summary Labels
        self.summary_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#f0f4f7", fg="#333")
        self.summary_label.pack(pady=5)

        # Treeview for Transactions
        self.tree = ttk.Treeview(self.root, columns=("Title", "Amount", "Type", "Date"), show="headings", height=8)
        self.tree.pack(pady=10)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Chart Button
        tk.Button(self.root, text="📊 Show Chart", command=self.show_chart).pack(pady=5)

    def add_transaction(self):
        title = self.title_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Amount must be a number")
            return
        t_type = self.type_combo.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.data["transactions"].append({
            "title": title, "amount": amount, "type": t_type, "date": date
        })
        self.save_data()
        self.update_summary()
        self.refresh_tree()

    def update_summary(self):
        income = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "Income")
        expense = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "Expense")
        balance = self.data["budget"] + income - expense
        self.summary_label.config(text=f"Budget: {self.data['budget']} | Income: {income} | Expense: {expense} | Balance: {balance}")
        self.refresh_tree()

    def refresh_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for t in self.data["transactions"]:
            self.tree.insert("", "end", values=(t["title"], t["amount"], t["type"], t["date"]))

    def set_budget(self):
        try:
            self.data["budget"] = float(self.budget_entry.get())
            self.save_data()
            self.update_summary()
        except ValueError:
            messagebox.showerror("Invalid Input", "Budget must be a number")

    def show_chart(self):
        income = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "Income")
        expense = sum(t["amount"] for t in self.data["transactions"] if t["type"] == "Expense")
        labels = ['Income', 'Expense']
        sizes = [income, expense]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        chart_win = tk.Toplevel(self.root)
        chart_win.title("Finance Chart")
        chart_canvas = FigureCanvasTkAgg(fig, master=chart_win)
        chart_canvas.draw()
        chart_canvas.get_tk_widget().pack()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.data = json.load(f)

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

# Run App
root = tk.Tk()
app = ExpenseTrackerApp(root)
root.mainloop()
# This code is a simple expense tracker application using Tkinter for the GUI and Matplotlib for charting.
# It allows users to set a monthly budget, add income and expenses, and view a summary of their finances.