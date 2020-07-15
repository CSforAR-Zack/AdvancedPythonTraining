import pygame as p
from random import randint

class Ball(p.sprite.Sprite):
    # Represents the ball in the game

    def __init__(self, color, width, height):
        super().__init__()

        # Prep the ball image (no actual image sprite)
        self.image = p.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        p.draw.rect(self.image, color, [0, 0, width, height]) # Create teh ball shape (square)

        self.velocity = [randint(4,8), randint(-8, 8)] # Set ball velocity

        self.rect = self.image.get_rect() # Store the area rectangle of the surface

    def update(self):
        # Update the velocity of the ball (movement)
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        # Flip the velocities when the ball hits an object (paddle)
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
