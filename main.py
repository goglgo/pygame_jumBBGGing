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

        if self.rect.y > self.screen_height - self.picture.get_height():
            self.player_y_momentum = -self.player_y_momentum
        
        else:
            self.player_y_momentum += 0.2
        
        self.rect.move_ip(0, self.player_y_momentum)


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
        dirt_path = os.path.join(ASSET_DIR, "tiles", "dirt.png")
        grass_path = os.path.join(ASSET_DIR, "tiles", "grass.png")
        
        self.tile_size = 25
        self.dirt_img = pygame.image.load(dirt_path)
        self.grass_img = pygame.image.load(grass_path)
        self.none_img = pygame.Surface((self.tile_size, self.tile_size))
        self.none_img.fill((82, 89, 93))
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

    
    def update(self, surf : pygame.Surface):
        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == 0 :
                    surf.blit(self.none_img, (x * self.tile_size, y * self.tile_size))
                if tile == 1 :
                    surf.blit(self.grass_img, (x * self.tile_size, y * self.tile_size))
                if tile == 2 :
                    surf.blit(self.dirt_img, (x * self.tile_size, y * self.tile_size))
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

    # screen에 흰색을 채웁니다.
    screen.fill((255, 255, 255))
    
    # display에 다른 색을 채웁니다.
    display.fill((82, 89, 93))
    display.blit(Player.surf, Player.rect)
    display.blit(test_sprite.surf, test_sprite.rect)
    
    # display를 screen (0,0) 좌표에 뿌립니다.
    display = pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT))
    Map.update(display)
    
    screen.blit(display, (0, 0))

    Player.update()

    # collide check
    if pygame.sprite.spritecollideany(Player, collide_sprites):
        test_sprite.red_update()
    
    else:
        test_sprite.black_update()

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
