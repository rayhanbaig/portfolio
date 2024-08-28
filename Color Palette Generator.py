from PIL import Image, ImageDraw
import random

def generate_color_palette(user_colors=None, num_colors=5):
    if user_colors:
        # Use user-defined colors
        colors = user_colors
    else:
        # Generate random colors
        colors = ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(num_colors)]
    
    return colors

def display_palette(colors):
    # Create an image with a white background
    width = 800
    height = 200
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    
    # Calculate the width of each color block
    block_width = width // len(colors)
    
    # Draw the color blocks
    for i, color in enumerate(colors):
        draw.rectangle([i * block_width, 0, (i + 1) * block_width, height], fill=color)
    
    # Show the image
    img.show()

# User input section
user_choice = input("Do you want to provide colors? (yes/no): ").strip().lower()

if user_choice == 'yes':
    user_colors = input("Enter your colors in hex format separated by commas (e.g., #FF5733, #33FF57): ")
    user_colors = [color.strip() for color in user_colors.split(',')]
    palette = generate_color_palette(user_colors)
else:
    num_colors = int(input("How many random colors do you want? "))
    palette = generate_color_palette(num_colors=num_colors)

# Display the generated color palette
display_palette(palette)
