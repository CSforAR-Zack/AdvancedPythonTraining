import tkinter as tk

from random import randint
from time import sleep


def main():
    # This are the variables you can change
    number_of_bars = 40
    low_value = 0
    high_value = 40
    speed = .5
    random = False
    values = [1, 3, 5, 8, 9, 12, 15, 123, 435, 4, 23, 4, 7, 3, 4, 5, 4, 3, 769, 6, 5, 34]

    # Set up window
    wn = tk.Tk()
    wn.title('Visual Search')
    wn.config(bg='black')

    # Create bars
    boxes = Boxes(wn, speed, values)

    # boxes.create_boxes(number_of_bars, low_value, high_value, random, sorted=True)    
    # boxes.linear_search(123)

    boxes.create_boxes(number_of_bars, low_value, high_value, random, sorted=True)
    boxes.binary_search(123)

    wn.mainloop()

class Boxes:
    '''
    A class to represent and manage the bars.

    '''

    def __init__(self, wn, speed, values=None):
        self.boxes = list()
        self.wn = wn
        self.speed = speed
        self.values = values

    def create_boxes(self, num_of_boxes, low_value, high_value, random, sorted=False):
        color = 'white'
        width = 6
        height = 3
        padx = 2
        pady = 2

        if random:
            self.values = list()
            for _ in range(num_of_boxes):
                value = randint(low_value, high_value)
                self.values.append(value)


        if sorted:
            self.values.sort()
        
        for value in self.values:
            box = tk.Label(self.wn, text=value, width=width, height=height, bg=color)
            
            box.pack(anchor="s", side = "left", padx=padx, pady=pady)
            self.boxes.append(box)

    def linear_search(self, target):
        found_color = 'cyan'
        not_found_color = 'grey'

        for box in self.boxes:
            if box['text'] == target:
                box.config(bg=found_color)
                return
            else:
                box.config(bg=not_found_color)
           
            self.wn.update()
            sleep(self.speed)

    def binary_search(self, target):

        found_color = 'cyan'
        not_found_color = 'grey'

        lower = 0
        upper = len(self.boxes) - 1

        while lower <= upper:
            mid = (lower + upper) // 2

            if target == self.boxes[mid]['text']:
                self.boxes[mid].config(bg=found_color)
                return
            elif self.boxes[mid]['text'] > target:
                upper = mid - 1
            else:
                lower = mid + 1

            self.boxes[mid].config(bg=not_found_color)

            self.wn.update()
            sleep(self.speed)

        return -1

    # Others
    # Clear boxes
    def clear_bars(self):
        for box in self.boxes:
            box.destroy()
        self.boxes.clear()


if __name__ == '__main__':
    main()