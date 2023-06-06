import os

def main():
    # Get directory of this script.
    dirPath = os.path.dirname(os.path.realpath(__file__))

    fileDeleter(dirPath, "txt")

def fileDeleter(dirPath, ext):
    for file in os.listdir(dirPath):
        if file.endswith(f".{ext}"):
            os.remove(str(file))

if __name__ == "__main__":
    main()