# Simple pygame program
# Import and initialize the pygame library
import pygame
from pygame.locals import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


class EventCheck(object):
    def __init__(self):
        self.running = True
    
    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

# Run until the user asks to quit
EVENT = EventCheck()

while EVENT.running:
    # Did the user click the window close button?
    EVENT.check()

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
