import pygame as p

class Paddle(p.sprite.Sprite):
    # Paddle class in the game

    def __init__(self, color, width, height):
        super().__init__()

        # Prep the paddle image (no actual image sprite)
        self.image = p.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        p.draw.rect(self.image, color, [0, 0, width, height]) # Create the paddle

        self.rect = self.image.get_rect() # Store the rect information for paddle

    def moveUp(self, pixels):
        # Move paddle up but not beyond top of screen
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        # Move paddle down but not below screen
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400