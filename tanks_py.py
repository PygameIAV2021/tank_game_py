# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
#                                     Rudolf-Diesel-Fachschule                                  #
#                                        script programming                                     #
#                                               wit-a                                           #
#                                             Tank Game                                         #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                      
#                                                                                               #
#                                         File: tanks_py.py                                     #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

### ### ### ### ### ### ### ### ### ### IMPORTS  ### ### ### ### ### ### ### ### ### 
# Import the pygame library
import pygame, sys, random, time, os, webbrowser
import pygame. freetype
from pygame.locals import *
from os import path 

# my Container with Maps
from Map_Container import Map_Container

# constant variables for Game
import pygame

# inziealisierung von pygame
pygame.init()

# for music
pygame.mixer.init()
### ### ### ### ### ### ### ### ### ### END IMPORTS  ### ### ### ### ### ### ### ### 

#####################################################################################

### ### ### ### ### ### ### ### ### ### SETTINGS ### ### ### ### ### ### ### ### ### 

# multipler
MULTIPLER = 20

# game fields
FIELDS = 30

# frames per second update game window
FPS = 5

# colors in game
GRAY = (138, 138, 138)
BLACK = (0, 0, 0)
# text color in the button
WHITE = (255, 255, 255)
# light for the start button in start menu
RED = (255, 96,104 )
# light for the start button in start menu
GREEN = (51,113,57)
# light shade of the button in start menu 
LIGHT = (170,170,170)  
# dark shade of the button in start menu
DARK = (100,100,100)  
# possible directions of tank and shots

# the possible directions in which a tank can turn ... in degrees
UP = 00
LEFT = 90
DOWN = 180
RIGHT = 270

# MapSymbols 
EMPTY_PLACE_ON_MAP = 00
BRICK_WAL = 11 # brick wall can destroed
BETON_WAL = 21 # beton wall can't destroed
EXPLOSION_ON_BETON_WALL = 17 # beton need light explosion with 3 frames
WATER = 32 # water cannot be driven on but shots go through

# BASE-Player consists of 4 parts
BASE_LE_UP = 91 
BASE_LE_DOWN = 93
BASE_RE_UP = 92
BASE_RE_DOWN = 94

# explosion on this place
EXPLOSION = 7

# payer tank is shown in the map
PLAYER_TANK = 99 

# images for static game/elements 
IMAGE_BRICK_WALL = pygame.image.load('pic/brick_wall.png')
IMAGE_BETON_WALL = pygame.image.load('pic/beton_wall.png')
IMAGE_WATER = pygame.image.load('pic/watter.png')
IMAGE_BASE_LE_UP = pygame.image.load('pic/base_le_up.png')
IMAGE_BASE_LE_DOWN = pygame.image.load('pic/base_le_down.png')
IMAGE_BASE_RE_UP = pygame.image.load('pic/base_re_up.png')
IMAGE_BASE_RE_DOWN = pygame.image.load('pic/base_re_down.png')
IMAGE_GROUND_1 = pygame.image.load('pic/ground_1.png')

# images dynamic game elements
IMAGE_PLAYER_TANK_LEVEL_1 = pygame.image.load('pic/palyer_tank.png')
IMAGE_BULLET = pygame.image.load('pic/bullet.png')
IMAGE_OPONENT_TANK_LEVEL_1 = pygame.image.load('pic/oponent_tank.png')

# sound elements
SOUND_SHOT = pygame.mixer.Sound('sounds/shot.wav')
SOUND_HIT_BRICK = pygame.mixer.Sound('sounds/shot_hit_brick.wav')
SOUND_GAMEOVER = pygame.mixer.Sound('sounds/game_over.wav')
SOUND_HIT_BETTON = pygame.mixer.Sound('sounds/shot_hit_betton.wav')
SOUND_HIT_WATER = pygame.mixer.Sound('sounds/shot_hit_water.wav')
SOUND_KEY_MOVING = pygame.mixer.Sound('sounds/key_moving.wav')
SOUND_ENGINE = pygame.mixer.Sound('sounds/engine_player.wav')
SOUND_GAME_PAUSE = pygame.mixer.Sound('sounds/game_pause.wav')
SOUND_HIT_FROM_OPPONENT = pygame.mixer.Sound('sounds/hit_from_opponent.wav')
SOUND_GAME_OVER_SCREEN = pygame.mixer.Sound('sounds/game_over_screen.wav')
SOUND_OPPONENT_DESTROY = pygame.mixer.Sound('sounds/opponent_hit.mp3')

