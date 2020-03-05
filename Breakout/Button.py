import pygame
import ObjectProperties

class button(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(ObjectProperties.BLACK)
        self.image.set_colorkey(ObjectProperties.BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
