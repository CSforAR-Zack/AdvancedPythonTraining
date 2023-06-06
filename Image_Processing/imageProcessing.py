from PIL import Image, ImageFilter, ImageOps

def main():
    im = Image.open('lotus.png')
        
    #pngToJpg(im, 'flower')

    #imageFun(im)

    im1 = Image.open('earth.png')
    im1 = im1.convert('RGBA')
    im2 = Image.open('color_grade.png')

    mergeThee(im1, im2)

def mergeThee(image1, image2):
    """ Composite image2 onto image1.
    image1 and image 2 must be same size.
    """

    mergedImage = Image.alpha_composite(image1, image2)
    mergedImage.save('mergedImage.png')

def imageFun(image):
    """ A function of tons of fun. """
    funImage = image.filter(ImageFilter.SHARPEN)
    funImage = funImage.rotate(180)
    #funImage = ImageOps.mirror(funImage)

    funImage.save('fun.png')

def pngToJpg(image, fileName):
    image = image.convert('RGB')
    image.save(f'{fileName}.jpg')

main()
