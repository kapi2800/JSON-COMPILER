import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from main import parse_json

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path, "r") as f:
                json_str = f.read()
            result = parse_json(json_str)
            output_area.config(state='normal')
            output_area.delete(1.0, tk.END)
            output_area.insert(tk.END, f"✅ Valid JSON:\n{result}")
            output_area.config(state='disabled')
        except Exception as e:
            output_area.config(state='normal')
            output_area.delete(1.0, tk.END)
            output_area.insert(tk.END, f"❌ Invalid JSON:\n{str(e)}")
            output_area.config(state='disabled')

# Set up the main window
window = tk.Tk()
window.title("JSON Parser & Validator")
window.geometry("600x400")

# Header label
title_label = tk.Label(window, text="JSON Parser & Validator", font=("Arial", 16))
title_label.pack(pady=10)

# Button to browse file
browse_button = tk.Button(window, text="Select JSON File", command=browse_file, width=30, bg="lightblue")
browse_button.pack(pady=10)

# Output area
output_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15, state='disabled', font=("Consolas", 10))
output_area.pack(pady=10)

# Start GUI loop
window.mainloop()
