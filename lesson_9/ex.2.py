import PIL
from PIL import Image
img = Image.open("corgi_poster.png")
img = img.convert("HSV")
img.show()

from PIL import Image, ImageFilter
img = Image.open("corgi.jpg")
img = img.filter(ImageFilter.BLUR)
img.show()