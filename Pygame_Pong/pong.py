import pygame as p
from paddle import Paddle
from ball import Ball

def main():
    p.init() # Start up Pygame

    # Window Settings
    xSize = 700
    ySize = 500
    size = (xSize, ySize)
    screen = p.display.set_mode(size)
    p.display.set_caption('Pong Fun!')

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    cyan = (0, 255, 255)

    # Paddle
    paddle = Paddle(white, 10, 100)
    paddle.rect.x = 20
    paddle.rect.y = 200

    # Ball
    ball = Ball(cyan, 10, 10)
    ball.rect.x = int(xSize / 2)
    ball.rect.y = int(ySize / 2)

    # Adding sprites to a sprite group
    sprites = p.sprite.Group()
    sprites.add(paddle)
    sprites.add(ball)

    playing = True # Boolean to check game loop
    clock = p.time.Clock() # Create a clock to manage framerate

    score = 0

    # Game Loop
    while playing:

        # Check if player is exiting the game
        for event in p.event.get():
            if event.type == p.QUIT:
                playing = False
            elif event.type==p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    playing = False

        # Check key presses to move paddle.
        keys = p.key.get_pressed()
        if keys[p.K_UP]:
            paddle.moveUp(5)
        if keys[p.K_DOWN]:
            paddle.moveDown(5)

        # Update ball's velocity if it hits a wall
        if ball.rect.x >= xSize - 10 or ball.rect.x <= 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > ySize - 10 or ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # Check if the ball hits the paddle and bounce it if it does
        if p.sprite.collide_mask(ball, paddle):
            score += 1
            ball.bounce()

        sprites.update() # Update sprites 

        screen.fill(black) # Background of screen

        p.draw.line(screen, white, [int(xSize / 2), 0], [int(xSize / 2), ySize], 5) # Middle line

        sprites.draw(screen) # Draws sprites to the surface

        # Set font for scoreboard
        font = p.font.Font(None, 74)
        text = font.render(str(score), 1, white)
        screen.blit(text, (int(xSize / 4), 10))

        p.display.flip() # Updates the display to the new surface (updates the frame)

        clock.tick(60) # Update game clock (run no more than 60 frames per second)

    p.quit() # Exit the game application

if __name__ == '__main__':
    main()