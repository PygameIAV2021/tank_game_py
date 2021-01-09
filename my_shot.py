# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
#                                     Rudolf-Diesel-Fachschule                                  #
#                                        script programming                                     #
#                                               wit-a                                           #
#                                             Tank Game                                         #
#                                                                                               #                              
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                      
#                                                                                               #
#                                       File: shot.py                                  #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Mögliche Richtungen des Panzers
UP = 00
LEFT = 90
DOWN = 180
RIGHT = 270

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
    
   
