'''
Created on Feb 22, 2017

@author: Razvan
'''
from src.repo import FileRepository
from src.Sentence import SentenceValidator
from src.controller import Controller
from src.console import Console

if __name__ == '__main__':
    
    sentenceRepo = FileRepository(SentenceValidator, "input.txt")
    scrambleController = Controller(sentenceRepo)
    
    console = Console(scrambleController)
    
    try:
        console.run()
    except Exception as ex:
        print(ex)
        
    print("Bye")