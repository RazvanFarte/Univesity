'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.entities import Question

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, questionController, quizzController):
        '''
        Constructor
        '''
        self.__questionController = questionController
        self.__quizzController = quizzController

    def get_question_controller(self):
        return self.__questionController


    def get_quizz_controller(self):
        return self.__quizzController


    def set_question_controller(self, value):
        self.__questionController = value


    def set_quizz_controller(self, value):
        self.__quizzController = value


    def del_question_controller(self):
        del self.__questionController


    def del_quizz_controller(self):
        del self.__quizzController

    questionController = property(get_question_controller, set_question_controller, del_question_controller, "questionController's docstring")
    quizzController = property(get_quizz_controller, set_quizz_controller, del_quizz_controller, "quizzController's docstring")
    
    
    def __readLine(self):
        line = input("Command: ")
        line = line.strip()
        line = line.split(" ", 1)
        
        if len(line) > 1:
            return line[0], line[1].split(";")
        
        return line[0], []
    
    def run(self):
        
        commands = {"add": self.__addQuestion, "create": self.__createQuizz,
                    "start": self.__startQuizz}
        
        while True:
            command, args = self.__readLine()
            
            if command == "exit":
                break
            
            try:
                commands[command](*args)
            except Exception as ex:
                print(ex)
    
    def __addQuestion(self, id, text, a, b, c, answer, difficulty):
        self.questionController.save(int(id), text, a, b, c, answer, difficulty)
    
    def __createQuizz(self, difficulty, numOfQuestions, fileToSave):
        self.quizzController.create(difficulty, int(numOfQuestions), fileToSave)
        
    def __getQuizzFromFile(self, fileName):
        l = []
        with open(fileName, "r") as f:
            for line in f:
                line = line.strip()
                line = line.split(";")
                
                l.append(Question(int(line[0]), line[1], line[2], line[3], line[4],
                                      line[5], line[6]))
        
        return l
    
    def __startQuizz(self, fileName):
        listOfQuestions = self.__getQuizzFromFile(fileName)
        
        score = 0
        for elem in listOfQuestions:
            print("{}. {} \na. {}\nb. {}\nc. {}".format(elem.id,elem.text,elem.a,elem.b,elem.c))
            answer = input("Answer: ")
            if answer == elem.answer:
                print("Correct!")
                
                if elem.difficulty == "easy":
                    score += 1
                elif elem.difficulty == "medium":
                    score += 2
                elif elem.difficulty == "hard":
                    score += 3
            else:
                print("Incorrect!")
                
        print("Quizz done!\nScore: ", score)
        