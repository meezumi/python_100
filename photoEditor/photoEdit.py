from PIL import Image, ImageEnhance, ImageFilter
import os

# documentation: "https://pillow.readthedocs.io/en/stable/"

path = "./images"
pathOut = "/editedImages"

for filename in os.listdir(path):
    # choose the file to be edited from the folder
    img = Image.open(f"{path}/{filename}")
    # apply edits such as sharpen to the photo
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 2.0
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # generate the edited version of the photo
    clean_name = os.path.splitext(filename)[0]
    # save the edited photo in the pathOut folder
    edit.save(f".{pathOut}/{clean_name}_edited.jpg")
