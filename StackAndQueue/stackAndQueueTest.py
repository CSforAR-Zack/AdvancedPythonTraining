from PIL import Image, ImageFilter, ImageOps
#from os import chdir, path

def main():
    #dirPath = path.dirname(path.realpath(__file__))
    #chdir(dirPath)
    im = Image.open('lotus.png')
        
    #pngToJpg(im, 'flower')

    imageFun(im)


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