from random import randrange

class Food:
    
    def __init__(self, canvas, settings):        
        self.canvas = canvas
        self.settings = settings
        self.color = 'red'
        self.size = settings.segmentSize
        self.id = canvas.create_rectangle(0,0,self.size,self.size,fill=self.color)
        self.coordinates = canvas.coords(self.id)

    def placeFood(self, settings):
        xLoc = randrange(0,settings.width, settings.segmentSize)
        yLoc = randrange(0,settings.width, settings.segmentSize)
        xLoc2 = xLoc + settings.segmentSize
        yLoc2 = yLoc + settings.segmentSize
        self.canvas.coords(self.id, xLoc, yLoc, xLoc2, yLoc2)


