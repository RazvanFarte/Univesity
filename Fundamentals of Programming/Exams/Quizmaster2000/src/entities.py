'''
Created on Feb 15, 2017

@author: Razvan
'''
from src.validators import QuestionsValidator

class IDObject(object):
    '''
    classdocs
    '''


    def __init__(self, id):
        '''
        Constructor
        '''
        self.__id = id
        
        
    def get_id(self):
        return self.__id

    id = property(get_id, None, None, "id's docstring")


class Question(IDObject):
    def __init__(self, id, text, a, b, c, answer, difficulty, validator = QuestionsValidator):
        IDObject.__init__(self, id)
        self.__text, self.__a = text, a
        self.__b, self.__c, self.__answer, self.__difficulty = b, c, answer, difficulty
        self.__validator = validator
    
    def get_validator(self):
        return self.__validator


    def get_text(self):
        return self.__text


    def get_a(self):
        return self.__a


    def get_b(self):
        return self.__b


    def get_c(self):
        return self.__c


    def get_answer(self):
        return self.__answer


    def get_difficulty(self):
        return self.__difficulty


    def set_text(self, value):
        self.__text = value


    def set_a(self, value):
        self.__a = value


    def set_b(self, value):
        self.__b = value


    def set_c(self, value):
        self.__c = value


    def set_answer(self, value):
        self.__answer = value


    def set_difficulty(self, value):
        self.__difficulty = value


    def del_text(self):
        del self.__text


    def del_a(self):
        del self.__a


    def del_b(self):
        del self.__b


    def del_c(self):
        del self.__c


    def del_answer(self):
        del self.__answer


    def del_difficulty(self):
        del self.__difficulty

     
    text = property(get_text, set_text, del_text, "text's docstring")
    a = property(get_a, set_a, del_a, "a's docstring")
    b = property(get_b, set_b, del_b, "b's docstring")
    c = property(get_c, set_c, del_c, "c's docstring")
    answer = property(get_answer, set_answer, del_answer, "answer's docstring")
    difficulty = property(get_difficulty, set_difficulty, del_difficulty, "difficulty's docstring")
    validator = property(get_validator, None, None, "validator's docstring")
    
    
    def __str__(self, *args, **kwargs):
        return "{};{};{};{};{};{};{}".format(self.id, self.text, self.a, self.b, self.c, self.answer, self.difficulty)
    
    
    def __eq__(self, other):
        if not isinstance(other, Question):
            raise Exception("Operands mismatch")
        return self.id == other.id
    
    def __lt__(self, other):
        if not isinstance(other, Question):
            raise Exception("Operands mismatch")
        
        cases = {"easy":0, "medium":1, "hard":2}
        
        return cases[self.difficulty] < cases[other.difficulty]
    
    def __gt__(self, other):
        if not isinstance(other, Question):
            raise Exception("Operands mismatch")
        
        cases = {"easy":0, "medium":1, "hard":2}
        
        return cases[self.difficulty] > cases[other.difficulty]
    
    def __ge__(self, other):
        return not self < other
    
    def __le__(self, other):
        return not self > other
        
