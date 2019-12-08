import pygame

import constants
from platforms import *

class BaseLevel(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.background = None # background image

    def update(self): # updae everything on this level
        self.platform_list.update()
        self.enemy_list.update()
    
    def draw(self, screen):
        screen.fill(constants.BLUE)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
    
class Level1(BaseLevel):
    def __init__(self, player):
        super().__init__(player)

        items = [[210, 70, 500, 500],
                 [210, 70, 200, 400],
                 [210, 70, 600, 300]]        
        
        for item in items:
            block = Platform(item[0], item[1])
            block.rect.x = item[2]
            block.rect.y = item[3]
            block.player = self.player
            self.platform_list.add(block)
