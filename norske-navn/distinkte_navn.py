#!/usr/bin/env python
# encoding: utf-8
"""
Hvis jeg skal lage en loop-up tabell trenker jeg fornavn på menn og kvinner og bruke look-up på de som KUN brukes på et av kjønnene.

Trenger å håndtere CAP og Camel-case bedre, og kanskje dobbeltnavn?

Returnerer pr nå tupler med inputnavn og kjønn

Data fra: https://github.com/georgboe/norske-navn
Created by Eirik Stavelin on 2013-08-04.
Copyright (c) 2013 Eirik Stavelin. All rights reserved.
"""

import sys
import os

class noNamesLookup:
    ''' class to lookup gender from First names in Norwegian'''

    def __init__(self):
        self.jente_liste = []
        self.gutte_liste = []
        # jenter = last_jenter()
        # gutter = last_gutter()
        # begge = self.intersect(jenter, gutter) # [u'Inge\n', u'Kim\n', u'Tonny\n', u'Thanh\n', u'Marian\n'] ?? Har sjekket, det stemmer...
        self.jenter = self.last_jenter()
        self.gutter = self.last_gutter()
        self.begge = self.intersect(self.jenter, self.gutter)

    def intersect(self, a, b):
         return list(set(a) & set(b))

    def last_jenter(self):
        jenter = open("jentenavn.txt", 'U') #.read()
        for j in jenter:
            self.jente_liste.append(j.decode("utf8").rstrip())
        return self.jente_liste

    def last_gutter(self):
        gutter = open("guttenavn.txt", "U")
        for g in gutter:
            self.gutte_liste.append(g.decode("utf8").rstrip())
        return self.gutte_liste
    
    def get_gender(self, name):
        name = name.decode("utf8")      # Her forventer vi noen André-er og Åshilder og Øyvinder..
        if name in self.begge:
            return (name, u"begge")
        elif name in self.jenter:
            return (name, u"kvinne")
        elif name in self.gutter:
            return (name, u"man")
        else:
            return (name, u"ikke funnet, kjør AI eller flipp en mynt")

    
if __name__ == '__main__':
    names = noNamesLookup()
    print names.get_gender("Eirik")
    print names.get_gender("Kjartan")
    print names.get_gender("Sindre")
    print names.get_gender("Pål")
    print names.get_gender("Øyvind")
    print names.get_gender("André")
    print names.get_gender("Kim")   # vanligst blant menn i Norge, antar jeg?
    
    print names.get_gender("Cathrine")
    print names.get_gender("Inger")
    print names.get_gender("Siri")
    print names.get_gender("Camilla")
    print names.get_gender("Linn")
    print names.get_gender("Olga")
    print names.get_gender("Åse")
    print names.get_gender("Siri-Kathrine")    # 
    
    print names.get_gender("Anne-Britt")
    print names.get_gender("Anne Marie")
    print names.get_gender("May-britt")    # bussig med listen b?
    print names.get_gender("Siri-Kathrine")           