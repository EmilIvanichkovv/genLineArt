from curses import start_color
from PIL import Image, ImageDraw
import random

def generate_random_color():
    return(random.randint(0,225),random.randint(0,225),random.randint(0,225))


def color_interpolate(start_color, end_color, factor: float):
    # Find the color that is exactly factor (0.0 - 1.0) between the two colors.
    new_color_rgb = []
    for i in range(3):
        new_color_value = factor * end_color[i] + (1 - factor) * start_color[i]
        new_color_rgb.append(int(new_color_value))

    return tuple(new_color_rgb)

def generate_art():
    print("Hello world")
    image_size_px = 250
    padding_px = 20
    image_bg_color = (255,255,255)
    start_color = generate_random_color()
    end_color = generate_random_color()

    image = Image.new(
        "RGB", 
        size=(image_size_px, image_size_px), 
        color=(255,255,255))
    # Draw some lines

    draw = ImageDraw.Draw(image)
    points = []

    # Generate The points
    for _ in range(15):
        random_point= (
            random.randint(padding_px, image_size_px - padding_px),
            random.randint(padding_px, image_size_px - padding_px))
        points.append(random_point)

    # Center image.
    # Find the bounding box.
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    # Find offsets.
    x_offset = (min_x - padding_px) - (image_size_px - padding_px - max_x)
    y_offset = (min_y - padding_px) - (image_size_px - padding_px - max_y)

    # Move all points by offset.
    for i, point in enumerate(points):
        points[i] = (point[0] - x_offset // 2, point[1] - y_offset // 2)


    # Draw the lines
    thickness = 0
    n_point = len(points) - 1
    for i, point in enumerate(points):
        p1 = point
        if i == n_point:
            p2 = points[0]
        else:
            p2 = points[i-1]
            
        line_xy = (p1,p2)
        color_factor = i /n_point
        line_color = color_interpolate(start_color, end_color, color_factor)
        thickness = random.randint(1,i+1)
        draw.line(line_xy, fill= line_color, width=thickness)
    
    image.save("test.png")

generate_art()