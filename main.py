import pygame
import sys

from settings import *

pygame.init()

# Window
width = mines_width * 16
height = mines_height * 16
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.time.Clock().tick(fps)