import pygame

import constants

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert() # create a new blank image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height)) # copy sprite from large sheet onto smaller image
        image.set_colorkey(constants.BLACK) # assuming black works as the transparent color
        return image
