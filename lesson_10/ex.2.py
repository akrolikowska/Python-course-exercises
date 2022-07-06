from PIL import Image, ImageDraw, ImageFont, ImageColor

imgdraw = ImageDraw.Draw(img)
imgdraw.rectangle((10,10,300,500), fill="red")
imgdraw.line((500,100,600,1000), width=5, fill="green")
imgdraw.ellipse((400,500,600,800), fill="purple")
imgdraw.arc((200,300,300, 500), start=30, end=180, width=10, fill="yellow")

font = ImageFont.truetype("arial", 100)
imgdraw.text((10,50), "HeloWorld", font = font, fill=(199,220,100))
img.show()