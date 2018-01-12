import random

def roll(race):

    genderroll=random.randint(1,100)

    if race == 'Human':
        if genderroll<=75:
            x='Male'
        else: x='Female'

    elif race == 'Half-Elf':
        if genderroll<=33:
            x='Male'
        else: x='Female'

    elif race == 'Dwarf':
        if genderroll<=99:
            x='Male'
        else: x='Female'

    elif race == 'Halfling':
        if genderroll<=75:
            x='Male'
        else: x='Female'

    elif race == 'Wood Elf':
        if genderroll<=50:
            x='Male'
        else: x='Female'

    elif race == 'Orc Merchant':
        x='Male'

    elif race == 'Goblin Merchant':
        x='Male'
 
    elif race == 'Kobold Pilgrim':
        if genderroll<=50:
            x="""yabba-de'gap"""
        else: x="""Soppu'bogh"""

    elif race == 'Foreigner':
        if genderroll<=75:
            x='Male'
        else: x='Female'

    elif race == 'Oni':
        if genderroll<=90:
            x='Male'
        else: x='Female'

    elif race == 'Elven Spy':
        if genderroll<=50:
            x='Male'
        else: x='Female'

    elif race == 'Drow Refugee':
        x='Female'

    elif race == 'Fairy':
        if genderroll<=50:
            x='Male'
        else: x='Female'

    elif race == 'Ogre':
        x='Male'

    else:x='!!!check for errors!!!'

    return str(x)
