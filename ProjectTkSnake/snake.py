

class Snake:
    def __init__(self, canvas, settings):
        self.size = settings.segmentSize
        self.color = 'cyan'
        self.canvas = canvas
        self.head = canvas.create_rectangle(0,0,self.size,self.size,fill=self.color)

        self.canvas.move(self.head, settings.width/2 + (settings.width/2)%10, settings.height/2 + (settings.height/2)%10)
        self.coordinates = self.canvas.coords(self.head)
        self.segments = [[self.head, 90]]

        # Key bindings for movement of snake
        self.canvas.bind_all("<KeyPress-Left>", self.turnLeft)
        self.canvas.bind_all("<KeyPress-Right>", self.turnRight)
        self.canvas.bind_all("<KeyPress-Up>", self.turnUp)
        self.canvas.bind_all("<KeyPress-Down>", self.turnDown)
    
    def checkForCollisions(self, manager, food, settings):
        if self.coordinates[0] < 0 or self.coordinates[1] < 0:
            manager.endGame()
        elif self.coordinates[2] > settings.width or self.coordinates[3] > settings.height:
            manager.endGame()
        
        collisions = self.canvas.find_enclosed(self.coordinates[0]-1, self.coordinates[1]-1, self.coordinates[2]+1, self.coordinates[3]+1)
        
        if len(collisions) > 0 and collisions[0] == food.id:
            manager.foodPlaced = False      

    def turnRight(self, evt):
        self.canvas.move(self.head, self.size, 0)

    def turnUp(self, evt):
        self.canvas.move(self.head, 0, -self.size)

    def turnDown(self, evt):
         self.canvas.move(self.head, 0, self.size)

    def turnLeft(self, evt):
        self.canvas.move(self.head, -self.size, 0)


    

