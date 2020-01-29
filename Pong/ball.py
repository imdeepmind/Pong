import pygame
from random import randint

from constants import *

class Ball:
    def __init__(self):
        self.x = randint(0, SCREEN_WIDTH)
        self.y = SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)
        
        self.radius = 5

        self.xv = 5
        self.yv = 5

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
    
    def update(self):
        if self.x >= SCREEN_WIDTH or self.x <= 0:
            self.xv *= -1
        
        if self.y >= SCREEN_HEIGHT or self.y <= 0:
          self.yv *= -1  

        self.x += self.xv
        self.y += self.yv
    
    def isGameOver(self):
        if self.y > SCREEN_HEIGHT - 10:
            return True
        else:
            return False