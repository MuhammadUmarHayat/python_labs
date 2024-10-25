import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Paint Application")
        
        # Default settings for color and brush
        self.color = "black"
        self.brush_size = 5

        # Canvas setup
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        # Button to change color
        color_button = tk.Button(root, text="Select Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        # Slider to adjust brush size
        brush_slider = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size")
        brush_slider.set(self.brush_size)
        brush_slider.pack(side=tk.LEFT)
        brush_slider.bind("<Motion>", self.update_brush_size)

        # Clear canvas button
        clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        # Mouse events for painting
        self.canvas.bind("<B1-Motion>", self.paint)

    def choose_color(self):
        color = askcolor(color=self.color)[1]
        if color:
            self.color = color

    def update_brush_size(self, event):
        self.brush_size = event.widget.get()

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

# Main application
root = tk.Tk()
app = PaintApp(root)
root.mainloop()
