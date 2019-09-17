# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:01:01 2019

@author: Thangarajan
"""

def add(number):
    return number+1
print(add(10))

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")
parent()
second_child()
first_child()

