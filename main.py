import os
import tkinter as tk

from components.color_scheme import ColorScheme
from components.control_panel import ControlPanel
from components.logo_creator import LogoCreator
from components.logo_preview import LogoPreview


class LogoGeneratorApp:
    """Main application class that integrates all components."""

    def __init__(self, root):
        self.root = root
        self.root.title("Logo Generator")

        self.default_font_dir = 'assets/fonts'  # Set your default directory here
        self.default_font = os.path.join(self.default_font_dir, 'SuisseIntl-Regular.otf')
        self.color_scheme = ColorScheme()
        self.logo_creator = LogoCreator(font_path=self.default_font)

        self.control_panel = ControlPanel(self.root, self._update_settings, self.default_font_dir)
        self.logo_preview = LogoPreview(self.root)

        self.settings = {
            "text": "Lb",
            "font_size": 100,
            "text_height_scale": 1.0,
            "primary_color": "#f0c952",
            "text_color": "#000000",
            "font_path": self.default_font,
            "theme": "yellow"  # Add theme to settings
        }

        # Apply the initial color scheme based on the default theme
        self._apply_color_scheme(self.settings["theme"])
        self._refresh_preview()

    def _update_settings(self, **kwargs):
        """Update settings based on user input and refresh the preview."""
        if 'save_path' in kwargs:
            save_path = kwargs['save_path']
            image = self.logo_creator.create_logo(
                self.settings["text"],
                self.settings["font_size"],
                self.settings["text_height_scale"],
                self.settings["primary_color"],
                self.settings["text_color"],
                self.logo_preview.size
            )
            self.logo_creator.save_logo(image, save_path)
        elif 'theme' in kwargs:
            self.settings['theme'] = kwargs['theme']
            self._apply_color_scheme(self.settings['theme'])
        else:
            self.settings.update(kwargs)
            self._refresh_preview()

    def _apply_color_scheme(self, theme):
        """Apply the selected color theme."""
        colors = self.color_scheme.apply_theme(theme)
        self.root.config(bg=colors["background"])
        self.control_panel.frame.config(bg=colors["background"])
        self.logo_preview.frame.config(bg=colors["background"])  # Fix for frame background
        self.logo_preview.canvas.config(bg=colors["canvas_bg"])
        # Set primary_color and text_color based on theme
        self.settings["primary_color"] = colors["primary_color"]
        self.settings["text_color"] = colors["color"]  # Or any other color for text
        self._refresh_preview()

    def _refresh_preview(self):
        """Refresh the logo preview."""
        image = self.logo_creator.create_logo(
            self.settings["text"],
            self.settings["font_size"],
            self.settings["text_height_scale"],
            self.settings["primary_color"],
            self.settings["text_color"],
            self.logo_preview.size
        )
        info_text = (f"Font Size: {self.settings['font_size']}\n"
                     f"Text Height Scale: {self.settings['text_height_scale']:.2f}\n"
                     f"Primary Color: {self.settings['primary_color']}\n"
                     f"Text Color: {self.settings['text_color']}")
        self.logo_preview.update(image, info_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = LogoGeneratorApp(root)
    root.mainloop()
