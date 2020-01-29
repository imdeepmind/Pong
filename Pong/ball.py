import pygame

from constants import *

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
    
    def update(self):
        pass