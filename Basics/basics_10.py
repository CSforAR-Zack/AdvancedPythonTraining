# Opening Files and reading them.

from os import chdir, path

def main():
    # Get the directory of this script.
    dirpath = path.dirname(path.realpath(__file__))
    chdir(dirpath)

    # Working on files
    with open('sample.txt', 'r') as fileContents:
        #text = fileContents.read() # Reads all content in file.
        #text = fileContents.readline() # Reads the current line in the file.
        text = fileContents.readlines() # Returns a list of strings representing each line.

    print(text)

if __name__ == '__main__':
    main()