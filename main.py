import random
import math
from copy import deepcopy

class Node:

    def __init__(self, data, cost):
        '''Initializes the node class and fills the node with required data'''

        self.data = data
        self.cost = cost
        self.goal = [['0', '1', '2'],['3', '4', '5'], ['6', '7', '8']]

    def createChild(self, parent):
        '''creates all child nodes off of current node, returns list of possible nodes'''


        xValue = None
        yValue = None

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
        for childNode in possibleChildren:
            possibleChildData = possibleChildren.pop(0)
            tempHolder = self.data[possibleChildData[1]][possibleChildData[0]]
            childData = deepcopy(self.data)

            childData[possibleChildData[1]][possibleChildData[0]] = '0'
            childData[yValue][xValue] = tempHolder
            children.append(Node(childData, 0))

        return children

    def costCalculate(self, start, goal):

        temp = 0

        for y in range(0, 3):
            for x in range(0, 3):
                if start[y][x] != goal[y][x] and start[y][x] != '0':
                    temp += 1
class simulatedAnneal:

    def annealalgorithm(self,  iterate):

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
