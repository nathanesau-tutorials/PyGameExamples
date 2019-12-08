import pygame

import constants

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0 # set speed vector
        self.change_y = 0 # set speed vector
        self.walls = None

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x # move left/right

        for block in pygame.sprite.spritecollide(self, self.walls, False):
            if self.change_x > 0: # if moving right, set right side to left side of the item we hit
                self.rect.right = block.rect.left
            else: # if moving left, do the opposite
                self.rect.left = block.rect.right
            
        self.rect.y += self.change_y # move up/down

        for block in pygame.sprite.spritecollide(self, self.walls, False):
            # reset our position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
