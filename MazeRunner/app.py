import pygame

from game import *
from player import *
from rooms import *
from wall import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Maze Runner')

    screen = pygame.display.set_mode([800, 600])
    moving_sprites = pygame.sprite.Group()

    game = Game(screen, moving_sprites)
    game.initializePlayer()
    game.initializeRooms()
    game.initializeCurrentRoomNo()
    game.initializeCurrentRoom()
    game.initializeClock()
    game.runGame()

    pygame.quit()