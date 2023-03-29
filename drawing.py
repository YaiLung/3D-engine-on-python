import pygame
from settings import *
from ray_casting import ray_Casting
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map, player, clock):
        self.sc = sc
        self.sc_map = sc_map
        self.player = player
        self.clock = clock
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_win = pygame.font.Font('font/font.ttf', 100)
        self.textures = {1: pygame.image.load('img/1.png').convert(),
                         2: pygame.image.load('img/wall4.png').convert(),
                         3: pygame.image.load('img/wall5.png').convert(),
                         4: pygame.image.load('img/wall6.png').convert(),
                         'S': pygame.image.load('img/sky2.png').convert()
                         }

    # menu
    self.menu_trigger = True
    self.menu_picture = pygame.image.load('img/bg.jpg').convert()
    # weapon parameters
    self.weapon_base_sprite = pygame.image.load('sprites/weapons/shotgun/base/0.png').convert_alpha()
    self.weapon_shot_animation = deque([pygame.image.load(f'sprites/weapons/shotgun/shot/{i}.png').convert_alpha()
    def backround(self):
        pygame.draw.rect(self.sc, DARKGRAY, (0, 0, width, half_heigth))
        pygame.draw.rect(self.sc, DARKGRAY, (0, half_heigth, width, half_heigth))

    def world(self, player_pos, player_angle):
        ray_Casting(self.sc, player_pos, player_angle, self.texture)
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0,RED)
        self.sc.blit(render, FPS_pos)
    def mini_map (self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math.sin(player.angle)), 2)

        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

