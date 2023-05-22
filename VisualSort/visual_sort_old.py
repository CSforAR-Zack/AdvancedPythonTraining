import tkinter as tk

from random import randint
from time import sleep


def main():
    number_of_bars = 100
    width = 4
    max_height = 500
    x_pad = 1
    y_pad = 5
    speed = 0

    wn = tk.Tk()
    canvas = tk.Canvas(wn, width=number_of_bars * (width + x_pad), height=max_height + y_pad * 2, bg='black')
    canvas.pack()
    wn.title('Visual Sort')

    bars = Bars(canvas, width, max_height, x_pad, y_pad, speed)
    bars.create_bars(number_of_bars)

    insertion_sort(bars)

    wn.mainloop()

class Bars:
    def __init__(self, canvas, width, max_height, x_pad, y_pad, speed):
        self.values = list()
        self.canvas = canvas
        self.width = width
        self.max_height = max_height
        self.x_pad = x_pad
        self.y_pad = y_pad
        self.speed = speed

    def update_bars(self):
        rects = self.canvas.find_all()
        for i, rect in enumerate(rects):
           x1, y1, x2, y2 = self.canvas.coords(rect)
           y1 = self.max_height + self.y_pad - self.values[i]
           self.canvas.coords(rect, x1, y1, x2, y2)
        
        self.canvas.update()
        sleep(self.speed)

    def create_bars(self, num_of_bars):
        for i in range(num_of_bars):
            height = randint(2, self.max_height)
            self.values.append(height)

            # Create Rectangle on Canvas
            bottom = self.max_height + self.y_pad

            x1 = i * (self.width + self.x_pad)
            y1 = bottom - height
            x2 = x1 + self.width
            y2 = bottom
            
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='lime green')

def insertion_sort(bars):
    for j in range(1, len(bars.values)):
        k = j - 1
        while k >= 0 and bars.values[k] > bars.values[k + 1]:
            swap(bars, k, k + 1)
            k -= 1
            bars.update_bars() #######################

def swap(bars, left, right):
    bars.values[left], bars.values[right] = bars.values[right], bars.values[left]


if __name__ == '__main__':
    main()