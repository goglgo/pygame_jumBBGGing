import pygame, os
BASE_DIR = os.getcwd()
ASSET_DIR = os.path.join(BASE_DIR, "assets")

SCREEN_WIDTH = int(os.environ.get('SCREEN_WIDTH', 500))
SCREEN_HEIGHT = int(os.environ.get('SCREEN_HEIGHT', 500))

# https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

class Tile(pygame.sprite.Sprite):
    def __init__(self, img: pygame.Surface, x, y, w, h):
        super(Tile, self).__init__()
        self.surf = img.convert()
        self.image = self.surf
        self.rect = pygame.Rect(x, y, w, h)

class GameMap(object):
    def __init__(self, file_path=None):
        dirt_path = os.path.join(ASSET_DIR, "tiles", "dirt.png")
        grass_path = os.path.join(ASSET_DIR, "tiles", "grass.png")
        
        self.tile_size = int(os.environ.get('TILE_SIZE', 32))
        self.dirt_img = pygame.image.load(dirt_path)
        self.grass_img = pygame.image.load(grass_path)
        self.none_img = pygame.Surface((self.tile_size, self.tile_size))
        self.none_img.fill((82, 89, 93))
        self.scroll = [0, 0]

        if file_path is None:
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
        else:    
            self.game_map = self.load(file_path)
        
        TILE_SIZE = self.tile_size
        # self.tile_size_y = TILE_SIZE
        # self.tile_size_x = TILE_SIZE

        self.dirt_img = pygame.transform.scale(self.dirt_img, (TILE_SIZE, TILE_SIZE))
        self.grass_img = pygame.transform.scale(self.grass_img, (TILE_SIZE, TILE_SIZE))
        self.none_img = pygame.transform.scale(self.none_img, (TILE_SIZE, TILE_SIZE))

        self.grass_img.set_colorkey((255,255,255))
        
        self.collision_group = pygame.sprite.Group()

        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                # if tile == 0 :
                    # surf.blit(self.none_img, (x * self.tile_size_x, y * self.tile_size_y))
                if tile == 1 :
                    vx = x * self.tile_size
                    vy = y * self.tile_size
                    w =  self.tile_size
                    h = self.tile_size
                    grass = Tile(self.grass_img, vx, vy, w, h)
                    self.collision_group.add(grass)

                if tile == 2 :
                    vx = x * self.tile_size
                    vy = y * self.tile_size
                    w =  self.tile_size
                    h = self.tile_size
                    dirt = Tile(self.dirt_img, vx, vy, w, h)
                    self.collision_group.add(dirt)
                x += 1
            y += 1

    def load(self, file_path:str):
        f = open(file_path, 'r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            res = list(row)
            res = [ eval(i) for i in res ]
            game_map.append(res)
        return game_map


    def update(self, surf):
        self.collision_group.draw(surf)
        # pass
        # for e in self.collision_group:
        #     surf.blit(e.image, camera.apply(e))

    @property
    def total_width(self):
        return len(self.game_map[0])*self.tile_size

    @property
    def total_height(self):
        return len(self.game_map)*self.tile_size

