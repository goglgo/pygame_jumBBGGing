import pygame, os
from pygame.locals import *
from .map import Tile

BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

class PlayerObject(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerObject, self).__init__()
        player_picture_path = os.path.join(ASSET_DIR, "player", "player.png")
        picture = pygame.image.load(player_picture_path)
        self.picture = picture

        # surf from picture by .convert()
        self.surf = picture.convert()

        # rect from surf by .get_rect()
        self.rect = self.surf.get_rect()

        # get screen_width, height from environment
        self.screen_width = int(os.environ.get('SCREEN_WIDTH', 500))
        self.screen_height = int(os.environ.get('SCREEN_HEIGHT', 500))

        # self.player_y_momentum = 0.2
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def move(self):
        pressed_keys = pygame.key.get_pressed()  
        
        x_velocity = 0
        y_velocity = 0

        if pressed_keys[K_LEFT]:
            x_velocity -= 10
        
        if pressed_keys[K_RIGHT]:
            x_velocity += 10

        if pressed_keys[K_UP]:
            y_velocity -= 10
        
        if pressed_keys[K_DOWN]:
            y_velocity += 10

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        if self.rect.y > self.screen_height - self.picture.get_height():
            # self.player_y_momentum = -self.player_y_momentum
            self.rect.top = self.screen_height - self.picture.get_height()
            # self.player_y_momentum = 0
        if self.rect.y < 0:
            self.rect.top = 0
        
        self.rect.x += x_velocity
        self.rect.y += y_velocity


    def check_collison(self, collisoned_tile_rect:Tile):
        if self.rect.bottom >= collisoned_tile_rect.rect.top :
            self.player_y_momentum = 0

