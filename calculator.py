from tkinter import Tk, Frame, Entry, Label, Button
from tkinter.font import Font

def main():
    window = Tk()
    window.title('Calculator')

    fontStyle = Font(family='Courier', size=20)

    entryExpression = Entry(master=window, width=30, font=fontStyle)
    labelEqual = Label(master=window, text=' = ', font=fontStyle)
    labelResult = Label(master=window, text='0', font=fontStyle)

    entryExpression.grid(row=0, column=0)
    labelEqual.grid(row=0, column=1)
    labelResult.grid(row=0, column=2)

    buttonCalc = Button(master=window, text='Calculate', font=fontStyle, command=lambda : calculate(entryExpression, labelResult))

    buttonCalc.grid(row=1)

    window.mainloop()

def calculate(expression, labelResult):
    """Evaluate the expression in the entry widget.
    Update the label with the result on row 1.
    """
    
    e = expression.get()
    result = eval(e)
    labelResult['text'] = result

if __name__ == '__main__':
    main()