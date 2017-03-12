'''
Created on Jan 13, 2017

@author: Razvan
'''
from random import random

def initialize(solutionList, initializationList, position):
    '''Initializes the current level of the solution stack
        
    Input:
        solutionList - a stack with solutions
        initializationList - list of given values to be added to solution list
        position - index in initializationList that will show the next value to be put in solution
        
    We assume that initializationList is sorted
    '''
    solutionList.append(initializationList[position])


def hasSuccessor(initializationList, indexInitializationList):
    if indexInitializationList < len(initializationList):
        return True
    return False


def isValid(solutionList, element):
    if solutionList == []:
        return True
    for c in str(solutionList[-1]):
        if c in str(element):
            return True
    return False


def isSolution(solutionList):
    if len(solutionList) >= 2:
        return True
    return False
    

def printSolution(solutionList):
    print(solutionList)


def readSet():
    '''Returns a list of integers readed from the console
    
    Output:
        - returns - a list with elements read from keyboard
    '''
    while True:
        try:
            n = int(input("Give me the dimension of set: ").strip())
            if n < 3:
                continue
            break
        except ValueError:
            print("Dimension of the set must be an integer!")
    
    l = []
    while len(l) < n:
        try:
            l.append(int(input("Element {0}: ".format(len(l) + 1)).strip()))
        except ValueError:
            print("Element of the set must be an integer")
    
    return l


def backTracking(initializationList):  
    initializationList = sorted(initializationList)  
    indexInitializationList = 1

    solutionList = initializationList[0:indexInitializationList]
    
    while True:
        
        while hasSuccessor(initializationList, indexInitializationList):
                if isValid(solutionList, initializationList[indexInitializationList]):
                    initialize(solutionList, initializationList, indexInitializationList)
                    
                    indexInitializationList += 1
                    if isSolution(solutionList):
                        printSolution(solutionList)
                        continue
                else:
                    indexInitializationList += 1
        else:
            if not len(solutionList):
                break
            indexInitializationList = initializationList.index(solutionList.pop()) + 1


def backTrackingRec(initializationList):
    _backTrackingRec([], initializationList[:])
    
def _backTrackingRec(solutionList, initializationList):    
    indexInitializationList = 0
    
    while hasSuccessor(initializationList, indexInitializationList):
        if isValid(solutionList, initializationList[indexInitializationList]):
            initialize(solutionList, initializationList, indexInitializationList)
            
            indexInitializationList += 1
            _backTrackingRec(solutionList, initializationList[indexInitializationList:])
            if isSolution(solutionList):
                print(solutionList)
                solutionList.pop()
                continue
            solutionList.pop()
        else:
            indexInitializationList += 1
            
            
def  testBackTracking(numElements, numberOfDigits):
    l = []
    for i in range(numElements):
        l.append(int(random()*10**numberOfDigits))
    print("List is:",l)
    l = sorted(l)
    print("Sorted list is:",l)
    backTrackingRec(l)
    

if __name__ == '__main__':
    
#     initializationList = sorted(readSet())
#     backTracking(initializationList)
    testBackTracking(int(input("Give the size of set: ")), int(input("Give the number of digits of numbers: ")))
    print("End of program")