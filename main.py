# Simple pygame program
# Import and initialize the pygame library
import pygame, os

BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

# Set up the drawing window size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


from pygame.locals import *
from modules.map import *
from modules.player import *

pygame.init()



# Set up clock
clock = pygame.time.Clock()


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


class CollideTest(pygame.sprite.Sprite):
    def __init__(self):
        super(CollideTest, self).__init__()
        self.surf = pygame.Surface((100,100))
        self.surf.fill((255,0,0))
        self.rect = pygame.Rect(100,100,100,50)
    
    def resize(self, size:tuple):
        pygame.transform.scale(self.surf, size)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(100, 80)

    def red_update(self):
        self.surf.fill((255,0,0))

    def black_update(self):
        self.surf.fill((0,0,0))
    


Player = PlayerObject()

Map = GameMap()

test_sprite = CollideTest()

collide_sprites = pygame.sprite.Group()
collide_sprites.add(test_sprite)

EVENT = EventCheck()
collisions_group = {
    "map" : Map.collision_group,
    "test": collide_sprites
}

while EVENT.running:
    EVENT.check()

    # screen에 흰색을 채웁니다.
    screen.fill((255, 255, 255))
    
    # display에 다른 색을 채웁니다.
    display.fill((82, 89, 93))
    Map.update(display)
    
    display.blit(Player.surf, Player.rect)
    display.blit(test_sprite.surf, test_sprite.rect)
    screen.blit(display, (0, 0))
    
    display = pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # test_sprite.resize((SCREEN_WIDTH, SCREEN_HEIGHT))

    # if pygame.sprite.spritecollideany(Player, collide_sprites):
    #     test_sprite.red_update()
    # else :
    #     test_sprite.black_update()

    Player.move(collisions_group)

    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
