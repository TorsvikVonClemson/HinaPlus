import random
import os


def roll(playerclass, god):
    wplist = []
    error = 20
    errormatch = 0
    extra = False
    wpcount = 5
    file = ""
    doublespec = ["Composite Long Bow", "Composite Short Bow", "Short Bow", "Long Bow"]

    if playerclass in ["Fighter", "Ranger", "Paladin", "Green Knight"]:
        wpcount = 4
        file = "Fighter"
    elif playerclass == "Wizard":
        wpcount = 1
        file = "Wizard"
    elif playerclass == "Cleric":
        wpcount = 2
        file = god
    elif playerclass == "Rogue" or playerclass == "Bard":
        wpcount = 2
        file = "Rogue"

    if playerclass in ["Paladin", "Green Knight"]:
        file = god

    fp = "/generators/adnd/charactersheet/resources/weapon proficiencies/{}.txt".format(file)
    path = os.getcwd() + fp
    with open(path, "r") as text_file:
        proficiencylist = text_file.readlines()
    text_file.close()

    while wpcount > 0:
        wp = (random.choice(proficiencylist)).rstrip("\n")

        if wp not in wplist:
            if playerclass == "Fighter" and wp not in doublespec and wpcount > 1:
                wp = wp + " Specialist"
                wpcount -= 2
                wplist.append(wp)
            elif playerclass == "Fighter" and wp in doublespec and wpcount > 2:
                wp = wp + " Specialist"
                wpcount -= 3
                wplist.append(wp)
            else:
                wpcount -= 1
                wplist.append(wp)
        else:
            errormatch += 1

        if error == errormatch:
            extra = True
            wplist.append(wpcount)
            wpcount = -1;

    if not extra:
        wplist.append(0)

    return wplist
