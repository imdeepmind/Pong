import pygame

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

# Initializing the player and ball
player = Player()
ball = Ball()
score = Score()

gameStatus = "SCORE: "
gameScore = 0

movement = 0
move = False

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

    # Moving the player based on movement
    if move:
        print('Move')
        if movement == 0:
            player.update("LEFT")
        else:
            player.update("RIGHT")

    # Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Setting FPS for the game
    clock.tick(FPS)

    # Updating the screen
    pygame.display.update()

def movePlayer(movement):
    print(movement)
    move = True
    movement = movement