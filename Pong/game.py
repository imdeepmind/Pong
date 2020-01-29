import pygame

from player import Player
from constants import *

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Window title
pygame.display.set_caption("Pong Game")

player = Player()

# Game loop
running = True
while running:
  # Checking for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Filling the screen with white color
  screen.fill(WHITE)  

  player.draw(screen)    

  # Updating the screen
  pygame.display.update()