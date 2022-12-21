import pygame, os
BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

SCREEN_WIDTH = int(os.environ.get('SCREEN_WIDTH', 500))
SCREEN_HEIGHT = int(os.environ.get('SCREEN_HEIGHT', 500))

class Tile(pygame.sprite.Sprite):
    def __init__(self, img: pygame.Surface, x, y, w, h):
        super(Tile, self).__init__()
        self.surf = img.convert()
        self.image = self.surf
        self.rect = pygame.Rect(x, y, w, h)

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
                            [1,1,1,1,0,0,0,0,1,1,1,1],
                            [2,2,2,2,0,0,0,0,2,2,2,2],
                            [2,2,2,2,1,1,1,1,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2],   ]
        
        self.tile_size_y = SCREEN_HEIGHT // len(self.game_map)
        self.tile_size_x = SCREEN_WIDTH // len(self.game_map[0])
        self.dirt_img = pygame.transform.scale(self.dirt_img, (self.tile_size_x, self.tile_size_y))
        self.grass_img = pygame.transform.scale(self.grass_img, (self.tile_size_x, self.tile_size_y))
        self.none_img = pygame.transform.scale(self.none_img, (self.tile_size_x, self.tile_size_y))

        self.grass_img.set_colorkey((255,255,255))
        
        self.collision_group = pygame.sprite.Group()

        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                # if tile == 0 :
                    # surf.blit(self.none_img, (x * self.tile_size_x, y * self.tile_size_y))
                if tile == 1 :
                    vx = x * self.tile_size_x
                    vy = y * self.tile_size_y
                    w =  self.tile_size_x
                    h = self.tile_size_y
                    grass = Tile(self.grass_img, vx, vy, w, h)
                    self.collision_group.add(grass)

                if tile == 2 :
                    vx = x * self.tile_size_x
                    vy = y * self.tile_size_y
                    w =  self.tile_size_x
                    h = self.tile_size_y
                    dirt = Tile(self.dirt_img, vx, vy, w, h)
                    self.collision_group.add(dirt)
                x += 1
            y += 1
    
    def update(self, surf : pygame.Surface):
        self.collision_group.draw(surf)

        