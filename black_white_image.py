from PIL import Image

img = Image.open("images/milkbirdy.jpg")


img2 = img.convert("L")

img2 .save("images/black_white_image.jpg")