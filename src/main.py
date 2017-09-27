import time
import sys
import os
from bomb import bomb
from bomberman import bomber
from board import gameArr
from helper import getch
from bricks import gameBricks
from enemy import enemy
from termcolor import colored

bombArr = []
enemyArr = []


class game():

    # This function starts the game with 10 enemies
    def __init__(self):
        self.makeEnemies(4)
        self.flag = 1
        self.run()

    def makeEnemies(self, x):
        for i in range(x):
            enemyArr.append(enemy())

    # This function updates the status of bomb and if bomberman is killed,
    # remakes it (if lives are left).
    def bombUpdate(self):
        for i in bombArr:
            tp = i.update(time.time())
            if(tp == 0):
                bombArr.remove(i)
            elif(tp == 2):
                self.remakeBomber()

    # This function remakes the bomberman at the top-left corner
    def remakeBomber(self):
        bomber.removeBomber()
        bomber.setPosition(2, 4)
        bomber.makePerson()

    # This funcion move the enemies and changes level if no enemies remain.
    def enemyUpdate(self):
        for i in enemyArr:
            tp = i.move()
            if(tp == 0):
                enemyArr.remove(i)
                if(not len(enemyArr)):
                    gameArr.level += 1
                    if(gameArr.level == 5):
                        print(colored("You Won!!", "yellow", attrs=["bold"]))
                        sys.exit()
                    else:
                        self.flag = 2
                        self.makeEnemies(3 * gameArr.level)
            elif(tp == 2):
                self.remakeBomber()

    # This funciton contains main game loop
    def run(self):
        while(1):
            # Clearing the screen
            os.system('clear')

            # Pringting Matrix
            gameArr.printMat()
            if(self.flag == 2):
                print(
                    colored(
                        "You reached the next level!",
                        "yellow",
                        attrs=["bold"]))

            self.flag = 1

            # Taking single character input using getch
            c = getch()

            # Now acts according to input
            if(c == 'q'):
                sys.exit()
            elif(c == 'a'):
                bomber.removeBomber()
                if(bomber.moveLeft()):
                    bomber.makePerson()
                else:
                    self.flag = 0
                    self.remakeBomber()
            elif(c == 's'):
                bomber.removeBomber()
                if(bomber.moveDown()):
                    bomber.makePerson()
                else:
                    self.flag = 0
                    self.remakeBomber()
            elif(c == 'd'):
                bomber.removeBomber()
                if(bomber.moveRight()):
                    bomber.makePerson()
                else:
                    self.flag = 0
                    self.remakeBomber()
            elif(c == 'w'):
                bomber.removeBomber()
                if(bomber.moveUp()):
                    bomber.makePerson()
                else:
                    self.flag = 0
                    self.remakeBomber()
            elif(c == 'b'):
                bombArr.append(bomb(time.time(), bomber.getPosition()))

            # Updating status of bomb in every iteration
            self.bombUpdate()
            if(self.flag):
                self.enemyUpdate()


blender = game()
