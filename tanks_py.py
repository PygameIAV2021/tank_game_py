# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
#                                     Rudolf-Diesel-Fachschule                                  #
#                                        script programming                                     #
#                                               wit-a                                           #
#                                             Tank Game                                         #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                      
#                                                                                               #                                                                                         #
#                                         File: tanks_py.py                                     #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import the pygame library
import pygame, sys, time, random
from pygame.locals import *

# import random numbers
import random

# my Container with Maps
from Map_Container import Map_Container

# SHots 
from my_shot import Shot

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

# create a game field
game_window = pygame.display.set_mode((FIELDS * MULTIPLER, FIELDS * MULTIPLER))

# head title of game window
pygame.display.set_caption("Tanks")

# game is active
game_active = True

# Set screen updates
clock = pygame.time.Clock()

# Game Level by start
LEVEL = 1

# curent Game Level
current_map = Map_Container.load_Map(LEVEL)

# background game window
game_window.fill(GRAY)

# default oponent tank direction
oponent_tank_direction = DOWN

# Calculate correction factor
def correction_factor(correction_number):
    correction_number = correction_number * MULTIPLER
    return correction_number

# draw static game element
def draw_game_element(column, row, element_type):
    if (element_type == EMPTY_PLACE_ON_MAP):
        game_window.blit(IMAGE_GROUND_1, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == BRICK_WAL):
        game_window.blit(IMAGE_BRICK_WALL, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == BETON_WAL):
        game_window.blit(IMAGE_BETON_WALL, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == WATER):
        game_window.blit(IMAGE_WATER, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == BASE_LE_UP):
        game_window.blit(IMAGE_BASE_LE_UP, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == BASE_LE_DOWN):
        game_window.blit(IMAGE_BASE_LE_DOWN, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == BASE_RE_UP):
        game_window.blit(IMAGE_BASE_RE_UP, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == BASE_RE_DOWN):
        game_window.blit(IMAGE_BASE_RE_DOWN, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))

# draw player tank
def draw_player_tank(postion_player_tank_column, postion_player_tank_row):
    game_window.blit(IMAGE_PLAYER_TANK_LEVEL_1, (
    [correction_factor(postion_player_tank_column) + 1, correction_factor(postion_player_tank_row) + 1,
     correction_factor(1) - 1, correction_factor(1) - 1]))

# draw oponent tank
def draw_oponent_tank(position_oponent_tank_column, position_oponent_tank_row):
    global IMAGE_OPONENT_TANK_LEVEL_1
    #current_map[position_oponent_tank_column][position_oponent_tank_row] = 77
    game_window.blit(IMAGE_OPONENT_TANK_LEVEL_1, (
    [correction_factor(position_oponent_tank_column) + 1, correction_factor(position_oponent_tank_row) + 1,
     correction_factor(1) - 1, correction_factor(1) - 1]))

def moving_oponent_tank(oponent_tank_column_fk, oponent_tank_row_fk, oponent_tank_direction):
    #print("moving_oponent_tank","direction",oponent_tank_direction)
    global IMAGE_OPONENT_TANK_LEVEL_1, current_map, oponent_tank_column, oponent_tank_row
    if oponent_tank_direction == UP:
        if (oponent_tank_row_fk > 0) and (
                current_map[oponent_tank_row_fk - 1][oponent_tank_column_fk] == EMPTY_PLACE_ON_MAP):
            oponent_tank_row -= 1
    if oponent_tank_direction == DOWN:
        print("Bin hier Row:",oponent_tank_row_fk, "column", oponent_tank_column_fk)
        if (oponent_tank_row_fk < FIELDS - 1) and (
                current_map[oponent_tank_row_fk + 1][oponent_tank_column_fk] == EMPTY_PLACE_ON_MAP):
            oponent_tank_row += 1
    if oponent_tank_direction == LEFT:
        if (oponent_tank_column_fk > 0) and (
                current_map[oponent_tank_row_fk][oponent_tank_column_fk - 1] == EMPTY_PLACE_ON_MAP):
            oponent_tank_column -= 1
    if oponent_tank_direction == RIGHT:
        if (oponent_tank_column_fk < FIELDS - 1) and (
                current_map[oponent_tank_row_fk][oponent_tank_column_fk + 1] == EMPTY_PLACE_ON_MAP):
            oponent_tank_column += 1

def change_direction_oponent_tank( oponent_tank_direction_fk, moving_direction):
    #print("moving_oponent_tank","direction",oponent_tank_direction,"moving direction",moving_direction)
    global IMAGE_OPONENT_TANK_LEVEL_1, current_map, oponent_tank_direction
    if moving_direction == 1:
        if oponent_tank_direction_fk != UP:
            IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (UP - oponent_tank_direction))
            oponent_tank_direction = UP
    if moving_direction == 2:
        if oponent_tank_direction_fk != DOWN:
            IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (DOWN - oponent_tank_direction))
            oponent_tank_direction = DOWN
    if moving_direction == 3:
        if oponent_tank_direction_fk != LEFT:
            IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (LEFT - oponent_tank_direction))
            oponent_tank_direction = LEFT
    if moving_direction == 4:
        if oponent_tank_direction_fk != RIGHT:
            IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (RIGHT - oponent_tank_direction))
            oponent_tank_direction = RIGHT

