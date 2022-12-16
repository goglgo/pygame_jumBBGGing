# Simple pygame program
# Import and initialize the pygame library
import pygame, os
from pygame.locals import *

pygame.init()

BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])


class EventCheck(object):
    def __init__(self):
        self.running = True
    
    def check(self):
        for event in pygame.event.get():

            # Did the user click the window close button?
            if event.type == pygame.QUIT:
                self.running = False


class PlayerObject(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerObject, self).__init__()
        player_picture_path = os.path.join(ASSET_DIR, "player", "player.png")
        picture = pygame.image.load(player_picture_path)

        # surf from picture by .convert()
        self.surf = picture.convert()

        # rect from surf by .get_rect()
        self.rect = self.surf.get_rect()
        
Player = PlayerObject()
# Run until the user asks to quit
EVENT = EventCheck()

while EVENT.running:
    EVENT.check()

    # Fill the background with white
    screen.fill((255, 255, 255))
    screen.blit(Player.surf, Player.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
