# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:03:32 2020

@author: Thanga
"""

def valid_age(age):
    if age>= 18:
        return True
    
def test_age(age):
    assert valid_age(age)==True, "age Should be 18"

if __name__ == "__main__":
    test_age(7)
    print("Everything passed")