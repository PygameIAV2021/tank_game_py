# Tank Game 
---
My first Game
---
### 1. Description of the project
The player controls a tank and shoot projectiles to destroy enemy tanks around the playfield. The enemy tanks enter from the top of the screen and attempts to destroy the player's base (represented on the screen as a phoenix symbol), as well as the player's tank itself. A level is completed when the player destroys all enemy tanks, but the game ends if the player's base is destroyed or the player hit. The player can destroy the base as well, so the player can still lose even after all enemy tanks are destroyed.

The game contain 2 maps. Each map contains different types of terrain and obstacles. Examples include brick walls that can be destroyed by having either the player's tank or an enemy tank shoot at them. Beton walls con not be destroyed, patches of water which cannot be crossed by tanks. 
different sounds are played when the shot touches water or concrete or wall.

---
### 2. Current status and screenshots
![level1:](https://www.bilder-upload.eu/thumb/1871d7-1611564145.jpg)
![level2t:](https://www.bilder-upload.eu/thumb/f04ed6-1611563806.jpg)
![menu:](https://www.bilder-upload.eu/thumb/5b6d4c-1611563776.jpg)
![pause_screen:](https://www.bilder-upload.eu/thumb/79d6b7-1611563838.jpg)

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
        (91,92,93,94)   is a command point of gamer  <br>
                        if this destryed is GAME OVER <br>
                        if gamer have no more tanks is GAME OVER  <br>
                        the gamer have 3 Lifs = 3 Tanks  <br>
        99              is the player tank
        <100 + id       are opponent tanks
***
### 4. control of player tank
The tank is controlled with arrow keys

Moving with arrow key UP,DOWN,LEFT,RIGHT
Shot with space key 
pause is created with button 2
with ESC you can leave the game

### 5. Start menu
The player is greeted with a start screen.
The player can select the level and display the readme file or end the game immediately.

### 6. TODO: 

~~19.11 Import graphics for immovable elements~~
~~19.11 Map Class is reday <br>~~
~~26.11 Document changes in the maps  <br>~~
~~26.11 Implement player  <br>~~
~~26.11 turning in the direction of travel tank <br>~~
~~26.11 Player Movements  <br>~~
~~26.11/03.12 implement shots for player <br>~~
~~clear old player position is obsolet<br>~~
~~03.12 implement oponent tank<br>~~
~~03.12 shots from oponent tanks<br>~~
~~10.12 Implement object player tank<br>~~
~~10.12 Implement stupid boot for oponent tanks <br>~~
~~16.12 moving for oponent tank<br>~~
~~16.12 bug fix (by shots, moving) from player tank<br>~~
14.01.21 ~~code maintenance~~
~~opponents burning points flexible~~
~~implement sounds~~
~~Add opponents to a list~~
~~Shots for all opponents correct implement~~
21.01.21
~~code maintenance~~
~~colisions control implement for tanks~~
~~Pause bildschirm, Game Over bildschirm~~

### 7. Erweiterungen:
HP bar mit aktueller anzeige der gesundheits Punkte für den Player.
Save und Loading funktion.
Other types of tanks for the player and opponents would also be possible.

---

### 8. Project 
Project is being created in script programming at the Rudolf Diesel Technical School in Nuremberg.

---

