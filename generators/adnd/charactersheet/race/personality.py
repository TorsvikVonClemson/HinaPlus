import random
import os

def roll(race):
    if race=="Human":
        file = "/generators/adnd/charactersheet/resources/minorpersonalities.txt"
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            minorlist=text_file.readlines()
            text_file.close()
        minor=random.choice(minorlist)
        minor=minor.rstrip('\n')
        file = "/generators/adnd/charactersheet/resources/majorpersonalities.txt"
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            majorlist=text_file.readlines()
            text_file.close()
        major=random.choice(majorlist)
        major=major.rstrip('\n')

        person=major+'/'+minor
    return person
