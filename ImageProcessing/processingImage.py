from PIL import Image
from os import chdir, path

def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    im = Image.open('lotus.png')
    #im = im.rotate(90)
    #im.save('lotus_rotated.png')

    #pngToJpg(im)
    im1 = Image.open('image2.png')
    im2 = Image.open('image1.png')
    im2 = im2.convert('RGBA')
    mergeThee(im2, im1)

def pngToJpg(image):
    '''Convert a .png to a .jpg.'''
    image = image.convert('RGB')
    image.save('lotus.jpg')

def mergeThee(image1, image2):
    ''' Composite the second image onto the first
    if the modes and size are the same.'''

    mergedImage = Image.alpha_composite(image1, image2)
    mergedImage.save('Cool_Image.png')

if __name__ == '__main__':
    main()
