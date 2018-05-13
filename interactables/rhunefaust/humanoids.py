import os
import fnmatch
import random



def humanoids(partysize,level,race):

    file = "/interactables/rhunefaust/Races/{}.txt"
    path = os.getcwd() + file
    racepath=path.format(race)

    with open(racepath, "r") as text_file:
        workingfile = text_file.readlines()
    text_file.close()


    size=0
    a='\n'
    b=''
    d=''
    herolist=[]
    henchmanlist=[]
    MAAlist=[]



    for i in range(2):
        size+=random.randint(1,6)

    heroes=0
    while heroes==0 or heroes>size or heroes>partysize:
        heroes=random.randint(1, 4)+1

    #give magic here

    henchmen=0
    if size-heroes>1:
        while henchmen>heroes or henchmen>partysize or henchmen>size-heroes or henchmen==0:
            henchmen=random.randint(1, 4)+1

    for i in range(heroes):
        HP=0
        for i in range(level):
            HP+=random.randint(1, int(workingfile[3].rstrip('\n')))+ float(workingfile[4].rstrip('\n'))
        speed=random.randint(1,10)+int(workingfile[8].rstrip('\n'))
        AC=workingfile[1].rstrip('\n')
        THACO=21-level
        DMG= workingfile[5].rstrip('\n')
        magic=magicitems(level)
        herolist.append(workingfile[0].rstrip('\n')+" Hero:   HP: " + str(HP) +'   AC: ' +str(AC)
                        +'   THAC0: ' +str(THACO)+'   DMG: ' + str(DMG)+"   Speed: "+str(speed)
                        +'\n         '+'\n         '.join(magic))

    for i in range(henchmen):
        HP=0
        for i in range(level):
            HP+=random.randint(1, int(workingfile[3].rstrip('\n')))+ float(workingfile[4].rstrip('\n'))
        speed=random.randint(1,10)+int(workingfile[9].rstrip('\n'))
        AC=workingfile[2].rstrip('\n')
        THACO=21-int(level/2)
        DMG=workingfile[6].rstrip('\n')
        henchmanlist.append(workingfile[0].rstrip('\n')+ " Henchman:   HP: " + str(HP) +'   AC: ' +str(AC)
                            +'   THAC0: ' +str(THACO)+'   DMG: ' + str(DMG)+"   Speed: "+str(speed))

    if level>2:
        for i in range(size-heroes-henchmen):
            HP=0
            for i in range(int(level/3)):
                HP+=random.randint(1,  int(workingfile[3].rstrip('\n')))+ float(workingfile[4].rstrip('\n'))
            speed = random.randint(1, 10)
            AC=int(workingfile[2].rstrip('\n'))+2
            THACO=21-int(level/6)
            DMG=workingfile[7].rstrip('\n')
            MAAlist.append(workingfile[0].rstrip('\n')+ " Man-at-Arms:   HP: " + str(HP) +'   AC: ' +str(AC) +'   THAC0: '
                       +str(THACO)+'   DMG: ' + str(DMG)+"   Speed: "+str(speed))

    return ('\n'+'\n'.join(herolist)+'\n\n'+'\n'.join(henchmanlist)+'\n\n'+'\n'.join(MAAlist)+'\n\nParty Morale is: '+
            workingfile[10]+workingfile[12])

def magicitems(level):
    items=[]
    if level==1:
        if random.randint(1,10)==1:
            itemlist =getitem('1')
            items.append(random.choice(itemlist).rstrip('\n'))


    if level==2:
        if random.randint(1,5)==1:
            itemlist =getitem('1')
            for i in range(2):
                items.append(random.choice(itemlist).rstrip('\n'))

    if level==3:
        if random.randint(1,3)==1:
            itemlist =getitem('1')
            for i in range(2):
                items.append(random.choice(itemlist).rstrip('\n'))
        if random.randint(1,10)==1:
            itemlist =getitem('2')
            items.append(random.choice(itemlist).rstrip('\n'))

    return items

def getitem(table):
    file = "/interactables/rhunefaust/Item Tables/{}.txt".format(table)
    path = os.getcwd() + file
    fp = open(path, 'r+');
    with open(path, "r") as text_file:
        itemlist = text_file.readlines()
        text_file.close()
    return itemlist