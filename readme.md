# Tank Game 
---
### 1. Description of the project
The player controls a tank and shoot projectiles to destroy enemy tanks around the playfield. The enemy tanks enter from the top of the screen and attempts to destroy the player's base (represented on the screen as a phoenix symbol), as well as the player's tank itself. A level is completed when the player destroys xx enemy tanks, but the game ends if the player's base is destroyed or the player loses all available lives. The player can destroy the base as well, so the player can still lose even after all enemy tanks are destroyed.

The game contain xx maps. Each map contains different types of terrain and obstacles. Examples include brick walls that can be destroyed by having either the player's tank or an enemy tank shoot at them. Beton walls con not be destroyed, patches of water which cannot be crossed by tanks. The enemy tanks come in four different sizes, with the largest one requiring four shots to destroy.

---
### 2. Current status

Level 1 and the map are done.
Static/Immovable elements inserted: wall, beton wall, water, player's staff.
        
---
### 3. Description of the map 
the map is structured like this

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
***


### 3. TODO: 
19.11 Import graphics for immovable elements, Map Class is reday 
26.11 Document changes in the maps
26.11 Implement player
11/26 Player Movements
implement shots

---
---
### 4. Project 
Project is being created in script programming at the Rudolf Diesel Technical School in Nuremberg.
---



