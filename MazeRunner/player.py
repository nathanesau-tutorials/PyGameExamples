import pygame

import constants

# represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0 # set speed vector
        self.change_y = 0 # set speed vector
        self.image = pygame.Surface([15, 15])
        self.image.fill(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        self.rect.x += self.change_x

        for block in pygame.sprite.spritecollide(self, walls, False):
            if self.change_x > 0: # if moving right, set right side to left side of item we hit
                self.rect.right = block.rect.left
            else: # if moving left, do the opposite
                self.rect.left = block.rect.right

        self.rect.y += self.change_y # move up/down

        for block in pygame.sprite.spritecollide(self, walls, False):
            # reset position based on top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
