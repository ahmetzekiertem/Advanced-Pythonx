#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:44:11 2019

@author: mac
"""

def kareleri_al():
    sonuc = []
    
    for i in range(1,6):
        
        sonuc.append(i**2)
        
    return sonuc
    
print(kareleri_al())


""" Eger yuz bin sayiyla bu islemi yapsaydik listenin icinde saklayamazdik, eger yapsaydik
 bellegi isgal etmis olurduk."""
 

def kareleri_al2():
    for i in range(1,6):
        yield i ** 2
        
generator = kareleri_al2()

# Biz sadece istedigimizde uretilecek/

iterator = iter(generator)

print(next(iterator))

print(next(iterator))
print(next(iterator))

print(next(iterator))

print(next(iterator))

iterator2 = iter(generator)

"Eger degerleri uretmek ve gormek yani hicbir yerde saklamak istemiyorsan generatorlari kullaniriz."
 
liste1 = [i**3 for i in range(5)]

print(liste1)

generator2 = (i**3 for i in range(5))

print(generator2)

iterator3 = iter(generator2)

print(next(iterator3))
print(next(iterator3))
print(next(iterator3))
print(next(iterator3))

def carpim_tablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} * {} = {}".format(i,j,i*j)
            
for i in carpim_tablosu():
    print(i)
    
# Range fonksiyonu generator seklinde yazilmiz bir fonksiyon.



