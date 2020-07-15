# Creating and Writing Files

from os import chdir, path

def main():
    # Get the directory of this script.
    dirpath = path.dirname(path.realpath(__file__))
    chdir(dirpath)

    # Working on files
#    with open('writing_file.txt', 'w') as fileContents:
#        text = 'Still the coolest file ever!\n'
#        fileContents.write(text)
#        fileContents.write(text)

    with open('writing_file.txt', 'a') as fileContents:
        for line in range(10):
            fileContents.write(f'This is line {line + 1}!\n')

if __name__ == '__main__':
    main()