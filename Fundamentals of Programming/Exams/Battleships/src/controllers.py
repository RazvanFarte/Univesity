'''
Created on Feb 23, 2017

@author: Razvan
'''
from src.domain import Battleship
import random
import unittest
from src.repo import Repository
from src.validators import BattleshipValidator

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self, playerBattleshipsRepo, computerBattleshipRepo):
        '''
        Constructor
        '''
        self.__player= playerBattleshipsRepo
        self.__computer = computerBattleshipRepo

    def get_player(self):
        return self.__player


    def get_computer(self):
        return self.__computer


    def set_player(self, value):
        self.__player = value


    def set_computer(self, value):
        self.__computer = value


    def del_player(self):
        del self.__player


    def del_computer(self):
        del self.__computer

    player = property(get_player, set_player, del_player, "player's docstring")
    computer = property(get_computer, set_computer, del_computer, "computer's docstring")

    def __addShip(self, collums, rows, repository):
        """Adds a ship to repository. Collums and rows are lists of strings 
        
        Input
            collums - a list of strings, representing coordinates of ship
        """
        for i in range(len(collums)):
            collums[i] = Battleship.lettersToInt[collums[i]]
            
        for i in range(len(rows)):
            rows[i] = Battleship.lettersToInt[rows[i]]
        
        repository.save(Battleship(collums, rows))
        
    def __getEmptyGrid(self):
        li = []
        for i in range(6):
            li.append(list("."*6))
        
        return li
        
    def __getSquareWithCar(self, matrix, collum, row, ch):
        matrix[row][collum] = ch
        return matrix
    
    def __getMatrixMissed(self, matrix, missed):
        """
        Input
            missed - list with lists. Each small list contain row, collum
        """
        for miss in missed:
            matrix = self.__getSquareWithCar(matrix, miss[1], miss[0], "0")
        
        return matrix
    
    def __getMatrixWithBattleship(self, matrix, battleship):
        """
        Input
            battleship - BattleShip object
        """
        collums = battleship.collums
        rows = battleship.rows
        for i in range(3):
            row = rows[i]
            collum = collums[i]
            car = battleship.battleship[i]
            matrix[row][collum] = car
            
        return matrix
    
    
    def __getMatrixWithBattleships(self, matrix, repository):
        
        for bs in repository.objects:
            matrix = self.__getMatrixWithBattleship(matrix, bs)
            
        return matrix
    
    
    def __printMatrix(self, matrix):
        for line in matrix:
            lineString = ""
            for collum in line:
                lineString += collum + " "
            print(lineString)
    
    def __getPlaterGrid(self, repository, missedHits):
        matrix = self.__getEmptyGrid()
        matrix = self.__getMatrixWithBattleships(matrix, repository)
        matrix = self.__getMatrixMissed(matrix, missedHits)
        
        return matrix
        
    def __printGrid(self, repository, missedHits):
        """Prints the player grid
        Input
            missedHits - list containing pairs [row,collum]
        """
        matrix = self.__getPlaterGrid(repository, missedHits)
        
        self.__printMatrix(matrix)
    
    def printPlayersGrid(self, missedHits):
        self.__printGrid(self.player, missedHits)
    
    def printCheat(self, missedHits):
        self.__printGrid(self.computer, missedHits)
    
    def __getEnemyGrid(self, missedHits):
        matrix = self.__getEmptyGrid()
        matrix = self.__getMatrixMissed(matrix, missedHits)
        
        return matrix
    
    def printEnemysGrid(self, missedHits):
        matrix = self.__getEnemyGrid(missedHits)
        self.__printMatrix(matrix)
    
    def addShip(self, collums, rows):
        """Adds a ship to players grid"""
        self.__addShip(collums, rows, self.player)
        self.printPlayersGrid([])
    
    def __generateBattleships(self):
        battleships = []
        
        for row in range(4):
            for collum in range(4):
                battleships.append(Battleship([collum,collum, collum], [row,row+1,row+2]))
                battleships.append(Battleship([collum,collum+1, collum+2], [row,row,row]))
        
        return battleships
    
    def __chooseBattleship(self, battleships):        
        return random.choice(battleships)
    
    def __chooseBatleships(self):
        battleships = self.__generateBattleships()
        while len(self.computer.objects) != 2:
            boat = self.__chooseBattleship(battleships)
            
            try:
                self.computer.save(boat)
            except Exception as ex:
                pass
    
    def __hasBattleship(self, repository, position):
        for bs in repository.objects:
            for i in range(3):
                if(position[0] == bs.rows[i] and position[1] == bs.collums[i]):
                    return bs
        return None
                    
    
    def __attack(self, repository1, repository2, position, missList):
        hitedBs = self.__hasBattleship(repository2, position)
        if not hitedBs is None:
            #Set that to x
            hitedBs.setSquare(position[1], position[0])
            return True
        else:
            #Set that to 0
            missList.append(position)
            return False
    
    
    def incPosition(self, position):
        position[1] += 1
        if position[1] > 6:
            position[1] -= 6
            position[0] +=1   
            
             
    def start(self):
        playerMissed = []
        enemyMissed = []
        enemyHits = 0
        playerHits = 0
        enemyPositionAttacks = [0,0]
        
        self.__chooseBatleships()
        
        while True:
            print("Player: ")
            self.printPlayersGrid(enemyMissed)
            print("Enemy: ")
            self.printEnemysGrid(playerMissed)
            if enemyHits == 6:
                print("You lost")
                break
            if playerHits == 6:
                print("You win")
                break
            
            try:
                comm, args = self.__readLine()
                if comm == "attack":
                    position = list(args[0])
                    position[0] = Battleship.lettersToInt[position[0]]
                    position[1] = Battleship.lettersToInt[position[1]]
                    
                    hit = self.__attack(self.player, self.computer, [position[1], position[0]], playerMissed)
                    
                    if hit:
                        playerHits += 1
                        print("Player hits")
                    else:
                        print("Player misses")
                    
                elif comm == "cheat":
                    self.printCheat(playerMissed)
                else:
                    raise Exception("Inexistent command")
            except Exception as ex:
                print("Invalid command", ex)
                
            #Now enemy attacks
            
            print("Enemy attacks", Battleship.collumToLetters[enemyPositionAttacks[1]], Battleship.rowToLetters[enemyPositionAttacks[0]])
            hit = self.__attack(self.computer, self.player, [enemyPositionAttacks[0],enemyPositionAttacks[1]], enemyMissed)
            self.incPosition(enemyPositionAttacks)
            
            if hit:
                enemyHits += 1
                print("Enemy hits")
            else:
                print("Enemy missed")

    
    def __readLine(self):
        line = input("Command: ")
        line = line.strip()
        
        line = line.split(" ", 1)
        
        return line[0], line[1:] if len(line) > 1 else []


                
class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.playerRepo = Repository(BattleshipValidator)
        self.enemyRepo = Repository(BattleshipValidator)
        self.controller = Controller(self.playerRepo, self.enemyRepo)
        
        self.battleship1 = Battleship([1,2,3], [3,3,3])
        self.battleship2 = Battleship([3,3,3], [0,1,2])

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAddShip(self):
        self.assertTrue(self.controller.addShip(["b","c","d"], ["3","3","3"]) is None, "It should be ok")
        self.assertRaises(Exception, self.controller.addShip, ["b","c","d"], ["3","3","3"])
        try:
            self.controller.addShip(["b","c","d"], ["3","3","3"])
        except Exception as ex:
            pass
        self.assertTrue(self.controller.addShip(["3","3","3"], ["a","b","c"]) is None, "It sohuld be ok")
    
    
if __name__ == '__main__':
    unittest.main()    
            