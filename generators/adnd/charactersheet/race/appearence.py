import random
import os

def roll(race,gender):
    appearence=''

    file = "/generators/adnd/charactersheet/resources/human/appearence.txt"
    path=os.getcwd()+file
    fp=open(path,'r+');
    with open(path,"r") as text_file:
        appearencelist=text_file.readlines()
        text_file.close()

    appearence=random.choice(appearencelist)
    appearence=appearence.rstrip('\n')

    if '@' in appearence:
        x=appearence.split('@')
        if gender== "Male":
            appearence=x[0]
        else:
            appearence=x[1]

    return appearence
