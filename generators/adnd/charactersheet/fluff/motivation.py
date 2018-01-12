import random
import os

def roll(race,deity,playerclass):
    if race=="Human":
        file = "/generators/adnd/charactersheet/resources/human/humanmotives.txt"
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            motivelist=text_file.readlines()
            text_file.close()
        motive=random.choice(motivelist)
        motive=motive.rstrip('\n')

        if "[family]" in motive:
            file = "/generators/adnd/charactersheet/resources/human/humanfamily.txt"
            path=os.getcwd()+file
            fp=open(path,'r+');
            with open(path,"r") as text_file:
                familylist=text_file.readlines()
                text_file.close()
            motive=motive.replace("[family]",random.choice(familylist).rstrip('\n')) 
    
        if "[antagonist]" in motive:
            file = "/generators/adnd/charactersheet/resources/human/humanantagonists.txt"
            path=os.getcwd()+file
            fp=open(path,'r+');
            with open(path,"r") as text_file:
                antagonistlist=text_file.readlines()
                text_file.close()
            motive=motive.replace("[antagonist]",random.choice(antagonistlist).rstrip('\n'))  
    
        if "[villain]" in motive:
            file = "/generators/adnd/charactersheet/resources/human/humanvillains.txt"
            path=os.getcwd()+file
            fp=open(path,'r+');
            with open(path,"r") as text_file:
                villainlist=text_file.readlines()
                text_file.close()
            motive=motive.replace("[villain]",random.choice(villainlist).rstrip('\n')) 
    
        if "[monster]" in motive:
            file = "/generators/adnd/charactersheet/resources/human/humanmonsters.txt"
            path=os.getcwd()+file
            fp=open(path,'r+');
            with open(path,"r") as text_file:
                monsterlist=text_file.readlines()    
                text_file.close()    
            motive=motive.replace("[monster]",random.choice(monsterlist).rstrip('\n'))

        if "[protagonist]" in motive:
            file = "/generators/adnd/charactersheet/resources/human/humanprotagonists.txt"
            path=os.getcwd()+file
            fp=open(path,'r+');
            with open(path,"r") as text_file:
                protagonistlist=text_file.readlines()
                text_file.close()
            motive=motive.replace("[protagonist]",random.choice(protagonistlist).rstrip('\n'))                    

    if "[deity]" in motive:
        motive=motive.replace("[deity]",deity) 

    if "[class]" in motive:
        motive=motive.replace("[class]",playerclass) 

    return motive   
