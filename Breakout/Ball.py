import pygame, ObjectProperties
from random import randint

class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame
    # it was decided to enherrit from the class "Sprite", due to it having necessary methods and properties

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(ObjectProperties.BLACK)
        self.image.set_colorkey(ObjectProperties.BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Define the balls velocity
        self.velocity = [randint(4,8), randint(-8,8)]

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    # This Method is used to move the ball (update it's position)
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # This Method is used to make the ball bounce
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)