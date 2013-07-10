#!/usr/bin/env python
# encoding: utf-8
"""
NOLoader.py
"""
import os
#import re
import urllib2
from zipfile import ZipFile
import csv
import pickle
import requests
        
def getNameList():
    if not os.path.exists('no_names.pickle'):
        print 'no_names.pickle does not exist, generating'
        if not os.path.exists('no_names.zip'):
            print 'no_names.zip does not exist, downloading from google docs'
            downloadNames() # laste ned zip
        else:
            print 'no_names.zip exists, not downloading'
    
        print 'Extracting names from no_names.zip'
        namesDict=extractNamesDict()
        
        maleNames=list()
        femaleNames=list()
        
        print 'Sorting Names'
        for name in namesDict:
            counts=namesDict[name] 
            
            tuple=(name,counts[0],counts[1]) #navn, antall_menn, antal_kvinnr
            # hvis et navn er vanligere for et kjønn settes navnet til det kjønnet
            if counts[0]>counts[1]:
                maleNames.append(tuple)
            elif counts[1]>counts[0]:
                femaleNames.append(tuple)
        #print maleNames
        names=(maleNames,femaleNames)
        
        print 'Saving names.pickle'
        fw=open('no_names.pickle','wb')
        pickle.dump(names,fw,-1)
        fw.close()
        print 'Saved no_names.pickle'
    else:
        print 'no_names.pickle exists, loading data'
        f=open('no_names.pickle','rb')
        names=pickle.load(f)
        print 'no_names.pickle loaded'
        
    print '%d male names loaded, %d female names loaded'%(len(names[0]),len(names[1]))
    
    return names
    
def downloadNames():
    """ function to download zipfile of names data"""
    pass
    # response = requests.get('https://docs.google.com/spreadsheet/pub?key=0AgAXDJuvjySMdDNyNlc0RGh1N19jYTZ0ajNvTTRqYlE&output=csv')
    # response2 = requests.get('https://docs.google.com/spreadsheet/pub?key=0AgAXDJuvjySMdDNyNlc0RGh1N19jYTZ0ajNvTTRqYlE&single=true&gid=1&output=csv')
    # assert response.status_code == 200, 'Wrong status code'
    # response2.raise_for_status()
    # print response.content
    # print response2.content
    # # u = urllib2.urlopen('https://github.com/downloads/sholiday/genderPredictor/names.zip')
    # localFile = open('no_names.zip', 'w')
    # localFile.write(response.content.text) # jentene
    # localFile.write(response2.content.text) # guttene
    # localFile.close()
    
def extractNamesDict():
    zf=ZipFile('no_names.zip', 'r')
    filenames=zf.namelist()
    
    names=dict()
    genderMap={'no_names/boys.csv':0,'no_names/girls.csv':1} #    genderMap={'M':0,'F':1}
    
    # her summeres alle med samme navn opp etter kjønn
    for filename in filenames:
        #print filename # osx creates fucking anoying __MACOSX folders!! http://stackoverflow.com/questions/10924236/mac-zip-compress-without-macosx-folder
        file=zf.open(filename,'rU')
        rows=csv.reader(file, delimiter=',')

        first_itteration = True
        for row in rows:
            print row
            if not first_itteration:         # skip first itteration (header)
                #print row                   # name, gender, number  ## nina, F, 132
                #print row[1:], sum(map(int, [i for i in row[1:] if i is not ':']))
                name=row[0].upper()          # NINA
                gender=genderMap[filename]   # 1
                # sum list when ':' are removed
                count = sum(map(int, [i for i in row[1:] if i is not ':']))           # 132
            else:
                first_itteration=False      # set flag
                continue                    # skip rest of itteration

            if not names.has_key(name):
                names[name]=[0,0]
            # Navn [antall menn, antall kvinner]
            #print type(names[name][gender]), name, gender
            names[name][gender]=names[name][gender]+count # <- her er trikset. genderMap endre første ELLER andre tall
            
        file.close()
        print '\tImported %s'%filename
    print names
    return names
if __name__ == "__main__":
    getNameList()
        