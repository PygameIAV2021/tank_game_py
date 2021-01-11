# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
#                                     Rudolf-Diesel-Fachschule                                  #
#                                        script programming                                     #
#                                               wit-a                                           #
#                                             Tank Game                                         #
#                                                                                               #                              
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # self.position_oponent_tank_row # # # # # # # # # # # # # # # # # # #                                                                      
#                                                                                               #
#                                       File: my_oponent.py                                     #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random

UP = 00
LEFT = 90
DOWN = 180
RIGHT = 270

FIELDS = 30

class oponent:
    def __init__(self, oponent_tank_direction, position_oponent_tank_row, position_oponent_tank_column, IMAGE_OPONENT_TANK_LEVEL_1):
        self.oponent_tank_direction = oponent_tank_direction
        self.position_oponent_tank_row = position_oponent_tank_row
        self.position_oponent_tank_column = position_oponent_tank_column
        self.IMAGE_OPONENT_TANK_LEVEL_1 = IMAGE_OPONENT_TANK_LEVEL_1

    # Calculate correction factor
    def correction_factor(self, correction_number):
        correction_number = correction_number * self.MULTIPLER
        return correction_number

    # draw oponent tank an sat in the map
    def draw_oponent_tank(self):
        game_window.blit(self.IMAGE_OPONENT_TANK_LEVEL_1, (
        [self.correction_factor(self.self.position_oponent_tank_column) + 1, self.correction_factor(self.position_oponent_tank_row) + 1,
         self.correction_factor(1) - 1, self.correction_factor(1) - 1]))

    def moving_oponent_tank(self, position_oponent_tank_column, position_oponent_tank_row , oponent_tank_direction):
        #print("moving_oponent_tank","direction",self.oponent_tank_direction)
        #print("Bin hier Row:",self.position_oponent_tank_row , "column", self.position_oponent_tank_column)
    # if the tank in the corner they must change direction and call function change direction?. 
    # the chances that it won't stick in the corner are greater....
        if ( self.position_oponent_tank_column == 0 and self.position_oponent_tank_row  == 0 ) and ( 
            self.oponent_tank_direction == UP or self.oponent_tank_direction == LEFT ): # the corner left & up and direction up or left 
                #print("Ecke oben links")
                moving_direction = random.randrange(2, 4, 2)
                change_direction_oponent_tank(self.oponent_tank_direction, moving_direction)
        if ( self.position_oponent_tank_column == (FIELDS - 1) and self.position_oponent_tank_row  == 0 ) and (
            self.oponent_tank_direction == UP or self.oponent_tank_direction == RIGHT ): # the corner right & up and direction up or right
                #print("Ecke oben rechts")
                moving_direction = random.randrange(2, 3, 1)
                change_direction_oponent_tank(self.oponent_tank_direction, moving_direction)
        if ( self.position_oponent_tank_column == 0 and self.position_oponent_tank_row  == (FIELDS - 1) ) and ( 
            self.oponent_tank_direction == DOWN or self.oponent_tank_direction == LEFT ): # the corner down & left and direction down or left
                #print("Ecke unten links")
                moving_direction = random.randrange(1, 4, 3)
                change_direction_oponent_tank(self.oponent_tank_direction, moving_direction)
        if ( self.position_oponent_tank_column == (FIELDS - 1) and self.position_oponent_tank_row  == (FIELDS - 1) ) and (
            self.oponent_tank_direction == DOWN or self.oponent_tank_direction == RIGHT): # the corner down & right and direction down or right 
                #print("Ecke unten rechts")
                moving_direction = random.randrange(1, 3, 2)
                change_direction_oponent_tank(self.oponent_tank_direction, moving_direction)
    # if the place in the front of moving tank direktion not empty or rand of map musst the tank change the direction 180 degree
        if ( self.oponent_tank_direction == UP and self.position_oponent_tank_row  == 0): # direction up and the row is 0 musst the tank turn 
            #print("wand oben")
            change_direction_oponent_tank(self.oponent_tank_direction, 2)
        if ( self.oponent_tank_direction == DOWN and self.position_oponent_tank_row  == ( FIELDS - 1 )): # direction down and the row is 29 musst the tank turn
            #print("wand unten")
            change_direction_oponent_tank(self.oponent_tank_direction, 1)
        if ( self.oponent_tank_direction == LEFT and self.position_oponent_tank_column == 0): # direction left and the row is 0 musst the tank turn
            #print("wand links")
            change_direction_oponent_tank(self.oponent_tank_direction, 4)
        if ( self.oponent_tank_direction == RIGHT and self.position_oponent_tank_column == ( FIELDS - 1 )): # direction right and the row is 29 musst the tank turn
           #print("wand rechts")
            change_direction_oponent_tank(self.oponent_tank_direction, 3)
    # if the place in the tank direction free they can drive in this place 
        if self.oponent_tank_direction == UP:
            if (self.position_oponent_tank_row  > 0) and (
                    current_map[self.position_oponent_tank_row  - 1][self.position_oponent_tank_column] == EMPTY_PLACE_ON_MAP):
                oponent_tank_row -= 1
        if self.oponent_tank_direction == DOWN:
            if (self.position_oponent_tank_row  < FIELDS - 1) and (
                    current_map[self.position_oponent_tank_row  + 1][self.position_oponent_tank_column] == EMPTY_PLACE_ON_MAP):
                oponent_tank_row += 1
        if self.oponent_tank_direction == LEFT:
            if (self.position_oponent_tank_column > 0) and (
                    current_map[self.position_oponent_tank_row ][self.position_oponent_tank_column - 1] == EMPTY_PLACE_ON_MAP):
                oponent_tank_column -= 1
        if self.oponent_tank_direction == RIGHT:
            if (self.position_oponent_tank_column < FIELDS - 1) and (
                    current_map[self.position_oponent_tank_row ][self.position_oponent_tank_column + 1] == EMPTY_PLACE_ON_MAP):
                oponent_tank_column += 1



