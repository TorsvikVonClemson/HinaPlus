import random
import os
from generators.adnd.charactersheet.classes import strength


def roll(dosh, playerclass, weightlimit, weaponlist, playerarmour, playershield, proficiencies):
    purchases = []
    prepurchases = []
    i = 0
    failures = 0

    # ---Define Repeatables --- #

    repeatable = getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'Repeatable')

    # ---Define Weight Limit--- #

    # Weapons #
    for x in range(0, 4):
        if weaponlist[x] != "":
            weaponstats = getlist("/generators/adnd/charactersheet/resources/equipment/weapons/{}.txt", weaponlist[x])
            weightlimit -= float(weaponstats[1].rstrip('\n'))

    # Armour #
    armourstats = getlist("/generators/adnd/charactersheet/resources/equipment/armour/{}.txt", playerarmour)
    weightlimit -= float(armourstats[1])

    # Shield #
    shieldstats = getlist("/generators/adnd/charactersheet/resources/equipment/armour/{}.txt", playershield)
    weightlimit -= float(shieldstats[1])

    # ---Forced Purchases--- #
    for x in range(0, 4):
        if weaponlist[x] in ['Hand Crossbow', 'Light Crossbow', 'Heavy Crossbow']:
            prepurchases.append('Bolt Case')
    for x in range(0, 4):
        if weaponlist[x] in ['Composite Short Bow', 'Short Bow', 'Composite Long Bow', 'Long Bow']:
            prepurchases.append('Quiver')
    if playerclass == 'Cleric':
        prepurchases.append('Holy Item')
    if playerclass == 'Bard':
        prepurchases.append('Instrument')
    if playerclass == 'Thief':
        prepurchases.append("Thieves' Picks")
        prepurchases.append("Weaponblack")

    while i < len(prepurchases):
        purchasestats = getlist("/generators/adnd/charactersheet/resources/equipment/misc/treasury/{}.txt",
                                prepurchases[i])
        dosh -= int(purchasestats[0]) * int(purchasestats[2])
        weightlimit -= float(purchasestats[1]) * int(purchasestats[2])
        i += 1

    # --- Define Shopping List --- #

    shoppinglist = getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'General')

    if 'Cooking' in proficiencies:
        shoppinglist += getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'Cooking')

    if 'Fishing' in proficiencies:
        shoppinglist += getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'Fishing')

    if 'Healing' in proficiencies:
        shoppinglist += getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'Healing')

    if 'Reading' in proficiencies:
        shoppinglist += getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'Reading')

    if 'Tailoring' in proficiencies:
        shoppinglist += getlist("/generators/adnd/charactersheet/resources/equipment/misc/{}.txt", 'Tailoring')

    while failures < 10:
        item = random.choice(shoppinglist).rstrip('\n')
        purchasestats = getlist("/generators/adnd/charactersheet/resources/equipment/misc/treasury/{}.txt", item)
        if int(purchasestats[0]) * int(purchasestats[2]) < dosh and float(purchasestats[1]) * int(
                purchasestats[2]) < weightlimit:
            if item not in purchases or item in repeatable:
                purchases.append(item)
                dosh -= int(purchasestats[0]) * int(purchasestats[2])
                weightlimit -= float(purchasestats[1]) * int(purchasestats[2])

            else:
                failures += 1
        else:
            failures += 1

    # --- Quantity --- #

    i = 0
    finalpurchases = prepurchases + purchases

    while i < len(finalpurchases):
        purchasestats = getlist("/generators/adnd/charactersheet/resources/equipment/misc/treasury/{}.txt",
                                finalpurchases[i])
        finalpurchases[i] += ":" + purchasestats[2]
        i += 1

    return finalpurchases


def purchase(dosh, purchaselist):
    i = 0
    while i < len(purchaselist):
        details = purchaselist[i].split(':')
        purchasestats = getlist("/generators/adnd/charactersheet/resources/equipment/misc/treasury/{}.txt",
                                details[0])

        dosh -= int(purchasestats[0]) * int(details[1])
        i += 1
    return dosh


def getlist(exten, dir):
    fp = exten.format(dir)
    path = os.getcwd() + fp
    with open(path, "r") as text_file:
        stats = text_file.readlines()
    text_file.close()
    return stats
