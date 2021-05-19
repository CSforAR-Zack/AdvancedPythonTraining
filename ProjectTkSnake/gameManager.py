from food import Food
from snake import Snake

class GameManager:

    def __init__(self):
        self.gameRunning = True
        self.foodPlaced = False
        self.inStartMenu = True
        self.gamePaused = False
        self.gameOver = False

    def startGame(self, evt):
        self.inStartMenu = False
        self.gameOver = False

    def pauseGame(self, evt):
        if self.gamePaused == False:
            self.gamePaused = True
        else:
            self.gamePaused = False

    def endGame(self):
        self.gameOver = True
        self.inStartMenu = True

    def closeGame(self, evt):
        self.gameRunning = False


