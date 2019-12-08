import pygame

import constants

from platforms import *
from spritesheet_functions import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.change_x = 0 # set speed vector
        self.change_y = 0 # set speed vector
        self.walking_frames_l = [] # holds all images for animated walk left/right
        self.walking_frames_r = [] # holds all images for animated walk left/right
        self.direction = "R" # direction player is facing
        self.level = None # list of sprites we can bump against
        
        sprite_sheet = SpriteSheet("images/p1_walk.png")
        
        items = [[0, 0, 66, 90],
                 [66, 0, 66, 90],
                 [132, 0, 67, 90],
                 [0, 93, 66, 90],
                 [66, 93, 66, 90],
                 [132, 93, 72, 90],
                 [0, 186, 70, 90]]
    
        # load all the right facing images
        for item in items:
            image = sprite_sheet.get_image(item[0], item[1], item[2], item[3])
            self.walking_frames_r.append(image)

        # load all the right facing images, then flip them to face left
        for item in items:
            image = sprite_sheet.get_image(item[0], item[1], item[2], item[3])
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0] # set image the player starts with
        self.rect = self.image.get_rect()

    def update(self): # move the player
        self.calc_grav() # gravity

        self.rect.x += self.change_x # move left/right

        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        for block in pygame.sprite.spritecollide(self, self.level.platform_list, False):
            if self.change_x > 0: # if moving right, set right side to left side of the item we hit
                self.rect.right = block.rect.left
            elif self.change_x < 0: # if moving left, do the opposite
                self.rect.left = block.rect.right
        
        self.rect.y += self.change_y # move up/down

        for block in pygame.sprite.spritecollide(self, self.level.platform_list, False):
            # reset ouf position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0 # stop our vertical movement

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self): # calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
    
        # see if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # called when user hits 'jump' button
        # move down a bit and see if there is a platform below us.
        # move down two pixels because it doesn't work well if we only move down one when working with platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
        
    def go_left(self): # called when user hits the left arrow
        self.change_x = -6
        self.direction = "L"
    
    def go_right(self):
        self.change_x = 6
        self.direction = "R"
    
    def stop(self):
        self.change_x = 0