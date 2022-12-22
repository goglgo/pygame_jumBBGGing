import pygame, os
from pygame.locals import *
from .map import Tile

BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

class PlayerObject(pygame.sprite.Sprite):
    def __init__(self, collision_group:dict[pygame.sprite.Group]):
        super(PlayerObject, self).__init__()
        player_picture_path = os.path.join(ASSET_DIR, "player", "player.png")
        picture = pygame.image.load(player_picture_path)
        self.picture = picture

        # surf from picture by .convert()
        self.surf = picture.convert()
        self.surf.set_colorkey((255,255,255))
        self.image = self.surf

        # rect from surf by .get_rect()
        self.rect = self.surf.get_rect()

        # get screen_width, height from environment
        self.screen_width = int(os.environ.get('SCREEN_WIDTH', 500))
        self.screen_height = int(os.environ.get('SCREEN_HEIGHT', 500))

        # self.player_y_momentum = 0.2
        self.right = False
        self.left = False
        # self.up = False
        # self.down = False
        self.y_acc = 0
        self.x_acc = 0

        self.x_velocity = 0
        self.y_velocity = 0

        self.collision_group = collision_group

    def jump(self):
        # self.rect.y += 1
        # self.rect.y -= 1
        self.y_velocity -= 10

    def update(self):
        pressed_keys = pygame.key.get_pressed()  
        
        self.x_velocity = 0
        self.y_velocity = 0

        if pressed_keys[K_LEFT]:
            self.x_velocity -= 5
        
        if pressed_keys[K_RIGHT]:
            self.x_velocity += 5
        
        if pressed_keys[K_SPACE]:
            self.jump()

        # if pressed_keys[K_UP]:
        #     self.y_velocity -= 10
        #     self.x_acc += 0.15
        #     if self.x_acc > 10 :
        #         self.x_acc = 10
        
        # if pressed_keys[K_DOWN]:
        #     self.y_velocity += 10

        if self.rect.left < 0:
            self.rect.left = 0

        # if self.rect.right > self.screen_width:
        #     self.rect.right = self.screen_width

        # if self.rect.y > self.screen_height - self.picture.get_height():
        #     self.rect.top = self.screen_height - self.picture.get_height()
            
        if self.rect.y < 0:
            self.rect.top = 0

        self.y_acc += 0.15
        self.y_velocity += 5 + self.y_acc

        # # when left
        # if self.x_velocity < 0:
        #     self.x_velocity += self.x_acc
        
        # # when right
        # elif self.x_velocity > 0:
        #     self.x_velocity -= self.x_acc

        self.rect.x += self.x_velocity
        self._check_collision_x(self.x_velocity, self.collision_group["map"])

        self.rect.y += self.y_velocity
        self._check_collision_y(self.y_velocity, self.collision_group["map"])
        

    def _check_collision_x(self, x_velocity, collision_group, is_Destroy=False):
        # check for map sprites collisions.
        collisions = pygame.sprite.spritecollide(self, collision_group, is_Destroy)
        for tile in collisions:
            # x velocity 가 0보다 클 때 :: 오른쪽으로 갈 때
            if x_velocity > 0 :
                # 플레이어의 오른쪽은 충될된 타일의 왼쪽과 같게
                self.rect.right = tile.rect.left

            # x velocity 가 0보다 작을 때 :: 왼쪽으로 갈 때
            if x_velocity < 0 :
                # 플레이어의 왼쪽은 충될된 타일의 오른쪽과 같게
                self.rect.left = tile.rect.right



    def _check_collision_y(self, y_velocity, collision_group, is_Destroy=False):
        # check for map sprites collisions.
        collisions = pygame.sprite.spritecollide(self, collision_group, is_Destroy)
        for tile in collisions:
            # y velocity 가 0보다 클 때 :: 아래쪽으로 떨어질 때
            if y_velocity > 0 :
                # 플레이어의 아래쪽은 충될된 타일의 윗쪽과 같게
                self.rect.bottom = tile.rect.top
                self.y_acc = 0 
                self.x_acc = 0

            # y velocity 가 0보다 작을 때 :: 윗 쪽으로 갈 대
            if y_velocity < 0 :
                self.rect.top = tile.rect.bottom
                self.y_acc = 0
                self.x_acc = 0 
