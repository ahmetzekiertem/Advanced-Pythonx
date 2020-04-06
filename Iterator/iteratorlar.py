#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:02:10 2019

@author: mac
"""

# Iter() ve next() kesinlikle tanimlanmali



liste = [1,2,3,4,5]

iterator = iter(liste) # Iterator oluşturma

print(iterator)
print(next(iterator)) # next metoduyla sıradaki eleman
print(next(iterator)) # next metoduyla sıradaki eleman
print(next(iterator)) # next metoduyla sıradaki eleman
print(next(iterator)) # next metoduyla sıradaki eleman
print(next(iterator)) # next metoduyla sıradaki eleman

"""Pyton biz gormesekde for dongulerini kullanirken Iterator kullaniyor 

liste = [1,2,3,4,5]
for i in liste
    print(i) """


liste = [1,2,3,4,5]
 
iterator = iter(liste)
 
while True:
    try:
        print(next(iterator))
        
    except StopIteration:
        break
    

class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi # Kanal Listemiz
        self.index = -1 # İndeksimiz
        
    def __iter__(self):
        return self # iterator oluşturduğumuzda (iter fonksiyonu çağrıldığında )objemizi döneceğiz.
    def __next__(self): # next fonksiyonu çağrıldığında burası çalışacak.
        self.index += 1
        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration
            
kumanda = Kumanda(["Kanal d","Trt","Atv","Fox","Bloomberg"]) # Objemizi oluşturuyoruz.
 
iterator =  iter(kumanda) # Objemiz iterable olduğu için iterator oluşturulabilir.
 
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))