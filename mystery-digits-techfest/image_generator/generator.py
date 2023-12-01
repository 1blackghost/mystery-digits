# Save this as yourmodule.py

from PIL import Image, ImageDraw, ImageFont
import random
import os

def draw_complex_patterns(draw, width, height, num_complex_shapes):
    for _ in range(int(num_complex_shapes * 0.5)):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.arc([x1, y1, x2, y2], random.randint(0, 360), random.randint(0, 360), fill=random_color())

    for _ in range(int(num_complex_shapes)):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.line([(x, y), (x + random.randint(5, 20), y + random.randint(5, 20))], fill=random_color())

    for _ in range(int(num_complex_shapes * 2)):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), fill=random_color())

    for _ in range(int(num_complex_shapes * 0.5)):
        x, y = random.randint(0, width), random.randint(0, height)
        size = random.randint(5, 20)
        draw.rectangle([x, y, x + size, y + size], fill=random_color())

    for _ in range(int(num_complex_shapes * 0.5)):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = x1 + random.randint(5, 20), y1 + random.randint(5, 20)
        x3, y3 = x1 + random.randint(5, 20), y1 - random.randint(5, 20)
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=random_color())

    for _ in range(int(num_complex_shapes)):
        x, y = random.randint(0, width), random.randint(0, height)
        size = random.randint(5, 20)
        draw.ellipse([x, y, x + size, y + size], fill=random_color())

def scatter_numbers_and_shapes(draw, width, height, num_digits, num_complex_shapes):
    # Scatter shapes
    draw_complex_patterns(draw, width, height, num_complex_shapes)

    # Scatter random numbers with a border
    base_font_size = 200
    digits_positions = []

    for i in range(num_digits):
        digit = str(random.randint(0, 9))
        x, y = random.randint(20, width - 42), random.randint(20, height - 42)
        font_size = max(20, base_font_size - i * 10) 
        font = ImageFont.truetype("FreeSans.ttf", int(font_size))
        draw.text((x, y), digit, font=font, fill=random_color())
        digits_positions.append((x, y, font_size, digit))

    return digits_positions

def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def generate_and_get_digits(width, height, num_digits,filename):
    # Calculate the number of complex shapes based on the number of digits
    num_complex_shapes = max(10, num_digits * 2)

    # Create a black background image
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    # Scatter shapes and numbers
    digits_positions = scatter_numbers_and_shapes(draw, width, height, num_digits, num_complex_shapes)

    # Extract digits from positions
    digits = [digit for _, _, _, digit in digits_positions]

    # Save the image
    directory = os.getcwd()+"/static/"

    # Ensure the directory exists, create it if necessary

    # Construct the full path including the directory and filename
    full_path = os.path.join(directory, filename)

    # Save the image to the specified path
    image.save(full_path,dpi=(300,300))

    return digits


