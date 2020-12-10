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

# my Container with Maps
from Map_Container import Map_Container
# SHots 
from my_shot import Shot

# multipler
MULTIPLER = 20

# game fields
FIELDS = 30

# frames per second update game window
FPS = 5

# static game/elements 

IMAGE_BRICK_WALL = pygame.image.load('pic/brick_wall.png')

IMAGE_BETON_WALL= pygame.image.load('pic/beton_wall.png')
IMAGE_WATTER = pygame.image.load('pic/watter.png')

IMAGE_BASE_LE_UP = pygame.image.load('pic/base_le_up.png')
IMAGE_BASE_LE_DOWN = pygame.image.load('pic/base_le_down.png')
IMAGE_BASE_RE_UP = pygame.image.load('pic/base_re_up.png')
IMAGE_BASE_RE_DOWN = pygame.image.load('pic/base_re_down.png')

IMAGE_PLAYER_TANK_LEVEL_1 = pygame.image.load('pic/palyer_tank.png')

IMAGE_GROUND_1 = pygame.image.load('pic/ground_1.png')

IMAGE_BULLET = pygame.image.load('pic/bullet.png')
IMAGE_EXPLOSION = pygame.image.load('pic/explosion.png')


# create a game field
game_window = pygame.display.set_mode((FIELDS * MULTIPLER, FIELDS * MULTIPLER))

# head title of game window
pygame.display.set_caption("Tanks")
game_active = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# colors in game
GRAY  = ( 138, 138, 138)
BLACK = ( 0, 0, 0)
WITHE  = ( 255, 255, 255)
BRICK_COLOR = (143, 38, 0)

# Game Level by start
LEVEL = 1

# curent Game Level
current_map = Map_Container.load_Map(LEVEL)

# background game window
game_window.fill(GRAY)

# Korrekturfaktor berechnen
def correction_factor(correction_number):
    correction_number = correction_number * MULTIPLER
    return correction_number

# draw a game element
# ein pygame.draw und die Farbe übergeben 
def draw_game_element(column, row, element_type):
    if(element_type == 00):
       game_window.blit(IMAGE_GROUND_1, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 11):
       game_window.blit(IMAGE_BRICK_WALL, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 21):
        game_window.blit(IMAGE_BETON_WALL, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 32):
       game_window.blit(IMAGE_WATTER, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 91):
        game_window.blit(IMAGE_BASE_LE_UP, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))  
    if(element_type == 93):
        game_window.blit(IMAGE_BASE_LE_DOWN, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 92):
        game_window.blit(IMAGE_BASE_RE_UP, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 94):
        game_window.blit(IMAGE_BASE_RE_DOWN, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    
def draw_player_tank(postion_player_tank_column, postion_player_tank_row):
    game_window.blit(IMAGE_PLAYER_TANK_LEVEL_1, ([correction_factor(postion_player_tank_column)+1, correction_factor(postion_player_tank_row)+1,correction_factor(1)-1,correction_factor(1)-1]))



       

# default burn poit of player is right oder left side from base
player_column = 5
player_row = 20


# direction of player tank clockwise rotation
# UP    --> 00
# RIGHT --> 90
# DOWN  --> 180
# LEFT  --> 270
player_tank_direction = 00

# rotate of tank in deriction 
def player_tank_rotate(tank ,player_tank_direction):
    tank = pygame.transform.rotate(tank, player_tank_direction)

# Kolisionskontrolle 
def collision_check_of_shot(position_column, position_row):
    if current_map [position_column][position_row] != 00:
        game_window.blit(IMAGE_EXPLOSION , ([correction_factor(position_column)+1, correction_factor(position_row)+1,correction_factor(1)-1,correction_factor(1)-1]))
        current_map[position_column][position_row] = 00

# Liste der Schüsse 
shot_list = []

# main game loop
while game_active:
    # Check whether the user has taken an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_active = False
            print("GAME END BY USER")
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_SPACE]:  # keyboard key space
            owner = 1
            shot = Shot(player_tank_direction, player_column, player_row, owner, current_map, game_window, IMAGE_BULLET)
            shot_list.append(shot)
        if keys[pygame.K_UP]: # keyboard key up arrow
            if player_tank_direction != 00:
                IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1, (00 - player_tank_direction) )
                player_tank_direction = 00
            if ( player_row > 0 ) and ( current_map[player_row - 1][player_column] == 00 ): 
                player_row -= 1
            else:
                player_row = player_row
        if keys[pygame.K_DOWN]:  # keyboard key down arrow
            if player_tank_direction != 180:
                IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1, (180 - player_tank_direction) )
                player_tank_direction = 180
            if ( player_row < FIELDS - 1 ) and ( current_map[player_row + 1][player_column] == 00 ):  
                player_row += 1
            else:
                player_row = player_row
        if keys[pygame.K_LEFT]:  # keyboard key left arrow
            if player_tank_direction != 90:
                IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1, (90 - player_tank_direction) )
                player_tank_direction = 90
            if ( player_column > 0 ) and ( current_map[player_row][player_column - 1] == 00 ):
                player_column -= 1
            else:
                player_column = player_column
            # pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,90)
        if keys[pygame.K_RIGHT]:  # keyboard key rigt arrow
            if player_tank_direction != 270:
                IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1, (270 - player_tank_direction) )
                player_tank_direction = 270
            if ( player_column <  FIELDS - 1 ) and ( current_map[player_row][player_column + 1] == 00 ):
                player_column += 1
            else:
                player_column = player_column


    for column in range(0,FIELDS):
        for row in range(0,FIELDS): 
            element_type = current_map[row][column]
            draw_game_element(column,row,element_type)

    # position by moving
    draw_player_tank(player_column , player_row)


    # shot 
    for shot in shot_list:
        shot.draw()
        if shot.shot_move() == False:
            shot_list.remove(shot)



        collision_check_of_shot(shot.position_column, shot.position_row)
           


    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

pygame.quit()