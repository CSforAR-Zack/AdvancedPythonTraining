from tkinter import Tk, Frame, Entry, Label, Button
from tkinter.font import Font

def main():
    wn = Tk()
    wn.title('Temperature Converter')

    fontStyle = Font(family='Courier', size=20)

    # F to C Setup
    frameEntryF = Frame(master=wn)
    entryF = Entry(master=frameEntryF, width=10, font=fontStyle)
    labelF = Label(master=frameEntryF, text='\u00b0 F', font=fontStyle)
    labelResultC = Label(master=wn, text='\u00b0 C', font=fontStyle)

    frameEntryF.grid(row=0, column=0, padx=10)
    entryF.grid(row=0,column=0, padx=10)
    labelF.grid(row=0,column=2, padx=10)

    buttonFtoC = Button(master=wn, text='\u2192', font=fontStyle, 
                        command=lambda : fToC(entryF, labelResultC))

    buttonFtoC.grid(row=0, column=1, pady=10)
    labelResultC.grid(row=0, column=2, padx=10)

    wn.mainloop()

def fToC(entryF, labelResultC):

    f = entryF.get()
    c = (5/9) * (float(f) - 32)
    labelResultC['text'] = f'{round(c, 2)} \u00b0 C'

if __name__ == '__main__':
    main()