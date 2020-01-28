import pygame
from pygame.locals import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()

done = False

while not done:
    clock.tick(FPS)
    screen.fill(WHITE)

pygame.quit()