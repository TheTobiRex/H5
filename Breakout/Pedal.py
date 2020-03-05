import ObjectProperties
import pygame

class pedal(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame
    # it was decided to enherrit from the class "Sprite", due to it having necessary methods and properties


    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(ObjectProperties.BLACK)
        self.image.set_colorkey(ObjectProperties.BLACK)

        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    # Move if you press right arrow
    def moveright(self, pixels):
        self.rect.x += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.x > 700:
            self.rect.x = 700

    # Move if you press left arrow
    def moveleft(self, pixels):
        self.rect.x -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0