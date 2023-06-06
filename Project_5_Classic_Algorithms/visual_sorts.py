import tkinter as tk

from random import randint
from time import sleep


def main():
    # This are the variables you can change
    number_of_bars = 40
    width = 10
    max_height = 500
    x_pad = 1
    y_pad = 5
    speed = 0
    color = 'grey'

    # Set up window
    wn = tk.Tk()
    wn.title('Visual Sort')
    wn.config(bg='black')

    # Create bars
    bars = Bars(wn, x_pad, y_pad, speed)
    bars.create_bars(number_of_bars, max_height, width, color)
    
    # Sort bars
    # bars.insertion_sort()
    # bars.selection_sort()
    # bars.bubble_sort()
    # bars.insertion_sort_color()
    # bars.selection_sort_color()
    bars.bubble_sort_color()

    wn.mainloop()

class Bar:
    '''
    A class to represent a bar.
    '''
    def __init__(self, height, width, color):
        self.height = height
        self.frame = tk.Frame(width=width, height=self.height, bg=color)

    def color(self, color):
        self.frame.config(bg=color)
    
    def __lt__(self, __value: object) -> bool:
        return self.height < __value.height
    
    def __gt__(self, __value: object) -> bool:
        return self.height > __value.height

class Bars:
    '''
    A class to represent and manage the bars.

    '''

    def __init__(self, wn, x_pad, y_pad, speed):
        self.bars = list()
        self.wn = wn
        self.x_pad = x_pad
        self.y_pad = y_pad
        self.speed = speed

    def update_bars(self):
        for bar in self.bars:
            bar.frame.pack_forget()
        for bar in self.bars:
            bar.frame.pack(anchor="s", side="left", padx=self.x_pad, pady=self.y_pad)
        self.wn.update()
        sleep(self.speed)

    def create_bars(self, num_of_bars, max_height, width, color):
        for _ in range(num_of_bars):
            height = randint(2, max_height)
            bar = Bar(height, width, color)
            bar.frame.pack(anchor="s", side = "left", padx=self.x_pad, pady=self.y_pad)
            self.bars.append(bar)

    def insertion_sort(self):
        for j in range(1, len(self.bars)):
            k = j - 1
            while k >= 0 and self.bars[k] > self.bars[k + 1]:
                self.bars[k], self.bars[k + 1] = self.bars[k + 1], self.bars[k]
                k -= 1
                self.update_bars()

    def selection_sort(self):
        for i in range(len(self.bars) - 1):
            best = i
            for j in range(i + 1, len(self.bars)):
                if self.bars[j] < self.bars[best]:
                    best = j
                self.update_bars()
            self.bars[i], self.bars[best] = self.bars[best], self.bars[i]

    def bubble_sort(self):
        for i in range(len(self.bars)):
            for j in range(len(self.bars) - 1 - i):
                if self.bars[j] > self.bars[j + 1]:
                    self.bars[j], self.bars[j + 1] = self.bars[j + 1], self.bars[j]
                self.update_bars()

    # Others
  
    # Colors
    def insertion_sort_color(self):
        self.bars[0].color('lime green') ############
        for j in range(1, len(self.bars)):
            k = j - 1
            self.bars[j].color('yellow') ############
            while k >= 0 and self.bars[k] > self.bars[k + 1]:
                self.bars[k], self.bars[k + 1] = self.bars[k + 1], self.bars[k]
                self.bars[k].color('yellow') ############
                self.bars[k + 1].color('lime green') ############
                k -= 1
                self.update_bars()
            self.bars[k + 1].color('lime green') ############

    def bubble_sort_color(self):
        for i in range(len(self.bars)):
            for j in range(len(self.bars) - 1 - i):
                if self.bars[j] > self.bars[j + 1]:
                    self.bars[j], self.bars[j + 1] = self.bars[j + 1], self.bars[j]
                self.bars[j].color('grey') ############
                self.bars[j + 1].color('yellow') ############
                self.update_bars()
            self.bars[len(self.bars) - 1 - i].color('lime green') ############

    def selection_sort_color(self):
        for k in range(len(self.bars)):
            best = k
            self.bars[-1].color('grey') #########
            self.bars[k].color('cyan') ############
            for q in range(k + 1, len(self.bars)):
                if q - 1 > k and q - 1 != best: ############
                    self.bars[q - 1].color('grey') ############
                self.bars[q].color('yellow') ############
                if self.bars[q] < self.bars[best]:
                    if best != k: ############
                        self.bars[best].color('grey') ############
                    best = q
                    if best != k: ############
                        self.bars[q].color('red') ############
                self.update_bars() ############
            self.bars[k], self.bars[best] = self.bars[best], self.bars[k]
            self.bars[k].color('lime green') ############
            if best != k: ############
                self.bars[best].color('grey') ############
        self.update_bars() ############