# explosion images
IMAGE_EXPLOSION_1 = pygame.image.load('dyn_pic/explosion/1.png')
IMAGE_EXPLOSION_2 = pygame.image.load('dyn_pic/explosion/2.png')
IMAGE_EXPLOSION_3 = pygame.image.load('dyn_pic/explosion/3.png')
IMAGE_EXPLOSION_4 = pygame.image.load('dyn_pic/explosion/4.png')
IMAGE_EXPLOSION_5 = pygame.image.load('dyn_pic/explosion/5.png')
IMAGE_EXPLOSION_6 = pygame.image.load('dyn_pic/explosion/6.png')
IMAGE_EXPLOSION_7 = pygame.image.load('dyn_pic/explosion/7.png')

# screen images for pause screen, game end by user GEBU, menu screen
IMAGE_SCREEN_PAUSE = pygame.image.load('pic/pause.jpg')
IMAGE_SCREEN_GEBU = pygame.image.load('pic/game_end_by_user.jpg')
IMAGE_SCREEN_MENU = pygame.image.load('pic/start_screen.jpg')
IMAGE_SCREEN_GAME_OVER = pygame.image.load('pic/game_over.jpg')
IMAGE_SCREEN_WIN_LEVEL = pygame.image.load('pic/level_win.jpg')

# screen resolution for my game
screen_resolution = (1 + FIELDS * MULTIPLER, FIELDS * MULTIPLER)

# surface = game_window
game_window = pygame.display.set_mode(screen_resolution)

# head title of game window
pygame.display.set_caption("Tanks - Game menu")

# set game aktive, pause false, game_end_bu false
game_active = True  # the game is running
pause = False       # when a break is made
game_end_bu = False # game was terminated by user
start_menu = True   # show start menu
game_over = False   # game over screen
win_level = False

# Set screen updates
clock = pygame.time.Clock()

# Game Level by start
LEVEL = 1

# background game window
game_window.fill(BLACK)

# default opponent tank direction
opponent_tank_direction = DOWN

# default player direction at start
player_tank_direction = UP

# default burn point of player is right oder left side from base
player_column = 5
player_row = 20

# default burn point of opponent tank
opponent_tank_column = random.randrange(1, 30, 1)
opponent_tank_row = 1

# opponent counter 
enemy_counter = 0

### ### ### ### ### ### ### ### END SETTINGS AND VARIABLES  ### ### ### ### ### ### ### ### 

############################################################################################

### ### ### ### ### ### ### ### ### ### SETTINGS SCREENS ### ### ### ### ### ### ### ### ###

# show the pause screen 
def show_pause_screen():
    game_window.fill(BLACK)
    game_window.blit(IMAGE_SCREEN_PAUSE , ([1, 1, 50,50]))

# show screen game end by user
def show_game_end_by_user():
    game_window.fill(BLACK)
    game_window.blit(IMAGE_SCREEN_GEBU, ([1, 1, 50,50]))

# show screen game over
def show_screen_game_over():
    global game_window
    game_window.fill(BLACK)
    game_window.blit(IMAGE_SCREEN_GAME_OVER, ([1, 1, 50,50]))

# show screen level win
def show_level_win():
    global game_window
    game_window.fill(BLACK)
    game_window.blit(IMAGE_SCREEN_WIN_LEVEL, ([1, 1, 50,50]))
     
# game end by user
def do_game_end_by_user():
    global game_active
    show_game_end_by_user()
    pygame.display.flip()
    close_game = True
    while close_game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                close_game = False
                game_active = False
                print("GAME END BY USER")

