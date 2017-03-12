'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.entities import Question

class Controller(object):
    def __init__(self, repo):
        self.__repository = repo

    def get_repository(self):
        return self.__repository

    repository = property(get_repository, None, None, "repository's docstring")
    
    def save(self):
        pass
    
    def getObjects(self):
        return self.repository.getObjects()
    
    def findById(self, objId):
        return self.repository.findById(objId)


class QuestionController(Controller):

    def __init__(self, repo):
        super().__init__(repo)
    
    def save(self, id, text, a, b, c, answer, difficulty):
        Controller.save(self)
        
        super().repository.save(Question(id, text, a, b, c, answer, difficulty))
        

class QuizzController(Controller):
    
    def __init__(self, repo, questionRepo):
        Controller.__init__(self, repo)
        self.__questionRepository = questionRepo

    def get_question_repository(self):
        return self.__questionRepository

    questionRepository = property(get_question_repository, None, None, "questionRepository's docstring")
    
    def create(self, difficulty, numOfQuestions, file):
        self.repository.fileName = file
        questions = list(self.questionRepository.getObjects())
        
        if len(questions) < numOfQuestions:
            raise Exception("There are not enough questions")
        
        difficultyQuestions = self.__getQuestions(difficulty, questions)
        
        if not self.__hasEnoghQuestions(difficultyQuestions, numOfQuestions):
            raise Exception("There are no enough {} questions".format(difficulty))
        
        for elem in questions:
            if len(difficultyQuestions) == numOfQuestions:
                break
            if not elem in difficultyQuestions:
                difficultyQuestions.append(elem)
        
        difficultyQuestions.sort()
        
        for i in range(numOfQuestions):
            el = difficultyQuestions[i]
            self.repository.save(Question(i+1, el.text, el.a, el.b, el.c, el.answer, el.difficulty))
        
    def __getQuestions(self, difficulty, questions):
        quest = []
        for elem in questions:
            if elem.difficulty == difficulty:
                quest.append(elem)
        
        return quest
    
    def __hasEnoghQuestions(self, questions, questionsNeeded):
        if len(questions) >= questionsNeeded//2:
            return True
        return False
                