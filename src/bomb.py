from board import gameArr
from person import person
from termcolor import colored
import sys


class bomb(person):

        # This funcion initializes various parameters of bomb like time,
        # position, life(seconds) remaining, etc. and make bombs
    def __init__(self, time, pos):
        self.time = time
        self.position = pos
        """ Just change this variable if you want to
            change the time for explosion of bomb."""
        self.life = 3
        self.shape = [['B', 'O', 'M', 'B'], ['B', 'O', 'M', 'B']]
        self.makePerson()

    # Check what is there at [x,y] in board and act accordingly during
    # explosion
    def checkRes(self, x, y):
        tp = gameArr.getVal(x, y)
        if(tp == '0'):
            gameArr.score += 100
            return 1
        elif(tp == 8):
            gameArr.score += 20
            return 1
        elif(tp == 9):
            return 1
        elif(tp == ']'):
            gameArr.lives -= 1
            if(not gameArr.lives):
                print(colored("You Lost ):", "yellow", attrs=["bold"]))
                sys.exit()
            else:
                return 2
        return 0

    # Changes the view of bomb. Basically shows no. of seconds remaining for
    # explosion
    def changeBombView(self, val):
        self.shape = [[val, val, val, val], [val, val, val, val]]
        self.makePerson()

    # Checks what should happen at explosion at various places in its
    # neighbourhood using checkRes() function and acts accordingly.
    def explode(self):
        flag = 1
        [x, y] = self.getPosition()
        gameArr.setVal(x, y, 0)
        tp = self.checkRes(x - 1, y + 1)
        if(tp == 1):
            gameArr.setVal(x - 2, y, 0)
        elif(tp == 2):
            flag = 2
        tp = self.checkRes(x + 1, y - 3)
        if(tp == 1):
            gameArr.setVal(x, y - 4, 0)
        elif(tp == 2):
            flag = 2
        tp = self.checkRes(x + 3, y + 1)
        if(tp == 1):
            gameArr.setVal(x + 2, y, 0)
        elif(tp == 2):
            flag = 2
        tp = self.checkRes(x + 1, y + 5)
        if(tp == 1):
            gameArr.setVal(x, y + 4, 0)
        elif(tp == 2):
            flag = 2
        return flag

    # This function updates the bomb. Basically processes only after 1 second
    # from previous update.
    def update(self, currTime):
        if(currTime - self.time >= 1):
            self.time = currTime
            self.life -= 1
            if(self.life == -1):
                [x, y] = self.getPosition()
                gameArr.setVal(x, y, 9)
                if(gameArr.getVal(x - 2, y) == 0):
                    gameArr.setVal(x - 2, y, 9)
                if(gameArr.getVal(x + 2, y) == 0):
                    gameArr.setVal(x + 2, y, 9)
                if(gameArr.getVal(x, y - 4) == 0):
                    gameArr.setVal(x, y - 4, 9)
                if(gameArr.getVal(x, y + 4) == 0):
                    gameArr.setVal(x, y + 4, 9)
                return 0
            elif(self.life == 0):
                return self.explode()
            else:
                self.changeBombView(self.life)
        return 1