# pause 
def do_pause():
    global game_active
    show_pause_screen()
    pygame.display.flip()
    warte_zeit = True
    while warte_zeit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                do_game_end_by_user()
                warte_zeit = False
                pause = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    SOUND_GAME_PAUSE.stop()
                    warte_zeit = False

# game over
def do_game_over():
    global game_active, game_over   
    SOUND_GAMEOVER.play()
    time.sleep(2)
    game_active = False
    game_over = True 

# level ist win 
def do_level_win():
    global game_active, win_level
    game_active = False
    win_level = True
    show_level_win()

### ### ### ### ### ### ### ### ### ### END SETTINGS SCREENS ### ### ### ### ### ### ### ### ###

### ### ### ### ### ### ### ### ### ### GAME MENU ### ### ### ### ### ### ### ### ###
# Start and menu Screen will show on start of game or press [esc] in the game 
def show_start_menu():

    global start_menu, LEVEL

    # you need to get into the menu at the start if false the game starts
    show_menu = True

    # play menu sound 
    SOUND_GAME_PAUSE.play(-1) 
  
    # stores the width of the  
    # screen into a variable  
    width = game_window.get_width()  
  
    # stores the height of the  
    # screen into a variable  
    height = game_window.get_height()  
  
    # defining a font  
    smallfont = pygame.font.SysFont('Corbel',30)  
  
    # rendering a text written in  
    # this font  
    text_start = smallfont.render('start' , True , WHITE)
    text_readme = smallfont.render('readme on Github' , True , WHITE)
    text_level_1 = smallfont.render('Level 1' , True , WHITE)
    text_level_2 = smallfont.render('Level 2' , True , WHITE)
    text_exit = smallfont.render('exit' , True , WHITE)  
    
    # button size
    button_size_on_width = 300
    button_size_off_width = 270
    while show_menu:  
      
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  

            #checks if a mouse is clicked  
            if event.type == pygame.MOUSEBUTTONDOWN:  
              
        # START BUTTTON - if the mouse is clicked on the button the start the game  
                if width/2 <= mouse[0] <= width/2+140 and height/2-250 <= mouse[1] <= height/2+40-250:
                    SOUND_GAME_PAUSE.stop()
                    show_menu = False
                    game_active = True
        # README BUTTTON -  if the mouse is clicked on the button you can see readme file on github  
                if width/2 <= mouse[0] <= width/2+140 and height/2-200 <= mouse[1] <= height/2+40-200:  
                    webbrowser.open('https://github.com/PygameIAV2021/tank_game_py/blob/master/readme.md')
        # LEVEL-1 BUTTON - if the mouse is clicked on the button you can open the settings blit 
                if width/2 <= mouse[0] <= width/2+140 and height/2-150 <= mouse[1] <= height/2+40-150:  
                    pass
        # LEVEL-2 BUTTON - if the mouse is clicked on the button you can open the settings blit 
                if width/2 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2+40-100:
                    print("level 2")
                    LEVEL = 2
        # SETTINGS BUTTON - if the mouse is clicked on the button you can open the settings blit 
                if width/2 <= mouse[0] <= width/2+140 and height/2+230 <= mouse[1] <= height/2+40+230:
                    sys.exit(0)

        # fills the screen with a color  
        game_window.blit(IMAGE_SCREEN_MENU , ([1, 1, 50,50]))

        # stores the (x,y) coordinates into  
        # the variable as a tuple  
        mouse = pygame.mouse.get_pos() 
        
     # START BUTTON 
        # if mouse is hovered on a button it  
        # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2-250 <= mouse[1] <= height/2+40-250:  
            pygame.draw.rect(game_window,GREEN,[width/2,height/2-250,button_size_on_width,40])  
        else:  
            pygame.draw.rect(game_window,DARK,[width/2,height/2-250,button_size_off_width,40])  
      
        # positin font in the button the text onto button
        game_window.blit(text_start , (width/2+50,height/2-250))
        
    # README BUTTON
        # if mouse is hovered on a button it  
        # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2-200 <= mouse[1] <= height/2+40-200:  
            pygame.draw.rect(game_window,LIGHT,[width/2,height/2-200,button_size_on_width,40])  
          
        else:  
            pygame.draw.rect(game_window,DARK,[width/2,height/2-200,button_size_off_width,40])  

        # positin font in the button the text onto button  
        game_window.blit(text_readme , (width/2+50,height/2-200))
    # LEVEL 1 BUTTON
        # if mouse is hovered on a button it  
        # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2-150 <= mouse[1] <= height/2+40-150:  
            pygame.draw.rect(game_window,LIGHT,[width/2,height/2-150,button_size_on_width,40])  
          
        else:  
            pygame.draw.rect(game_window,DARK,[width/2,height/2-150,button_size_off_width,40])  

        # positin font in the button the text onto button  
        game_window.blit(text_level_1 , (width/2+50,height/2-150))  
    # LEVEL 2 BUTTON
        # if mouse is hovered on a button it  
        # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2+40-100:  
            pygame.draw.rect(game_window,LIGHT,[width/2,height/2-100,button_size_on_width,40])  
          
        else:  
            pygame.draw.rect(game_window,DARK,[width/2,height/2-100,button_size_off_width,40])  

        # positin font in the button the text onto button  
        game_window.blit(text_level_2 , (width/2+50,height/2-100))  

    # EXIT BUTTON
        # if mouse is hovered on a button it  
        # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2+230 <= mouse[1] <= height/2+40+230:  
            pygame.draw.rect(game_window,RED,[width/2,height/2+230,button_size_on_width,40])  
          
        else:  
            pygame.draw.rect(game_window,DARK,[width/2,height/2+230,button_size_off_width,40])  

        # superimposing the text onto our button  
        game_window.blit(text_exit , (width/2+50,height/2+230))

        # updates the frames of the game  
        pygame.display.update()  
