# constant variables for Game
import pygame

# multipler
MULTIPLER = 20

# game fields
FIELDS = 30

# frames per second update game window
FPS = 10

# colors in game
GRAY = (138, 138, 138)
BLACK = (0, 0, 0)
WITHE = (255, 255, 255)
BRICK_COLOR = (143, 38, 0)

# possible directions of tank and shots
UP = 00
LEFT = 90
DOWN = 180
RIGHT = 270

# MapSymbols
EMPTY_PLACE_ON_MAP = 00
BRICK_WAL = 11
BETON_WAL = 21
WATER = 32
BASE_LE_UP = 91
BASE_LE_DOWN = 93
BASE_RE_UP = 92
BASE_RE_DOWN = 94

# static game/elements 
IMAGE_BRICK_WALL = pygame.image.load('pic/brick_wall.png')
IMAGE_BETON_WALL = pygame.image.load('pic/beton_wall.png')
IMAGE_WATER = pygame.image.load('pic/watter.png')
IMAGE_BASE_LE_UP = pygame.image.load('pic/base_le_up.png')
IMAGE_BASE_LE_DOWN = pygame.image.load('pic/base_le_down.png')
IMAGE_BASE_RE_UP = pygame.image.load('pic/base_re_up.png')
IMAGE_BASE_RE_DOWN = pygame.image.load('pic/base_re_down.png')
IMAGE_GROUND_1 = pygame.image.load('pic/ground_1.png')

# dynamic game elements
IMAGE_PLAYER_TANK_LEVEL_1 = pygame.image.load('pic/palyer_tank.png')
IMAGE_BULLET = pygame.image.load('pic/bullet.png')
IMAGE_EXPLOSION = pygame.image.load('pic/explosion.png')
IMAGE_OPONENT_TANK_LEVEL_1 = pygame.image.load('pic/oponent_tank.png')