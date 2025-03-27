
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img =Image.open('images/milkbirdy.jpg')

img2 =ImageDraw.Draw(img)

img2 =text()

myFont = ImageFont.truetype("arial.ttf", size=20)

img2.show()


img2.save('images/milkbirdy.jpg')


#cloudinary







