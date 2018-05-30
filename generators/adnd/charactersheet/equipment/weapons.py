import os


def roll(dosh, wp):
    i = 0
    weapons = []
    halfhand = ["Bastard Sword", "Harpoon", "Javelin", "Long Spear", "Spear", "Trident"]
    arrows = ["Composite Long Bow", "Composite Short Bow", "Long Bow", "Short Bow"]
    darts = ["Blowgun", "Darts"]
    quarrel = ["Hand Crossbow", "Heavy Crossbow", "Light Crossbow"]

    hasarrows = False
    hasdarts = False

    while len(wp) > i:

        half = False

        file = wp[i].replace(" Specialist", "")

        # Check for half hand
        if file in halfhand:
            half = True
            twohand = file + ", Two-Handed"
            file = file + ", One-Handed"

        if file == "Dart":
            file = "Dart, Barbed"

        fp = "/generators/adnd/charactersheet/resources/equipment/weapons/{}.txt".format(file)
        path = os.getcwd() + fp
        with open(path, "r") as text_file:
            weaponstats = text_file.readlines()
        text_file.close()

        if dosh >= int(weaponstats[0].rstrip("\n")):
            weapons.append(file)
            dosh -= int(weaponstats[0].rstrip("\n"))

            # For 1.5 Handed Weapons
            if half:
                weapons.append(twohand)

            # For Weapons with Ammo
            if file in arrows and not hasarrows:
                weapons.append("Sheaf Arrow")
                weapons.append("Flight Arrow")
                hasarrows = True

            if file in darts and not hasdarts:
                weapons.append("Dart, Needle")
                weapons.append("Dart, Barbed")
                hasdarts = True

            if file in quarrel:
                weapons.append(file.rstrip("Crossbow") + "Quarrel")

            if file == "Sling":
                weapons.append("Sling Bullet")
                weapons.append("Sling Stone")

        i += 1

    return weapons


def purchase(dosh, weaponlist):
    i = 0

    while len(weaponlist) < i:
        fp = "/generators/adnd/charactersheet/resources/equipment/weapons/{}.txt".format(weaponlist[i])
        path = os.getcwd() + fp
        with open(path, "r") as text_file:
            weaponstats = text_file.readlines()
        text_file.close()

        dosh -= weaponstats[0]

        ++i

    return dosh
