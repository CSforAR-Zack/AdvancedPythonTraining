from PIL import Image
from os import chdir, path, getcwd

def main():
    if path.dirname(__file__) == '':
        dirPath = f'{getcwd()}'
    else:
        dirPath = f'{path.dirname(__file__)}'
        chdir(dirPath)

    im = Image.open('lotus.png')
    im.show()

if __name__ == '__main__':
    main()