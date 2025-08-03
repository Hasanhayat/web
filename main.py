import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hassan's Modern GUI App")
        self.root.geometry("900x600")
        self.root.configure(bg="#121212")

        title = tk.Label(root, text="🚀 Hassan's Modern Python App", font=("Segoe UI", 24, "bold"), bg="#121212", fg="white")
        title.pack(pady=30)

        self.progress = ttk.Progressbar(root, length=500, mode='determinate')
        self.progress.pack(pady=20)

        self.status = tk.Label(root, text="", font=("Segoe UI", 12), bg="#121212", fg="#00ffcc")
        self.status.pack()

        ttk.Button(root, text="Start Animation", command=self.start).pack(pady=10)

        self.features_frame = tk.Frame(root, bg="#1e1e1e")
        self.features_frame.pack(pady=30, fill="x")
        self.add_features()

    def add_features(self):
        features = [
            "✔ Fully Modern GUI",
            "✔ Animated Progress Bar",
            "✔ Responsive Layout",
            "✔ Dark Theme",
            "✔ Message Alerts",
            "✔ Built with Python"
        ]
        for f in features:
            tk.Label(self.features_frame, text=f, font=("Segoe UI", 13), bg="#1e1e1e", fg="#00ffcc", anchor="w", padx=20).pack(fill="x", pady=4)

    def start(self):
        self.status.config(text="⏳ Please wait, loading...")
        threading.Thread(target=self.animate).start()

    def animate(self):
        for i in range(101):
            time.sleep(0.02)
            self.progress["value"] = i
        self.status.config(text="✅ Done!")
        messagebox.showinfo("Finished", "Animation completed successfully!")

root = tk.Tk()
app = ModernApp(root)
root.mainloop()

