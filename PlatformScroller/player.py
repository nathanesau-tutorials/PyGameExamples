import pygame

import constants

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([40, 60])
        self.image.fill(constants.RED)
        self.rect = self.image.get_rect()
        self.change_x = 0 # set speed vector
        self.change_y = 0 # set speed vector
        self.level = None

    def update(self): # move the player
        self.calc_grav() # gravity

        self.rect.x += self.change_x # move left/right

        for block in pygame.sprite.spritecollide(self, self.level.platform_list, False):
            if self.change_x > 0: # if we are moving right, set our right side to the left side of the item we hit
                self.rect.right = block.rect.left
            elif self.change_x < 0: # if we are moving left, do the opposite
                self.rect.left = block.rect.right

        self.rect.y += self.change_y # move up/down

        for block in pygame.sprite.spritecollide(self, self.level.platform_list, False):
            # reset or position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            
            self.change_y # stop our vertical movements

    def calc_grav(self): # calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        # see if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
    
    def jump(self):
        # called when user hits 'jump' button
        # move down a bit and see if there is a platform below us.
        # move down 2 pixedls because it doesn't work well if we only move down one pixel when working with platform moving down
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
        
    def go_left(self): # called when user hits the left arrow
        self.change_x = -6
    
    def go_right(self): # called when the user hits the right arrow
        self.change_x = 6
    
    def stop(self): # called when the user lets off the keyboard
        self.change_x = 0
