import pygame, os
BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

SCREEN_WIDTH = int(os.environ.get('SCREEN_WIDTH', 500))
SCREEN_HEIGHT = int(os.environ.get('SCREEN_HEIGHT', 500))


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
        
        self.tile_size_y = SCREEN_HEIGHT // len(self.game_map)
        self.tile_size_x = SCREEN_WIDTH // len(self.game_map[0])
        self.dirt_img = pygame.transform.scale(self.dirt_img, (self.tile_size_x, self.tile_size_y))
        self.grass_img = pygame.transform.scale(self.grass_img, (self.tile_size_x, self.tile_size_y))
        self.none_img = pygame.transform.scale(self.none_img, (self.tile_size_x, self.tile_size_y))

    
    def update(self, surf : pygame.Surface):
        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile == 0 :
                    surf.blit(self.none_img, (x * self.tile_size_x, y * self.tile_size_y))
                if tile == 1 :
                    surf.blit(self.grass_img, (x * self.tile_size_x, y * self.tile_size_y))
                if tile == 2 :
                    surf.blit(self.dirt_img, (x * self.tile_size_x, y * self.tile_size_y))
                x += 1
            y += 1
        