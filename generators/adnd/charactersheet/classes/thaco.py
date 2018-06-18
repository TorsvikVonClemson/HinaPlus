def find(playerclass, level):
    warrior = ['Fighter', 'Ranger', 'Paladin', 'Green Knight']
    rogue = ['Rogue', 'Bard']
    if playerclass in warrior:
        thaco = 21 - level
    elif playerclass in rogue:
        thaco = 20 - int((level - 1) / 2)
    elif playerclass == 'Cleric':
        thaco = 20 - int((level - 1) / 3) * 2
    elif playerclass == 'Wizard':
        thaco = 20 - int((level - 1) / 3)

    return thaco
