from PIL import Image, ImageDraw
import random

def generate_art():
    print("Hello world")
    image_size_px = 250
    padding_px = 20
    image_bg_color = (255,255,255)
    image = Image.new(
        "RGB", 
        size=(image_size_px, image_size_px), 
        color=(255,255,255))
    # Draw some lines

    draw = ImageDraw.Draw(image)
    thickness = 0
    points = []

    # Generate The points
    for _ in range(15):
        random_point= (
            random.randint(padding_px, image_size_px - padding_px),
            random.randint(padding_px, image_size_px - padding_px))
        points.append(random_point)

    for i, point in enumerate(points):
        p1 = point
        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i-1]
            
        line_xy = (p1,p2)
        line_color = (0, 0, 0)
        thickness = random.randint(1,i+1)
        draw.line(line_xy, fill= line_color, width=thickness)
    
    image.save("test.png")

generate_art()