import pygame

import constants
from player import *
from wall import *

class Game:
    def __init__(self, screen, all_sprite_list):
        self.screen = screen # reference to screen
        self.all_sprite_list = all_sprite_list # reference to all_sprite_list

        self.wall_list = None
        self.player = None
        self.clock = None

    def initializeWallList(self):
        self.wall_list = pygame.sprite.Group()
        
        items = [[0, 0, 10, 600],
                 [10, 0, 790, 10],
                 [10, 200, 100, 10]]

        for item in items:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
            self.all_sprite_list.add(wall)

    def initializePlayer(self):
        self.player = Player(50, 50)
        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player)

    def initializeClock(self):
        self.clock = pygame.time.Clock()

    def processEvents(self): # return True if quit, false otherwise
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True # quit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3)

        return False # continue

    def runGame(self):
        while True:
            if self.processEvents():
                return

            self.all_sprite_list.update()

            self.screen.fill(constants.BLACK)
            self.all_sprite_list.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)