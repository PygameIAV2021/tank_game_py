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
    if(element_type == 1):
       game_window.blit(IMAGE_BRICK_WALL, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
    if(element_type == 2):
        game_window.blit(IMAGE_BETON_WALL, ([correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1]))
        # pygame.draw.rect(game_window, WITHE, [correction_factor(column)+1, correction_factor(row)+1,correction_factor(1)-1,correction_factor(1)-1])

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

    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

pygame.quit()