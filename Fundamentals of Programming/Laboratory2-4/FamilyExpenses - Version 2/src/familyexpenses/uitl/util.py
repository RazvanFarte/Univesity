'''
Created on 24 oct. 2016

@author: Dell
'''

def is_int(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    pass