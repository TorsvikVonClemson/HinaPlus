import os
from reportlab.pdfgen import canvas
from generators.adnd.charactersheet import pdfwriter
from generators.adnd.charactersheet import savewriter

from generators.adnd.charactersheet.race import races
from generators.adnd.charactersheet.race import genders
from generators.adnd.charactersheet.race import names
from generators.adnd.charactersheet.race import religion
from generators.adnd.charactersheet.race import age
from generators.adnd.charactersheet.race import height
from generators.adnd.charactersheet.race import hair
from generators.adnd.charactersheet.race import eyes
from generators.adnd.charactersheet.race import weight
from generators.adnd.charactersheet.race import facialhair
from generators.adnd.charactersheet.race import personality
from generators.adnd.charactersheet.race import appearence
from generators.adnd.charactersheet.classes import classes
from generators.adnd.charactersheet.classes import saves
from generators.adnd.charactersheet.classes import attribute
from generators.adnd.charactersheet.classes import strength
from generators.adnd.charactersheet.classes import dexterity
from generators.adnd.charactersheet.classes import constitution
from generators.adnd.charactersheet.classes import intelligence
from generators.adnd.charactersheet.classes import wisdom
from generators.adnd.charactersheet.classes import charisma
from generators.adnd.charactersheet.classes import wp
from generators.adnd.charactersheet.classes import dosh
from generators.adnd.charactersheet.classes import proficiencies
from generators.adnd.charactersheet.classes import hitdie
from generators.adnd.charactersheet.classes import occupation
from generators.adnd.charactersheet.equipment import weapons
from generators.adnd.charactersheet.equipment import armour
from generators.adnd.charactersheet.equipment import movement
from generators.adnd.charactersheet.equipment import miscequip
from generators.adnd.charactersheet.special import rogue
from generators.adnd.charactersheet.special import spells
from generators.adnd.charactersheet.fluff import motivation


def main(x):
    x = []
    skills = []
    spelllist = []
    equipweight = 0

    # ---Chargen Headers--- #

    race = ""
    playerclass = ""  #
    while race != "Human":  # Temporary Code to force Race
        race = races.roll()
    gender = genders.roll(race)
    name = names.roll(race, gender)
    # while playerclass!="Rogue":		#Force Class
    playerclass = classes.roll(race)
    save = saves.roll(playerclass)
    god = religion.roll(race)
    years = age.roll(race)
    alt = height.roll(race, gender)
    lbs = weight.roll(race, gender)
    beard = facialhair.roll(race, gender)
    hairs = hair.roll(race)
    person = personality.roll(race)
    eye = eyes.roll(eyes)
    motive = motivation.roll(race, god, playerclass)
    app = appearence.roll(race, gender)
    occ = occupation.roll(race, playerclass)

    # ---Alter Special Classes--- #
    if playerclass == "Paladin" and god == "Hina":
        playerclass = "Green Knight"

    # ---Chargen Attributes--- #
    attributes = attribute.roll(race, playerclass)
    stronk = strength.roll(attributes[0])
    move = movement.roll(race, stronk[3])
    dex = dexterity.roll(attributes[1])
    con = constitution.roll(attributes[2])
    smarts = intelligence.roll(attributes[3])
    wis = wisdom.roll(attributes[4])
    cha = charisma.roll(attributes[5])
    hp = hitdie.roll(playerclass, con[0])

    # ---Proficencies and Special Skills--- #

    wplist = wp.roll(playerclass, god)
    profs = proficiencies.roll(race, playerclass, attributes[3], wplist[len(wplist) - 1])
    del wplist[len(wplist) - 1]

    proficiencieslist = wplist + profs
    while len(proficiencieslist) < 20:
        proficiencieslist.append("")

    if playerclass == 'Rogue':
        skills = skills + rogue.roll(attributes[1], occ)
    while len(skills) < 20:
        skills.append('')

    if playerclass == 'Wizard' or playerclass == 'Cleric':
        spelllist = spelllist + spells.roll(playerclass, smarts[0], god)
    else:
        while len(spelllist) < 31:
            spelllist.append("")

    # ---Equipment--- #

    # Money #
    money = dosh.roll(playerclass)

    # Weapons #
    weaponlist = weapons.roll(money, wplist)
    while len(weaponlist) < 5:
        weaponlist.append('')
    money = weapons.purchase(money, weaponlist)

    # Armour #
    playerarmour = armour.choosearmour(money, playerclass, god)
    money = armour.purchase(money, playerarmour)
    playershield = armour.chooseshield(money, weaponlist)
    money = armour.purchase(money, playershield)

    # Misc #
    items = miscequip.roll(money, playerclass, float(move[6]), weaponlist, playerarmour, playershield,
                           proficiencieslist)
    money = miscequip.purchase(money, items)

    while len(items) < 10:
        items.append('')

    # ---Raw Dosh to Mint--- #
    mint = []
    mint.append(int(money / 5000))
    money %= 5000
    mint.append(int(money / 1000))
    money %= 1000
    mint.append(int(money / 100))
    money %= 100
    mint.append(int(money / 10))
    money %= 10
    mint.append(int(money))

    # ------------- #
    # Doc Formatter #
    # ------------- #

    # ---Header--- #

    header = [name, '1', '0', race, playerclass, 'TN', god, 'Home', gender, years, alt, lbs, hairs, eye, app, beard,
              occ, person, motive]

    # ----------- #
    # Save Writer #
    # ----------- #

    savewriter.save(header, attributes, hp, playerarmour, playershield, weaponlist, mint, items, proficiencieslist,
                    skills, spelllist)

    # ------ #
    # Return #
    # ------ #

    title = name + ' ' + race + ' ' + playerclass

    file = "/generators/adnd/charactersheet/saved/trash/{}".format(title) + "/{}.txt".format(title)
    path = os.getcwd() + file
    x.append(path)

    pdfwriter.write(path)

    x.append("**Character Sheets are automatically saved to a trash folder that will be occasionally cleared, "
             "notify me if there is one you want to keep.**\n**The only race that can be rolled right now is "
             "'Human' while tests are being conducted**\n**Right now proficiencies sometimes get rolled twice. "
             "If its non-weapon treat it as specialized, if its a weapon proficincy you're just out of luck for "
             "now**\n**I encourage contributions, it means a lot more can get done.**\n**Tell me if an error "
             "occurs!**\n**        "
             "-Love, Hina**")

    return x
