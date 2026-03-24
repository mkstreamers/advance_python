#18. Create a Tkinter form:
#- Name input
#- Submit button
#- Show entered name

import tkinter as tk

def submit():
    name = entry.get().strip()
    if name:
        result_label.config(text=f"Hello, {name}!", fg="green")
    else:
        result_label.config(text="Please enter a name.", fg="red")

root = tk.Tk()
root.title("Name Form")
root.geometry("300x180")
root.resizable(False, False)

tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack(pady=(20, 5))
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack()

tk.Button(root, text="Submit", font=("Arial", 11), command=submit).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
