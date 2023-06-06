from PIL import Image, ImageOps

def main():
    image = Image.open("bfly.jpg")

    # Color Changes
    # new_image = ImageOps.autocontrast(image, 20)
    # new_image = ImageOps.invert(image)
    # new_image = ImageOps.solarize(image, 100)
    # new_image = ImageOps.posterize(image, 1)
    # new_image = ImageOps.grayscale(image)
    # new_image = ImageOps.equalize(image)
    # new_image = ImageOps.colorize(image.convert("L"), black="white", white=(0,100,100))

    # Dim Changes
    # new_image = ImageOps.mirror(image)
    # new_image = ImageOps.flip(image)
    # new_image = ImageOps.scale(image, .1)
    # new_image = ImageOps.contain(image,(500, 200)) # not stretching (selects smallest of two numbers)

    # Adding and Removing
    new_image = ImageOps.expand(image, 100, (0,255,255))
    new_image = ImageOps.fit(image, (500, 300)) # cropping image from senter
    new_image = ImageOps.crop(image, 500) # cropping image from senter

    new_image.save("new_image.jpg")

if __name__ == "__main__":
    main()