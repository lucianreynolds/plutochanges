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


def list2dict(plutolist):
    listprep = []
    plutodict = {}
    for a in range(len(plutolist[0])):
        step = a
        plutodict[plutolist[0][a]] = step

##    pprint.pprint(plutodict)
    
##        step = int(a)
##        listprep.append[step]
##        plutodict = dict(zip(listprep,plutolist))        
    return plutodict

#OLD PLUTO: reads and loads
print('Reading PLUTO ' + oldPlutoName + '...')

oldPlutoFile = open(oldPluto)
oldPlutoReader = csv.reader(oldPlutoFile)
oldPlutoData = list(oldPlutoReader)
# Creates Column Lookup Dict
oldPlutoDict = {}
oldPlutoDict = list2dict(oldPlutoData)
oPD = oldPlutoDict
#pprint.pprint(oldPlutoDict)
##print(str(oldPlutoDict))

#TODO: Create dictionaries from column headers and position numbers

#NEW PLUTO: reads and loads
##print('Reading PLUTO ' + newPlutoName + '...')

newPlutoFile = open(newPluto)
newPlutoReader = csv.reader(newPlutoFile)
newPlutoData = list(newPlutoReader)
# Creates Column Lookup Dict
newPlutoDict = {}
newPlutoDict = list2dict(newPlutoData)
nPD=newPlutoDict
print(len(newPlutoData))
#pprint.pprint(newPlutoDict)
#TODO: Compare and append changes into a list.

##print('Contrasting data...')

changelist = []

for i in range(len(newPlutoData)):
    try:
        print(oldPlutoData.index(newPlutoData[i][nPD['BBL']]))
    except ValueError:
        continue


##    newPlutoBBL = newPlutoData[i][nPD['BBL']]
##    print(newPlutoData[i][nPD['BBL']])
##    print(oldPlutoData[i][oPD['BBL']])
    print('-------------')
    
    try:
        oldPlutoData.index(newPlutoBBL)
        print(oldPlutoData.index(newPlutoBBL))
    except ValueError:
        continue

##for x in range(len(oldPlutoData[0])):
##    print(str(x) + oldPlutoData[0][x])
