
#optimal

import random
import copy

class board:

    def __init__(self, initialBoard=None):  # initialBoard must be 1d list whit lenght 8
        if (initialBoard == None):
            self.boardvar = [i for i in range(8)]
            random.shuffle(self.boardvar)
        else:
            self.setboard(initialBoard)

    def setboard(self, nextboard):
        for i in range(8):
            self.boardvar[i] = nextboard[i]

    def getboard(self):
        return self.boardvar

    def getindex(self, x):
        return self.boardvar[x]

    def isGoal(self):
        for i in range(8):
            for k in range(8):
                if (abs(self.boardvar[k] - self.boardvar[i]) == abs(i-k)  and k != i):
                    return False
        return True

    def findNeighbor(self):
        neighbor = []
        for i in range(8):
            for forward in range(i+1,8):
                boardtmp = copy.deepcopy(self.getboard())
                boardtmp = swapElements(boardtmp,i,forward)
                neighbor.append(boardtmp)
            for backward in range(0,i):
                boardtmp = copy.deepcopy(self.getboard())
                boardtmp = swapElements(boardtmp,i,backward)
                neighbor.append(boardtmp)
        return neighbor


def cmpCost(boardv):
    cost = 0
    for i in range(8):
        for k in range(8):
            if (abs(boardv[k] - boardv[i]) == abs(i - k) and k != i):
                cost += 1
    return cost

def swapElements(boardv,index1,index2):
    temp = boardv[index1]
    boardv[index1] = boardv[index2]
    boardv[index2] = temp
    return boardv

def stepAscent(boardv=None):  # if boardv be None then randomly create a board for initial board
    tempboard = board(boardv)  # intial the first board in init board func
    print(tempboard.getboard())
    print(cmpCost(tempboard.getboard()))
    while (True):
        neighbors = tempboard.findNeighbor()
        bestnibr = tempboard.getboard()
        lowestcost = cmpCost(tempboard.getboard())
        while (neighbors.__len__() > 0):
            nibrboard = neighbors.pop()
            nibrcost = cmpCost(nibrboard)
            if (nibrcost < lowestcost):
                bestnibr = nibrboard
                lowestcost = nibrcost
        if (bestnibr == tempboard.getboard()):
            break
        tempboard.setboard(bestnibr)
    return tempboard.getboard()

boardv = stepAscent()
print(boardv)
print(cmpCost(boardv))