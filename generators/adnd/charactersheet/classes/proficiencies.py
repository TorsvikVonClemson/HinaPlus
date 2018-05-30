import random
import os


def roll(race, playerclass, intel, overflow):
    proffinal = []
    doublelist = ["Mining:Wis-3", "Astrology:Int", "Engineering:Int-3", "Healing:Wis-2", "Herbalism:Int-2",
                  "Blind-Fighting:", "Gem Cutting:Dex-2", "Reading Lips:Int-2", "Armorer:Int-2",
                  "Bowyer/Fletcher:Dex-1", "Endurance:Con", "Survival:Int", "Tracking:Wis"]

    # ------------------------#
    # Starting proficiencies #
    # ------------------------#

    proffinal.append('Language (Faustic)')

    if race == 'Dwarf':
        proffinal.append('Language (Dwarven)')

    if race == 'Wood Elf':
        proffinal.append('Language (Sylvan)')

    if race == 'Orc Merchant' or race == 'Goblin Merchant':
        proffinal.append('Language (Greenskin)')

    if race == 'Kobold Pilgrim':
        proffinal.append('Language (Utterances)')

    if race == 'Elven Spy':
        proffinal.append('Language (Langue Digne)')

    if race == 'Drow Refugee':
        proffinal.append('Language (Deepspeech)')
        proffinal.append('Language (Kehlig)')
        proffinal.append('Language (Kehlig Silent)')

    if race == 'Oni' or race == 'Ogre':
        proffinal.append("Language (Yu'yen)")

    if race == 'Fairy':
        proffinal.append('Language (Sylvan)')

    if playerclass == 'Rogue':
        proffinal.append("Language (Thieves' Cant)")

    # -------------------------------#
    # Count Number of proficiencies  #
    # -------------------------------#

    if playerclass == 'Cleric':
        profcount = 4
    elif playerclass == 'Rogue' or 'Bard':
        profcount = 3
    elif playerclass in ['Fighter', 'Ranger', 'Paladin', 'Green Knight']:
        profcount = 3
    elif playerclass == 'Wizard':
        profcount = 4
    else:
        profcount = 0

    profcount += overflow

    if intel < 9:
        profcount = profcount + 1
    elif 8 < intel < 12:
        profcount = profcount + 2
    elif 11 < intel < 14:
        profcount = profcount + 3
    elif 13 < intel < 16:
        profcount = profcount + 4
    elif intel == 16:
        profcount = profcount + 5
    elif intel == 17:
        profcount = profcount + 6
    elif intel == 18:
        profcount = profcount + 7
    elif intel == 19:
        profcount = profcount + 8
    elif intel == 20:
        profcount = profcount + 9
    elif intel == 21:
        profcount = profcount + 10
    elif intel == 22:
        profcount = profcount + 11
    elif intel == 23:
        profcount = profcount + 12
    elif intel == 24:
        profcount = profcount + 15
    elif intel == 25:
        profcount = profcount + 20

    # ----------------------------#
    # Fill General proficiencies #
    # ----------------------------#

    file = "/generators/adnd/charactersheet/resources/proficiencies/general.txt"
    path = os.getcwd() + file
    fp = open(path, 'r+');
    with open(path, "r") as text_file:

        proflist = text_file.readlines()

        text_file.close()

    # ---------------------------#
    # Fill Cleric proficiencies #
    # ---------------------------#

    if playerclass == 'Cleric':
        file = "/generators/adnd/charactersheet/resources/proficiencies/priest.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # --------------------------#
    # Fill Rogue proficiencies #
    # --------------------------#

    if playerclass == 'Rogue':
        file = "/generators/adnd/charactersheet/resources/proficiencies/rogue.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # ----------------------------#
    # Fill Fighter proficiencies #
    # ----------------------------#

    if playerclass == 'Fighter':
        file = "/generators/adnd/charactersheet/resources/proficiencies/warrior.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # ---------------------------#
    # Fill Wizard proficiencies #
    # ---------------------------#

    if playerclass == 'Wizard':
        file = "/generators/adnd/charactersheet/resources/proficiencies/wizard.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # -------------------------#
    # Fill Bard Proficiencies #
    # -------------------------#

    if playerclass == 'Bard':
        file = "/generators/adnd/charactersheet/resources/proficiencies/warrior.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

        file = "/generators/adnd/charactersheet/resources/proficiencies/rogue.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

        file = "/generators/adnd/charactersheet/resources/proficiencies/wizard.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # ----------------------------#
    # Fill Paladin Proficiencies #
    # ----------------------------#

    if playerclass in ['Paladin', 'Green Knight']:
        file = "/generators/adnd/charactersheet/resources/proficiencies/priest.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

        file = "/generators/adnd/charactersheet/resources/proficiencies/warrior.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # ---------------------------#
    # Fill Ranger Proficiencies #
    # ---------------------------#

    if playerclass == 'Ranger':
        file = "/generators/adnd/charactersheet/resources/proficiencies/warrior.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

        file = "/generators/adnd/charactersheet/resources/proficiencies/wizard.txt"
        path = os.getcwd() + file
        fp = open(path, 'r+');
        with open(path, "r") as text_file:
            proflist.extend(text_file.readlines())

            text_file.close()

    # -----------------#
    # Roll From Lists #
    # -----------------#

    while profcount > 0:
        profchoice = random.choice(proflist)
        profchoice = profchoice.rstrip('\n')

        if profchoice in proffinal:
            location = proffinal.index(profchoice)
            proffinal[location] = proffinal[location] + '+1'
            profcount -= 1
        else:

            # ---Check Validity---#
            if (profchoice in doublelist) and profcount >= 2:

                proffinal.append(profchoice)
                profcount -= 2

            elif (profchoice in doublelist) and profcount < 2:

                break

            elif profchoice == "Weaponsmithing:Int-3" and profcount >= 3:

                proffinal.append(profchoice)
                profcount -= 3

            elif profchoice == "Weaponsmithing:Int-3" and profcount < 3:

                break

            else:

                proffinal.append(profchoice)
                profcount -= 1

        if proffinal[len(proffinal) - 1].find('{RacialMusic}') != -1:
            file = "/generators/adnd/charactersheet/resources/proficiencies/{}".format(race.lower()) + 'music.txt'
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                raciallist = text_file.readlines()
                text_file.close()

            racial = random.choice(raciallist)
            racial = racial.rstrip('\n')

            proffinal[len(proffinal) - 1] = proffinal[len(proffinal) - 1].replace('{Racial}', racial)

    return proffinal
