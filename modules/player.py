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

        self.player_y_momentum = 0.2
        self.player_x_momentum = 10

        self.movement = {
            "right" : False,
            "left" : False,
            "up" : False,
            "down" : False
        }

    def update(self):
        pressed_keys = pygame.key.get_pressed()      
        self.rect.move_ip(self.player_x_momentum, self.player_y_momentum)  

        # self.player_x_momentum = 0
        if pressed_keys[K_LEFT] and pressed_keys[K_RIGHT]:
            self.player_x_momentum = 0

        elif pressed_keys[K_LEFT]:
            # self.rect.move_ip(-self.player_x_momentum,0)
            self.player_x_momentum -= 2
            if self.player_x_momentum < -6:
                self.player_x_momentum = -6        
        
        elif pressed_keys[K_RIGHT]:
            # self.rect.move_ip(self.player_x_momentum,0)
            self.player_x_momentum += 2
            if self.player_x_momentum > 6:
                self.player_x_momentum = 6
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

        

    def check_collison(self, collisoned_tiles:list[Tile]):
        # if self.rect.bottom >= collisoned_tiles[0].rect.top :
        #     self.player_y_momentum = 0

        # for tile in collisoned_tiles:
        #     left_distance = self.rect.left - tile.rect.right
        #     right_distance = tile.rect.left - self.rect.right

        #     if self.movement["right"] == True:
        #         right_distance = tile.rect.left - self.rect.right
        #         height_distance = abs(tile.rect.centery - self.rect.centery)
        #         # print(height_distance)
        #         if right_distance < 10 and height_distance < 10:
        #             self.rect.right = tile.rect.left
        #             break
        #             # print(111)
            
        #     if self.movement["left"] == True:
        #         left_distance = self.rect.left - tile.rect.right
        #         height_distance = abs(tile.rect.centery - self.rect.centery)
        #         # print(height_distance)
        #         if left_distance < 10 and height_distance < 10:
        #             self.rect.left = tile.rect.right
        #             break
            
        #     if self.rect.bottom >= tile.rect.top:
        #         self.player_y_momentum = 0
        #         self.rect.bottom = tile.rect.top

        for tile in collisoned_tiles:
        
            if self.player_y_momentum > 0 :
                if self.player_x_momentum == 0:
                    self.rect.bottom = tile.rect.top
                self.player_y_momentum = 0
            
            # elif self.player_y_momentum < 0:
            #     self.rect.top = tile.rect.bottom
            #     self.player_y_momentum = - self.player_y_momentum
            # self.rect.move_ip(0, self.player_y_momentum)

        # for tile in collisoned_tiles:
            # when go to left
            if self.player_x_momentum < 0:
                self.player_x_momentum = 0    
                # print("go left", self.player_x_momentum)
                # self.player_x_momentum = 0
            
            # when go to right
            elif self.player_x_momentum > 0:
                self.player_x_momentum = 0   
                self.rect.right = tile.rect.left
                # print("go right", self.player_x_momentum)
                # self.player_x_momentum = 0
            # self.rect.move_ip(self.player_x_momentum, 0)
            
            
        # if self.rect.left 

