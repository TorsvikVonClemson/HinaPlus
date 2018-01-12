import random
import os

def roll(race):

    file = "/generators/adnd/charactersheet/resources/human/humaneyes.txt"
    path=os.getcwd()+file
    fp=open(path,'r+');
    with open(path,"r") as text_file:
        eyelist=text_file.readlines()
        text_file.close()
    eye=random.choice(eyelist)
    eye=eye.rstrip('\n')
    return eye