if __name__ == '__main__':
    main()




# Standards

# Depending on what you are doing, you may hit more standards than what is listed here.

# CSPG.Y2.2.1 - Construct and evaluate compound expressions using multiple relational and logical operators
# The insertion sort, selection sort, and bubble sort use multiple relational and logical operators
# For example: while k >= 0 and self.bars[k] > self.bars[k + 1]: in the insertion sort

# CSPG.Y2.2.4 - Analyze and utilize concepts of abstraction as modeling and abstraction as encapsulation
# Displaying the bars is an example of abstraction as modeling
# Creating classes to represent the bar and bars is an example of abstraction as encapsulation

# CSPG.Y2.3.1 - Create programs to store, access, and manipulate level-appropriate data (e.g., structured data, objects)
# The bars are stored in a list of Bar objects in the Bars class (structured data) 
# The bars are accessed and manipulated in the Bars class (objects)

# CSPG.Y2.3.4 - Analyze, utilize, and visually represent level appropriate static and dynamic data
# The bars are visually represented in the Bars class
# The heights of the bars are visually represented in the Bar class

# CSPG.Y2.3.5 - Perform level-appropriate data analysis using computing tools
# Sorting the heights is an example of data analysis using computing tools

# CSPG.Y2.5.1 - Design and implement level-appropriate algorithms that use iteration, recursion, selection, and sequence
# Iteration is used in the insertion sort, selection sort, and bubble sort
# Example: for i in range(len(self.bars) - 1):
# Selection is used when finding the best bar in the selection sort and when swapping the best bar with the current bar
# Example: if self.bars[j] < self.bars[best]:
# Sequence is the order in which the program is executed (top to bottom) and the order in which the bars are sorted
# Example: self.bars[j], self.bars[j + 1] = self.bars[j + 1], self.bars[j]
# Recursion is not used in this program

# CSPG.Y2.5.3 - Evaluate the qualities of level-appropriate student created and non-student-created algorithms including classic search and sort algorithms
# The insertion sort, selection sort, and bubble sort are classic sort algorithms

# CSPG.Y2.5.4 - Use a systematic approach to detect and resolve errors in a given algorithm
# CSPG.Y2.6.5 - Use a systematic approach to detect logic, runtime, and syntax errors within a program
# We used print statements to detect errors in the algorithms
# We run the program to detect errors in the algorithms
# We could use a debugger to detect errors in the algorithms
# We could use rubber duck debugging to detect errors in the algorithms
# We could use a flowchart to detect errors in the algorithms by seeing if the program follows the flowchart

# CSPG.Y2.6.1 - Create programs to solve problems of level appropriate complexity - Programs must include classes.
# The Bars class is used to solve the problem of sorting the bars
# The Bars class includes the insertion sort, selection sort, and bubble sort to solve the problem of sorting the bars

# CSPG.Y2.6.2 - Discuss and apply best practices of program design and format (e.g., descriptive names, documentation,
# indentation, user experience design, whitespace)
# The names of the variables and functions are descriptive
# The program is documented by using comments and docstrings.
# The program is indented
# The program has a good user experience design by allowing for the user to choose the number of bars, the width of the bars,
# the maximum height of the bars, the x padding, the y padding, the speed, and the color of the bars
# The program has whitespace

# CSPG.Y2.6.3 - Determine the scope and state of variables defined in classes and class procedures
# The scope of the variables defined in the Bars class is useable in the entire Bars class
# We use a main function to control the scope of the variables in the program by avoiding global variables that could be
# usable in the Bars class. We want to control the scope of the variables in the program so that we can avoid errors.

# CSPG.Y2.10.9 - Create and maintain a digital collection of self created work
# This program could have been a self created work by a student. If it was, then the student
# could have added it to their digital collection of self created work.
