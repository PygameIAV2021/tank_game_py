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

# import all constant variables
from constant_variables.py import *

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
game_window.fill(BLACK)

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
        #game_window.blit(IMAGE_EXPLOSION, ([correction_factor(shot.position_column) + 1, correction_factor(shot.position_row) + 1,correction_factor(1) - 1, correction_factor(1) - 1]))
        current_map[shot.position_row][shot.position_column] = EMPTY_PLACE_ON_MAP
        shot_list.remove(shot)
        print("owner:", shot.owner, "pos of shot (collision): ", shot.position_column, shot.position_row)

# main game loop
while game_active:
    # Check whether the user has taken an event
    for event in pygame.event.get():
        # hey down ??? obsoled 
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_active = False
            print("GAME END BY USER")
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_SPACE]:  # keyboard key space
        owner = 1
        shot = Shot(player_tank_direction, player_column, player_row, owner, current_map, game_window, IMAGE_BULLET)
        shot_list.append(shot)
        #print("Shotliste:", shot_list)
    if keys[pygame.K_1]:  # keyboard key 1 for test shot 
        print("1 gedrückt test oponent shot")
        shot_from_oponent(oponent_tank_direction, oponent_tank_column, oponent_tank_row)
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


# TODO:
# 1. BUG Column 0 no shot 