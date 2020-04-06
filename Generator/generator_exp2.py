#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:52:38 2019

@author: mac
"""

class Kareler():
    
    def __init__(self,maksimum):
        self.maksimum = maksimum
        
        self.sayı = 1
        
    def __iter__(self):
        return self
    def __next__(self):
        
        if (self.sayı <= self.maksimum):
            
            sonuc =  self.sayı ** 2
            self.sayı += 1
            return sonuc
        else:
            self.sayı = 1
            raise StopIteration



def asal_mı(sayı):
    i =  2
    
    while i < sayı:
        if (sayı % i == 0):
            return False
        i += 1
    return True
def asal_generator():
    i =  2
    while True:
        if (asal_mı(i)):
            yield i
        i += 1

for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)
        
    