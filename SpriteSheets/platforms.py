import pygame

from spritesheet_functions import *

# platform the user can jump on
class Platform(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        super().__init__()

        sprite_sheet = SpriteSheet("images/tiles_spritesheet.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])
        self.rect = self.image.get_rect()

# a fancier platform that can actually move
class MovingPlatform(Platform):
    def __init__(self, sprite_sheet_data):
        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.level = None
        self.player = None

    def update(self):
        # move the platform
        # if the player is in the way, it will shove the player out of the way.
        # this does not handle what happens if a platform shoves a player into another object.
        # make sure moving platforms have clearance to push player around or add code to handle what happens if they don't.
        self.rect.x += self.change_x # move left/right

        if pygame.sprite.collide_rect(self, self.player): # shove the player around and assume they won't hit anything else
            if self.change_x < 0: # if moving right, set out right side to left side of the item we hit
                self.player.rect.right = self.rect.left
            else: # if moving left, do the opposite
                self.player.rect.left = self.rect.right
        
        self.rect.y += self.change_y # move up/down

        if pygame.sprite.collide_rect(self, self.player): # shove the player around and assume they won't hit anything else
            # reset our position based on the top/bottom of the object
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        
        # check the boundaries and see if we need to reverse direction
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
