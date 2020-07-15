# unzipper.py
# Unzips files in directory where script is located.
# unzipFiles can be imported into another program.

from os import chdir, listdir, path, remove, getcwd
from zipfile import ZipFile, is_zipfile

def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    # Unzip all files and remove them in directory
    unzipFiles(dirPath)

def unzipFiles(dirPath):
    '''Unzip all files in target directory.'''

    chdir(dirPath) # Change active directory to target

    # Loop through all files in director unzipping
    # zipped files and removing the old file.
    for item in listdir(dirPath):
        if is_zipfile(item):
            with ZipFile(item) as f:
                f.extractall()
            remove(item)

if __name__ == '__main__':
    main()
