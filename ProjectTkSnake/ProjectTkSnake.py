from tkinter import Tk, Canvas, Label
from time import sleep
from random import randint

from gameManager import GameManager
from food import Food
from snake import Snake
from gameSettings import GameSettings

def main():
    tk = Tk()
    tk.title('Snake')
    tk.resizable(0,0)
    tk.wm_attributes('-topmost', 1)

    manager = GameManager()
    settings = GameSettings()

    canvas = Canvas(tk, width=settings.width, height=settings.height, bd=0, highlightthickness=0, background='black')
    canvas.pack()

    textLabel = Label(tk, text='Press ENTER to begin.\nPress ESCAPE at anytime to exit.')
    textLabel.pack()

    tk.update()   

    canvas.bind_all("<Return>", manager.startGame)
    canvas.bind_all("<space>", manager.pauseGame)
    canvas.bind_all("<Escape>", manager.closeGame)

    while manager.gameRunning:        
        while manager.inStartMenu:
            if not manager.gameRunning:
                break
            tk.update_idletasks()
            tk.update()
            sleep(settings.gameSpeed)            
        
        canvas.delete("all")
        
        food = Food(canvas, settings)
        manager.foodPlaced = False
        snake = Snake(canvas, settings)
        textID = canvas.create_text(settings.width-45, 20, text = f'Segments: {str(len(snake.segments))}', fill='yellow')

        while not manager.inStartMenu:
            if not manager.gameRunning:
                break
            elif manager.gameOver:
                manager.inStartMenu == True
            elif not manager.gamePaused:
                textLabel.configure(text='Press SPACE to pause game!')
                gameLoop(tk, canvas, manager, settings, snake, food)
                canvas.itemconfig(textID, text = f'Segments: {str(len(snake.segments))}')
            else:
                textLabel.configure(text='GAME PAUSED!')
                tk.update_idletasks()
                tk.update()
                sleep(settings.gameSpeed)
        textLabel.configure(text='GAME OVER!\nPress ENTER to start a new game!')
    tk.destroy()


def gameLoop(tk, canvas, manager, settings, snake, food):
    
    if not manager.foodPlaced:
        food.placeFood(settings)
        manager.foodPlaced = True
    snake.checkForCollisions(manager, food, settings)
            
    tk.update_idletasks()
    tk.update()
    sleep(settings.gameSpeed)

if __name__ == '__main__':
    main()