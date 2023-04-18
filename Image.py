from PIL import Image

image = Image.open("rainbow.jpg")
pixels = image.load()

color_count = {
    'red': 0,
    'orange': 0,
    'yellow': 0,
    'green': 0,
    'blue': 0,
    'indigo': 0,
    'violet': 0
}

for x in range(image.width):
    for y in range(image.height):
        r, g, b = pixels[x, y]
        
        if r > 200 and g < 100 and b < 100
