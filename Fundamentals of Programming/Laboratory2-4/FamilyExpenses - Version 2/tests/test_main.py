'''
Created on 25 oct. 2016

@author: Dell
'''
from tests.domain.test_operations import test_all_operations
from tests.util.test_utils import test_all_utils
from tests.domain.test_entities import test_all_entities

def test_all():
    test_all_operations()
    test_all_utils()
    test_all_entities()

if __name__ == '__main__':
    test_all()