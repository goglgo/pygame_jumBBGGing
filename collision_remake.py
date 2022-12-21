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
    
    def move(self, movement:list):
        self.rect.x += movement[0] # right move
        # collisions = collision_test(rect,tiles)
        collisions = pygame.sprite.spritecollide(self, tiles_group, False)
        for tile in collisions:
            if movement[0] > 0:
                self.rect.right = tile.rect.left
            if movement[0] < 0:
                self.rect.left = tile.rect.right
        self.rect.y += movement[1]
        # collisions = collision_test(rect,tiles)
        collisions = pygame.sprite.spritecollide(self, tiles_group, False)
        for tile in collisions:
            if movement[1] > 0:
                self.rect.bottom = tile.rect.top
            if movement[1] < 0:
                self.rect.top = tile.rect.bottom


# def collision_test(rect,tiles):
#     collisions = []
#     for tile in tiles:
#         if rect.colliderect(tile):
#             collisions.append(tile)
#     return collisions

# def move(rect,movement,tiles): # movement = [5,2]
#     rect.x += movement[0] # right move
#     collisions = collision_test(rect,tiles)
#     for tile in collisions:
#         if movement[0] > 0:
#             rect.right = tile.left
#         if movement[0] < 0:
#             rect.left = tile.right
#     rect.y += movement[1]
#     collisions = collision_test(rect,tiles)
#     for tile in collisions:
#         if movement[1] > 0:
#             rect.bottom = tile.top
#         if movement[1] < 0:
#             rect.top = tile.bottom
#     return rect

right = False
left = False
up = False
down = False
    
player = Player()

# loop #
while True:
    
    # clear display #
    screen.fill((0,0,0))

    movement = [0,0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -= 5
    if up == True:
        movement[1] -= 5
    if down == True:
        movement[1] += 5

    # player = move(player,movement,tiles)
    player.move(movement)
    tiles_group.draw(screen)
    screen.blit(player.surf, player.rect)

    # pygame.draw.rect(screen,(255,255,255),player)

    # for tile in tiles:
    #     pygame.draw.rect(screen,(255,0,0),tile)
    
    # event handling #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_DOWN:
                down = True
            if event.key == K_UP:
                up = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_UP:
                up = False
    
    # update display #
    pygame.display.update()
    mainClock.tick(60)