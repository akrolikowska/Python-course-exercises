from PIL import Image

img = Image.open("corgi_poster.png")
width, height = img.width, img.height
threshold = 128

for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        grey = int((r + g + b) / 3)
        val = ImageColor.getrgb("white") if grey >= threshold else ImageColor.getrgb("black")
        img.putpixel((x, y), val)
img.show()
