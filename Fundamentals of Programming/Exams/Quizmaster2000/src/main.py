'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.validators import QuestionsValidator, QuizzValidator
from src.repository import FileRepository
from src.controllers import QuizzController, QuestionController
from src.ui import Console

if __name__ == '__main__':
    
    quizzFile = "quizz"
    questionFile = "question"
    
    questionsRepository = FileRepository(QuestionsValidator, questionFile)
    questionsController = QuestionController(questionsRepository)
    
    quizzRepository = FileRepository(QuestionsValidator, quizzFile)
    quizzController = QuizzController(quizzRepository, questionsRepository)
    
    console = Console(questionsController, quizzController)
    try:
        console.run()
    except Exception as ex:
        print("Error:" + str(ex))
        
    print("Bye Bye!")
    
    