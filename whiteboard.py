import tkinter as tk
from tkinter.colorchooser import askcolor

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard")
        
        # Initialize drawing variables
        self.pen_color = "black"
        self.eraser_on = False
        self.last_x, self.last_y = None, None

        # Create canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # buttons
        self.create_buttons()

        # Bind mouse events to canvas
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        color_button = tk.Button(button_frame, text="Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5, pady=5)

        eraser_button = tk.Button(button_frame, text="Eraser", command=self.use_eraser)
        eraser_button.pack(side=tk.LEFT, padx=5, pady=5)

        pen_button = tk.Button(button_frame, text="Pen", command=self.use_pen)
        pen_button.pack(side=tk.LEFT, padx=5, pady=5)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = askcolor(color=self.pen_color)[1]
        if color:
            self.pen_color = color
            self.eraser_on = False

    def use_eraser(self):
        self.pen_color = "white"
        self.eraser_on = True

    def use_pen(self):
        self.eraser_on = False
        self.pen_color = "black"

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                fill=self.pen_color, width=3, capstyle=tk.ROUND, smooth=True
            )
        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    root.mainloop()