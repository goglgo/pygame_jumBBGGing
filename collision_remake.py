import pygame, sys
# setup pygame/window #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Physics Explanation')
screen = pygame.display.set_mode((500,500),0,32)

# player = pygame.Rect(100,100,40,80)



class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Tile, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        self.surf.fill((255,0,0))
        self.image = self.surf
        self.rect.move_ip(x, y)

# tiles = [pygame.Rect(200,350,50,50),pygame.Rect(260,320,50,50)]
tiles_group = pygame.sprite.Group()

tiles_group.add(Tile(200, 350))
tiles_group.add(Tile(260, 320))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.fill((255, 255, 255))

        self.x_velocity = 0
        self.y_velocity = 0

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.x_acc = 0

    def check_input_key(self)->None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.right = True
                if event.key == K_LEFT:
                    self.left = True
                if event.key == K_DOWN:
                    self.down = True
                if event.key == K_UP:
                    self.up = True
                    
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.right = False
                    self.x_acc = 0
                if event.key == K_LEFT:
                    self.left = False
                if event.key == K_DOWN:
                    self.down = False
                if event.key == K_UP:
                    self.up = False
    
    def move(self, movement=None):
        self.check_input_key()
        self.x_velocity = 0
        self.y_velocity = 0

        if self.right == True:
            # self.x_acc += 0.2
            # print(self.x_acc)
            self.x_velocity += 5 + self.x_acc
        if self.left == True:
            self.x_velocity -= 5
        if self.up == True:
            self.y_velocity -= 5
        if self.down == True:
            self.y_velocity += 5

        self.rect.y += self.y_velocity
        # collision recheck after x move completed.(tile.rect.right or left)
        collisions = pygame.sprite.spritecollide(self, tiles_group, False)
        for tile in collisions:
            if self.y_velocity > 0:
                self.rect.bottom = tile.rect.top
                self.y_velocity = 0
            if self.y_velocity < 0:
                self.rect.top = tile.rect.bottom
                self.y_velocity = 0

        # collision check after x moved
        self.rect.x += self.x_velocity # right move
        collisions = pygame.sprite.spritecollide(self, tiles_group, False)
        for tile in collisions:
            if self.x_velocity > 0:
                self.rect.right = tile.rect.left
                self.x_velocity = 0
            if self.x_velocity < 0:
                self.rect.left = tile.rect.right
                self.x_velocity = 0


    
player = Player()

# loop #
while True:
    
    screen.fill((0,0,0))
    player.move()
    tiles_group.draw(screen)
    screen.blit(player.surf, player.rect)

    pygame.display.update()
    mainClock.tick(60)