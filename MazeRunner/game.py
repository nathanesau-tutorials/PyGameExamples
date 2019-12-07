import pygame

from player import *
from rooms import *

class Game:
    def __init__(self, screen, movingsprites):
        self.screen = screen # reference to screen
        self.movingsprites = movingsprites # reference to moving sprites
        self.player = None
        self.rooms = None
        self.current_room_no = None
        self.current_room = None
        self.clock = None

    def initializePlayer(self):
        self.player = Player(50, 50)
        self.movingsprites.add(self.player)
    
    def initializeRooms(self):
        self.rooms = [Room1(), Room2(), Room3()]

    def initializeCurrentRoomNo(self):
        self.current_room_no = 0
    
    def initializeCurrentRoom(self):
        self.current_room = self.rooms[self.current_room_no]
    
    def initializeClock(self):
        self.clock = pygame.time.Clock()

    def processEvents(self): # return True if quit, false otherwise
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True # quit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    self.player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 5)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    self.player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -5)

        self.player.move(self.current_room.wall_list)
        return False # continue

    def updatePlayerPosAfterMove(self):
        if self.player.rect.x < -15:
            if self.current_room_no == 0:
                self.current_room_no = 2
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 790
            elif self.current_room_no == 2:
                self.current_room_no = 1
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 790
            else:
                self.current_room_no = 0
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 790
        
        if self.player.rect.x > 801:
            if self.current_room_no == 0:
                self.current_room_no = 1
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 0
            elif self.current_room_no == 1:
                self.current_room_no = 2
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 0
            else:
                self.current_room_no = 0
                self.current_room = self.rooms[self.current_room_no]
                self.player.rect.x = 0

    def runGame(self):
        while True:
            if self.processEvents(): # quit
                return
            self.updatePlayerPosAfterMove()
            self.screen.fill(constants.BLACK)
            self.movingsprites.draw(self.screen)
            self.current_room.wall_list.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)