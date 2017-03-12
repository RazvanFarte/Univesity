'''
Created on Feb 22, 2017

@author: Razvan
'''
import unittest
from src.repo import FileRepository
from src.Sentence import SentenceValidator, Sentence
from src.controller import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.repository = FileRepository(SentenceValidator, "emptyFile")
        
        self.sentence1 = Sentence(["ana", "are", "mere"])
        self.sentence2 = Sentence(["Dana", "are", "pere"])
        self.sentence3 = Sentence(["Oana", "are", "bere"])
        
        self.repository.save(self.sentence1)
        self.repository.save(self.sentence2)
        self.repository.save(self.sentence3)
        
        self.controller = Controller(self.repository)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testGetScore(self):
        self.assertTrue(self.controller.getScore(self.sentence1) == 10, "Number of letters is 10")
        self.assertTrue(self.controller.getScore(self.sentence2) == 11, "Number of letters is 11")
        self.assertTrue(self.controller.getScore(self.sentence3) == 11, "Number of letters is 11")
        
    def testScramble(self):
        self.assertTrue(self.controller.scramble(self.sentence1) != self.sentence1, "There was no scramble")
        self.assertTrue(self.controller.scramble(self.sentence2) != self.sentence2, "There was no scramble")
        self.assertTrue(self.controller.scramble(self.sentence3) != self.sentence3, "There was no scramble")
    
    def testSwapLetters(self):
#         self.assertRaises(Exception, self.controller.swapLetters(self.sentence1, 0, 0, 1, 1))
        
        resultSentence = self.controller.swapLetters(self.sentence1, 0, 1, 1, 1)
        self.assertNotEqual(resultSentence, self.sentence1, "There was a swap")
        
if __name__ == '__main__':
    unittest.main()              
