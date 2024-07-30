import tkinter as tk
from PIL import ImageTk


class LogoPreview:
    """Handles the logo preview and updates."""

    def __init__(self, master, size=250):
        self.master = master
        self.size = size

        # Define default colors
        self.colors = {
            "background": "#FFFFFF",
            "canvas_bg": "#FFFFFF"
        }

        # Create a frame to hold the canvas and info label
        self.frame = tk.Frame(master, bg=self.colors["background"])
        self.frame.grid(row=0, column=1, sticky="nsew")

        # Create and configure the canvas
        self.canvas = tk.Canvas(self.frame, width=size, height=size, bg=self.colors["canvas_bg"])
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Create and configure the info label
        self.info_label = tk.Label(self.frame, text="", bg=self.colors["background"])
        self.info_label.grid(row=1, column=0, padx=10, pady=5)

        # Ensure the frame expands with the parent window
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def update(self, image, info_text):
        """Update the preview canvas and info label."""
        self.canvas.delete("all")
        self.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.info_label.config(text=info_text)

    def update_colors(self, colors):
        """Update the colors of the preview components."""
        self.colors.update(colors)
        self.frame.config(bg=self.colors.get("background", "#FFFFFF"))
        self.canvas.config(bg=self.colors.get("canvas_bg", "#FFFFFF"))
        self.info_label.config(bg=self.colors.get("background", "#FFFFFF"))
