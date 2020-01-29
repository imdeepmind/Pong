import pygame

from constants import *

class Player:
    def __init__(self):
        self.width = SCREEN_WIDTH // 4
        self.height = 5

        self.x = (SCREEN_WIDTH // 2) - (self.width // 2)
        self.y = SCREEN_HEIGHT - (self.height * 2)
        
        self.vx = 5
        self.vy = 5
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))