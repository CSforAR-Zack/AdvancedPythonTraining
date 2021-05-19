from PIL import Image, ImageEnhance, ImageFilter
from os import chdir, path

def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)


    im = Image.open('lotus.png')

    # Convert .png to .jpg
    #pngToJpg(im) # Lossy compression occurs.

    # convert .png RGBA to .png RGB
    #pngRgbaToRgb(im) # Lossless compression occurs.

    # Some custom image processing
    #imageFun(im)

    # Alpha composite example
    im1 = Image.open('image1.png')
    im1 = im1.convert('RGBA')
    im2 = Image.open('image2.png')
    mergeThee(im1, im2)

def pngToJpg(image):
    ''' Convert a .png to a .jpg. '''

    image = image.convert('RGB')
    image.save('lotus.jpg')

def pngRgbaToRgb(image):
    ''' Convert a .png from RGBA to RGB. '''

    image = image.convert('RGB')    
    image.save('lotus_1.png')

def imageFun(image):
    ''' Function of fun.'''

    # Sharpent the image
    sImage = image.filter(ImageFilter.SHARPEN)
    
    #Rotate the image 180 degress
    rImage = sImage.rotate(180)

    # Increase contrast of image and save it.
    enhImage = ImageEnhance.Contrast(rImage)
    enhImage.enhance(1.8).save('lotus_fun.png')

def mergeThee(image1, image2):
    ''' Composite the second image onto the first if mode and size are the same.'''

    mergedImage = Image.alpha_composite(image1, image2)
    mergedImage.show() # Show the image instead of saving it.

if __name__ == '__main__':
    main()
