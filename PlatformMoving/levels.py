import pygame

import constants
from platforms import *

class BaseLevel(object):
    def __init__(self, screen, player):
        self.screen = screen  # reference to screen
        self.player = player # reference to player

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.background = None # background image
        self.world_shift = 0 # how far this world has been scrolled left/right
        self.level_limit = -1000

    def update(self): # update everything on this level
        self.platform_list.update()
        self.enemy_list.update()
    
    def draw(self, screen): # draw everything on this level
        self.screen.fill(constants.BLUE)
        self.platform_list.draw(self.screen)
        self.enemy_list.draw(self.screen)

    def shift_world(self, shift_x): # when user moves left/right and we need to scroll everything
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x
        
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

class Level1(BaseLevel):
    def __init__(self, screen, player):
        super().__init__(screen, player)

        self.level_limit = -1500

        # array with width, height, x and y of platform
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

        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level2(BaseLevel):
    def __init__(self, screen, player):
        super().__init__(screen, player)

        self.level_limit = -1000

        # array with width, height, x and y of platform
        items = [[210, 70, 500, 550],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280]]

        for item in items:
            block = Platform(item[0], item[1])
            block.rect.x = item[2]
            block.rect.y = item[3]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(70, 70)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)