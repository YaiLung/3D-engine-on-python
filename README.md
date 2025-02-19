# 3D Engine
## Hello there! I want to introduce a 3d engine made in Python.
### I'll briefly tell you about the project. The project itself includes two main parts: The 3d engine itself and the game on which it is made, the game is an old-generation Doom.
___
# About the Game
## Here's the gameplay:
### Gane have menu list
![ezgif-38471ab3f917aa](https://github.com/user-attachments/assets/060d68a5-75ab-4530-82ca-ee0949b767e1)

### The game has movement and camera rotation mechanics.

![2025-02-20 01-01-02 (online-video-cutter com) (1)](https://github.com/user-attachments/assets/f7d5a94a-0038-4fb5-8fb5-96219094e77e)

### There are also shooting mechanics, enemies and their logic, destruction and animated animations.

![2025-02-20 01-01-02 (online-video-cutter com) (3)](https://github.com/user-attachments/assets/6120159f-790e-4865-861f-437ed80fb8c8)

### Also map and Game lose/Game win

![2025-02-20 01-01-02 (online-video-cutter com) (1)](https://github.com/user-attachments/assets/785557c8-2d41-49df-afd4-812d3b99e42e)
___
# About Engine
## Downloading a project
+ Download the repository and unpack
+ Enable [GostScript](https://www.ghostscript.com/)
+ Download the dependencies(pygame, nympy)
### Great, you can create your own game.
___
# Settings
### The engine uses RayCasting to convert 2d to 3d. You can configure the parameters yourself in the file settings.py
``` python
# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# minimap settings
MINIMAP_SCALE = 5
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)
MAP_SCALE = 2 * MINIMAP_SCALE # 1 -> 12 x 8, 2 -> 24 x 16, 3 -> 36 x 24
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# sprite settings
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# player settings
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 3

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)
```
