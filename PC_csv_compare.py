#python3
#this program compares the current
#Pluto CSV with the previous to
#discover changes, which are then
#documented in a txt file.

import csv,os,pprint

#TODO: Read log file to ascertain ultimate and
    #penultimate CSVs.

print(os.getcwd())
oldPluto = '../16v1/16v1.csv'
oldPlutoName = '16v1'
newPluto = '../16v2/16v2.csv'
newPlutoName = '16v2'

#Load CSVs into lists

#OLD PLUTO: reads and loads
print('Reading PLUTO ' + oldPlutoName + '...')

oldPlutoFile = open(oldPluto)
oldPlutoReader = csv.reader(oldPlutoFile)
oldPlutoData = list(oldPlutoReader)
oldBBLindex = oldPlutoData[0].index('BBL')
print(str(oldBBLindex))
print(len(oldPlutoData))

#TODO: Create dictionaries from column headers and position numbers

#NEW PLUTO: reads and loads
##print('Reading PLUTO ' + newPlutoName + '...')

##newPlutoFile = open(newPluto)
##newPlutoReader = csv.reader(newPlutoFile)
##newPlutoData = list(newPlutoReader)
##
##print(len(newPlutoData))

#TODO: Compare and append changes into a list.

##print('Contrasting data...')

##changelist = []

##for i in range(len(newPlutoData)):
##    newPlutoBBL = newPlutoData[i][70]
##    print(newPlutoData[i][70]
##    print(oldPlutoData[i][70])
##    print('-------------')
##    
##    try:
##        oldPlutoData.index(newPlutoBBL)
##        print(oldPlutoData.index(newPlutoBBL))
##    except ValueError:
##        continue

##for x in range(len(oldPlutoData[0])):
##    print(str(x) + oldPlutoData[0][x])
