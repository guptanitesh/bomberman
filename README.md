BOMBERMAN
=========

A command line colorized  BOMBERMAN game based on non Pygame and ncurses implemenation. The game is implemented in python3 and  OOP Principles like Inheritance, Polymorphism, 
Encapsulation and Modularity are followed.

## Running the game 
Before running the code, run the following command in the terminal.
``` sudo -H pip3 install termcolor ```

Now the game can be run by the following command in the terminal. 
``` python3 main.py ```

## Classes
The game contains several classes each of which represents an object in the game. These are as follows:-
* board - Class to implement the main playing area i.e, the board for the game along with the Walls and also has method to print it.
* game - Class to implement main processing for the game.
* brick - Class to implement bricks which can be destroyed by the explosion of bombs.
* person - Parent class for the non various objects present in the game.
* bomberman - Class to implement the bomberman which will be operated by the user.
* enemy - Class to implement the enemies of the game which will move in pseudo random motion. Enemies with different speed according to level.
* bomb - Class to implement the bombs that will be planted by the bomberman.

#### board
	It defines main playing area i.e., the board for the game.
	* Properties - mat(matrix), score, lives
	* Methods - `__init__()`, `setVal()`, `getVal()`, `setBomber()`, `printMat()`

#### game
	It contains the main processing of the game
	* Properties - flag
	* Methods - `__init__()`, `bombUpdate()`, `enemyUpdate()`, `remakeBomber()`, `run()`

#### brick
	It is the counterpart of walls which can be destroyed by the bombs
	* Properties - shape, place
	* Methods - `__init__()`, `getPlace()`, `putBricks()`

### person
	Parent class for the enemies, bomb and the bomberman (player)
	* Properties - rt(return value)
	* Methods - `__init__()`, `setPosition()`, `getPosition()`, `makePerson()`, `moveLeft()`, `moveRight()`, `moveUp()`, `moveDown()`

#### bomberman
	It defines the main character of the game i.e., Bomberman which is controlled by the user
	* Properties - position, shape, rt (return value)
	* Methods - `__init__()`, ,`removeBomber()`, `isValid()`

#### enemy
	It defines the enemies for the game which move in pseudo random motion
	* Properties - position, type, lives, shape
	* Methods - `__init__()`, `getPlace()`, `makeEnemy()`, `removeEnemy()`, `isValid()`, `move()`

#### bomb
	It defines the bomb that will be planted by the bomberman
	* Properties - time, position, life, shape
	* Methods - `__init__()`, `checkRes()`,`changeBombView()`, `explode()`, `update()`


## Basic Controls
	* b - Place Bomb
	* a - Left
	* s - Down
	* d - Right
	* w - Up
	* q - Quit the game

## Symbols
	* [^^] - Bomberman
	   ][
	* #### - Wall
	  ####
	* %%%% - Bricks
	  %%%%
	* [00] - Enemy
	
	  [00] 
	* BOMB - Bomb
	  BOMB 
	* 0000 - Explosion
	  0000

## Features
1. Bomb with time ticker explosion. Bomb counter is initially 3 seconds (can be changed). Multiple bombs are allowed but this can be easily changed. Bomb explosion is as specified in the rules.
2. Enemy: They can spawn anywhere on the board where there are no obstacles and move around in a pseudo-random motion. They get destroyed when they get caught in an explosion.
3. Scoreboard: 20 points for brick breaking and 100 points for killing enemies.
4. Lives for both Bomberman (3).
5. Highly modular and well commented OOPS implementation which is easily understandable.
6. Has multiple levels , 4 now but can be changed to any number of levels. Number of enemies and their speed increases with level, so difficulty increases. To reach next level, one has to beat all enemies in current level.
