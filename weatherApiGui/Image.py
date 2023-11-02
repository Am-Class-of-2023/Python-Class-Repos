from PIL import Image
with Image.open("\\weatherApiGui\\images.png") as im:
    im.rotate(45).show()