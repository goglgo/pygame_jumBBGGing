import pygame, os
from pygame.locals import *
from .map import Tile

# https://github.com/IIITSERC/SSAD_2015_A3_Group2_7/blob/aabc2b87a18c7fba7d0c63ab46cd6a97ea6613e1/201402087/Player.py

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

        self.player_y_momentum = 0.2
        self.player_x_momentum = 10

        self.right = True
        self.left = True


    def update(self, collisioned_tiles:list[Tile] = None):
        # if collisioned_tiles:
        #     self.rect.x += self.player_x_momentum
        #     for tile in collisioned_tiles:
        #         if self.player_x_momentum > 0:
        #             self.rect.right = tile.rect.left

        #         elif self.player_x_momentum < 0:
        #             self.rect.left = tile.rect.right

        #     self.rect.y += self.player_y_momentum
        #     for tile in collisioned_tiles:

        #         if self.player_y_momentum > 0:
        #             self.rect.bottom = tile.rect.top
        #             self.player_y_momentum = 0

        #         if self.player_y_momentum < 0:
        #             self.rect.top = tile.rect.bottom
            
        # else:
        self.rect.move_ip(self.player_x_momentum, self.player_y_momentum)  

        pressed_keys = pygame.key.get_pressed()

        # self.player_x_momentum = 0
        
        if pressed_keys[K_LEFT] and pressed_keys[K_RIGHT]:
            self.player_x_momentum = 0

        elif pressed_keys[K_LEFT]:
            # self.rect.move_ip(-self.player_x_momentum,0)
            if self.left:
                self.player_x_momentum -= 2
                if self.player_x_momentum < -10:
                    self.player_x_momentum = -10
        
        elif pressed_keys[K_RIGHT]:
            # self.rect.move_ip(self.player_x_momentum,0)
            if self.right:
                self.player_x_momentum += 2
                if self.player_x_momentum > 10:
                    self.player_x_momentum = 10
        else:
            self.player_x_momentum = 0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        if self.rect.y > self.screen_height - self.picture.get_height():
            self.player_y_momentum = 0
        
        else:
            self.player_y_momentum += 0.2

        # self.rect.move_ip(self.player_x_momentum, self.player_y_momentum)  

    def check_collison(self, collision_group:pygame.sprite.Group):
        collisioned_game_tile = pygame.sprite.spritecollide(self, collision_group, False)
        for tile in collisioned_game_tile:
            if self.player_y_momentum > 0:
                self.rect.bottom = tile.rect.top
                self.player_y_momentum = 0
            if self.player_y_momentum < 0:
                self.rect.top = tile.rect.bottom
                self.player_y_momentum = 0

        # self.rect.move_ip(0, self.player_y_momentum)  
        collisioned_game_tile = pygame.sprite.spritecollide(self, collision_group, False)
        for tile in collisioned_game_tile:
            if self.player_x_momentum > 0:
                self.rect.right = tile.rect.left
                self.player_x_momentum = 0 
            if self.player_x_momentum < 0:
                self.rect.left = tile.rect.right
                self.player_x_momentum = 0 
        
        # self.rect.move_ip(self.player_x_momentum, 0)  

        

        # self.rect.move_ip(0, self.player_y_momentum)  

        # for tile in collisoned_tiles:
        #     if self.player_y_momentum > 0:
        #         self.rect.bottom = tile.rect.top

        #     elif self.player_y_momentum < 0:
        #         self.rect.top = tile.rect.bottom
        #     self.player_y_momentum = 0

        # for tile in collisoned_tiles:
        #     if self.player_x_momentum > 0:
        #         self.player_x_momentum = 0
        #         self.rect.right = tile.rect.left
        #         self.right = False
        #         self.left = True
                    
        #         # left
        #     elif self.player_x_momentum < 0:
        #         self.player_x_momentum = 0
        #         self.rect.left = tile.rect.right



            
            
        # if self.rect.left 