def change_direction_oponent_tank(self, oponent_tank_direction_fk, moving_direction):
    #print("Drehe mich nach... direction:",oponent_tank_direction_fk,"moving direction:",moving_direction)
    if moving_direction == 1:
        if oponent_tank_direction_fk != UP:
            self.IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (UP - self.oponent_tank_direction))
            self.oponent_tank_direction = UP
    if moving_direction == 2:
        if oponent_tank_direction_fk != DOWN:
            self.IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (DOWN - self.oponent_tank_direction))
            self.oponent_tank_direction = DOWN
    if moving_direction == 3:
        if oponent_tank_direction_fk != LEFT:
            self.IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (LEFT - self.oponent_tank_direction))
            self.oponent_tank_direction = LEFT
    if moving_direction == 4:
        if oponent_tank_direction_fk != RIGHT:
            self.IMAGE_OPONENT_TANK_LEVEL_1 = pygame.transform.rotate(self.IMAGE_OPONENT_TANK_LEVEL_1,
                                                                 (RIGHT - self.oponent_tank_direction))
            self.oponent_tank_direction = RIGHT

def shot_from_oponent(self, oponent_tank_direction, oponent_tank_column, oponent_tank_row):
    # shot from oponent tank
        owner = 2
        shot = Shot(oponent_tank_direction, oponent_tank_column, oponent_tank_row, owner, current_map, game_window, IMAGE_BULLET)
        shot_list.append(shot)

def what_does_the_opponent_want_to_do(self, oponent_tank_column, oponent_tank_row, oponent_tank_direction):
    #print("column:", oponent_tank_column, "row:", oponent_tank_row, "direction:" ,oponent_tank_direction)
    # in order to increase the likelihood of drelosening, I roll the dice from 1 to 10 only with numbers between 1 and 4 the direction will change
    moving_direction = random.randrange(1, 51)
    if moving_direction in range(1, 5):
        self.change_direction_oponent_tank( oponent_tank_direction, moving_direction)
    if moving_direction in range(5, 51 , 2):
        pass
    else:
        #print("bewege dich","richtung:",oponent_tank_direction)
        self.moving_oponent_tank(oponent_tank_column, oponent_tank_row, oponent_tank_direction)