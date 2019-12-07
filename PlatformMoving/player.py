import pygame

import constants
from platforms import *

# this class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([40, 60])
        self.image.fill(constants.RED)
        self.rect = self.image.get_rect()
        self.change_x = 0 # set speed vector of player
        self.change_y = 0 # set speed vector of player
        self.level = None # list of sprites we can bump against

    def update(self):
        self.calc_grav() # gravity
        self.rect.x += self.change_x
        for block in pygame.sprite.spritecollide(self, self.level.platform_list, False):
            if self.change_x > 0: # if moving right, set right side to left side of item we hit
                self.rect.right = block.rect.left
            elif self.change_x < 0: # if moving left, do the opposite
                self.rect.left = block.rect.right
        
        self.rect.y += self.change_y # move up/down

        for block in pygame.sprite.spritecollide(self, self.level.platform_list, False):
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            
            self.change_y = 0 # stop our verticla movement

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
    
    def calc_grav(self): # calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35
        
        # see if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self): # called when user hits 'jump' button
        # move down a bit and see if platform below us
        # move down two pixels because it doesn't work well to move down one pixel with platform moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT: # if ok to jump, set speed upwards
            self.change_y = -10

    def go_left(self): # called when user hits left arrow
        self.change_x = -6
    
    def go_right(self): # called when user hits right arrow
        self.change_x = 6
    
    def stop(self): # called when user lets off the keyboard
        self.change_x = 0
