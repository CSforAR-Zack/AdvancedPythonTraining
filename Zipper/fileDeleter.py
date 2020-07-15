
from os import path, listdir, remove, chdir, getcwd


def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    fileDeleter(dirPath)

def fileDeleter(dirPath):
    ''' Zips all .txt files in target directory. '''

    # Loop over all files in target directory.
    for file in listdir(dirPath):
        # Check if file ends in .txt.
        if file.endswith('.txt'):
            remove(f'{file}')

if __name__ == '__main__':
    main()