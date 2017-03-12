'''
Created on Feb 22, 2017

@author: Razvan
'''
import unittest
from src.repo import FileRepository
from src.Sentence import Sentence, SentenceValidator

class FileRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.repository = FileRepository(SentenceValidator, "emptyFile")
        
        self.sentence1 = Sentence(["ana", "are", "mere"])
        self.sentence2 = Sentence(["Dana", "are", "pere"])
        self.sentence3 = Sentence(["Oana", "are", "bere"])
        
        self.repository.save(self.sentence1)
        self.repository.save(self.sentence2)
        self.repository.save(self.sentence3)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSave(self):
        
        s = Sentence(["ana", "are", "mere"])
        self.assertIsNone(self.repository.save(s), "There should be no problem")
        self.assertRaises(Exception, self.repository.save(s))
    
    def testChooseObject(self):
        ch = self.repository.chooseObject()
        
        self.assertTrue(ch in self.repository.objects, "Choice must be in repository")

if __name__ == '__main__':
    unittest.main()