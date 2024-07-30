import tkinter as tk
from tkinter import filedialog, colorchooser, simpledialog


class ControlPanel:
    """Handles the control panel UI and interactions."""

    def __init__(self, master, on_update, default_font_dir):
        self.master = master
        self.default_font_dir = default_font_dir
        self.on_update = on_update
        self.colors = {
            "background": "#FFFFFF",
            "button_bg": "#DDDDDD",
            "button_fg": "#000000",
            "canvas_bg": "#FFFFFF",
        }
        self._create_widgets()

    def _create_widgets(self):
        """Create and place widgets in the control panel."""
        self.frame = tk.Frame(self.master, bg=self.colors["background"], width=250)
        self.frame.grid(row=0, column=0, sticky="ns")

        self.theme_var = tk.StringVar(value="yellow")
        self.theme_menu = tk.OptionMenu(self.frame, self.theme_var, "green", "yellow", command=self._change_theme)
        self.theme_menu.pack(pady=5, padx=10)

        self.text_color_button = tk.Button(self.frame, text="Select Text Color", command=self._select_text_color,
                                           bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        self.text_color_button.pack(pady=5, padx=10)

        self.text_button = tk.Button(self.frame, text="Set Text", command=self._set_text,
                                     bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        self.text_button.pack(pady=5, padx=10)

        self.font_button = tk.Button(self.frame, text="Upload Font", command=self._upload_font,
                                     bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        self.font_button.pack(pady=5, padx=10)

        self.refresh_button = tk.Button(self.frame, text="Refresh/Generate", command=self.on_update,
                                        bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        self.refresh_button.pack(pady=5, padx=10)

        self.save_button = tk.Button(self.frame, text="Save Logo", command=self._save_logo,
                                     bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        self.save_button.pack(pady=5, padx=10)

        self.text_height_label = tk.Label(self.frame, text="Text Height Scale:")
        self.text_height_label.pack(pady=5, padx=10)

        self.text_height_spinbox = tk.Spinbox(self.frame, from_=0.1, to=10.0, increment=0.1, format="%.1f",
                                              command=self._update_text_height_scale)
        self.text_height_spinbox.pack(pady=5, padx=10)

        self.font_size_slider = tk.Scale(self.frame, from_=20, to=200, orient=tk.HORIZONTAL, label="Text Size (px)",
                                         command=self._update_font_size)
        self.font_size_slider.pack(pady=5, padx=10)

    def _change_theme(self, new_theme):
        """Change the theme and update the application."""
        self.on_update(theme=new_theme)

    def _select_text_color(self):
        """Select a text color and update the application."""
        color = colorchooser.askcolor(title="Select Text Color")[1]
        if color:
            self.on_update(text_color=color)

    def _set_text(self):
        """Set the logo text and update the application."""
        new_text = simpledialog.askstring("Set Text", "Enter text for the logo:")
        if new_text:
            self.on_update(text=new_text)

    def _upload_font(self):
        """Upload a font file and update the application."""
        font_path = filedialog.askopenfilename(initialdir=self.default_font_dir,
                                               filetypes=[("Font files", "*.ttf;*.otf")])
        print(f"Selected font path: {font_path}")  # Debugging statement
        if font_path:
            self.on_update(font_path=font_path)

    def _update_text_height_scale(self, value=None):
        """Update text height scale from the spinbox."""
        try:
            scale = float(self.text_height_spinbox.get())
            self.on_update(text_height_scale=scale)
        except ValueError:
            self.on_update(text_height_scale=1.0)

    def _update_font_size(self, value):
        """Update font size from the slider."""
        self.on_update(font_size=int(value))

    def _save_logo(self):
        """Open a file dialog to save the logo."""
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.on_update(save_path=file_path)

    def update_colors(self, colors):
        """Update the colors of the control panel components."""
        self.colors.update(colors)
        self.frame.config(bg=self.colors["background"])
        for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.config(bg=self.colors.get("button_bg", "#DDDDDD"), fg=self.colors.get("button_fg", "#000000"))
