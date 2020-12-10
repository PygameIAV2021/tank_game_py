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


    # hier werden die abgegebenen Schüße gezeichnet.
    def draw(self):
        self.game_window.blit(self.IMAGE_BULLET, ([self.correction_factor(self.position_column)+1, self.correction_factor(self.position_row)+1, self.correction_factor(1)-1, self.correction_factor(1)-1]))

    # für die abgabe des Schusses ist die Richtung von Tank entscheident.
    def shot_move(self):
        if self.shot_direction == 00:
            self.position_row -= 1
        if self.shot_direction == 90:
            self.position_column -= 1
        if self.shot_direction == 180:
            self.position_row += 1
        if self.shot_direction == 270:
            self.position_column += 1
        if self.position_row > 31 or self.position_row <= 0 or self.position_column > 31 or self.position_column <= 0:
            return False


    def correction_factor(self, correction_number):
        correction_number = correction_number * self.MULTIPLER
        return correction_number
    
   
