'''
Created on Feb 23, 2017

@author: Razvan
'''

class BattleshipValidator(object):
    '''
    classdocs
    '''
    @staticmethod
    def validate(battleship):
        for collum in battleship.collums:
            if collum > 5 or collum < 0:
                raise Exception("Battleship outside of grid: collum", collum)
        
        for row in battleship.rows:
            if row > 5 or row < 0:
                raise Exception("Battleship outside of grid: row ", row)
