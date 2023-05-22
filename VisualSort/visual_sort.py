import tkinter as tk

from random import randint
from time import sleep


def main():
    number_of_bars = 40
    width = 4
    max_height = 500
    x_pad = 1
    y_pad = 5
    speed = 0
    color = 'grey'

    wn = tk.Tk()
    wn.title('Visual Sort')
    wn.config(bg='black')

    bars = Bars(wn, x_pad, y_pad, speed)
    bars.create_bars(number_of_bars, max_height, width, color)

    # bars.insertion_sort()
    # bars.clear_bars()
    # sleep(1)
    # bars.create_bars(number_of_bars, max_height, width)
    # bars.selection_sort()
    # bars.bubble_sort()

    # bars.selection_sort()
    # sleep(1)
    # bars.clear_bars()
    # bars.create_bars(number_of_bars, max_height, width, color)
    # bars.selection_sort_color()

    # bars.insertion_sort()
    # sleep(1)
    # bars.clear_bars()
    # bars.create_bars(number_of_bars, max_height, width, color)
    # bars.insertion_sort_color()
    bars.bubble_sort_color()
    bars.reset_bars()
    sleep(.5)
    bars.selection_sort_color()
    bars.reset_bars()
    sleep(.5)
    bars.insertion_sort_color()

    wn.mainloop()

class Bars:
    '''
    A class to represent and manage the bars.
    '''

    def __init__(self, wn, x_pad, y_pad, speed):
        self.bars = list()
        self.heights = list()
        self.original_heights = list() # Omit unless resetting bars
        self.wn = wn
        self.x_pad = x_pad
        self.y_pad = y_pad
        self.speed = speed

    def update_bars(self):
        for i, bar in enumerate(self.bars):
            bar.config(height=self.heights[i])
            bar.pack(anchor="s", side="left", padx=self.x_pad, pady=self.y_pad)
        self.wn.update()
        sleep(self.speed)

    def create_bars(self, num_of_bars, max_height, width, color):
        for _ in range(num_of_bars):
            height = randint(2, max_height)
            self.heights.append(height)
            self.original_heights.append(height) # Omit unless resetting bars

            bar = tk.Frame(width=width, height=height, bg=color)
            bar.pack(anchor="s", side = "left", padx=self.x_pad, pady=self.y_pad)
            self.bars.append(bar)

    def insertion_sort(self):
        for j in range(1, len(self.heights)):
            k = j - 1
            while k >= 0 and self.heights[k] > self.heights[k + 1]:
                self.heights[k], self.heights[k + 1] = self.heights[k + 1], self.heights[k]
                k -= 1
                self.update_bars()

    def selection_sort(self):
        for i in range(len(self.heights) - 1):
            best = i
            for j in range(i + 1, len(self.heights)):
                if self.heights[j] < self.heights[best]:
                    best = j
                self.update_bars()
            self.heights[i], self.heights[best] = self.heights[best], self.heights[i]

    def bubble_sort(self):
        for i in range(len(self.heights)):
            for j in range(len(self.heights) - 1 - i):
                if self.heights[j] > self.heights[j + 1]:
                    self.heights[j], self.heights[j + 1] = self.heights[j + 1], self.heights[j]
                self.update_bars()

    # Others
    # Clear bars
    def clear_bars(self):
        self.heights.clear()
        for bar in self.bars:
            bar.destroy()
        self.bars.clear()

    # Reset bars
    # This is for when you want to sort the bars again
    def reset_bars(self):
        for bar in self.bars:
            bar.config(bg='grey') ############
        self.heights = self.original_heights.copy()
        self.update_bars()
    
    # Colors
    def insertion_sort_color(self):
        self.bars[0].config(bg='lime green') ############
        for j in range(1, len(self.heights)):
            k = j - 1
            self.bars[j].config(bg='yellow') ############
            while k >= 0 and self.heights[k] > self.heights[k + 1]:
                self.heights[k], self.heights[k + 1] = self.heights[k + 1], self.heights[k]
                self.bars[k].config(bg='yellow') ############
                self.bars[k + 1].config(bg='lime green') ############
                k -= 1
                self.update_bars()
            self.bars[k + 1].config(bg='lime green') ############

    def bubble_sort_color(self):
        for i in range(len(self.heights)):
            for j in range(len(self.heights) - 1 - i):
                self.bars[j].config(bg='grey') ############
                self.bars[j + 1].config(bg='yellow') ############
                if self.heights[j] > self.heights[j + 1]:
                    self.heights[j], self.heights[j + 1] = self.heights[j + 1], self.heights[j]
                self.update_bars()
            self.bars[len(self.heights) - 1 - i].config(bg='lime green') ############

    def selection_sort_color(self):
        for k in range(len(self.heights)):
            best = k
            self.bars[-1].config(bg='grey') #########
            self.bars[k].config(bg='cyan') ############
            for q in range(k + 1, len(self.heights)):
                if q - 1 > k and q - 1 != best: ############
                    self.bars[q - 1].config(bg='grey') ############
                self.bars[q].config(bg='yellow') ############
                if self.heights[q] < self.heights[best]:
                    if best != k: ############
                        self.bars[best].config(bg='grey') ############
                    best = q
                    if best != k: ############
                        self.bars[q].config(bg='red') ############
                self.update_bars() ############
            self.heights[k], self.heights[best] = self.heights[best], self.heights[k]
            self.bars[k].config(bg='lime green') ############
            if best != k: ############
                self.bars[best].config(bg='grey') ############
        self.update_bars() ############

if __name__ == '__main__':
    main()


# Standards

# Depending on what you are doing, you may hit more standards than what is listed here.

# CSPG.Y2.2.1 - Construct and evaluate compound expressions using multiple relational and logical operators
# The insertion sort, selection sort, and bubble sort use multiple relational and logical operators
# For example: while k >= 0 and self.heights[k] > self.heights[k + 1]: in the insertion sort

# CSPG.Y2.2.4 - Analyze and utilize concepts of abstraction as modeling and abstraction as encapsulation
# Displaying the bars is an example of abstraction as modeling
# Creating a class to represent the bars is an example of abstraction as encapsulation

# CSPG.Y2.3.1 - Create programs to store, access, and manipulate level-appropriate data (e.g., structured data, objects)
# The bars are stored in a list of Frame objects in the Bars class (structured data) 
# The heights of the bars are stored in a list of integers in the Bars class (structured data)
# The bars are accessed and manipulated in the Bars class (objects)
# The heights of the bars are accessed and manipulated in the Bars class (objects)

# CSPG.Y2.3.4 - Analyze, utilize, and visually represent level appropriate static and dynamic data
# The bars are visually represented in the Bars class
# The heights of the bars are visually represented in the Bars class

# CSPG.Y2.3.5 - Perform level-appropriate data analysis using computing tools
# Sorting the heights is an example of data analysis using computing tools

# CSPG.Y2.5.1 - Design and implement level-appropriate algorithms that use iteration, recursion, selection, and sequence
# Iteration is used in the insertion sort, selection sort, and bubble sort
# Example: for i in range(len(self.heights) - 1):
# Selection is used when finding the best bar in the selection sort and when swapping the best bar with the current bar
# Example: if self.heights[j] < self.heights[best]:
# Sequence is the order in which the program is executed (top to bottom) and the order in which the bars are sorted
# Example: self.heights[j], self.heights[j + 1] = self.heights[j + 1], self.heights[j]
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
