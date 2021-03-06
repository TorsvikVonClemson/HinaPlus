import random


def roll(playerclass):
    if playerclass in ["Fighter", "Paladin", "Ranger", "Green Knight"]:
        dosh = (random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)) * 1000
    elif playerclass == "Wizard":
        dosh = (random.randint(1, 4) + 1) * 1000
    elif playerclass == "Rogue" or playerclass == "Bard":
        dosh = (random.randint(1, 6) + random.randint(1, 6)) * 1000
    elif playerclass == "Cleric":
        dosh = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)) * 1000
    return dosh
