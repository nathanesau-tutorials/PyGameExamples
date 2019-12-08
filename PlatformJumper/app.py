import pygame

import constants
from game import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Platformer Jumper")

    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
    active_sprite_list = pygame.sprite.Group()

    game = Game(screen, active_sprite_list)
    game.initializePlayer()
    game.initializeLevelList()
    game.initializeCurrentLevelNo()
    game.initiailizeCurrentLevel()
    game.initializeClock()
    game.runGame()