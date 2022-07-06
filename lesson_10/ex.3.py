from PIL import ImageFilter
img = Image.open("corgi.jpg")
img = img.filter(ImageFilter.MedianFilter(size=7))
img.show()