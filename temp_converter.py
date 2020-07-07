from tkinter import Tk, Frame, Entry, Label, Button
from tkinter.font import Font

def main():
    window = Tk()
    window.title('Temperature Converter')

    fontStyle = Font(family='Courier', size=20)

    # Fahrenheit to Celcius GUI Setup
    frameEntryFahr = Frame(master=window)
    entryFahr = Entry(master=frameEntryFahr, width=10, font=fontStyle)
    labelTempFahr = Label(master=frameEntryFahr, text='\u00b0 F', font=fontStyle) #\00b0 is degree symbol

    entryFahr.grid(row=0, column=0, sticky='e')
    labelTempFahr.grid(row=0, column=1, sticky='w')

    buttonConvertFtoC = Button(master=window, text='\u2192', font=fontStyle, command=lambda : fahrToCel(entryFahr, labelResultCel))
    labelResultCel = Label(master=window, text='\u00b0 C', font=fontStyle)

    frameEntryFahr.grid(row=0, column=0, padx=10)
    buttonConvertFtoC.grid(row=0, column=1, pady=10)
    labelResultCel.grid(row=0, column=2, padx=10)

    # Celcius to Fahrenheit GUI Setup
    frameEntryCel = Frame(master=window)
    entryCel = Entry(master=frameEntryCel, width=10, font=fontStyle)
    labelTempCel = Label(master=frameEntryCel, text='\u00b0 C', font=fontStyle) #\00b0 is degree symbol

    entryCel.grid(row=0, column=0, sticky='e')
    labelTempCel.grid(row=0, column=1, sticky='w')

    buttonConvertCtoF = Button(master=window, text='\u2192', font=fontStyle, command=lambda : celToFahr(entryCel, labelResultFahr))
    labelResultFahr = Label(master=window, text='\u00b0 F', font=fontStyle)

    frameEntryCel.grid(row=1, column=0, padx=10)
    buttonConvertCtoF.grid(row=1, column=1, pady=10)
    labelResultFahr.grid(row=1, column=2, padx=10)

    window.mainloop()

def fahrToCel(entryFahr, labelResultFahr):
    """Convert a Fahrenheit value to Celsius and
    update labelResult.
    """

    f = entryFahr.get()
    c = (5/9) * (float(f) - 32)
    labelResultFahr['text'] = f'{round(c, 2)} \u00b0 C'

def celToFahr(entryCel, labelResultCel):
    """Convert a Fahrenheit value to Celsius and
    update labelResult.
    """

    c = entryCel.get()
    f = 9/5 * float(c) + 32
    labelResultCel['text'] = f'{round(f, 2)} \u00b0 F'

if __name__ == '__main__':
    main()