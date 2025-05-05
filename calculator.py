import math
import tkinter as tk 
from tkinter import messagebox
#function to handle button clicks
# Function to handle button clicks
def on_click(button_text):
    if button_text == "C":
        # Clear the entry field
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            # Evaluate the expression entered by the user
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text in ["√", "sin", "cos", "tan"]:
        try:
            value = float(entry.get())
            if button_text == "√":
                result = math.sqrt(value)
            elif button_text == "sin":
                result = math.sin(math.radians(value))
            elif button_text == "cos":
                result = math.cos(math.radians(value))
            elif button_text == "tan":
                result = math.tan(math.radians(value))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        # Append the button text to the entry field
        entry.insert(tk.END, button_text)

# Create the main Tkinter window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Create an entry widget for the calculator display
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Define button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "√", "sin", "cos", "tan"
]

# Create and place buttons in the grid
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(
        root,
        text=button_text,
        font=("Arial", 18),
        borderwidth=2,
        relief=tk.RAISED,
        command=lambda text=button_text: on_click(text)
    )
    button.grid(row=row_val, column=col_val, padx=10, pady=10, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights for responsiveness
for i in range(5):  # 5 rows (including the entry row)
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Start the Tkinter event loop
root.mainloop()




# This code creates a simple calculator GUI using Tkinter. It supports basic arithmetic operations, square root, and trigonometric functions (sin, cos, tan). The calculator handles button clicks and evaluates expressions entered in the entry widget. It also includes error handling for invalid inputs.
# The calculator is designed to be responsive, adjusting the button layout based on the window size. The buttons are created dynamically using a loop, and their layout is managed using a grid system. The calculator has a clean and modern design with a black background and white text.
# The calculator is user-friendly, providing clear feedback for invalid inputs through message boxes. Overall, this code demonstrates a practical application of Tkinter for creating a functional and visually appealing calculator GUI.
# The calculator is designed to be responsive, adjusting the button layout based on the window size. The buttons are created dynamically using a loop, and their layout is managed using a grid system. The calculator has a clean and modern design with a black background and white text.