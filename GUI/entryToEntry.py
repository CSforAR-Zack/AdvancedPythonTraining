from tkinter import Tk, Entry, Label, StringVar

def send(textSender, textReceiver):
    ''' Update other StringVar with
    the current StringVar being edited.'''

    # Get the value from the sender and use it to
    # update the value of the reveiver
    textReceiver.set(textSender.get())

window = Tk()

# StringVars hold strings and send updates to the program to update when they change
textLeft = StringVar()
textRight = StringVar()

entryLeft = Entry(window, textvariable=textLeft) # Assign a textvariable to a StringVar
entryRight = Entry(window, textvariable=textRight)

# If the user changes the text in the entry field 'w', call the send function
# The lambda function allows to send arguments without making global vars
textLeft.trace('w', lambda *args : send(textLeft, textRight))
textRight.trace('w', lambda *args : send(textRight, textLeft))

label = Label(window, text=' <--> ')

entryLeft.grid(column=0, row=0)
entryRight.grid(column=2, row=0)
label.grid(column=1, row=0)

window.mainloop()