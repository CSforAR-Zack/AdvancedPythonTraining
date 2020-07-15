# Word counting program.
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    filename = fileSelector()

    fileContents = getFileContents(filename)
    
    text = fileContents.lower()

    omitChars = '`!@#$%^&*()_+~-=[]{};"\\:,./<>?'

    for char in omitChars:
        text = text.replace(char, ' ')

    words = text.split()
    numWords = len(words)
    print(numWords)

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