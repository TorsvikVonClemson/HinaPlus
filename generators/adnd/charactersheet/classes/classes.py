import random

def roll(race):

    classroll=random.randint(1,100)
    x='!!!check for errors!!!'

    if race == 'Human' or race=='Foreigner':
        if classroll >=1 and classroll <=30:
            x='Fighter'

        elif classroll >=31 and classroll <=35:
            x='Paladin'

        elif classroll >=36 and classroll <=40:
            x='Ranger'

        elif classroll >=41 and classroll <=60:
            x='Rogue'

        elif classroll >=61 and classroll <=70:
            x='Bard'

        elif classroll >=71 and classroll <=90:
            x='Cleric'

        elif classroll >=91 and classroll <=100:
            x='Wizard'


    elif race == 'Half-Elf':
        if classroll >=1 and classroll <=30:
            x='Fighter'

        elif classroll >=31 and classroll <=40:
            x='Ranger'

        elif classroll >=41 and classroll <=60:
            x='Rogue'

        elif classroll >=61 and classroll <=80:
            x='Bard'

        elif classroll >=81 and classroll <=90:
            x='Cleric'

        elif classroll >=91 and classroll <=100:
            x='Wizard'

    elif race == 'Dwarf':
        if classroll >=1 and classroll <=35:
            x='Fighter'

        elif classroll >=36 and classroll <=40:
            x='Paladin'

        elif classroll >=41 and classroll <=60:
            x='Rogue'

        elif classroll >=61 and classroll <=70:
            x='Bard'

        elif classroll >=71 and classroll <=100:
            x='Cleric'

    elif race == 'Halfling':
        if classroll >=1 and classroll <=30:
            x='Fighter'

        elif classroll >=41 and classroll <=70:
            x='Rogue'

        elif classroll >=71 and classroll <=80:
            x='Bard'

        elif classroll >=71 and classroll <=90:
            x='Cleric'

        elif classroll >=91 and classroll <=100:
            x='Wizard'

    elif race == 'Wood Elf':
        if classroll >=1 and classroll <=25:
            x='Fighter'

        elif classroll >=26 and classroll <=50:
            x='Barbarian'

        elif classroll >=51 and classroll <=62:
            x='Rogue'

        elif classroll >=63 and classroll <=75:
            x='Bard'

        elif classroll >=76 and classroll <=100:
            x='Druid'

    elif race == 'Orc Merchant':
        if classroll >=1 and classroll <=25:
            x='Fighter'

        elif classroll >=26 and classroll <=55:
            x='Barbarian'

        elif classroll >=56 and classroll <=80:
            x='Rogue'

        elif classroll >=81 and classroll <=95:
            x='Cleric'

        elif classroll >=96 and classroll <=100:
            x='Shaman'

    elif race == 'Goblin Merchant':
        if classroll >=1 and classroll <=5:
            x='Fighter'

        elif classroll >=6 and classroll <=20:
            x='Barbarian'

        elif classroll >=21 and classroll <=50:
            x='Rogue'

        elif classroll >=51 and classroll <=75:
            x='Cleric'

        elif classroll >=76 and classroll <=100:
            x='Shaman'

    elif race == 'Kobold Pilgrim':
        if classroll >=1 and classroll <=20:
            x='Fighter'

        elif classroll >=21 and classroll <=70:
            x='Rogue'

        elif classroll >=71 and classroll <=100:
            x='Cleric'

    elif race == 'Oni':
        x='Fighter-Sorcerer'

    elif race == 'Elven Spy':
        if classroll >=1 and classroll <=40:
            x='Fighter'

        elif classroll >=41 and classroll <=70:
            x='Rogue'

        elif classroll >=71 and classroll <=100:
            x='Cleric'

    elif race == 'Drow Refugee':
        if classroll >=1 and classroll <=50:
            x='Fighter'

        elif classroll >=51 and classroll <=100:
            x='Rogue'

    elif race == 'Fairy':
        x='NoClass'
    elif race == 'Ogre':
        x='Fighter'
    else:x='!!!check for errors!!!'

    return str(x)
