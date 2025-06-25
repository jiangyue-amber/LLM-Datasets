# Software Name: Photo_Color_Palette_Generator
# Category: Photo
# Description: A software application that generates color palettes based on the colors found in a photo. Users can select an image, and the software will analyze the colors present, extracting the dominant hues and generating a complementary color palette. The color palettes can be used for various purposes such as designing websites, creating artwork, or selecting color schemes for projects.

```python
from PIL import Image
from collections import Counter
import colorgram

def generate_color_palette(image_path, num_colors=5):
    """
    Generates a color palette from an image.

    Args:
        image_path: Path to the image file.
        num_colors: Number of colors to extract for the palette.

    Returns:
        A list of RGB tuples representing the color palette.
        Returns None if the image cannot be opened.
    """
    try:
        # Extract colors using colorgram
        colors = colorgram.extract(image_path, num_colors)

        # Convert Color objects to RGB tuples
        rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

        return rgb_colors
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


if __name__ == '__main__':
    # Example usage
    image_file = 'example.jpg'  # Replace with your image file
    palette = generate_color_palette(image_file, num_colors=5)

    if palette:
        print("Color Palette:")
        for color in palette:
            print(f"RGB: {color}")
```