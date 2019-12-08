import pygame

import constants

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.GREEN)
        self.rect = self.image.get_rect()
