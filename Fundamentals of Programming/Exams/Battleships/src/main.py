'''
Created on Feb 23, 2017

@author: Razvan
'''
from src.console import Console
from src.controllers import Controller
from src.repo import Repository
from src.validators import BattleshipValidator

if __name__ == '__main__':

    playerBattleshipsRepo = Repository(BattleshipValidator)
    computerBattleshipsRepo = Repository(BattleshipValidator)
    gameController = Controller(playerBattleshipsRepo, computerBattleshipsRepo)
    
    console = Console(gameController)
    
    try:
        console.run()
    except Exception as ex:
        print(ex)
        
    print("Bye")