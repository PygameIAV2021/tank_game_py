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

# multipler
MULTIPLER = 20

# game fields
FIELDS = 30

# frames per second update game window
FPS = 60

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
    
def draw_player_tank(column, row):
    game_window.blit(IMAGE_PLAYER_TANK_LEVEL_1, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))

def clear_old_position_of_player_tank(clumn, row):
    game_window.blit(IMAGE_GROUND_1, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))

# default burn poit of player is right oder left side from base
player_column = 5
player_row = 20

# old position after moving tank 
old_player_coumn = 0
old_player_row = 0

# print bricks in dame
for column in range(0,FIELDS):
    for row in range(0,FIELDS):
        if current_map[row][column] != 0:
            element_type = current_map[row][column]
            draw_game_element(column,row,element_type)

# main game loop
while game_active:
    # Check whether the user has taken an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_active = False
            print("GAME END BY USER")
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
           old_player_row = player_row
           player_row -= 1
        if keys[pygame.K_DOWN]:
            old_player_row = player_row
            player_row += 1
        if keys[pygame.K_LEFT]:
           old_player_coumn = player_column
           player_column -= 1
        if keys[pygame.K_RIGHT]:
            old_player_coumn = player_column
            player_column += 1
            
    # game Logic

    # draw the player tank and cler old position by moving
    draw_player_tank(player_column, player_row)
    clear_old_position_of_player_tank(old_player_coumn, old_player_row)


    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

pygame.quit()