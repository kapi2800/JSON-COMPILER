import tkinter as tk
from tkinter import filedialog
from main import parse_json

def select_file():
    path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if path:
        try:
            with open(path, "r") as file:
                content = file.read()
                result = parse_json(content)
                output_label.config(text=" Valid JSON\n" + str(result), fg="green")
        except Exception as e:
            output_label.config(text=" Invalid JSON\n" + str(e), fg="red")

window = tk.Tk()
window.title("Simple JSON Validator")
window.geometry("500x300")

label = tk.Label(window, text="JSON Validator", font=("Arial", 16))
label.pack(pady=10)

button = tk.Button(window, text="Choose JSON File", command=select_file)
button.pack(pady=10)

output_label = tk.Label(window, text="", wraplength=450, justify="left", font=("Arial", 10))
output_label.pack(pady=20)
window.mainloop()