### ### ### ### ### ### ### ### ### ### END GAME MENU ### ### ### ### ### ### ### ### ###

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

        SOUND_SHOT.play()

    # the shots fired are drawn here
    def draw(self):
        self.game_window.blit(self.IMAGE_BULLET, ([self.correction_factor(self.position_column)+1, self.correction_factor(self.position_row)+1, self.correction_factor(1)-1, self.correction_factor(1)-1]))

    # the direction of the tank is decisive for firing the shot.
    def shot_move(self):
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
        global enemy_counter
        self.opponent_tank_direction = opponent_tank_direction
        self.opponent_tank_row = opponent_tank_row
        self.opponent_tank_column = opponent_tank_column
        self.IMAGE_OPPONENT_TANK_LEVEL_1 = IMAGE_OPPONENT_TANK_LEVEL_1
        self.id = 100 + enemy_counter
        enemy_counter += 1

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
    # if the tank in the corner they must change direction and call function change direction?. 
    # the chances that it won't stick in the corner are greater....
        old_column = self.opponent_tank_column
        old_row = self.opponent_tank_row
        if ( self.opponent_tank_column == 0 and self.opponent_tank_row  == 0 ) and ( 
            self.opponent_tank_direction == UP or self.opponent_tank_direction == LEFT ): # the corner left & up and direction up or left 
                moving_direction = random.randrange(2, 4, 2)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
        if ( self.opponent_tank_column == (FIELDS - 1) and self.opponent_tank_row  == 0 ) and (
            self.opponent_tank_direction == UP or self.opponent_tank_direction == RIGHT ): # the corner right & up and direction up or right
                moving_direction = random.randrange(2, 3, 1)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
        if ( self.opponent_tank_column == 0 and self.opponent_tank_row  == (FIELDS - 1) ) and ( 
            self.opponent_tank_direction == DOWN or self.opponent_tank_direction == LEFT ): # the corner down & left and direction down or left
                moving_direction = random.randrange(1, 4, 3)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
        if ( self.opponent_tank_column == (FIELDS - 1) and self.opponent_tank_row  == (FIELDS - 1) ) and (
            self.opponent_tank_direction == DOWN or self.opponent_tank_direction == RIGHT): # the corner down & right and direction down or right 
                moving_direction = random.randrange(1, 3, 2)
                self.change_direction_opponent_tank(self.opponent_tank_direction, moving_direction)
    # if the place in the front of moving tank direktion not empty or rand of map musst the tank change the direction 180 degree
        if ( self.opponent_tank_direction == UP and self.opponent_tank_row  == 0): # direction up and the row is 0 musst the tank turn 
            self.change_direction_opponent_tank(self.opponent_tank_direction, 2)
        if ( self.opponent_tank_direction == DOWN and self.opponent_tank_row  == ( FIELDS - 1 )): # direction down and the row is 29 musst the tank turn
            self.change_direction_opponent_tank(self.opponent_tank_direction, 1)
        if ( self.opponent_tank_direction == LEFT and self.opponent_tank_column == 0): # direction left and the row is 0 musst the tank turn
            self.change_direction_opponent_tank(self.opponent_tank_direction, 4)
        if ( self.opponent_tank_direction == RIGHT and self.opponent_tank_column == ( FIELDS - 1 )): # direction right and the row is 29 musst the tank turn
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
        current_map[old_row][old_column] = EMPTY_PLACE_ON_MAP
        current_map[self.opponent_tank_row][self.opponent_tank_column] = self.id

    def change_direction_opponent_tank(self, opponent_tank_direction_fk, moving_direction):
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

    def shot_from_opponent(self):
        # shot from opponent tank
            owner = self.id
            shot = Shot(self.opponent_tank_direction, self.opponent_tank_column, self.opponent_tank_row, owner, current_map, game_window, IMAGE_BULLET)
            shot_list.append(shot)

    def what_does_the_opponent_want_to_do(self, opponent_tank_column, opponent_tank_row, opponent_tank_direction):
        # in order to increase the likelihood of drelosening, I roll the dice from 1 to 10 only with numbers between 1 and 4 the direction will change
        moving_direction = random.randrange(1, 81)
        if moving_direction in range(1, 5):
            self.change_direction_opponent_tank( opponent_tank_direction, moving_direction)
        if moving_direction in range(5,81,3):
            self.moving_opponent_tank(opponent_tank_column, opponent_tank_row, opponent_tank_direction)
        if moving_direction in range(10,25,5):
           self.shot_from_opponent()

