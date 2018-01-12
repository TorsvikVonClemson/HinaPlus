import random
import os

def roll(race,playerclass):
    occ=''

    if playerclass=='Rogue':
        file = "/generators/adnd/charactersheet/resources/occupations/rogueoccupations.txt"
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            occlist=text_file.readlines()
            text_file.close()
    else:
        return ''

    occ=random.choice(occlist)
    occ=occ.rstrip('\n')

    return occ
