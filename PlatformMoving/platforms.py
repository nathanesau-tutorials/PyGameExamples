import pygame

import constants

# platform that the user can jump on
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.GREEN)
        self.rect = self.image.get_rect()

# this is a fancier platform that can actually move
class MovingPlatform(Platform):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.change_x = 0
        self.change_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.player = None
        self.level = None

    def update(self):
        # move the platform
        # if the player is in the way, it will shove the player out of the way.
        # this does not handle what happens if a platform shoves a player into another object.
        # make sure moving platforms have clearance to push player around or add code to handle what happens if they don't.
        self.rect.x += self.change_x
    
        if pygame.sprite.collide_rect(self, self.player): # we hit the player (shove player around and assume they won't hit anything else)
            if self.change_x < 0: # if moving right, set our right side to left side of item we hit
                self.player.rect.right = self.rect.left
            else: # if moving left, do the opposite
                self.player.rect.left = self.right.right
        
        self.rect.y += self.change_y

        if pygame.sprite.collide_rect(self, self.player): # we hit the player (shove player around and assume they won't hit anything else)
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        
        # check boundaries and see if we need to reverse direction
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= - 1
        