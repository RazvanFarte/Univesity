'''
Created on Feb 15, 2017

@author: Razvan
'''

class Validator:
    @staticmethod
    def validate(obj):
        pass 

class QuestionsValidator(Validator):
    @staticmethod
    def validate(obj):
        Validator.validate(obj)
        

class QuizzValidator(Validator):
    @staticmethod
    def validate(obj):
        Validator.validate(obj)