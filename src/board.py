'''
Integer value given in main game array to various things:
bricks = 8
air = 9
walls = 10
'''
from termcolor import colored


class board():

        # This function initialize matrix and various other variables
    def __init__(self):
        self.mat = [[9 for x in range(76)] for y in range(38)]
        self.score = 0
        self.lives = 3
        self.level = 1
        for i in range(0, 38, 2):
            for j in range(0, 76, 4):
                if(i == 0 or i == (36)):
                    self.setVal(i, j, 10)
                elif(j == 0 or j == 72):
                    self.setVal(i, j, 10)
                elif((i % 4 == 0)and (j % 8 == 0)):
                    self.setVal(i, j, 10)

    # This function set a particular value in a block of 2x4 in the matrix
    def setVal(self, x, y, val):
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                self.mat[i][j] = val

    # This function returns the value in a particular cell of matrix
    def getVal(self, x, y):
        return self.mat[x][y]

    # This funciotn sets a value in a particular cell of matrix
    def setBomber(self, x, y, val):
        self.mat[x][y] = val

    # This function prints the matrix. colored() of termcolor is used for
    # colorful printing.
    def printMat(self):
        for i in range(38):
            for j in range(76):
                tp = self.mat[i][j]
                if(tp == 9):
                    print(" ", end='')
                elif(tp == 10):
                    print(colored("#", "cyan", attrs=["bold", "dark"]), end='')
                elif(tp == 8):
                    print(colored("%", "yellow", attrs=["bold"]), end='')
                elif((not isinstance(tp, str)) or (tp >= 'A' and tp <= 'Z')):
                    print(colored(tp, "yellow", attrs=["bold"]), end='')
                elif((tp == '0') or (tp == '[' and self.mat[i][j + 1] == '0')):
                    print(colored(tp, "red", attrs=["bold"]), end='')
                elif(tp == ']' and self.mat[i][j - 1] == '0'):
                    print(colored(tp, "red", attrs=["bold"]), end='')
                else:
                    print(
                        colored(
                            self.mat[i][j],
                            "green",
                            attrs=["bold"]),
                        end='')
            print('')
        print(colored("Your score is : ", "magenta", attrs=["bold"]), end='')
        print(colored(gameArr.score, "magenta", attrs=["bold"]))
        print(colored("Lives Remaining : ", "magenta", attrs=["bold"]), end='')
        print(colored(gameArr.lives, "magenta", attrs=["bold"]))
        print(colored("Level: ", "magenta", attrs=["bold"]), end='')
        print(colored(gameArr.level, "magenta", attrs=["bold"]))


gameArr = board()
