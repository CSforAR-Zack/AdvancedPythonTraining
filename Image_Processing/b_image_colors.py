from PIL import Image, ImageFilter
from numpy import array

def main():
    # image = Image.open("simple.png")
    image = Image.open("bfly.jpg")

    # Get a pixel rgb values
    # print(image.getpixel((0,0)))
    # print(image.getcolors())

    # Picture Information
    # print(image.mode)

    # Numpy
    # print(array(image).shape)
    # print(array(image))
    # print(array(image.getchannel("R")))

    # Get Channels
    # new_image = image.getchannel("R")

    #Color Conversions
    # 1-bit Greyscale
    # new_image = image.convert("1")
    # 8-bit Greyscale
    # new_image = image.convert("L")
    # new_image.save("new_image.jpg")

    # Palette: 256 colors
    # new_image = image.convert("P")
    # new_image = image.convert("P", palette=Image.Palette.ADAPTIVE, colors=16) # flatten to 16 colors
    # new_image.save("new_image.bmp")

    # Change Pixels
    # image.putpixel((100,200), (255,255,255))
    # image.save("new_image.jpg")

    # for p in range(image.size[0]):
    #     image.putpixel((p, 200), (0,255,255))
    # image.save("new_image.jpg")

    # for y in range(200):
    #     for x in range(image.size[0]):
    #         image.putpixel((x, y), (0,255,255))
    # image.save("new_image.jpg")

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            cp = image.getpixel((x,y))
            new_pixel = (cp[0], cp[1]//2, cp[2])
            image.putpixel((x, y), new_pixel)
    image.show()
    # image.save("new_image.jpg")

if __name__ == "__main__":
    main()