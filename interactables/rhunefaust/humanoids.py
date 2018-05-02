import os
import fnmatch
import random



def humanoids():
    #TODO: De-hardcode number of players

    size=0
    a='\n'
    b=''
    d=''
    herolist=[]
    henchmanlist=[]


    i=0
    while int(i) < 2:
        roll = random.randint(1, 6)
        size+=roll
        i += 1

    heroes=0
    while heroes==0 or heroes>3 and not heroes>size:
        heroes=random.randint(1, 4)+1

    #give magic here

    henchmen=0
    if heroes!=size:
        while henchmen>heroes or henchmen>3 or henchmen>size-heroes or henchmen==0:
            henchmen=random.randint(1, 4)+1

    while heroes>0:
        HP=random.randint(1, 4)
        AC=6
        THACO=19
        DMG=6
        herolist.append("Hero: HP:" + str(HP) +'   AC:' +str(AC) +'   THAC0:' +str(THACO)+'   DMG:' + str(DMG))

        heroes-=1


    while henchmen>0:
        HP=random.randint(1, 4)
        AC=10
        THACO=20
        DMG=4
        henchmanlist.append("Henchman: HP:" + str(HP) +'   AC:' +str(AC) +'   THAC0:' +str(THACO)+'   DMG:' + str(DMG))
        henchmen-=1

    return ('\n'+'\n'.join(herolist)+'\n\n'+'\n'.join(henchmanlist))


