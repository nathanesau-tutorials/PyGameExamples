import pygame

import constants
from platforms import *

class BaseLevel:
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.world_shift = 0 # how far this world has been scrolled left/right
        
    def update(self): # update everything on this level
        self.platform_list.update()
        self.enemy_list.update()
    
    def draw(self, screen): # draw everything on this level
        screen.fill(constants.BLUE)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x): # when user moves left/right we need to scroll everything
        self.world_shift += shift_x
        
        for platform in self.platform_list:
            platform.rect.x += shift_x
        
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
    
class Level1(BaseLevel):
    def __init__(self, player):
        super().__init__(player)

        self.level_limit = -1000

        items = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280]]
                
        for item in items:
            block = Platform(item[0], item[1])
            block.rect.x = item[2]
            block.rect.y = item[3]
            block.player = self.player
            self.platform_list.add(block)
        
class Level2(BaseLevel):
    def __init__(self, player):
        super().__init__(player)

        self.level_limit = -1000

        items = [[210, 30, 450, 570],
                 [210, 30, 850, 420],
                 [210, 30, 1000, 520],
                 [210, 30, 1120, 280]]

        for item in items:
            block = Platform(item[0], item[1])
            block.rect.x = item[2]
            block.rect.y = item[3]
            block.player = self.player
            self.platform_list.add(block)
