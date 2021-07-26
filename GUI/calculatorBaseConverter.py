# Peforms the following tasks:
# - Arithmetic between two numbers.
# - Conversion on single numbers

from tkinter import Tk, Entry, Label, Button
from tkinter.font import Font

def main():
    wn = Tk()
    wn.title('Base Calculator')

    fontStyle = Font(family='Courier', size=20)

    entryExp = Entry(master=wn, width=30, font=fontStyle)
    labelEq = Label(master=wn, text=' = ', font=fontStyle)
    labelResult = Label(master=wn, text='0', font=fontStyle)    

    entryExp.grid(row=0, column=0)
    labelEq.grid(row=0, column=1)
    labelResult.grid(row=0, column=2)

    buttonCalc = Button(master=wn, text='Calculate', font=fontStyle, command=lambda : calculate(entryExp, labelResult))

    buttonCalc.grid(row=1)

    wn.mainloop()


def calculate(expression, labelResult):
    """ Evaluate the expression in the entry widget.
    Update the label with the result on row 0.
    """

    e = expression.get()
    expressionParts = splitUp(e)
    result = 0

    if len(expressionParts) > 0:
        newExpression = rebuildExpression(expressionParts)
        result = eval(newExpression)
    else:
        result = converter(e)

    labelResult['text'] = result


def splitUp(expression):
    """ Break the expression into its parts and return the list:
    [Left Number, Right Number, Operator]
    """

    parts = []

    if '*' in expression:
        parts = expression.split('*')
        parts.append('*')
    elif '/' in expression:
        parts = expression.split('/')
        parts.append('/')
    elif '+' in expression:
        parts = expression.split('+')
        parts.append('+')
    elif '-' in expression:
        parts = expression.split('-')
        parts.append('-')        

    return parts


def rebuildExpression(parts):
    """ Converts all numbers to decimal and
    return the expression with decimal numbers.
    """

    firstNumber = parts[0]
    secondNumber = parts[1]
    operator = parts[2]
   
    if '0b' in firstNumber:
        firstNumber = int(firstNumber[2:], 2)
    elif '0o' in firstNumber:
        firstNumber = int(firstNumber[2:], 8)
    elif '0d' in firstNumber:
        firstNumber = firstNumber[2:]
    elif '0x' in firstNumber:
        firstNumber = int(firstNumber[2:], 16)

    if '0b' in secondNumber:
        secondNumber = int(secondNumber[2:], 2)
    elif '0o' in secondNumber:
        secondNumber = int(secondNumber[2:], 8)
    elif '0d' in secondNumber:
        secondNumber = secondNumber[2:]
    elif '0x' in secondNumber:
        secondNumber = int(secondNumber[2:], 16)

    return f'{firstNumber}{operator}{secondNumber}'

    # tempList = []
    # for part in parts:
    #     if '0b' in part:
    #         tempList.append(int(part[2:], 2))
    #     elif '0o' in part:
    #         tempList.append(int(part[2:], 8))
    #     elif '0d' in part:
    #         tempList.append(part[2:])
    #     elif '0x' in part:
    #         tempList.append(int(part[2:], 16))
    #     else:
    #         tempList.append(part)
    
    # return f'{tempList[0]}{tempList[2]}{tempList[1]}'


def converter(number):
    """ Converts the number into all bases. """

    digits = number[2:]

    if '0b' in number:
        decimal = int(digits, 2)
    elif '0o' in number:
        decimal = int(digits, 8)
    elif '0d' in number:
        decimal = int(digits)
    elif '0x' in number:
        decimal = int(digits, 16)

    binaryNum = bin(decimal)
    octalNum = oct(decimal)
    decimalNum = f'0d{decimal}'
    hexidecimalNum = hex(decimal)

    return f'{binaryNum}, {octalNum}, {decimalNum}, {hexidecimalNum}'


if __name__ == '__main__':
    main()