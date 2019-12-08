import pygame

import constants
from platforms import *

class BaseLevel:
    def __init__(self, player):
        self.platform_list = None # list of sprites used in all levels
        self.enemy_list = None # list of sprites used in all levels
        self.background = None
        self.world_shift = 0 # how far this world has been scrolled left/right
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self): # update everything on this level
        self.platform_list.update()
        self.enemy_list.update()
    
    def draw(self, screen):
        screen.fill(constants.BLUE)
        # we don't shift the background as much as the sprites to give a feeling of depth
        screen.blit(self.background, (self.world_shift // 3, 0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

class Level1(BaseLevel):
    def __init__(self, player):
        super().__init__(player)
        
        self.background = pygame.image.load("images/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        items = [[constants.GRASS_LEFT, 500, 500],
                 [constants.GRASS_MIDDLE, 570, 500],
                 [constants.GRASS_RIGHT, 640, 500],
                 [constants.GRASS_LEFT, 800, 400],
                 [constants.GRASS_MIDDLE, 870, 400],
                 [constants.GRASS_RIGHT, 940, 400],
                 [constants.GRASS_LEFT, 1000, 500],
                 [constants.GRASS_MIDDLE, 1070, 500],
                 [constants.GRASS_RIGHT, 1140, 500],
                 [constants.STONE_PLATFORM_LEFT, 1120, 280],
                 [constants.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [constants.STONE_PLATFORM_RIGHT, 1260, 280]]
        
        for item in items:
            block = Platform(item[0])
            block.rect.x = item[1]
            block.rect.y = item[2]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(constants.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level2(BaseLevel):
    def __init__(self, player):
        super().__init__(player)

        self.background = pygame.image.load("images/background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        items = [[constants.STONE_PLATFORM_LEFT, 500, 550],
                 [constants.STONE_PLATFORM_MIDDLE, 570, 550],
                 [constants.STONE_PLATFORM_RIGHT, 640, 550],
                 [constants.GRASS_LEFT, 800, 400],
                 [constants.GRASS_MIDDLE, 740, 400],
                 [constants.GRASS_LEFT, 1000, 500],
                 [constants.GRASS_MIDDLE, 1070, 500],
                 [constants.GRASS_RIGHT, 1140, 500],
                 [constants.STONE_PLATFORM_LEFT, 1120, 280],
                 [constants.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [constants.STONE_PLATFORM_RIGHT, 1260, 280]]
        
        for item in items:
            block = Platform(item[0])
            block.rect.x = item[1]
            block.rect.y = item[2]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(constants.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
