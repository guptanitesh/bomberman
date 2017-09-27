import sys
from board import gameArr
from person import person
from termcolor import colored


class bomberman(person):

        # This function initializes various parameters of the bomberman and
        # makes it by calling appropriate function.
    def __init__(self):
        self.position = [2, 4]
        self.shape = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]
        self.makePerson()
        self.rt = 1

    # This function removes bomberman from its current position.
    def removeBomber(self):
        pos = self.getPosition()
        for i in range(pos[0], pos[0] + 2):
            for j in range(pos[1], pos[1] + 4):
                if(gameArr.getVal(i, j) == self.shape[i - pos[0]][j - pos[1]]):
                    gameArr.setBomber(i, j, 9)

    # This function checks if [x, y] is valid position for the bomberman.
    def isValid(self, x, y):
        flag = 1
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                if(gameArr.getVal(i, j) == '['):
                    self.rt = 0
                    gameArr.lives -= 1
                    if(not gameArr.lives):
                        print(colored("You Lost ):", "yellow", attrs=["bold"]))
                        sys.exit()
                    flag = 0
                elif(gameArr.getVal(i, j) != 9):
                    flag = 0
        return flag


bomber = bomberman()
