from PIL import Image, ImageChops

def main():
    bfly = Image.open("bfly.jpg")
    python = Image.open("python.png")
    waterfall = Image.open("waterfall.jpg")
    lotus = Image.open("lotus.png")
    earth = Image.open("earth.png")
    grade = Image.open("color_grade.png")
    mask = Image.open("mask.png")

    mask = mask.resize(bfly.size)

    # Merging Images
    # new_image = Image.blend(bfly, waterfall, 0.5)
    # new_image = Image.composite(bfly, waterfall, Image.new("L", bfly.size, 122))
    # new_image = Image.composite(bfly, waterfall, mask)

    # new_image.save("new_image.jpg")

    # pasting
    # bfly.paste(python, (0,0), mask=python)
    # bfly.save("new_image.jpg")

    # Channel stuff
    # new_image = ImageChops.overlay(bfly, waterfall)
    # new_image = ImageChops.soft_light(bfly, waterfall)

    # More Complex
    # new_image = ImageChops.logical_and(bfly.convert("1"), waterfall.convert("1"))
    # new_image = ImageChops.logical_or(bfly.convert("1"), waterfall.convert("1"))
    # new_image = ImageChops.logical_xor(bfly.convert("1"), waterfall.convert("1"))

    # Masking
    earth = earth.convert("RGBA")
    new_image = Image.alpha_composite(earth, grade)

    new_image.save("new_image.png")

    


if __name__ == "__main__":
    main()