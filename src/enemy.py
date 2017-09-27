import sys
from board import gameArr
from random import randint
from person import person


class enemy(person):

        # This function initializes various parameters of enemy and make one
        # enemy by calling appropriate functions.
    def __init__(self):
        self.place = []
        self.position = self.makeEnemy()
        self.shape = [['[', '0', '0', ']'], ['[', '0', '0', ']']]
        self.makePerson()
        self.rt = 1

    # This funtion makes a list of empty spaces on board.
    def getPlace(self):
        self.place = []
        for i in range(0, 38, 2):
            for j in range(0, 76, 4):
                if(gameArr.getVal(i, j) == 9):
                    self.place.append([i, j])

    # This function randomly put an enemy in empty space on board.
    def makeEnemy(self):
        self.getPlace()
        tp = randint(0, len(self.place) - 1)
        return self.place[tp]

    # This function removes enemy from current position.
    def removeEnemy(self):
        pos = self.getPosition()
        flag = 1
        for i in range(pos[0], pos[0] + 2):
            for j in range(pos[1], pos[1] + 4):
                if(gameArr.getVal(i, j) == self.shape[i - pos[0]][j - pos[1]]):
                    gameArr.setBomber(i, j, 9)
                else:
                    flag = 0
        return flag

    # This function checks if [x, y] is valid position for an enemy.
    def isValid(self, x, y):
        if(gameArr.getVal(x, y + 1) == '^'):
            gameArr.lives -= 1
            if(not gameArr.lives):
                print("You Lost")
                sys.exit()
            else:
                self.rt = 2
        flag = 1
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                if(gameArr.getVal(i, j) != 9):
                    flag = 0
        return flag

    # This function randomly moves the enemy.
    def move(self):
        if(not self.removeEnemy()):
            return 0
        tp = randint(1, 4)
        self.rt = 1
        if(tp == 1):
            self.moveLeft()
        if(tp == 2):
            self.moveUp()
        if(tp == 3):
            self.moveRight()
        if(tp == 4):
            self.moveDown()
        self.makePerson()
        return self.rt
