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
#from my_shot import Shot

# constant variables for Game
import pygame

# multipler
MULTIPLER = 20

# game fields
FIELDS = 30

# frames per second update game window
FPS = 5

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
game_window.fill(BLACK)

# default opponent tank direction
opponent_tank_direction = DOWN

# default/burn settings for player tank
# default player direction at start
player_tank_direction = UP

# default burn point of player is right oder left side from base
player_column = 5
player_row = 20

# default burn point of opponent tank
opponent_tank_column = 2
opponent_tank_row = 2

class Shot:
    def __init__(self, player_direction, player_column, player_row, owner, current_map, game_window, IMAGE_BULLET ):
        self.shot_direction = player_direction
        self.position_column = player_column
        self.position_row = player_row
        self.owner = owner
        self.current_map  = current_map 
        self.game_window = game_window
        self.IMAGE_BULLET = IMAGE_BULLET
        self.MULTIPLER = 20

    # the shots fired are drawn here
    def draw(self):
        self.game_window.blit(self.IMAGE_BULLET, ([self.correction_factor(self.position_column)+1, self.correction_factor(self.position_row)+1, self.correction_factor(1)-1, self.correction_factor(1)-1]))

    # the direction of the tank is decisive for firing the shot.
    def shot_move(self):
        print("shot is hier", self.position_column, self.position_row)
        if self.shot_direction == UP:
                self.position_row -= 1
        if self.shot_direction == LEFT:
                self.position_column -= 1
        if self.shot_direction == DOWN:
                self.position_row += 1
        if self.shot_direction == RIGHT:
                self.position_column += 1
        # when the bullet leaves the playing field it should be removed from the list
        if (self.position_column >= 30 or self.position_column <= 0) or (self.position_row >= 30 or self.position_row <= 0):
            return False

    # Calculate correction factor
    def correction_factor(self, correction_number):
        correction_number = correction_number * self.MULTIPLER
        return correction_number

