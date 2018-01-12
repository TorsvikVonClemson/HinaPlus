import random
import os

def roll(race):
    if race=="Human":
        file = "/generators/adnd/charactersheet/resources/human/humanhair.txt"
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            hairlist=text_file.readlines()
            text_file.close()
        hair=random.choice(hairlist)
        hair=hair.rstrip('\n')
    return str(hair)
