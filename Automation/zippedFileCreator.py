import os

from zipfile import ZipFile
from time import sleep

def main():
    # Get directory of this script.
    #dirPath = path.dirname(path.realpath(__file__))
    dirPath = os.getcwd()
    print(dirPath)
    numFilesToCreate = 10

    createFiles(numFilesToCreate)
    sleep(2)
    zipFiles(dirPath)

def createFiles(numFiles):
    """ Creates specified number of .txt files. """

    for file in range(numFiles):
        filename = f'file_{file}.txt'
        with open(filename, "w") as fObj:
            fObj.write(f'This is the file named {filename}!')

def zipFiles(dirPath):
    for file in os.listdir(dirPath):
        if file.endswith(".txt"):
            filename = f"{file[:-4]}.zip"
            with ZipFile(filename, "w") as zip:
                zip.write(f"{file}")

            os.remove(f"{file}")

if __name__ == "__main__":
    main()