import random

def roll():

    raceroll=random.randint(1,100)

    if raceroll >= 1 and raceroll <= 50:
        x='Human'

    elif raceroll >= 51 and raceroll <= 60:
        x='Half-Elf'

    elif raceroll >= 61 and raceroll <= 70:
        x='Dwarf'

    elif raceroll >= 71 and raceroll <= 80:
        x='Halfling'

    elif raceroll >= 81 and raceroll <= 83:
        x='Wood Elf'

    elif raceroll >= 84 and raceroll <= 86:
        x='Orc Merchant'

    elif raceroll >= 87 and raceroll <= 89:
        x='Goblin Merchant'

    elif raceroll >= 90 and raceroll <= 92:
        x='Kobold Pilgrim'

    elif raceroll >= 93 and raceroll <= 95:
        x='Foreigner'

    elif raceroll == 96:
        x='Oni'

    elif raceroll <= 97:
        x='Elven Spy'

    elif raceroll <= 98:
        x='Drow Refugee'

    elif raceroll <= 99:
        x='Fairy'

    elif raceroll <= 100:
        x='Ogre'

    else:x='!!!check for errors!!!'

    return str(x)
