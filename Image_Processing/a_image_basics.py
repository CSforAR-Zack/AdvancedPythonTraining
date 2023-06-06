from PIL import Image, ImageEnhance, ImageFilter

def main():
    image = Image.open("bfly.jpg")
    #image.show()
    #image.save("new.jpg")

    # Image information
    # print(image.size)
    # print(image.filename)
    # print(image.format)
    # print(image.format_description)

    # Basic Image manipulation
    # new_image = image.rotate(45, expand=True, fillcolor=(90, 255, 90))
    # new_image = image.crop((300, 0, 1500, 1000))
    # new_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) # FLIP_TOP_BOTTOM
    # new_image = image.resize((1000, 200))
    # scale_factor = .25
    # new_image_size = (int(image.size[0] * scale_factor), int(image.size[1] * scale_factor))
    # new_image = image.resize(new_image_size)

    # Filters and Enhancements
    # Enchancements -> vibrance, contrast, brightness, and sharpness
    # color_enhancer = ImageEnhance.Color(image)
    # new_image = color_enhancer.enhance(.25)
    # contrast_enhancer = ImageEnhance.Contrast(image)
    # new_image = contrast_enhancer.enhance(2)
    # brightness_enhancer = ImageEnhance.Brightness(image)
    # new_image = brightness_enhancer.enhance(2)
    # sharpness_enhancer = ImageEnhance.Sharpness(image)
    # new_image = sharpness_enhancer.enhance(5)

    # Filters -> blur, contour, emboss, sharpening, find_edges, smooth etc
    # new_image = image.filter(ImageFilter.BLUR)
    # new_image = image.filter(ImageFilter.CONTOUR)
    # new_image = image.filter(ImageFilter.DETAIL)
    # new_image = image.filter(ImageFilter.EDGE_ENHANCE)
    # new_image = image.filter(ImageFilter.FIND_EDGES)
    new_image = image.filter(ImageFilter.EMBOSS)
    # new_image = image.filter(ImageFilter.SHARPEN)
    # new_image = image.filter(ImageFilter.SMOOTH_MORE)

    # Rank Filters
    # new_image = image.filter(ImageFilter.MinFilter(size=5))
    # new_image = image.filter(ImageFilter.MedianFilter(size=5))
    # new_image = image.filter(ImageFilter.MaxFilter(size=5))

    # Multiband Filters
    # new_image = image.filter(ImageFilter.BoxBlur(10))
    # new_image = image.filter(ImageFilter.GaussianBlur(10))
    # new_image = image.filter(ImageFilter.UnsharpMask(10))

    # Combining Filters: blur + emboss
    # new_image = image.filter(ImageFilter.EMBOSS)
    # new_image = new_image.filter(ImageFilter.GaussianBlur(10))

    # new_image.save("new_image.jpg")

if __name__ == "__main__":
    main()