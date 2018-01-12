import random
def roll(playerclass,conadj):

#---Remove String Symbols---#

    conadj=conadj.lstrip('-')
    conadj=conadj.lstrip('+')
    conadj=conadj.rstrip('*')
    conadj=conadj.rstrip(')')
    if conadj.find('(') != -1:
        conadjlist=conadj.split('(')
        if playerclass=='Fighter' or playerclass=='Paladin' or playerclass=='Ranger':
            conadj=conadjlist[1]
            conadj=conadj.lstrip('+')
        else:
            conadj=conadjlist[0]
    conadj=int(conadj)


    if playerclass=='Fighter' or playerclass=='Paladin' or playerclass=='Ranger':
        hp=random.randint(1,10)+conadj
    elif playerclass=='Wizard':
        hp=random.randint(1,4)+conadj
    elif playerclass=='Rogue' or playerclass=='Bard':
        hp=random.randint(1,6)+conadj
    elif playerclass=='Cleric':
        hp=random.randint(1,8)+conadj
    else:
        hp=420

    return hp
