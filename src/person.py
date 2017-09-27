from board import gameArr
import sys


class person():

        # This function defines the rt (return) variale.
    def __init__(self):
        self.rt = 1

    # This function sets the position of person.
    def setPosition(self, x, y):
        self.position = [x, y]

    # This function returns the position of person.
    def getPosition(self):
        return self.position

    # This funcition makes the Person. Basically sets value of particular
    # cells in board to its shape.
    def makePerson(self):
        [x, y] = self.getPosition()
        for i in range(2):
            for j in range(4):
                gameArr.setBomber(x + i, y + j, self.shape[i][j])

    # This function basically sets the poition of person to one left if that
    # is a valid position.
    def moveLeft(self):
        self.rt = 1
        pos = self.getPosition()
        if(self.isValid(pos[0], pos[1] - 4)):
            self.setPosition(pos[0], pos[1] - 4)
        return self.rt

    # This function basically sets the poition of person to one right if that
    # is a valid position.
    def moveRight(self):
        self.rt = 1
        pos = self.getPosition()
        if(self.isValid(pos[0], pos[1] + 4)):
            self.setPosition(pos[0], pos[1] + 4)
        return self.rt

    # This function basically sets the poition of person to one up if that is
    # a valid position.
    def moveUp(self):
        self.rt = 1
        pos = self.getPosition()
        if(self.isValid(pos[0] - 2, pos[1])):
            self.setPosition(pos[0] - 2, pos[1])
        return self.rt

    # This function basically sets the poition of person to one down if that
    # is a valid position.
    def moveDown(self):
        self.rt = 1
        pos = self.getPosition()
        if(self.isValid(pos[0] + 2, pos[1])):
            self.setPosition(pos[0] + 2, pos[1])
        return self.rt
