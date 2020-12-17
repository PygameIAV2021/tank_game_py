# Tank Game 
---
My first Game
---
### 1. Description of the project
The player controls a tank and shoot projectiles to destroy enemy tanks around the playfield. The enemy tanks enter from the top of the screen and attempts to destroy the player's base (represented on the screen as a phoenix symbol), as well as the player's tank itself. A level is completed when the player destroys xx enemy tanks, but the game ends if the player's base is destroyed or the player loses all available lives. The player can destroy the base as well, so the player can still lose even after all enemy tanks are destroyed.

The game contain xx maps. Each map contains different types of terrain and obstacles. Examples include brick walls that can be destroyed by having either the player's tank or an enemy tank shoot at them. Beton walls con not be destroyed, patches of water which cannot be crossed by tanks. The enemy tanks come in four different sizes, with the largest one requiring four shots to destroy.

---
### 2. Current status

Level 1 and the map are done.

Static/Immovable elements inserted: wall, beton wall, water, player's staff.

Player tank moves, stays in the map and does not drive out,
objects cannot be driven on.
Shots are implemented for the player tank.
The enemy tank is also implemented movements in the framework of the map.
The control of opposing tanks is radmoic.
        
---
### 3. Description of the map 
the map is structured like this

Description of the numbers in the map:  <br>
        00              is a empty place  <br>
        11              is a brick-wall this can be destroyed with 1 shot  <br>
        21              is a beton-wall this can't be destroyed  <br>
        32              is wather can let a shot through but not drive through, can't destryed  <br>
        ??              is a possible burn point of opponent tanks  <br>
        ??              is a burn point of gamer  <br>
        (91,92,93,94)   is a command point of gamer  <br>
                        if this destryed is GAME OVER <br>
                        if gamer have no more tanks is GAME OVER  <br>
                        the gamer have 3 Lifs = 3 Tanks  <br>
***


### 3. TODO: 

~~19.11 Import graphics for immovable elements~~
~~19.11 Map Class is reday <br>~~
~~26.11 Document changes in the maps  <br>~~
~~26.11 Implement player  <br>~~
~~26.11 turning in the direction of travel tank <br>~~
~~26.11 Player Movements  <br>~~
~~26.11/03.12 implement shots for player <br>~~
~~clear old player position is obsolet ~~
~~03.12 implement oponent tank ~~
03.12 shots from oponent tanks
10.12 Implement object player tank
10.12 Implement stupid boot/ki for oponent tanks 
~~16.12 moving for oponent tank~~
~~16.12 bug fix (by shots, moving) from player tank~~
17.12 code maintenance
---

### 4. Project 
Project is being created in script programming at the Rudolf Diesel Technical School in Nuremberg.

---
### 5. Lizenz 

---

