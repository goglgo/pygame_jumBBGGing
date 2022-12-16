# Simple pygame program
# Import and initialize the pygame library
import pygame, os
from pygame.locals import *

pygame.init()

BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

clock = pygame.time.Clock()

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
    def __init__(self, screen_width=500, screen_height=500):
        super(PlayerObject, self).__init__()
        player_picture_path = os.path.join(ASSET_DIR, "player", "player.png")
        picture = pygame.image.load(player_picture_path)

        # surf from picture by .convert()
        self.surf = picture.convert()

        # rect from surf by .get_rect()
        self.rect = self.surf.get_rect()

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-10)
        
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,10)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10,0)
        
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10,0)

        if self.rect.left < 0:
            self.rect.left = 0

        # if self.rect.right > self.screen_width:
        #     self.rect.right = self.screen_width

        if self.rect.top <= 0:
            self.rect.top = 0
        
        # if self.rect.bottom >= self.screen_height:
        #     self.rect.bottom = self.screen_height


        
Player = PlayerObject()
# Run until the user asks to quit
EVENT = EventCheck()

while EVENT.running:
    EVENT.check()

    # Fill the background with white
    screen.fill((255, 255, 255))
    
    screen.blit(Player.surf, Player.rect)
    Player.update()

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
