import pygame

import constants
from levels import *
from player import *

class Game:
    def __init__(self, screen, active_sprite_list):
        self.screen = screen # reference to screen
        self.active_sprite_list = active_sprite_list # reference to active_sprite_list

        self.player = None
        self.level_list = None
        self.current_level_no = None
        self.current_level = None
        self.clock = None
    
    def initializePlayer(self):
        self.player = Player()
        self.player.rect.x = 340
        self.player.rect.y = constants.SCREEN_HEIGHT - self.player.rect.height
        self.active_sprite_list.add(self.player)

    def initializeLevelList(self):
        self.level_list = [Level1(self.player), Level2(self.player)]

    def initializeCurrentLevelNo(self):
        self.current_level_no = 0

    def initializeCurrentLevel(self):
        self.current_level = self.level_list[self.current_level_no]
        self.player.level = self.current_level

    def initializeClock(self):
        self.clock = pygame.time.Clock()

    def processEvents(self): # return True if quit, false otherwise
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True # quit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.go_left()
                if event.key == pygame.K_RIGHT:
                    self.player.go_right()
                if event.key == pygame.K_UP:
                    self.player.jump()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.change_x < 0:
                    self.player.stop()
                if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                    self.player.stop()

        return False # continue

    def shiftWorldIfNeeded(self):
        if self.player.rect.right >= 500: # if player gets near the right side, shift the world left (-x)
            diff = self.player.rect.right - 500
            self.player.rect.right = 500
            self.current_level.shift_world(-diff)
        
        if self.player.rect.left <= 120: # if player gets near the left side, shift the world right (+x)
            diff = 120 - self.player.rect.left
            self.player.rect.left = 120
            self.current_level.shift_world(diff)

    def goToNextLevelIfNeeded(self):
        # if player gets to the end of the level, go to the next level
        current_position = self.player.rect.x + self.current_level.world_shift
        if current_position < self.current_level.level_limit:
            self.player.rect.x = 120
            if self.current_level_no < len(self.level_list) - 1:
                self.current_level_no += 1
                self.current_level = self.level_list[self.current_level_no]
                self.player.level = self.current_level

    def runGame(self):
        while True:
            if self.processEvents():
                return

            self.active_sprite_list.update() # update the player
            self.current_level.update() # update items in the level

            self.shiftWorldIfNeeded()
            self.goToNextLevelIfNeeded()

            self.current_level.draw(self.screen)
            self.active_sprite_list.draw(self.screen)
            self.clock.tick(60) # limit to 60 frames per second
            pygame.display.flip()
