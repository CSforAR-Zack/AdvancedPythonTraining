# wordCountwExplorer.py
# Program that counts the words of a file and/or the n most common words.

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    filename = fileSelector()

    fileContents = getFileContents(filename)

    text = fileContents.lower()

    # Characters to omit. ' is not in list for contractions.
    nonAlphaNumChars = '!@#$%^&*()_+-={}[]|\\;:\",./<>?|'

    # Replace all special chars with spaces
    for char in nonAlphaNumChars:
        text = text.replace(char, ' ')

    words = text.split()
    
    print(countWords(words))
    print(wordFreq(words, 5))      

def fileSelector():
    ''' GUI file selector using Tk.'''

    Tk().withdraw()
    filename = askopenfilename()
    return filename

def getFileContents(filename):
    ''' Get contents of file. '''

    with open(filename, 'r') as f:
        fileContents = f.read()
    
    return fileContents

def countWords(words):
    ''' Return the number of words. '''

    return len(words)

def wordFreq(words, numOfWords):
    ''' Return most frequent words specified amount.'''

    # Get the unique words
    wordSet = set(words)

    # Get the frequency of each word.
    frequencies = {}
    for word in wordSet:
        f = words.count(word)
        frequencies[word] = f
    sortedFreq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    # Get the top numOfWords
    wordList =[]
    if numOfWords <= len(sortedFreq):
        # Store numOfWords of words.
        for word in range(numOfWords):
            wordList.append(sortedFreq[word])
    else:
        # Store all of the words
        for word in range(len(sortedFreq)):
            wordList.append(sortedFreq[word])

    # Return the top frequent words.
    return wordList

if __name__ == '__main__':
    main()