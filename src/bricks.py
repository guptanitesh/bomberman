from random import randint
from board import gameArr


class brick():

        # This funcition defines shape of brick and call functions for putting
        # bricks on board.
    def __init__(self):
        self.place = []
        self.shape = [['%', '%', '%', '%'], ['%', '%', '%', '%']]
        self.getPlace()
        self.putBricks()

    # This funtion makes a list of empty spaces on board.
    def getPlace(self):
        self.place = []
        for i in range(0, 38, 2):
            for j in range(0, 76, 4):
                if(gameArr.getVal(i, j) == 9):
                    self.place.append([i, j])

    # This funtion puts bricks randomly on board on empty spaces.
    def putBricks(self):
        for i in self.place:
            if(randint(0, 1) and randint(0, 1) and randint(0, 1)):
                gameArr.setVal(i[0], i[1], 8)


gameBricks = brick()
