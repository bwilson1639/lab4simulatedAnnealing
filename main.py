import random
import math
from copy import deepcopy

class Node:

    def __init__(self, data, cost):
        '''Initializes the node class and fills the node with required data'''

        self.data = data
        self.goal = [['0', '1', '2'],['3', '4', '5'], ['6', '7', '8']]
        self.cost = cost

    def createChild(self, parent):
        '''creates all child nodes off of current node, returns list of possible nodes'''


        xValue = None
        yValue = None
        randomNum = random.seed()

        for y in range(0,3):
            for x in range (0,3):
                if self.data[y][x] == '0':
                    xValue = x
                    yValue = y


        possibleList = [[xValue,yValue-1], [xValue,yValue+1], [xValue-1,yValue],[xValue+1,yValue]]
        possibleChildren = []
        children = []

        '''checks to see what moves are possible'''
        for coordinate in possibleList:
            if coordinate[0] >= 0 and coordinate[0] < 3 and coordinate[1] >= 0 and coordinate[1] < 3:
                possibleChildren.append(coordinate)

        '''moves the data around based on the possible children then saves it in children list'''
        while len(possibleChildren) > 0:

            possibleChildData = possibleChildren.pop(randomNum.randrange(len(possibleChildren)) -1)


            tempHolder = self.data[possibleChildData[1]][possibleChildData[0]]
            childData = deepcopy(self.data)

            childData[possibleChildData[1]][possibleChildData[0]] = '0'
            childData[yValue][xValue] = tempHolder

            if childData != parent.data or parent is None:
                children.append(Node(childData), self.costCalculate(childData))

        return children

    def costCalculate(self, data):

        temp = 0

        for y in range(0, 3):
            for x in range(0, 3):
                if data[y][x] != self.goal[y][x] and data[y][x] != '0':
                    temp += 1

        return temp


class simulatedAnneal:

    def annealAlgorithm(self,  iterate):

        inputProblem = self.getInput()
        t = 0
        current = Node(inputProblem) #need to solve cost calculation
        parent = None
        randomNum = random.seed()


        for t in iterate:

            T = (1-(t+1)/iterate)

            if T <= 0 :
                return current

            next = current.createChild(parent)

            deltaE = next.cost - current.cost

            deltaEProb = math.exp((-deltaE) / t)

            if deltaE > 0 or randomNum.uniform(0.0, 1.00000) > deltaEProb:

                parent = current

                current = next
                t += 1

            else:

                t += 1






    def getInput(self):
        """gets the user input for the starting state"""

        inputtedList = []

        print("Enter 9 numbers (including 0): (there should be a space between adjacent numbers")
        for inputs in range(0, 3):
            temp = input().split(" ")
            inputtedList.append(temp)

        return inputtedList #returns as a 2d list of strings
