from PIL import Image, ImageDraw
import random

def generate_art():
    print("Hello world")
    image_size_px = 128
    image_bg_color = (255,255,255)
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
            random.randint(0, image_size_px),
            random.randint(0, image_size_px))
        points.append(random_point)

    for i, point in enumerate(points):
        p1 = point
        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i-1]
            
        line_xy = (p1,p2)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill= line_color)
    
    image.save("test.png")

generate_art()