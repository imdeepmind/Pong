import pygame

from constants import *

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        
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