# Calculate correction factor for coordinates
def correction_factor(correction_number):
    correction_number = correction_number * MULTIPLER
    return correction_number

# draw static game element
def draw_game_element(column, row, element_type):
    # EXPLOSION
    if (element_type == 7 or element_type == 20):
        game_window.blit(IMAGE_EXPLOSION_7, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == 6 or element_type == 19):
        game_window.blit(IMAGE_EXPLOSION_6, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == 5 or element_type == 18):
        game_window.blit(IMAGE_EXPLOSION_5, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == 4 or element_type == 17):
        game_window.blit(IMAGE_EXPLOSION_4, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == 3 or element_type == 16):
        game_window.blit(IMAGE_EXPLOSION_3, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == 2 or element_type == 15):
        game_window.blit(IMAGE_EXPLOSION_2, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    if (element_type == 1 or element_type == 14):
        game_window.blit(IMAGE_EXPLOSION_1, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    # EMPTY PLACE ON MAP
    if (element_type == EMPTY_PLACE_ON_MAP):
        game_window.blit(IMAGE_GROUND_1, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    # BRIK WALL
    if (element_type == BRICK_WAL):
        game_window.blit(IMAGE_BRICK_WALL, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    # BETON WALL
    if (element_type == BETON_WAL):
        game_window.blit(IMAGE_BETON_WALL, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    # WATER
    if (element_type == WATER):
        game_window.blit(IMAGE_WATER, (
        [correction_factor(column) + 1, correction_factor(row) + 1, correction_factor(1) - 1,
         correction_factor(1) - 1]))
    # BSE FROM PLAYER BY 4 PIX
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
    # OPPONENT TANKS
         correction_factor(1) - 1]))
    if element_type >= 100:
        tank = getOpponentById(element_type)
        game_window.blit(tank.IMAGE_OPPONENT_TANK_LEVEL_1, (
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

# explosion list
explosion_list = []

# brauche es um aus der shotliste den richtigen Opponenten zu bestimmen 
def getOpponentById(id):
    for opponent in opponent_list: # type: Opponent
        if id == opponent.id:
            return opponent
    return None


# insert opponent depending on the map
def add_opponent_tank_to_level(number_of_opponents):
    for count in range(number_of_opponents):
        opponent_tank_column = random.randrange(1, 30, 1)
        opponent_tank_row = random.randrange(1,2,1)
        opponent = Opponent(opponent_tank_direction, opponent_tank_row, opponent_tank_column, IMAGE_OPONENT_TANK_LEVEL_1 )
        opponent_list.append(opponent)

# rotate of tank in deriction
def player_tank_rotate(tank, player_tank_direction):
    tank = pygame.transform.rotate(tank, player_tank_direction)

# Collision control with various dynamic and static elements
def collision_check_of_shot(shot):
    global shot_list, current_map, game_window, EMPTY_PLACE_ON_MAP, game_active, opponent_list
    if current_map[shot.position_row][shot.position_column] != EMPTY_PLACE_ON_MAP:
        if ((current_map[shot.position_row][shot.position_column] == BASE_LE_DOWN) or 
                (current_map[shot.position_row][shot.position_column] == BASE_LE_UP) or 
                    (current_map[shot.position_row][shot.position_column] == BASE_RE_DOWN) or 
                        (current_map[shot.position_row][shot.position_column] == BASE_RE_UP)):
            current_map[shot.position_row][shot.position_column] = EMPTY_PLACE_ON_MAP
            shot_list.remove(shot)
            print("GAME OVER")
            time.sleep(1)
            do_game_over()
        if current_map[shot.position_row][shot.position_column] == BETON_WAL:
            current_map[shot.position_row][shot.position_column] = EXPLOSION_ON_BETON_WALL
            shot_list.remove(shot)
            SOUND_HIT_BETTON.play()
        if current_map[shot.position_row][shot.position_column] == WATER:
            SOUND_HIT_WATER.play()
        if current_map[shot.position_row][shot.position_column] == BRICK_WAL:
            current_map[shot.position_row][shot.position_column] = EMPTY_PLACE_ON_MAP
            current_map[shot.position_row][shot.position_column] = 1
            shot_list.remove(shot)
            SOUND_HIT_BRICK.play()
        if current_map[shot.position_row][shot.position_column] >= 100:
            if shot.owner == 1:
                oppent_tank_id = current_map[shot.position_row][shot.position_column]
                for o in opponent_list:
                    if o.id == oppent_tank_id:
                        opponent_list.remove(o)
                        break
                shot_list.remove(shot)
                SOUND_OPPONENT_DESTROY.play()
                current_map[shot.position_row][shot.position_column] = 1
        if current_map[shot.position_row][shot.position_column] == PLAYER_TANK:
            if shot.owner != 1:
                SOUND_HIT_FROM_OPPONENT.play()
                shot_list.remove(shot)
                print("getrofen ")
                time.sleep(1)
                do_game_over()

# Start wiht menu screen 
if start_menu:
    show_start_menu()

# depending on the level, the number of opponents differs 
# Opponents in The currenty map
    # Level1  = 2 oponents
    # Level2  = 4 oponents
if LEVEL == 1:
    number_of_opponents = 2
    add_opponent_tank_to_level(number_of_opponents)
if LEVEL == 2:
    number_of_opponents = 4
    add_opponent_tank_to_level(number_of_opponents)

# curent Game Level
current_map = Map_Container.load_Map(LEVEL)

# main game loop
while game_active:
    if pause:
        do_pause()
        pause = False
    if game_end_bu:
        do_game_end_by_user()
        game_end_bu = True
    # Check whether the user has taken an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            do_game_end_by_user()
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_SPACE]:  # keyboard key space
        owner = 1
        shot = Shot(player_tank_direction, player_column, player_row, owner, current_map, game_window, IMAGE_BULLET)
        shot_list.append(shot)
    if keys[pygame.K_2]:  # keyboard key 1 for pause 
        print("2  gedrückt Pause")
        do_pause()
    if keys[pygame.K_UP]:  # keyboard key up arrow
        if player_tank_direction != UP:  # UP = 00*
            # rotation of the icon player tank
            IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,
                                                                (UP - player_tank_direction))
            player_tank_direction = UP
        if (player_row > 0) and (current_map[player_row - 1][player_column] == EMPTY_PLACE_ON_MAP):
            # check whether the tank is still in the field and the space in front of the tank is empty
            SOUND_KEY_MOVING.play()
            current_map[player_row][player_column] = EMPTY_PLACE_ON_MAP
            current_map[player_row - 1][player_column] = PLAYER_TANK
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
            SOUND_KEY_MOVING.play()
            current_map[player_row][player_column] = EMPTY_PLACE_ON_MAP
            current_map[player_row + 1][player_column] = PLAYER_TANK
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
            SOUND_KEY_MOVING.play()
            current_map[player_row][player_column] = EMPTY_PLACE_ON_MAP
            current_map[player_row][player_column - 1] = PLAYER_TANK
            player_column -= 1
        else:
            player_column = player_column
    if keys[pygame.K_RIGHT]:  # keyboard key rigt arrow
        if player_tank_direction != RIGHT:  # RIGHT == 270*
            # rotation of the icon player tank
            IMAGE_PLAYER_TANK_LEVEL_1 = pygame.transform.rotate(IMAGE_PLAYER_TANK_LEVEL_1,
                                                                (RIGHT - player_tank_direction))
            player_tank_direction = RIGHT
        if (player_column < FIELDS - 1) and (current_map[player_row][player_column + 1] == EMPTY_PLACE_ON_MAP):
            # check whether the tank is still in the field and the space in front of the tank is empty
            SOUND_KEY_MOVING.play()
            current_map[player_row][player_column] = EMPTY_PLACE_ON_MAP
            current_map[player_row][player_column + 1] = PLAYER_TANK
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

    # draw static game elements
    for column in range(0, FIELDS):
        for row in range(0, FIELDS):
            if current_map[row][column] in range(1,8):
                current_map[row][column] += 1
            element_type = current_map[row][column]
            draw_game_element(column, row, element_type)
            if current_map[row][column] == 7:
                current_map[row][column] = EMPTY_PLACE_ON_MAP   # TODO2 use a function for this 
            if current_map[row][column] in range(14,21):
                current_map[row][column] += 1
            element_type = current_map[row][column]
            draw_game_element(column, row, element_type)
            if current_map[row][column] == 20:
                current_map[row][column] = BETON_WAL

    for shot in shot_list:
        shot.draw()

    # position by moving
    draw_player_tank(player_column, player_row)

    # draw opponent tank on map
    for opponent in opponent_list:
        opponent.what_does_the_opponent_want_to_do(opponent_tank_column, opponent_tank_row, opponent_tank_direction)
        #opponent.draw_opponent_tank(opponent_tank_column, opponent_tank_row)

    # if opponetn list empty on this level your win this level
    if len(opponent_list) <= 0:
        do_level_win()
        
    # refresh game window
    pygame.display.flip()

    # define refresh times
    clock.tick(FPS)

# if the tank is destroyed by player us or the base is destroyed
while game_over:
    show_screen_game_over()
    pygame.display.flip()
    SOUND_GAME_OVER_SCREEN.play(1)
   
while win_level:
    do_level_win()
    pygame.display.flip()
    SOUND_GAME_OVER_SCREEN.play(1)

pygame.quit()
