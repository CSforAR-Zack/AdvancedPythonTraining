# zippedFileCreator.py
# This program creates zipped files in directory
# that script is located in out of .txt files.

from os import path, listdir, remove, chdir, getcwd
from zipfile import ZipFile


def main():
    # Get the directory of this script.
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    # How many zipped files to create
    numFiles = 10

    # Create files and then zip them.
    createFiles(numFiles)
    zipFiles(dirPath)

        
def createFiles(numFiles):
    ''' Creates specified number of .txt files.'''

    for file in range(numFiles):
        filename = f'file_{file}.txt'
        with open(filename, 'w') as f:
            f.write(f'This is the file at {filename}!')
    
def zipFiles(dirPath):
    ''' Zips all .txt files in target directory. '''

    # Loop over all files in target directory.
    for file in listdir(dirPath):
        # Check if file ends in .txt.
        if file.endswith('.txt'):
            # Determine name for zipped file.
            filename = f'{file[:-4]}.zip'
            # Zip the file
            with ZipFile(filename, 'w') as zip:
                zip.write(f'{file}')

            # Remove the old file.
            remove(f'{file}')

if __name__ == '__main__':
    main()