class Opponent:
    def __init__(self, opponent_tank_direction, opponent_tank_row, opponent_tank_column, IMAGE_OPPONENT_TANK_LEVEL_1):
        self.opponent_tank_direction = opponent_tank_direction
        self.opponent_tank_row = opponent_tank_row
        self.opponent_tank_column = opponent_tank_column
        self.IMAGE_OPPONENT_TANK_LEVEL_1 = IMAGE_OPPONENT_TANK_LEVEL_1

    # Calculate correction factor
    def correction_factor(self, correction_number):
        correction_number = correction_number * MULTIPLER
        return correction_number

    # draw opponent tank an sat in the map
    def draw_opponent_tank(self, opponent_tank_row, opponent_tank_column):
        game_window.blit(self.IMAGE_OPPONENT_TANK_LEVEL_1, (
        [self.correction_factor(self.opponent_tank_column) + 1, self.correction_factor(self.opponent_tank_row) + 1,
         self.correction_factor(1) - 1, self.correction_factor(1) - 1]))

    def moving_opponent_tank(self, opponent_tank_column, opponent_tank_row , opponent_tank_direction):
        print("moving_opponent_tank")
    # if the tank in the corner they must change direction and call function change direction?. 
    # the chances that it won't stick in the corner are greater....
        if ( self.opponent_tank_column == 0 and self.opponent_tank_row  == 0 ) and ( 
            self.opponent_tank_direction == UP or self.opponent_tank_direction == LEFT ): # the corner left & up and direction up or left 
                #print("Ecke oben links")
                moving_direction = random.randrange(2, 4, 2)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
        if ( self.opponent_tank_column == (FIELDS - 1) and self.opponent_tank_row  == 0 ) and (
            self.opponent_tank_direction == UP or self.opponent_tank_direction == RIGHT ): # the corner right & up and direction up or right
                #print("Ecke oben rechts")
                moving_direction = random.randrange(2, 3, 1)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
        if ( self.opponent_tank_column == 0 and self.opponent_tank_row  == (FIELDS - 1) ) and ( 
            self.opponent_tank_direction == DOWN or self.opponent_tank_direction == LEFT ): # the corner down & left and direction down or left
                #print("Ecke unten links")
                moving_direction = random.randrange(1, 4, 3)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
        if ( self.opponent_tank_column == (FIELDS - 1) and self.opponent_tank_row  == (FIELDS - 1) ) and (
            self.opponent_tank_direction == DOWN or self.opponent_tank_direction == RIGHT): # the corner down & right and direction down or right 
                #print("Ecke unten rechts")
                moving_direction = random.randrange(1, 3, 2)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
    # if the place in the front of moving tank direktion not empty or rand of map musst the tank change the direction 180 degree
        if ( self.opponent_tank_direction == UP and self.opponent_tank_row  == 0): # direction up and the row is 0 musst the tank turn 
            #print("wand oben")
            self.change_direction_opponent_tank(self.opponent_tank_direction, 2)
        if ( self.opponent_tank_direction == DOWN and self.opponent_tank_row  == ( FIELDS - 1 )): # direction down and the row is 29 musst the tank turn
            #print("wand unten")
            self.change_direction_opponent_tank(self.opponent_tank_direction, 1)
        if ( self.opponent_tank_direction == LEFT and self.opponent_tank_column == 0): # direction left and the row is 0 musst the tank turn
            #print("wand links")
            self.change_direction_opponent_tank(self.opponent_tank_direction, 4)
        if ( self.opponent_tank_direction == RIGHT and self.opponent_tank_column == ( FIELDS - 1 )): # direction right and the row is 29 musst the tank turn
           #print("wand rechts")
            self.change_direction_opponent_tank(self.opponent_tank_direction, 3)
    # if the place in the tank direction free they can drive in this place 
        if self.opponent_tank_direction == UP:
            if (self.opponent_tank_row  > 0) and (
                    current_map[self.opponent_tank_row  - 1][self.opponent_tank_column] == EMPTY_PLACE_ON_MAP):
                self.opponent_tank_row -= 1
        if self.opponent_tank_direction == DOWN:
            if (self.opponent_tank_row  < FIELDS - 1) and (
                    current_map[self.opponent_tank_row  + 1][self.opponent_tank_column] == EMPTY_PLACE_ON_MAP):
                self.opponent_tank_row += 1
        if self.opponent_tank_direction == LEFT:
            if (self.opponent_tank_column > 0) and (
                    current_map[self.opponent_tank_row ][self.opponent_tank_column - 1] == EMPTY_PLACE_ON_MAP):
                self.opponent_tank_column -= 1
        if self.opponent_tank_direction == RIGHT:
            if (self.opponent_tank_column < FIELDS - 1) and (
                    current_map[self.opponent_tank_row ][self.opponent_tank_column + 1] == EMPTY_PLACE_ON_MAP):
                self.opponent_tank_column += 1

    def change_direction_opponent_tank(self, opponent_tank_direction_fk, moving_direction):
        #print("Drehe mich nach... direction:",opponent_tank_direction_fk,"moving direction:",moving_direction)
        if moving_direction == 1:
            if opponent_tank_direction_fk != UP:
                self.IMAGE_OPPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPPONENT_TANK_LEVEL_1,
                                                                     (UP - self.opponent_tank_direction))
                self.opponent_tank_direction = UP
        if moving_direction == 2:
            if opponent_tank_direction_fk != DOWN:
                self.IMAGE_OPPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPPONENT_TANK_LEVEL_1,
                                                                     (DOWN - self.opponent_tank_direction))
                self.opponent_tank_direction = DOWN
        if moving_direction == 3:
            if opponent_tank_direction_fk != LEFT:
                self.IMAGE_OPPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPPONENT_TANK_LEVEL_1,
                                                                     (LEFT - self.opponent_tank_direction))
                self.opponent_tank_direction = LEFT
        if moving_direction == 4:
            if opponent_tank_direction_fk != RIGHT:
                self.IMAGE_OPPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPPONENT_TANK_LEVEL_1,
                                                                     (RIGHT - self.opponent_tank_direction))
                self.opponent_tank_direction = RIGHT

    def shot_from_opponent(self, opponent_tank_direction, opponent_tank_column, opponent_tank_row):
        # shot from opponent tank
            owner = 2
            shot = Shot(self.opponent_tank_direction, self.opponent_tank_column, self.opponent_tank_row, owner, current_map, game_window, IMAGE_BULLET)
            shot_list.append(shot)

    def what_does_the_opponent_want_to_do(self, opponent_tank_column, opponent_tank_row, opponent_tank_direction):
        #print("column:", opponent_tank_column, "row:", opponent_tank_row, "direction:" ,opponent_tank_direction)
        # in order to increase the likelihood of drelosening, I roll the dice from 1 to 10 only with numbers between 1 and 4 the direction will change
        moving_direction = random.randrange(1, 51)
        if moving_direction in range(1, 5):
            self.change_direction_opponent_tank( opponent_tank_direction, moving_direction)
        if moving_direction in range(5,51,2):
            pass
        else:
            #print("bewege dich","richtung:",opponent_tank_direction)
            self.moving_opponent_tank(opponent_tank_column, opponent_tank_row, opponent_tank_direction)

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

# List of shots
shot_list = []

# opponent list
opponent_list = []

opponent = Opponent(opponent_tank_direction, opponent_tank_row, opponent_tank_column, IMAGE_OPONENT_TANK_LEVEL_1 )
opponent2 = Opponent(opponent_tank_direction, opponent_tank_row, opponent_tank_column, IMAGE_OPONENT_TANK_LEVEL_1 )

opponent_list.append(opponent)
opponent_list.append(opponent2)

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
        print("1 gedrückt test opponent shot")
        opponent.shot_from_opponent(opponent_tank_direction, opponent_tank_column, opponent_tank_row)
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

    # draw opponent tank on map

    opponent.what_does_the_opponent_want_to_do(opponent_tank_column, opponent_tank_row, opponent_tank_direction)
    opponent.draw_opponent_tank(opponent_tank_column, opponent_tank_row)
    opponent2.what_does_the_opponent_want_to_do(opponent_tank_column, opponent_tank_row, opponent_tank_direction)
    opponent2.draw_opponent_tank(opponent_tank_column, opponent_tank_row)
    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

pygame.quit()