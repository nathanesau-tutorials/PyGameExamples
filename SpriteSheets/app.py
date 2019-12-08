import pygame

import constants
from game import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Platformer with sprite sheets")

    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
    active_sprite_list = pygame.sprite.Group()
    
    game = Game(screen, active_sprite_list)
    game.initializePlayer()
    game.initializeLevelList()
    game.initializeCurrentLevelNo()
    game.initializeCurrentLevel()
    game.initializeClock()
    game.runGame()

    pygame.quit()