#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:03:46 2019

@author: mac
"""


import time
        
def zaman_hesapla(func):
    def wrapper(sayiler):
        
        basla = time.time()
        
        sonuc = func(sayiler)
        
        bitis = time.time()
        
        print(func.__name__ + " " + str(bitis - basla) + " saniye surdu." )
        
        return sonuc
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuc = []
    
    
    for i in sayılar:
        sonuc.append(i ** 2)
    
    return sonuc
 
@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuc = []
    
    for i in sayılar:
        sonuc.append(i ** 3)
        
    return sonuc
   
 
    
kareleri_hesapla(range(10099000))



