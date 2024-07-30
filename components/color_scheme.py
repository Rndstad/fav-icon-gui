class ColorScheme:
    """Handles color schemes for the application."""

    def __init__(self):
        self.default_colors = {
            "green": {"background": "#F0F8F0", "button_bg": "#D0F0C0", "button_fg": "#003300", "canvas_bg": "#F0F8F0",
                      "primary_color": "#006E5B", "color": "white"},
            "yellow": {"background": "#FFFFE0", "button_bg": "#FFFF99", "button_fg": "#FFD700", "canvas_bg": "#FFFFE0",
                       "primary_color": "#f0c952", "color": "black"}
        }
        self.colors = self.default_colors["yellow"]

    def apply_theme(self, theme):
        """Apply the selected theme."""
        self.colors = self.default_colors.get(theme, self.default_colors["yellow"])
        return self.colors
