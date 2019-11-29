# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:22:00 2019

@author: Thanga
"""

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary
    def __add__(self, no):
        return complex(self.i+no.r, self.i+no.i)
    def __sub__(self, no):
        return complex(self.i-no.r, self.i-no.i)
    def __mul__(self, no):
        return complex(self.i*no.r, self.i*no.i)
    def __truediv__(self, no):
        try: 
            return self.__mul__(complex(no.r, -1*no.i)).__mul__(complex(1.0/(no.mod().r)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None
    def mod(self):
        return complex(pow(self.real**2+self.imag**2, 0.5), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, '2,1'.split(','))
    d = map(float, '5,6'.split(','))
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
