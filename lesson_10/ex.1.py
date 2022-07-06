from PIL import Image, ImageDraw, ImageFont, ImageColor

img = Image.open("corgi.jpg")

width, height = img.width, img.height
print(width,height)

scale = 0.25
#img_small = img.size((int(scale*width), int(scale*height)))
img = img.rotate(45, expand=True)
img.save("corgi_totate.jpg")

imgicon = Image.open("corgi_icon.png")
img.paste(imgicon, (20,30))
img.show()