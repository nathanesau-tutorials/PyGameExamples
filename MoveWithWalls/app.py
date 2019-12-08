import pygame

import constants
from game import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Move with Walls')

    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
    all_sprite_list = pygame.sprite.Group()

    game = Game(screen, all_sprite_list)
    game.initializeWallList()
    game.initializePlayer()
    game.initializeClock()
    game.runGame()

    pygame.quit()