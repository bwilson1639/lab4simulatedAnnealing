import random
import math
import sys
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
        manhattanCost = costCalculate()

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

            possibleChildData = possibleChildren.pop(random.randrange(len(possibleChildren)) - 1)


            tempHolder = self.data[possibleChildData[1]][possibleChildData[0]]
            childData = deepcopy(self.data)

            childData[possibleChildData[1]][possibleChildData[0]] = '0'
            childData[yValue][xValue] = tempHolder

            if  parent is None or childData != parent.data:
                children.append(Node(childData, manhattanCost.manhattanCalculate(childData)))

        return children




class simulatedAnneal:
    '''class that stores the simulated Anneal Algorithm. Uses the Node class to store the information, then either
     randomly selects either a better move, where it will then go into that move, or it randomly selects a worse
     move, in which it will go into it if deltaEProb < a random flode between 0.0 and 1.0'''
    def __init__(self, iterate):

        self.annealAlgorithm(iterate)

    def annealAlgorithm(self,  iterateNum):
        iterate = int(iterateNum)
        inputProblem = self.getInput()
        t = 1
        initialCost = costCalculate()
        current = Node(inputProblem, initialCost.manhattanCalculate(inputProblem)) #need to solve cost calculation
        parent = None


        for t in range(iterate):

            T = (1-(t+1)/iterate)

            if T <= 0 :
                return current

            childlist = current.createChild(parent)
            next = childlist.pop(random.randrange(0, len(childlist)))
            deltaE = next.cost - current.cost

            deltaEProb = math.exp(((-deltaE)/T))

            if deltaE < 0 or random.uniform(0.0, 1.00000) > deltaEProb:

                print(current.data[0])
                print(current.data[1])
                if deltaE <= 0:
                    line3 = str(current.data[2]) + "(value = " + str(deltaE) + ")"
                    print(line3)
                    print("\n")
                else:
                    line3 = str(current.data[2]) + "(value = " + str(deltaE) + ", BAD MODE was chosen)"
                    print(line3)
                    print("\n")
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

class costCalculate:
    ''''calculates the manhattan distance for any inputted state. uses a dictionary to store the final positions,
    then checks where the inputted boardData aligns with the dictionary'''
    def __init__(self):


        self.boardDictionary = {
                # x,y
            '1': [1,0],
            '2': [2,0],
            '3': [0,1],
            '4': [1,1],
            '5': [1,2],
            '6': [2,0],
            '7': [2,1],
            '8': [2,2]}


    def manhattanCalculate(self, boardData):
        '''the expression that calculates the manhattan distance'''
        manhattanCost = 0

        for y in range(0,3):
            for x in range(0,3):

                if boardData[y][x] == '0':
                    continue
                else:
                    temp = boardData[y][x]
                    dictionaryValue = self.boardDictionary[temp]
                    manhattanCost += (abs(y - dictionaryValue[1]) + abs(x - dictionaryValue[0]))

        return manhattanCost


start = simulatedAnneal(200)