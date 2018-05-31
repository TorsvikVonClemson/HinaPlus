import os


def choosearmour(dosh, playerclass, god):
    if playerclass in ["Fighter", "Paladin", "Ranger"]:
        playerclass = "Warrior"
    if playerclass in ["Rogue", "Bard"]:
        playerclass = "Rogue"
    if playerclass == "Cleric":
        playerclass = god

    if 4000 <= dosh < 5000 and playerclass in ["Warrior", "Rogue"] or playerclass == "Hina":
        buy = 'Padded'

    elif 5000 <= dosh < 20000 and playerclass in ["Warrior", "Rogue"] or playerclass in ["Leuchtag", "Kolsten"]:
        buy = 'Leather'

    elif 20000 <= dosh < 120000 and playerclass in ["Warrior", "Rogue"]:
        buy = 'Studded Leather'

    elif 40000 <= dosh < 75000 and playerclass in ["Warrior", "Rogue"] or playerclass == "Ilmura":
        buy = 'Brigadine'

    elif 75000 <= dosh < 200000 and playerclass in ["Warrior", "Rogue"] or playerclass == "Reueherr":
        buy = 'Chain Mail'

    elif 200000 <= dosh < 600000 and playerclass == "Warrior":
        buy = 'Banded Mail'

    elif 600000 <= dosh < 2000000 and playerclass == "Warrior" or playerclass in ["Makabel", "Green Knight"]:
        buy = 'Plate Mail'

    elif 2000000 <= dosh < 4000000 and playerclass == "Warrior":
        buy = 'Field Plate'

    elif dosh >= 4000000 and playerclass == "Warrior" or playerclass == "Tyr":
        buy = 'Full Plate'

    elif playerclass == "Strafeherr":
        buy = "Spiked Leather"

    elif playerclass == "Bahamut":
        buy = "Scale"

    elif playerclass == "Calandra":
        buy = "Hide"

    elif playerclass == "Cisa":
        buy = "Coin Mail"

    elif playerclass == "Gerdora":
        buy = "Cuirass"

    else:
        buy = 'Unarmoured'

    return buy


def chooseshield(dosh, weaponlist):
    # Set best possible shield using numbers, 4 for tower and 0 for none
    # 1.5 Hand weapons get body shield
    # weapons with damage above 4.5 get medium
    # weapons with damage above 3.5 get small
    # all others and some ranged get buckler

    bodyshield = ["Bastard Sword, One-Handed", "Harpoon, One-Handed", "Javelin, One-Handed", "Long Spear, One-Handed",
                  "Spear, One-Handed", "Trident, One-Handed"]
    mediumshield = ["Battle Axe", "Footman's Flail", "Footman's Mace", "Footman's Pick", "Heavy Horse Lance",
                    "Medium Horse Lance", "Morningstar", "Broad Sword", "Khopesh", "Long Sword", "Rapier", "Sabre",
                    "Scimitar"]
    smallshield = ["Club", "Chain", "Hand Axe", "Horseman's Flail", "Horseman's Mace", "Horseman's Pick",
                   "Light Horse Lance", "Sickle", "Cutlass", "Short Sword", "Warhammer"]
    buckler = ["Short Bow", "Composite Short Bow", "Hand Crossbow", "Light Crossbow", "Dagger", "Scourge", "Sling",
               "Whip"]

    shieldvalue = 0

    for x in range(0, len(weaponlist)):
        check = weaponlist[x].rstrip('\n')
        if check in bodyshield and dosh >= 10000:
            shieldvalue = 4
        elif check in mediumshield and dosh >= 7000 and shieldvalue < 4:
            shieldvalue = 3
        elif check in smallshield and dosh >= 3000 and shieldvalue < 3:
            shieldvalue = 2
        elif check in buckler and dosh >= 1000 and shieldvalue < 2:
            shieldvalue = 1

    if shieldvalue == 4:
        shield = "Body Shield"
    elif shieldvalue == 3:
        shield = "Medium Shield"
    elif shieldvalue == 2:
        shield = "Small Shield"
    elif shieldvalue == 1:
        shield = "Small Shield"
    else:
        shield = "None"

    return shield


def purchase(dosh, armour):
    fp = "/generators/adnd/charactersheet/resources/equipment/armour/{}.txt".format(armour)
    path = os.getcwd() + fp
    with open(path, "r") as text_file:
        armourstats = text_file.readlines()
    text_file.close()

    dosh -= int(armourstats[0].rstrip("\n"))

    return dosh
