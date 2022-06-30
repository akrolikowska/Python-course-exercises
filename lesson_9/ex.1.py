import PIL

from PIL import Image, ImageDraw,ImageFont

img = Image.open("corgi.jpg")
imgdraw = ImageDraw.Draw(img)
imgdraw.rectangle((10,10,300,500), fill="red")
imgdraw.line((500,100,600,1000), width=5, fill="green")
imgdraw.ellipse((400,500,600,800), fill="purple")
imgdraw.arc((200,300,500,600), start=30, end=180, width=10, fill="blue")
font = ImageFont.truetype("arial", 100)
imgdraw.text((10,50), "HelloWorld", font=font, fill="white")
img.show()