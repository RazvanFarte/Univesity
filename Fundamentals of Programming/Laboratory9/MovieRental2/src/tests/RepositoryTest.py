'''
Created on 14 dec. 2016

@author: Dell
'''
from unittest import TestCase
from movie.repo.Repository import Repository
from movie.repo.RepositoryException import RepositoryException
from movie.domain.validators.ClientValidator import ClientValidator
from movie.domain.entities.Client import Client

class RepositoryTest(TestCase):

    def setUp(self):
        self.__clientRepository = Repository(ClientValidator)
        
        self.__client1 = Client(1, "Aurel")
        self.__client2 = Client(2, "Viorel")
        self.__clientRepository.save(self.__client1)
        self.__clientRepository.save(self.__client2)
        
    def testSave(self):
        #We need an empty repo for this test
        self.__clientRepository = Repository(ClientValidator)
        
        self.assertTrue(self.__clientRepository.save(self.__client1), "Could not create student")
        self.assertTrue(self.__clientRepository.save(self.__client2), "Could not create student")
        
#         self.assertRaises(RepositoryException, self.__clientRepository.save(self.__client1))

        try:
            self.__clientRepository.save(self.__client1)
            self.fail("Duplicate ID at saving")
        except RepositoryException:
            pass
        
        try:
            self.__clientRepository.save(self.__client2)
            self.fail("Duplicate ID at saving")
        except RepositoryException:
            pass
        
        try:
            self.__clientRepository.save(Client("ab", "Ada"))
            self.fail("ID must be an integer")
        except RepositoryException:
            pass
        
        self.assertEqual(len(self.__clientRepository.get_all()), 2, "There must be 2 clients already saved")
        self.assertEqual(self.__clientRepository.find_by_id(1), self.__client1, "Client 1 was not save properly")
        self.assertEqual(self.__clientRepository.find_by_id(2), self.__client2, "Client 2 was not save properly")
        
    def testRemove(self):
        #These 2 lines are almost same thing
        self.assertEqual(self.__clientRepository.remove(1), self.__client1, "Client 1 was not deleted")
        self.assertEqual(self.__clientRepository.find_by_id(1), None, "Client 1 was not deleted properly")
        
        try:
            self.__clientRepository.remove(3)
            self.fail("There is no element 3 in repository")
        except RepositoryException:
            pass
        
        try:
            self.__clientRepository.remove(1)
            self.fail("There is no element 3 in repository")
        except RepositoryException:
            pass
         
        self.assertEqual(self.__clientRepository.remove(2), self.__client2, "Client 2 was not deleted")
         
        try:
            self.__clientRepository.remove(1)
            self.fail("Repository is empty")
        except RepositoryException:
            pass
         
    def testFindById(self):
        
        self.assertEqual(self.__clientRepository.find_by_id(1), self.__client1, "It does not return client 1")
        self.assertEqual(self.__clientRepository.find_by_id(2), self.__client2, "It does not return client 2")
        self.assertEqual(self.__clientRepository.find_by_id(3), None, "There is no client 3")
        
        
        clients = list(self.__clientRepository.get_all())
        
        self.assertEqual(len(clients), 2, "There must be 2 clients")
        self.assertEqual(clients[0],self.__client1,"This must be client 1")
        self.assertEqual(clients[1],self.__client2,"This must be client 2")
    
    
    def testUpdate(self):
        try:
            self.__clientRepository.update(3, Client(3,"Aurel"))
            self.fail("Client with id 3 does not exist")
        except RepositoryException:
            pass
        
        try:
            self.__clientRepository.update(1,Client(2,"Anakin"))
            self.fail("Id's mismatch. You are not allowed to change the Id.")
        except RepositoryException:
            pass
        
        self.__clientRepository.update(1,Client(1,"Antoniu"))
        self.assertEqual(self.__clientRepository.find_by_id(1).entityName, "Antoniu", "His name must be Antoniu")
        self.__clientRepository.update(1,Client(1,"Aurel"))
        self.assertEqual(self.__clientRepository.find_by_id(1).entityName, "Aurel", "His name must be Aurel")