def what_does_the_opponent_want_to_do(oponent_tank_column, oponent_tank_row, oponent_tank_direction):
    # in order to increase the likelihood of drelosening, I roll the dice from 1 to 10 only with numbers between 1 and 4 the direction will change
    moving_direction = random.randrange(1, 51)
    if moving_direction in range(1, 5):
        change_direction_oponent_tank( oponent_tank_direction, moving_direction)
    else:
        #print("bewege dich","richtung:",oponent_tank_direction)
        moving_oponent_tank(oponent_tank_column, oponent_tank_row, oponent_tank_direction)

# default/burn settings for player tank
# default player direction at start
player_tank_direction = UP

# default burn point of player is right oder left side from base
player_column = 5
player_row = 20

# default burn point of oponent tank
oponent_tank_column = 2
oponent_tank_row = 2

# List of shots
shot_list = []

# rotate of tank in deriction
def player_tank_rotate(tank, player_tank_direction):
    tank = pygame.transform.rotate(tank, player_tank_direction)

# Collision control
def collision_check_of_shot(shot):
    global shot_list, current_map, game_window, EMPTY_PLACE_ON_MAP
    if current_map[shot.position_row][shot.position_column] != EMPTY_PLACE_ON_MAP:
        game_window.blit(IMAGE_EXPLOSION, (
        [correction_factor(shot.position_column) + 1, correction_factor(shot.position_row) + 1,
         correction_factor(1) - 1, correction_factor(1) - 1]))
        current_map[shot.position_row][shot.position_column] = EMPTY_PLACE_ON_MAP
        shot_list.remove(shot)
        print("pos of shot (collision): ", shot.position_column, shot.position_row)

# main game loop
while game_active:
    # Check whether the user has taken an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_active = False
            print("GAME END BY USER")
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_SPACE]:  # keyboard key space
        owner = 1
        shot = Shot(player_tank_direction, player_column, player_row, owner, current_map, game_window, IMAGE_BULLET)
        shot_list.append(shot)
        print("Shotliste:", shot_list)
    if keys[pygame.K_UP]:  # keyboard key up arrow
        if player_tank_direction != UP:  # UP = 00*
            # rotation of the icon player tank
            IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,
                                                                (UP - player_tank_direction))
            player_tank_direction = UP
        if (player_row > 0) and (current_map[player_row - 1][player_column] == EMPTY_PLACE_ON_MAP):
            # check whether the tank is still in the field and the space in front of the tank is empty
            player_row -= 1
        else:
            player_row = player_row
    if keys[pygame.K_DOWN]:  # keyboard key down arrow
        if player_tank_direction != DOWN:  # DOWN = 180*
            # rotation of the icon player tank
            IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,
                                                                (DOWN - player_tank_direction))
            player_tank_direction = DOWN
        if (player_row < FIELDS - 1) and (current_map[player_row + 1][player_column] == EMPTY_PLACE_ON_MAP):
            # check whether the tank is still in the field and the space in front of the tank is empty
            player_row += 1
        else:
            player_row = player_row
    if keys[pygame.K_LEFT]:  # keyboard key left arrow
        if player_tank_direction != LEFT:  # LEFT = 90*
            # rotation of the icon player tank
            IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,
                                                                (LEFT - player_tank_direction))
            player_tank_direction = LEFT
        if (player_column > 0) and (current_map[player_row][player_column - 1] == EMPTY_PLACE_ON_MAP):
            # check whether the tank is still in the field and the space in front of the tank is empty
            player_column -= 1
        else:
            player_column = player_column
        # pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,90)
    if keys[pygame.K_RIGHT]:  # keyboard key rigt arrow
        if player_tank_direction != RIGHT:  # RIGHT == 270*
            # rotation of the icon player tank
            IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,
                                                                (RIGHT - player_tank_direction))
            player_tank_direction = RIGHT
        if (player_column < FIELDS - 1) and (current_map[player_row][player_column + 1] == EMPTY_PLACE_ON_MAP):
            # check whether the tank is still in the field and the space in front of the tank is empty
            player_column += 1
        else:
            player_column = player_column

    # shot
    for shot in shot_list:

        if shot.shot_move() == False:
            # when the bullet leaves the playing field it should be removed from the list
            shot_list.remove(shot)
        else:
            # in all other cases a collision check takes place
            collision_check_of_shot(shot)

    # draw dynamic game elements
    for column in range(0, FIELDS):
        for row in range(0, FIELDS):
            element_type = current_map[row][column]
            draw_game_element(column, row, element_type)

    for shot in shot_list:
        shot.draw()

    # position by moving
    draw_player_tank(player_column, player_row)

    # draw oponent tank on map
    what_does_the_opponent_want_to_do(oponent_tank_column, oponent_tank_row, oponent_tank_direction)
    draw_oponent_tank(oponent_tank_column, oponent_tank_row)

    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

pygame.quit()