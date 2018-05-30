import random

def roll(race,playerclass):
    
    classvalid=0
    racevalid=0
    p=[]
    n=[]
    

    while (classvalid==0 or racevalid==0):  
        p=[]
        num=6
        while num>0:
            
            rolls=4
            while rolls>0:

                    roll = random.randint(1,6)
                    n.append(roll)
                    rolls -= 1
            n.sort(key=None,reverse=1)
            attribute=n[0]+n[1]+n[2]
            p.append(attribute)
            num -= 1
            n=[]

#---------------------------#
# Racial Mods and 18/xx Str #
#---------------------------#

        ##p[0]=18 #18/xx Str test


        if race=='Dwarf':
            p[2]=p[2]+1
            p[5]=p[5]-1

        if race=='Elf':
            p[1]=p[1]+1
            p[2]=p[2]-1

        if race=='Gnome':
            p[3]=p[3]+1
            p[4]=p[4]-1

        if race=='Halfling':
            p[1]=p[1]+1
            p[0]=p[0]-1

        if playerclass=='Fighter' and p[0]==18:
             p[0]=str(p[0])+"/"+str(random.randint(1,100))
             if p[0]=="18/100":
                p[0]='18/00'

#--------------------#
# Check for validity #
#--------------------#

#----------------#
# Class validity #
#----------------#
        
        if playerclass=='Fighter':
            p[0]=str(p[0])
            if p[0].find('/') != -1:
                classvalid=1
            else:
                p[0]=int(p[0])
                if p[0]>8:
                    classvalid=1

        elif playerclass in ['Paladin','Green Knight']:
            if p[0]>=12 and p[2]>=9 and p[4]>=13 and p[5]>=17:
                classvalid=1

        elif playerclass=='Ranger':
            if p[0]>=13 and p[1]>=13 and p[2]>=14 and p[4]>=14:
                classvalid=1

        elif playerclass=='Wizard': # Remember to add specialists
            if p[3]>=9:
                 classvalid=1

        elif playerclass=='Cleric':
            if p[4]>=9:
                classvalid=1

        elif playerclass=='Druid':
            if p[4]>=12 or p[5]>=15:
                classvalid=1

        elif playerclass=='Rogue':
            if p[1]>=9:
                classvalid=1

        elif playerclass=='Bard':
            if p[1]>=12 and p[3]>=13 and p[5]>=15:
                classvalid=1
        else: classvalid=0

#---------------#
# Race Validity #
#---------------#

        if race=='Dwarf':
            if (p[0]<8 or p[0]>=19) or (p[1]<3 or p[1]>17) or (p[2]<11 or p[2]>18) or (p[3]<3 or p[3]>18) or (p[4]<3 or p[4]>18) or (p[5]<3 or p[5]>17):
                p=[]
            else: racevalid=1

        elif race=='Elf':
            if (p[0]<3 or p[0]>=19) or (p[1]<6 or p[1]>18) or (p[2]<7 or p[2]>18) or (p[3]<8 or p[3]>18) or (p[4]<3 or p[4]>18) or (p[5]<8 or p[5]>18):
                p=[]
            else: racevalid=1

        elif race=='Gnome':
            if (p[0]<6 or p[0]>=19) or (p[1]<3 or p[1]>18) or (p[2]<8 or p[2]>18) or (p[3]<6 or p[3]>18) or (p[4]<3 or p[4]>18) or (p[5]<3 or p[5]>18):
                p=[]
            else: racevalid=1

        elif race=='Half-Elf':
            if (p[0]<3 or p[0]>=19) or (p[1]<6 or p[1]>18) or (p[2]<6 or p[2]>18) or (p[3]<4 or p[3]>18) or (p[4]<3 or p[4]>18) or (p[5]<3 or p[5]>18):
                p=[]
            else: racevalid=1

        elif race=='Halfling':
            if (p[0]<7 or p[0]>=19) or (p[1]<7 or p[1]>18) or (p[2]<10 or p[2]>18) or (p[3]<6 or p[3]>18) or (p[4]<3 or p[4]>18) or (p[5]<3 or p[5]>18):
                p=[]
            else: racevalid=1

        else: racevalid=1

    return p

