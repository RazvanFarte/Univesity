'''
Created on Feb 23, 2017

@author: Razvan
'''
from src.validators import BattleshipValidator

class Battleship(object):
    '''
    classdocs
    '''
    
    lettersToInt = {'0':0,'1':1,"2":2, "3":3,"4":4,"5":5,'a':0,'b':1,"c":2, "d":3,"e":4,"f":5}
    rowToLetters = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5"}
    collumToLetters = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}
    

    def __init__(self, collums, rows , validator=BattleshipValidator):
        '''
        Input
            collums - list of integers
            rows - list of integers
        '''
        self.__collums = collums
        self.__rows = rows
        self.validator = validator
        self.battleship = list("+"*3)
        
    def get_collums(self):
        return self.__collums


    def get_rows(self):
        return self.__rows


    def set_collums(self, value):
        self.__collums = value


    def set_rows(self, value):
        self.__rows = value


    def del_collums(self):
        del self.__collums


    def del_rows(self):
        del self.__rows

    collums = property(get_collums, set_collums, del_collums, "collums's docstring")
    rows = property(get_rows, set_rows, del_rows, "rows's docstring")
    
    def __eq__(self, other):
        for square in range(3):
            if self.collums[square] == other.collums[square] and self.rows[square] == other.rows[square]:
                return True
        return False
    

    def setSquare(self, collum, row):
        """
        Input
            collum - int
            row - int
        """
        if collum not in self.collums:
            return
        if row not in self.rows:
            return
        
        if self.collums[0] == self.collums[1] == self.collums[2]:
            i = self.rows.index(row)
            
        if self.rows[0] == self.rows[1] == self.rows[2]:
            i = self.rows.index(collum)
            
        self.battleship[i] = "x"
        