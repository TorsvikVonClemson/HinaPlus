def roll(playerclass):
    if playerclass == 'Fighter' or playerclass == 'Ranger':
        ParaPoi = 14
        RSW = 16
        PetPoly = 15
        Breath = 17
        Spell = 17
    elif playerclass == 'Paladin':
        ParaPoi = 12
        RSW = 14
        PetPoly = 13
        Breath = 15
        Spell = 15
    elif playerclass == 'Rogue' or playerclass == 'Bard':
        ParaPoi = 13
        RSW = 14
        PetPoly = 12
        Breath = 16
        Spell = 15
    elif playerclass == 'Cleric':
        ParaPoi = 10
        RSW = 14
        PetPoly = 13
        Breath = 16
        Spell = 15
    elif playerclass == 'Wizard':
        ParaPoi = 14
        RSW = 11
        PetPoly = 13
        Breath = 15
        Spell = 12
    else:
        ParaPoi = 666
        RSW = 666
        PetPoly = 666
        Breath = 666
        Spell = 666

    save = [ParaPoi, RSW, PetPoly, Breath, Spell]

    return save
