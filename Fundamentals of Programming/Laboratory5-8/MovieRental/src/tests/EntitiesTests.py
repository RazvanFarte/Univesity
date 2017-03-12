'''
Created on 29 dec. 2016

@author: Dell
'''
from unittest.case import TestCase
from movie.domain.entities.Client import Client
from movie.domain.entities.Movie import Movie
from movie.domain.entities.Rental import Rental
import datetime

class ClientTest(TestCase):
    def setUp(self):
        self.__client1 = Client(1,"Lamaiel")
        self.__client2 = Client(2,"Mandarin")

    def testGettes(self):
        self.assertEqual(self.__client1.get_entity_id(), 1, "Client 1 id must be 1")
        self.assertEqual(self.__client2.get_entity_id(), 2, "Client 2 id must be 2")
        
        self.assertEqual(self.__client1.get_entity_name(), "Lamaiel", "Client 1 has name Lamaiel")
        self.assertEqual(self.__client2.get_entity_name(), "Mandarin", "Client 1 has name Mandarin")
        
    def testSetters(self):
        self.__client1.set_entity_name("Portocal")
        self.assertEqual(self.__client1.get_entity_name(), "Portocal", "Client 1 has name Portocal now")
        
    def testEqual(self):
        self.assertFalse(self.__client1 == self.__client2, "Client 1 and client 2 are not the same")
        
        try:
            self.__client1 == Movie(1, "Da", "Da", "Da")
            self.fail("A client cannot be a movie")
        except TypeError:
            pass

class MovieTest(TestCase):
    
    def setUp(self):
        self.__movie1 = Movie(1,"Da","Da","Da")
        self.__movie2 = Movie(2,"Nu", "Nu", "Nu")


    def testGettes(self):
        self.assertEqual(self.__movie1.get_entity_id(), 1, "Movie 1 id must be 1")
        self.assertEqual(self.__movie2.get_entity_id(), 2, "Movie 2 id must be 2")
        
        self.assertEqual(self.__movie1.get_entity_name(), "Da", "Movie 1 has name Da")
        self.assertEqual(self.__movie2.get_entity_name(), "Nu", "Movie 2 has name Nu")
        
        self.assertEqual(self.__movie1.get_entity_description(), "Da", "Movie 1 has description Da")
        self.assertEqual(self.__movie2.get_entity_description(), "Nu", "Movie 2 has description Nu")
        
        self.assertEqual(self.__movie1.get_entity_genre(), "Da", "Movie 1 has gendre Da")
        self.assertEqual(self.__movie2.get_entity_genre(), "Nu", "Movie 2 has gendre Nu")

        
    def testSetters(self):
        
        self.__movie1.set_entity_name("Nu")
        self.assertEqual(self.__movie1.get_entity_name(), "Nu", "Movie 1 has name Nu now")
        self.__movie2.set_entity_name("Da")
        self.assertEqual(self.__movie2.get_entity_name(), "Da", "Movie 2 has name Da now")
        
        self.__movie1.set_entity_description("Nu")
        self.assertEqual(self.__movie1.get_entity_description(), "Nu", "Movie 1 has description Nu now")
        self.__movie2.set_entity_description("Da")
        self.assertEqual(self.__movie2.get_entity_description(), "Da", "Movie 2 has description Da now")
        
        self.__movie1.set_entity_genre("Nu")
        self.assertEqual(self.__movie1.get_entity_genre(), "Nu", "Movie 1 has gendre Nu now")
        
        
    def testEqual(self):
        self.assertFalse(self.__movie1 == self.__movie2, "Movie 1 and movie 2 are not the same")
        
        try:
            self.__movie1 == Client(1, "Da")
            self.fail("A Movie cannot be a Client")
        except TypeError:
            pass
        
    #TODO Should I create also a test for __str__ method? Is it normal to test if the string is returned properly?

class RentalTest(TestCase):
    
    
    
    def setUp(self):
        self.__rental1 = Rental(1, 1, 1, datetime.date(1997,10,20), datetime.date(1997,10,27), datetime.date(1997,10,23))
        self.__rental2 = Rental(None, 1, 1, datetime.date(1997,10,20), datetime.date(1997,10,20), None)
    
    def tearDown(self):
        TestCase.tearDown(self)
        Rental.rentalCounter -= 2

    def testGettes(self):
        self.assertEqual(self.__rental1.get_entity_id(), 1, "Rental 1 id must be 1")
        self.assertEqual(self.__rental2.get_entity_id(), 2, "Rental 2 id must be 2")
        self.assertEqual(self.__rental1.get_client_id(), 1, "Rental 1 has client id 1")
        self.assertEqual(self.__rental1.get_movie_id(), 1, "Rental 1 has movie id 1")
        
        self.assertEqual(self.__rental1.get_rented_date(), datetime.date(1997,10,20), "Date mismatch")
        self.assertEqual(self.__rental1.get_due_date(), datetime.date(1997,10,27), "Date mismatch")
        self.assertEqual(self.__rental1.get_returned_date(), datetime.date(1997,10,23), "Date mismatch")

        
    def testSetters(self):
        
        self.__rental1.set_due_date(None)
        self.assertEqual(self.__rental1.get_due_date(), None, "Date mismatch")
        
        self.__rental1.set_rented_date(None)
        self.assertEqual(self.__rental1.get_rented_date(), None, "Date mismatch")
        
        self.__rental1.set_returned_date(None)
        self.assertEqual(self.__rental1.get_returned_date(), None, "Date mismatch")

        
    def testEqual(self):
        self.assertFalse(self.__rental1 == self.__rental2, "Rental 1 and Rental 2 are not the same")
        
        try:
            self.__rental1 == Client(1, "Da")
            self.fail("A Rental cannot be a Client")
        except TypeError:
            pass