import os

from zipfile import ZipFile, is_zipfile

def main():
    # Get directory of this script.
    dirPath = os.path.dirname(os.path.realpath(__file__))

    unzipFiles(dirPath)

def unzipFiles(dirPath):
    for item in os.listdir(dirPath):
        if is_zipfile(item):
            with ZipFile(item) as f:
                f.extractall()
            os.remove(item)

if __name__ == "__main__":
    main()