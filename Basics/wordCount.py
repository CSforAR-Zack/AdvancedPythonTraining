# Word counting program.
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    filename = fileSelector()

    fileContents = getFileContents(filename)
    print(fileContents)  

def fileSelector():
    ''' GUI file selector using Tk.'''

    Tk().withdraw()
    filename = askopenfilename()
    return filename

def getFileContents(filename):
    ''' Get contents of filename. '''

    with open(filename, 'r') as fo:
        fileContents = fo.read()

    return fileContents

if __name__ == '__main__':
    main()