import pygame

from .constants import *

class Score:
    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
    
    def write(self, screen, text):
        textsurface = self.font.render(text, False, (0, 0, 0))
        screen.blit(textsurface,(SCREEN_WIDTH // 3,10))