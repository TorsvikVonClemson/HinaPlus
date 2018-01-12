import random
import os

def roll(race,gender):
    facialhair=''
    if gender!="Female":
        file = "/generators/adnd/charactersheet/resources/human/humanfacialhair.txt"
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            facialhairlist=text_file.readlines()
            text_file.close()
        facialhair=random.choice(facialhairlist)
        facialhair=facialhair.rstrip('\n')
    return facialhair
