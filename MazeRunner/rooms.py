import pygame

import constants
from wall import *

class BaseRoom(object):
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

class Room1(BaseRoom):
    def __init__(self):
        super().__init__()

        items = [[0, 0, 20, 250, constants.WHITE],
                 [0, 350, 20, 250, constants.WHITE],
                 [780, 0, 20, 250, constants.WHITE],
                 [780, 350, 20, 250, constants.WHITE],
                 [20, 0, 760, 20, constants.WHITE],
                 [20, 580, 760, 20, constants.WHITE],
                 [390, 50, 20, 500, constants.BLUE]]
            
        for item in items:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room2(BaseRoom):
    def __init__(self):
        super().__init__()

        items = [[0, 0, 20, 250, constants.RED],
                 [0, 350, 20, 250, constants.RED],
                 [780, 0, 20, 250, constants.RED],
                 [780, 350, 20, 250, constants.RED],
                 [20, 0, 760, 20, constants.RED],
                 [20, 580, 760, 20, constants.RED],
                 [190, 50, 20, 500, constants.GREEN],
                 [590, 50, 20, 500, constants.GREEN]]
 
        for item in items:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room3(BaseRoom):
    def __init__(self):
        super().__init__()

        items = [[0, 0, 20, 250, constants.PURPLE],
                 [0, 350, 20, 250, constants.PURPLE],
                 [780, 0, 20, 250, constants.PURPLE],
                 [780, 350, 20, 250, constants.PURPLE],
                 [20, 0, 760, 20, constants.PURPLE],
                 [20, 580, 760, 20, constants.PURPLE]]

        for item in items:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
        
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, constants.RED)
                self.wall_list.add(wall)
            
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, constants.WHITE)
            self.wall_list.add(wall)
