# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                               #
#                                     Rudolf-Diesel-Fachschule                                  #
#                                        script programming                                     #
#                                               wit-a                                           #
#                                             Tank Game                                         #
#                                                                                               #                              
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                                                                      
#                                                                                               #
#                                       File: Map_Container.py                                  #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Map_Container:
    """ 
        Map_Container contain start levels and 
    """
    @staticmethod
    def load_Map(level):
        """ 
        return load_Map the level
        
        level_x is the level definiton 

        Description of the numbers in the map:
        00              is a empty place
        11              is a brick-wall this can be destroyed with 1 shot
        21              is a beton-wall this can't be destroyed
        32              is wather can let a shot through but not drive through, can't destryed
        
        ??              is a possible burn point of opponent tanks
        ??              is a burn point of gamer 
        (91,92,93,94)   is a command point of gamer 
                        if this destryed is GAME OVER
                        if gamer have no more tanks is GAME OVER
                        the gamer have 3 Lifs = 3 Tanks
        """
        return Map_Container.maps[level-1]

    level_1 = [ 
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,11 ,0,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,11,11,11,21,11,11,21,11,11,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,32,11,32,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,32,21,32,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,32,11,32,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,21,21,21,21,21,21,21,21,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,11,11,11,11,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,11,91,92,11,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,11,93,94,11,00,00,00,00,00,00,00,00,00,00,00,00,00,]
    ]
    level_2 = [ 
            [00,20,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,20,00,00,11,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,11 ,0,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],

            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,00,00,00,00,11,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,],
            [00,00,00,00,11,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,11,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],

            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,11,11,11,11,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,11,91,92,11,00,00,00,00,00,00,00,00,00,00,00,00,00,],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,11,93,94,11,00,00,00,00,00,00,00,00,00,00,00,00,00,]
]
    maps=[level_1,level_2]