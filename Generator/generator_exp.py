#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:23:05 2019

@author: mac
"""

class Kuvvet3():
    def __init__(self,max=0):
        
        self.max = max
        self.kuvvet = 0
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        if (self.kuvvet <= self.max):
            sonuc = 3**self.kuvvet
            
            self.kuvvet +=1
            
            return sonuc
        else:
            raise StopIteration
            

kuvvet = Kuvvet3(6)

iterator = iter(kuvvet)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


def fibonacci():
    
    a=1
    b=1
    yield a
    yield b
    
    while True:
        
        a,b = b, a+b
        
        yield b
        
for sayi in fibonacci():
    if (sayi >100000):
        break
    print(sayi)