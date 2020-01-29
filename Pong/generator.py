import pygame
import pandas as pd

from .player import Player
from .ball import Ball
from .score import Score

from .constants import *

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Window title
pygame.display.set_caption("Pong Game")

# Setting a clock
clock = pygame.time.Clock()

def generate():
  # Initializing the player and ball
  player = Player()
  ball = Ball()
  score = Score()

  gameStatus = "SCORE: "
  gameScore = 0

  # Dataset array
  dataset = []

  # Game loop
  running = True
  while running:
    # Filling the screen with white color
    screen.fill(WHITE)  

    # Drawing the player and ball on the screen
    ball.draw(screen)
    player.draw(screen) 
    score.write(screen, gameStatus + str(gameScore))

    # Checking for GAME OVER
    if ball.isGameOver():
      print('GAME OVER')
      running = False

    # Updating the position of the ball
    playerPosition = player.getPosition()
    gameScore = ball.update(playerPosition, gameScore)

    # Checking for events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      # Based on the keystrokes, changes the position of the player
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          player.update("LEFT")
      
        if event.key == pygame.K_RIGHT:
          player.update("RIGHT")
        
        # Getting the movement data for generating the dataset
        bx, by = ball.getPosition()
        px, py, pw, ph = player.getPosition()
        playerMovement = player.getMovement()

        dataset.append([bx, by, px, py, pw, ph, playerMovement, 1 if running else 0])
    
    # Setting FPS for the game
    clock.tick(FPS)

    # Updating the screen
    pygame.display.update()

  if len(dataset) > 0:
    df = pd.DataFrame(dataset)
    df.columns = ["BallX", "BallY", "PlayerX", "PlayerY", "PlayerW", "PlayerH", "PlayerMovement", "Running"]

    df.to_csv('dataset.csv', index=False)