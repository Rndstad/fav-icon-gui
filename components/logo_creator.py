from PIL import Image, ImageDraw, ImageFont


class LogoCreator:
    """Creates and manages the logo image."""

    def __init__(self, font_path='SuisseIntl-Regular.otf'):
        self.font_path = font_path

    def create_logo(self, text, font_size, text_height_scale, primary_color, text_color, size):
        """Generate a logo image with the given settings."""
        image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        radius = size // 6
        self._draw_rounded_rectangle(draw, [0, 0, size, size], radius, primary_color)

        font = ImageFont.truetype(self.font_path, int(font_size)) if self.font_path else ImageFont.load_default()
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        scaled_text_height = text_height * text_height_scale
        scaled_text_width = text_width

        text_x = (size - scaled_text_width) / 2
        text_y = (size - scaled_text_height) / 2

        draw.text((text_x, text_y), text, font=font, fill=text_color)

        return image

    def save_logo(self, image, file_path):
        """Save the generated logo image to a file."""
        image.save(file_path)

    def _draw_rounded_rectangle(self, draw, bbox, radius, fill):
        """Draw a rounded rectangle on the given draw object."""
        left, top, right, bottom = bbox
        radius = min(radius, (right - left) / 2, (bottom - top) / 2)

        draw.rectangle([left + radius, top, right - radius, bottom], fill=fill)
        draw.rectangle([left, top + radius, right, bottom - radius], fill=fill)
        draw.ellipse([left, top, left + 2 * radius, top + 2 * radius], fill=fill)
        draw.ellipse([right - 2 * radius, top, right, top + 2 * radius], fill=fill)
        draw.ellipse([left, bottom - 2 * radius, left + 2 * radius, bottom], fill=fill)
        draw.ellipse([right - 2 * radius, bottom - 2 * radius, right, bottom], fill=fill)
