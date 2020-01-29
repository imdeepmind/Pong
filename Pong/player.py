import pygame

from constants import *

class Player:
    def __init__(self):
        self.width = SCREEN_WIDTH // 4
        self.height = 5

        self.x = (SCREEN_WIDTH // 2) - (self.width // 2)
        self.y = SCREEN_HEIGHT - (self.height * 2)
        
        self.vx = 20

        self.movement = 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
    
    def update(self, direction):
        if direction == "LEFT":
            self.movement = 0
            if self.x >= 10:
                self.x -= self.vx
        elif direction == "RIGHT":
            self.movement = 1
            if self.x <= SCREEN_WIDTH - (self.width + 10):
                self.x += self.vx
    
    def getPosition(self):
        return (self.x, self.y, self.width, self.height)
    
    def getMovement(self):
        return self.movement