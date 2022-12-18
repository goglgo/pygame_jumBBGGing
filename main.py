# Simple pygame program
# Import and initialize the pygame library
import pygame, os
from pygame.locals import *

pygame.init()

BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

# Set up clock
clock = pygame.time.Clock()

# Set up the drawing window size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

os.environ['SCREEN_WIDTH'] = str(SCREEN_WIDTH)
os.environ['SCREEN_HEIGHT'] = str(SCREEN_HEIGHT)

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)

display = pygame.Surface((300, 300))


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
        self.picture = picture

        # surf from picture by .convert()
        self.surf = picture.convert()

        # rect from surf by .get_rect()
        self.rect = self.surf.get_rect()

        # get screen_width, height from environment
        self.screen_width = int(os.environ.get('SCREEN_WIDTH', 500))
        self.screen_height = int(os.environ.get('SCREEN_HEIGHT', 500))

        self.player_y_momentum = 0.2
        self.collide = {
            "left":False,
            "right":False,
            "up":False,
            "bottom":False,
        }

    def move_check(self, collison):
        # print(collison.rect)
        self.collide["bottom"] = True
        # print(self.collide["bottom"])

    def update(self):
        pressed_keys = pygame.key.get_pressed()        

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10,0)
        
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10,0)

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        if(self.collide["bottom"] == False):
            if self.rect.y > self.screen_height - self.picture.get_height():
                self.player_y_momentum = -self.player_y_momentum
            
            else:
                self.player_y_momentum += 0.2
        
            self.rect.move_ip(0, self.player_y_momentum)
            # print(self.collide["bottom"])
        else:
            self.rect.move_ip(0,0)

class GameTile(pygame.sprite.Sprite):
    def __init__(self, img_path, img_size_x, img_size_y):
        super(GameTile, self).__init__()
        img = pygame.image.load(img_path).convert()
        self.surf = pygame.transform.scale(img, (img_size_x, img_size_y))
        self.img_size_x = img_size_x
        self.img_size_y = img_size_y
    
    def set_rect(self, x, y):
        self.rect = pygame.Rect(x, y, self.img_size_x, self.img_size_y)
        
        return self


class CollideTest(pygame.sprite.Sprite):
    def __init__(self):
        super(CollideTest, self).__init__()
        self.surf = pygame.Surface((100,100))
        self.surf.fill((255,0,0))
        self.rect = pygame.Rect(100,100,100,50)

    def red_update(self):
        self.surf.fill((255,0,0))

    def black_update(self):
        self.surf.fill((0,0,0))
    

class GameMap(object):
    def __init__(self):
        self.dirt_path = os.path.join(ASSET_DIR, "tiles", "dirt.png")
        self.grass_path = os.path.join(ASSET_DIR, "tiles", "grass.png")

        self.screen_width = int(os.environ.get('SCREEN_WIDTH', 500))
        self.screen_height = int(os.environ.get('SCREEN_HEIGHT', 500))
        self.surf = pygame.Surface((self.screen_width, self.screen_height))
        
        # self.dirt_img = pygame.image.load(dirt_path).convert()
        # self.grass_img = pygame.image.load(grass_path).convert()
        
        self.game_map = [   [0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1],
                            [2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],   ]

        self.tile_size_x = self.screen_width // len(self.game_map)
        self.tile_size_y = self.screen_height // len(self.game_map[0])
        self.none_img = pygame.Surface((self.tile_size_x, self.tile_size_y)).convert()
        self.none_img.fill((82, 89, 93))

        # self.dirt_img = GameTile(dirt_path, self.tile_size_x, self.tile_size_y)
        # self.grass_img = GameTile(grass_path, self.tile_size_x, self.tile_size_y)

        # self.dirt_img = pygame.transform.scale(self.dirt_img, (self.tile_size_x, self.tile_size_y))
        # self.grass_img = pygame.transform.scale(self.grass_img, (self.tile_size_x, self.tile_size_y))

        self.collide_group = pygame.sprite.Group()
    
    def update(self):
        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == 0 :
                    self.surf.blit(self.none_img, (x * self.tile_size_x, y * self.tile_size_y))

                if tile == 1 :
                    grass_img = GameTile(self.grass_path, self.tile_size_x, self.tile_size_y)
                    grass_img.set_rect(x * self.tile_size_x, y * self.tile_size_y)
                    self.surf.blit(grass_img.surf, grass_img.rect)
                    self.collide_group.add(grass_img)
                    
                if tile == 2 :
                    dirt_img = GameTile(self.dirt_path, self.tile_size_x, self.tile_size_y)
                    dirt_img.set_rect(x * self.tile_size_x, y * self.tile_size_y)
                    self.surf.blit(dirt_img.surf, dirt_img.rect)
                x += 1
            y += 1
        




Player = PlayerObject()

Map = GameMap()

test_sprite = CollideTest()

collide_sprites = pygame.sprite.Group()
collide_sprites.add(test_sprite)

EVENT = EventCheck()

while EVENT.running:
    EVENT.check()

    Map.update()
    background = pygame.transform.scale(Map.surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    Player.update()

    background.blit(Player.surf, Player.rect)
    background.blit(test_sprite.surf, test_sprite.rect)
    screen.blit(background, (0, 0))
    
    # collide check
    if pygame.sprite.spritecollideany(Player, collide_sprites):
        test_sprite.red_update()
    
    else:
        test_sprite.black_update()
    
    collide_with_map = pygame.sprite.spritecollideany(Player, Map.collide_group)
    if collide_with_map:
        Player.move_check(collide_with_map)

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
