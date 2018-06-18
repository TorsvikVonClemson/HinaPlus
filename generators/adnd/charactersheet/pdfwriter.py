from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

from generators.adnd.charactersheet.classes import strength
from generators.adnd.charactersheet.classes import dexterity
from generators.adnd.charactersheet.classes import constitution
from generators.adnd.charactersheet.classes import intelligence
from generators.adnd.charactersheet.classes import wisdom
from generators.adnd.charactersheet.classes import charisma
from generators.adnd.charactersheet.equipment import movement
from generators.adnd.charactersheet.classes import saves
from generators.adnd.charactersheet.classes import thaco
from generators.adnd.charactersheet.classes import rof
from generators.adnd.charactersheet.classes import spellprogression

import os


# c.line(x1,y1,x2,y2)


def write(fp):
    c = canvas.Canvas(fp.replace('.txt', '.pdf'))
    c.translate(inch, inch)  # moves origin from bottom left to top left
    c.setFont("Helvetica", 10)

    # c.setFillColorRGB(.8,.8,.8)
    # c.rect(-1*inch,-1*inch,9.27*inch,12.69*inch,fill=1) Potential Colours
    # c.setFillColorRGB(0,0,0)

    with open(fp, "r") as text_file:
        charsheet = text_file.readlines()
    text_file.close()
    for x in range(0, len(charsheet)):
        charsheet[x] = charsheet[x].rstrip('\n')

    proflist = collectlist(charsheet, 'Prof')
    skilllist = collectlist(charsheet, 'Ability')
    spelllist = collectlist(charsheet, 'Spell')
    weight = 0

    # ---------------- #
    # Begin Section 1  #
    # ---------------- #

    # ----- #
    # Row 1 #
    # ----- #

    # -----Name----- #

    c.drawString(-.8 * inch, 10.5 * inch, "Character:")
    c.line(-.1 * inch, 10.45 * inch, 3 * inch, 10.45 * inch)
    c.drawString(-.1 * inch, 10.5 * inch, find(charsheet, 'Name:'))

    # -----Level-----#

    c.drawString(3.1 * inch, 10.5 * inch, "Level:")
    c.line(3.5 * inch, 10.45 * inch, 3.8 * inch, 10.45 * inch)
    c.drawString(3.5 * inch, 10.5 * inch, find(charsheet, 'Level:'))

    # -----Exp-----#

    c.drawString(3.9 * inch, 10.5 * inch, "Exp:")
    c.line(4.2 * inch, 10.45 * inch, 4.8 * inch, 10.45 * inch)
    c.drawString(4.2 * inch, 10.5 * inch, find(charsheet, 'Exp:'))

    # -----Race-----#

    c.drawString(5 * inch, 10.5 * inch, "Race:")
    c.line(5.4 * inch, 10.45 * inch, 7 * inch, 10.45 * inch)
    c.drawString(5.4 * inch, 10.5 * inch, find(charsheet, 'Race:'))

    # -------#
    # Row 2 #
    # -------#

    # -----Class-----#

    c.drawString(-.8 * inch, 10.25 * inch, "Class:")
    c.line(-.3 * inch, 10.20 * inch, .5 * inch, 10.20 * inch)
    c.drawString(-.3 * inch, 10.25 * inch, find(charsheet, 'Class:'))

    # -----Alignment----- #

    c.drawString(.6 * inch, 10.25 * inch, "Alignment:")
    c.line(1.3 * inch, 10.20 * inch, 1.5 * inch, 10.20 * inch)
    c.drawString(1.3 * inch, 10.25 * inch, find(charsheet, 'Alignment:'))

    # -----Religion----- #

    c.drawString(1.6 * inch, 10.25 * inch, "Religion:")
    c.line(2.2 * inch, 10.20 * inch, 3 * inch, 10.20 * inch)
    c.drawString(2.2 * inch, 10.25 * inch, find(charsheet, 'Religion:'))

    # -----Homeland----- #

    c.drawString(3.1 * inch, 10.25 * inch, "Homeland:")
    c.line(3.8 * inch, 10.20 * inch, 5.4 * inch, 10.20 * inch)
    c.drawString(3.8 * inch, 10.25 * inch, find(charsheet, 'Homeland:'))

    # -----Gender----- #

    c.drawString(5.5 * inch, 10.25 * inch, "Gender:")
    c.line(6 * inch, 10.20 * inch, 7 * inch, 10.20 * inch)
    c.drawString(6 * inch, 10.25 * inch, find(charsheet, 'Gender:'))

    # ----- #
    # Row 3 #
    # ----- #

    # -----Age----- #

    c.drawString(-.8 * inch, 10 * inch, "Age:")
    c.line(-.5 * inch, 9.95 * inch, -.3 * inch, 9.95 * inch)
    c.drawString(-.5 * inch, 10 * inch, find(charsheet, 'Age:'))

    # -----Height----- #

    c.drawString(-.2 * inch, 10 * inch, "Height:")
    c.line(.3 * inch, 9.95 * inch, .6 * inch, 9.95 * inch)
    c.drawString(.3 * inch, 10 * inch, find(charsheet, 'Height:'))

    # -----Weight----- #

    c.drawString(.7 * inch, 10 * inch, "Weight:")
    c.line(1.2 * inch, 9.95 * inch, 1.5 * inch, 9.95 * inch)
    c.drawString(1.2 * inch, 10 * inch, find(charsheet, 'Weight:'))

    # -----Hair----- #

    c.drawString(1.6 * inch, 10 * inch, "Hair:")
    c.line(1.95 * inch, 9.95 * inch, 2.8 * inch, 9.95 * inch)
    c.drawString(1.95 * inch, 10 * inch, find(charsheet, 'Hair:'))

    # -----Eyes----- #

    c.drawString(2.9 * inch, 10 * inch, "Eyes:")
    c.line(3.3 * inch, 9.95 * inch, 4.5 * inch, 9.95 * inch)
    c.drawString(3.3 * inch, 10 * inch, find(charsheet, 'Eyes:'))

    # -----Appearance----- #

    c.drawString(4.6 * inch, 10 * inch, "Trait:")
    c.line(5 * inch, 9.95 * inch, 7 * inch, 9.95 * inch)
    c.drawString(5 * inch, 10 * inch, find(charsheet, 'Trait:'))

    # ----- #
    # Row 4 #
    # ----- #

    # ---Facial Hair--- #

    c.drawString(-.8 * inch, 9.75 * inch, "Facial Hair:")
    c.line(0 * inch, 9.7 * inch, 1.5 * inch, 9.7 * inch)
    c.drawString(0 * inch, 9.75 * inch, find(charsheet, 'Facial Hair:'))

    # ---Previous Occupation--- #

    c.drawString(1.6 * inch, 9.75 * inch, "Occupation:")
    c.line(2.4 * inch, 9.7 * inch, 4.1 * inch, 9.7 * inch)
    c.drawString(2.4 * inch, 9.75 * inch, find(charsheet, 'Occupation:'))

    # ---Personality--- #

    c.drawString(4.2 * inch, 9.75 * inch, "Personality:")
    c.line(5 * inch, 9.7 * inch, 7 * inch, 9.7 * inch)
    c.drawString(5 * inch, 9.75 * inch, find(charsheet, 'Personality:'))

    # ----- #
    # Row 5 #
    # ----- #

    # ---Motivation--- #

    c.drawString(-.8 * inch, 9.50 * inch, "Motivation:")
    c.line(-.1 * inch, 9.45 * inch, 7 * inch, 9.45 * inch)
    c.drawString(-.1 * inch, 9.50 * inch, find(charsheet, 'Motivation:'))

    # ---------------- #
    # End of Section 1 #
    # ---------------- #

    c.line(-.8 * inch, 9.3 * inch, 7 * inch, 9.3 * inch)

    # --------------- #
    # Begin Section 2 #
    # --------------- #

    # -STRENGTH- #

    strengthmods = strength.roll(find(charsheet, 'Str:'))
    xpos = 8.9
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
    c.drawString(-.8 * inch, (xpos + .1) * inch, "STR")
    c.drawString(-.4 * inch, (xpos + .1) * inch, find(charsheet, 'Str:'))
    c.drawString(0 * inch, (xpos + .1) * inch, "Hit Prob:")
    c.drawString(.7 * inch, (xpos + .1) * inch, strengthmods[0])
    c.drawString(1.1 * inch, (xpos + .1) * inch, "DMG Adj.:")
    c.drawString(1.8 * inch, (xpos + .1) * inch, strengthmods[1])
    c.drawString(2.2 * inch, (xpos + .1) * inch, "Enc.:")
    c.drawString(2.6 * inch, (xpos + .1) * inch, strengthmods[2])
    c.drawString(3.3 * inch, (xpos + .1) * inch, "Max Press:")
    c.drawString(4.1 * inch, (xpos + .1) * inch, strengthmods[3])
    c.drawString(4.4 * inch, (xpos + .1) * inch, "Open Door:")
    c.drawString(5.2 * inch, (xpos + .1) * inch, strengthmods[4])
    c.drawString(5.5 * inch, (xpos + .1) * inch, "B.B./L.G.:")
    c.drawString(6.1 * inch, (xpos + .1) * inch, strengthmods[5])

    # -DEXTERITY- #

    dexmods = dexterity.roll(int(find(charsheet, 'Dex:')))
    xpos = xpos - .3
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
    c.drawString(-.8 * inch, (xpos + .1) * inch, "DEX")
    c.drawString(-.4 * inch, (xpos + .1) * inch, find(charsheet, 'Dex:'))
    c.drawString(0 * inch, (xpos + .1) * inch, "Reaction Adj.")
    c.drawString(1 * inch, (xpos + .1) * inch, dexmods[0])
    c.drawString(3 * inch, (xpos + .1) * inch, "Missile Attack Adj.")
    c.drawString(4.5 * inch, (xpos + .1) * inch, dexmods[1])
    c.drawString(5 * inch, (xpos + .1) * inch, "Defensive Adj.")
    c.drawString(6 * inch, (xpos + .1) * inch, dexmods[2])

    # -CONSTITUTION- #

    conmods = constitution.roll(int(find(charsheet, 'Con:')))
    xpos = xpos - .3
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
    c.drawString(-.8 * inch, (xpos + .1) * inch, "CON")
    c.drawString(-.4 * inch, (xpos + .1) * inch, find(charsheet, 'Con:'))
    c.drawString(0 * inch, (xpos + .1) * inch, "HP Adj.:")
    c.drawString(.6 * inch, (xpos + .1) * inch, conmods[0])
    c.drawString(1 * inch, (xpos + .1) * inch, "System Shock:")
    c.drawString(2 * inch, (xpos + .1) * inch, conmods[1])
    c.drawString(2.5 * inch, (xpos + .1) * inch, "Rez Survival:")
    c.drawString(3.5 * inch, (xpos + .1) * inch, conmods[2])
    c.drawString(4 * inch, (xpos + .1) * inch, "Poison Save:")
    c.drawString(5 * inch, (xpos + .1) * inch, conmods[3])
    c.drawString(5.5 * inch, (xpos + .1) * inch, "Regeneration:")
    c.drawString(6.5 * inch, (xpos + .1) * inch, conmods[4])

    # -Intelligence- #

    intmods = intelligence.roll(int(find(charsheet, 'Int:')))
    xpos = xpos - .3
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
    c.drawString(-.8 * inch, (xpos + .1) * inch, "INT")
    c.drawString(-.4 * inch, (xpos + .1) * inch, find(charsheet, 'Int:'))
    c.drawString(0 * inch, (xpos + .1) * inch, "Languages:")
    c.drawString(.8 * inch, (xpos + .1) * inch, intmods[0])
    c.drawString(1 * inch, (xpos + .1) * inch, "Spell Level:")
    c.drawString(2 * inch, (xpos + .1) * inch, intmods[1])
    c.drawString(2.5 * inch, (xpos + .1) * inch, "Chance to Learn:")
    c.drawString(3.7 * inch, (xpos + .1) * inch, intmods[2])
    c.drawString(4 * inch, (xpos + .1) * inch, "Max Spells:")
    c.drawString(5 * inch, (xpos + .1) * inch, intmods[3])
    c.drawString(5.5 * inch, (xpos + .1) * inch, "Illusion Immune:")
    c.drawString(6.6 * inch, (xpos + .1) * inch, intmods[4])

    # -Wisdom- #

    wismods = wisdom.roll(int(find(charsheet, 'Wis:')))
    xpos = xpos - .3
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
    c.drawString(-.8 * inch, (xpos + .1) * inch, "WIS")
    c.drawString(-.4 * inch, (xpos + .1) * inch, find(charsheet, 'Wis:'))
    c.drawString(0 * inch, (xpos + .1) * inch, "Magic Def. Adj.:")
    c.drawString(1 * inch, (xpos + .1) * inch, wismods[0])
    c.drawString(2 * inch, (xpos + .1) * inch, "Bonus Spells:")
    c.drawString(3 * inch, (xpos + .1) * inch, wismods[1])
    c.drawString(4 * inch, (xpos + .1) * inch, "Spell Fail:")
    c.drawString(5 * inch, (xpos + .1) * inch, wismods[2])
    c.drawString(6 * inch, (xpos + .1) * inch, "Spell Immune:")
    c.drawString(7 * inch, (xpos + .1) * inch, wismods[3])

    # -Charisma- #

    chamods = charisma.roll(int(find(charsheet, 'Cha:')))
    xpos = xpos - .3
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
    c.drawString(-.8 * inch, (xpos + .1) * inch, "CHA")
    c.drawString(-.4 * inch, (xpos + .1) * inch, find(charsheet, 'Cha:'))
    c.drawString(0 * inch, (xpos + .1) * inch, "Max Hench:")
    c.drawString(1 * inch, (xpos + .1) * inch, chamods[0])
    c.drawString(3 * inch, (xpos + .1) * inch, "Loyalty Base:")
    c.drawString(4.5 * inch, (xpos + .1) * inch, chamods[1])
    c.drawString(5 * inch, (xpos + .1) * inch, "Reaction Adj.:")
    c.drawString(6 * inch, (xpos + .1) * inch, chamods[2])

    # Divider #

    c.line(-.1 * inch, xpos * inch, -.1 * inch, (xpos + 1.75) * inch)

    # ------------- #
    # End Section 2 #
    # ------------- #

    # --------------- #
    # Begin Section 3 #
    # --------------- #

    # ---Health/Armour--- #

    xpos = xpos - 1.1
    c.rect(-.9 * inch, xpos * inch, 2.8 * inch, 1 * inch)
    c.drawString(-.8 * inch, (xpos + .85) * inch, "HP")
    c.drawString(-.1 * inch, (xpos + .85) * inch, find(charsheet, 'HP:'))

    c.drawString(-.8 * inch, (xpos + .475) * inch, "AC")
    if dexmods[2].find('-') != -1:
        dexmods[2] = dexmods[2].lstrip('-')
        c.drawString(-.1 * inch, (xpos + .475) * inch,
                     str(int(getarmour(find(charsheet, 'Armour:'), 1)) - int(dexmods[2]) - int(
                         getarmour(find(charsheet, 'Shield:'), 1))))
    elif dexmods[2].find('+') != -1:
        dexmods[2] = dexmods[2].lstrip('+')
        c.drawString(-.1 * inch, (xpos + .475) * inch,
                     str(int(getarmour(find(charsheet, 'Armour:'), 1)) + int(dexmods[2]) - int(
                         getarmour(find(charsheet, 'Shield:'), 1))))
    else:
        c.drawString(-.1 * inch, (xpos + .475) * inch,
                     str(int(getarmour(find(charsheet, 'Armour:'), 1)) - int(getarmour(find(charsheet, 'Shield:'), 1))))

    c.drawString(-.8 * inch, (xpos + .1) * inch, "Flatfoot")
    c.drawString(-.1 * inch, (xpos + .1) * inch, str(int(getarmour(find(charsheet, 'Armour:'), 1))))

    # Column 2 #

    c.drawString(1.2 * inch, (xpos + .85) * inch, "Weight:")
    armourweight = int(getarmour(find(charsheet, 'Armour:'), 2)) + int(getarmour(find(charsheet, 'Shield:'), 2))
    c.drawString(1.7 * inch, (xpos + .85) * inch,
                 str(armourweight))

    c.drawString(.5 * inch, (xpos + .85) * inch, "Armour")
    c.line(.5 * inch, (xpos + .8) * inch, 1 * inch, (xpos + .8) * inch)
    c.drawString(.5 * inch, (xpos + .475) * inch, find(charsheet, 'Armour:'))

    c.drawString(.5 * inch, (xpos + .1) * inch, find(charsheet, 'Shield:'))  # shield

    # ---Movement--- #

    c.rect(2.1 * inch, xpos * inch, 5 * inch, 1 * inch)

    movementstrings = ['Unencumbered:', 'Light:', 'Moderate:', 'Heavy:', 'Severe:']
    speedstrings = ['', 'Jog', 'Charge', 'Run', 'Sprint', 'Speed', 'X2', 'X3', 'X4', 'X5', 'Atk Adj.', '0', '+2',
                    '+4',
                    '+8', 'Dmg Adj.', '0', '0', '+1', '+2', 'AC Adj.', 'Flatfoot', '+1', '+3', '+5']
    movestats = movement.roll(find(charsheet, 'Race:'), strengthmods[3])

    for x in range(0, 5):
        c.drawString(2.2 * inch, (xpos + .85 - (.2 * x)) * inch, movementstrings[x])

    for x in range(0, 4):
        c.drawString(3.2 * inch, (xpos + .65 - (.2 * x)) * inch, '(' + str(movestats[x + 5]) + ')')  # weight

    for x in range(0, 5):
        c.drawString(3.7 * inch, (xpos + .85 - (.2 * x)) * inch, str(movestats[x]))  # speed

    for y in range(0, 5):
        for x in range(0, 5):
            c.drawString((4.2 + (y * .6)) * inch, (xpos + .85 - (x * .2)) * inch, speedstrings[x + (y * 5)])

    c.line(4.3 * inch, (xpos + .8) * inch, 7 * inch, (xpos + .8) * inch)  # Title Undeline

    # ---------------- #
    # Begin Weapon Box # Condense this section to a loop
    # ---------------- #

    xpos = xpos - .15
    c.drawString(2.5 * inch, xpos * inch, "Weapons")

    xpos = xpos - .4
    c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)

    positionlist = [-.8, 1.6, 2.1, 2.8, 3.5, 4.5, 5.5, 6, 6.6]
    weaponstrings = ['Name', 'Rof', 'THAC0', 'Dmg Adj.', 'Damage', 'Range', 'Type', 'Speed', 'Weight']

    xpos = xpos + .11
    for x in range(0, 9):
        c.drawString(positionlist[x] * inch, xpos * inch, weaponstrings[x])

    xpos += .04

    # ---Weapon--- #

    for x in range(0, 5):
        xpos -= .45
        c.rect(-.9 * inch, xpos * inch, 8 * inch, .3 * inch)
        xpos += .11

        weapon = find(charsheet, 'Weapon{}:'.format(str(x + 1)))
        if weapon not in ['\n', '']:
            weapon.replace(', One-Handed', '')
            weapon.replace(', Two-Handed', '')
            weaponspec = weapon + ' Specialist'

            # -Set THAC0- #

            spec = 0
            dmg = str(0 + int(strengthmods[1]))
            rofspec = False
            leveledthaco = thaco.find(find(charsheet, 'Class:'), int(find(charsheet, 'Level:')))

            if weaponspec in proflist:
                spec = 1
                dmg = str(2 + int(strengthmods[1]))
                rofspec = True

            if getweapon(weapon, 9) == 'Dex':
                playerthaco = str(leveledthaco - spec - int(dexmods[1]))
            elif getweapon(weapon, 9) == '-':
                playerthaco = ''
            elif getweapon(weapon, 9) == 'Str':
                playerthaco = str(leveledthaco - spec - int(strengthmods[0]))
            elif getweapon(weapon, 9) == 'Str(Dex)':
                playerthaco = str(leveledthaco - spec - int(strengthmods[0])) + '(' + str(
                    20 - spec - int(dexmods[1])) + ')'
            else:
                playerthaco = 'err'

            # -Set Damage- #

            if getweapon(weapon, 9) == '-':  # Override for ranged weapons
                dmg = ''

            # -Set RoF- #

            playerrof = rof.find(getweapon(weapon, 6), rofspec, int(find(charsheet, 'Level:')))

            c.drawString(positionlist[0] * inch, xpos * inch, weapon)
            c.drawString(positionlist[1] * inch, xpos * inch, playerrof)
            c.drawString(positionlist[2] * inch, xpos * inch, playerthaco)
            c.drawString(positionlist[3] * inch, xpos * inch, dmg)
            c.drawString(positionlist[4] * inch, xpos * inch, getweapon(weapon, 5))
            c.drawString(positionlist[5] * inch, xpos * inch, getweapon(weapon, 7))
            c.drawString(positionlist[6] * inch, xpos * inch, getweapon(weapon, 3))
            c.drawString(positionlist[7] * inch, xpos * inch, getweapon(weapon, 4))
            c.drawString(positionlist[8] * inch, xpos * inch, getweapon(weapon, 1))
        xpos += .04

        # ---Grid Lines--- #

    xpos = xpos - .15
    c.line(1.5 * inch, xpos * inch, 1.5 * inch, (xpos + 1.8) * inch)  # Name
    c.line(2 * inch, xpos * inch, 2 * inch, (xpos + 1.8) * inch)  # RoF
    c.line(2.7 * inch, xpos * inch, 2.7 * inch, (xpos + 1.8) * inch)  # atkadj
    c.line(3.4 * inch, xpos * inch, 3.4 * inch, (xpos + 1.8) * inch)  # dmgadj
    c.line(4.4 * inch, xpos * inch, 4.4 * inch, (xpos + 1.8) * inch)  # dmg
    c.line(5.4 * inch, xpos * inch, 5.4 * inch, (xpos + 1.8) * inch)  # range
    c.line(5.9 * inch, xpos * inch, 5.9 * inch, (xpos + 1.8) * inch)  # type
    c.line(6.5 * inch, xpos * inch, 6.5 * inch, (xpos + 1.8) * inch)  # speed

    # ----- #
    # Saves #
    # ----- #

    xpos = xpos - 2
    c.rect(-.9 * inch, xpos * inch, 2 * inch, 1.65 * inch)

    c.drawCentredString(.15 * inch, (xpos + 1.5) * inch, "Saving Throws")

    c.drawString(-.8 * inch, (xpos + 1.3) * inch, "Paralyze/Poison")
    c.drawString(-.8 * inch, (xpos + 1.1) * inch, "Rod, Staff or Wand")
    c.drawString(-.8 * inch, (xpos + .9) * inch, "Petrify/Polymorph")
    c.drawString(-.8 * inch, (xpos + .7) * inch, "Breath")
    c.drawString(-.8 * inch, (xpos + .5) * inch, "Spell")
    c.drawString(-.8 * inch, (xpos + .3) * inch, "Reaction Adj.")
    c.drawString(-.8 * inch, (xpos + .1) * inch, "Macabre")

    # ---Modify Saves Based on Attributes---#

    # Poison#

    save = saves.roll(find(charsheet, 'Class:').rstrip('\n'))

    if conmods[3].find('-') != -1:
        conmods[3] = conmods[3].lstrip('-')
        save[0] = save[0] + int(conmods[3])
    elif conmods[3].find('+') != -1:
        save[0] -= int(conmods[3])

    # Magic Save#

    if wismods[0].find('-') != -1:
        wismods[0] = wismods[0].lstrip('-')
        save[4] = save[4] + int(wismods[0])
    elif wismods[0].find('+') != -1:
        save[4] = save[4] - int(wismods[0])

    # Reaction Adj#

    react = 17
    # dex#
    if dexmods[0].find('-') != -1:
        dexmods[0] = dexmods[0].lstrip('-')
        react = react + int(dexmods[0])
    elif dexmods[0].find('+') != -1:
        dexmods[0] = dexmods[0].lstrip('+')
        react = react - int(dexmods[0])
    # cha #
    if chamods[2].find('-') != -1:
        chamods[2] = chamods[2].lstrip('-')
        react = react + int(chamods[2])
    elif chamods[2].find('+') != -1:
        chamods[2] = chamods[2].lstrip('+')
        react = react - int(chamods[2])

    # Mind that Dwarves get an additional Magic and Poison save.

    c.drawString(.6 * inch, (xpos + 1.3) * inch, str(save[0]))
    c.drawString(.6 * inch, (xpos + 1.1) * inch, str(save[1]))
    c.drawString(.6 * inch, (xpos + .9) * inch, str(save[2]))
    c.drawString(.6 * inch, (xpos + .7) * inch, str(save[3]))
    c.drawString(.6 * inch, (xpos + .5) * inch, str(save[4]))
    c.drawString(.6 * inch, (xpos + .3) * inch, str(react))
    c.drawString(.6 * inch, (xpos + .1) * inch, '0')

    # ---------------- #
    # Begin Ammo Table #
    # ---------------- #
    positionlist = [1.3, 4, 5.2, 6, 6.6]
    posnames = ['Name', 'Dmg', 'Range', 'Weight', 'Price']
    ammolist = []
    arrows = ["Composite Long Bow", "Composite Short Bow", "Long Bow", "Short Bow"]
    darts = ["Blowgun", "Darts"]
    quarrel = ["Hand Crossbow", "Heavy Crossbow", "Light Crossbow"]
    havearrows = False
    havedarts = False
    for x in range(0, 5):
        weapon = find(charsheet, 'Weapon{}:'.format(str(x + 1)))
        if weapon in arrows and not havearrows:
            ammolist.append('Flight Arrow')
            ammolist.append('Sheaf Arrow')
            havearrows = True
        elif weapon in darts and not havedarts:
            ammolist.append('Needle Dart')
            ammolist.append('Barbed Dart')
            havedarts = True
        elif weapon in quarrel:
            ammolist.append((weapon + ' Quarrel').replace(' Crossbow', ''))
        elif weapon == 'Sling':
            ammolist.append('Sling Bullet')
            ammolist.append('Sling Stone')
    while len(ammolist) < 5:
        ammolist.append('')

    c.drawCentredString(3.9 * inch, (xpos + 1.8) * inch, "Ammunition")
    for x in range(0, 5):
        c.rect(1.2 * inch, (xpos + x * .33) * inch, 5.9 * inch, .33 * inch)
        c.drawString(positionlist[0] * inch, (xpos + 1.35 - (x + 1) * .33) * inch, ammolist[x])
        if ammolist[x] != '':
            c.drawString(positionlist[1] * inch, (xpos + 1.35 - (x + 1) * .33) * inch, getweapon(ammolist[x], 5))
            c.drawString(positionlist[2] * inch, (xpos + 1.35 - (x + 1) * .33) * inch, getweapon(ammolist[x], 7))
            c.drawString(positionlist[3] * inch, (xpos + 1.35 - (x + 1) * .33) * inch, getweapon(ammolist[x], 1))
            c.drawString(positionlist[4] * inch, (xpos + 1.35 - (x + 1) * .33) * inch, getweapon(ammolist[x], 0))

    for x in range(0, 5):
        c.drawString(positionlist[x] * inch, (xpos + 1.4) * inch, posnames[x])
        c.line((positionlist[x] - .1) * inch, xpos * inch, (positionlist[x] - .1) * inch, (xpos + 1.65) * inch)

    # -------------- #
    # Begin Prof Box #
    # -------------- #

    xpos = xpos - 3.1
    c.drawString(1 * inch, (xpos + 2.7) * inch, "Proficiencies")
    c.rect(-.9 * inch, xpos * inch, 4.6 * inch, 2.85 * inch)
    profskill = ['', '']

    for x in range(0, 2):
        for y in range(0, 10):
            if ':' in proflist[y + (x * 10)]:
                profskill = proflist[y + x * 10].split(':')
            else:
                profskill[0] = proflist[y + x * 10]
            profskill[1] = ''
            c.drawString((-.8 + 2.2 * x) * inch, ((xpos + 2.5) - (y * .25)) * inch, profskill[0])
            c.drawString((.7 + 2.2 * x) * inch, ((xpos + 2.5) - (y * .25)) * inch, profskill[1])
            c.line((-.8 + 2.2 * x) * inch, ((xpos + 2.45) - (y * .25)) * inch, (1.2 + 2.2 * x) * inch,
                   ((xpos + 2.45) - (y * .25)) * inch)

    # ----------------- #
    # Begin Special Box #
    # ----------------- #

    c.drawString(4.9 * inch, (xpos + 2.7) * inch, "Special Abilities")
    c.rect(3.8 * inch, xpos * inch, 3.4 * inch, 2.85 * inch)

    # ---Fill With Special Rules---#
    i = 0
    specialweapons = ['Awl Pike', 'Bariche', 'Bec De Corbin', 'Bill', 'Bola', 'Caltrop', 'Fauchard', 'Glaive',
                      'Lasso',
                      'Long Spear', 'Spear', 'Main-Gauche', 'Mancatcher', 'Military Fork', 'Net', 'Parrying Dagger',
                      'Partisian', 'Ranseur', 'Sap', 'Scimitar', 'Scourge', 'Spear', 'Spetum', 'Staff Sling',
                      'Stiletto', 'Volgue', 'Whip']
    while i < len(proflist):
        if proflist[i].replace(' Specialist', '') in specialweapons:
            skilllist.append(proflist[i])
        i += 1

    for x in range(0, 2):
        for y in range(0, 10):
            c.drawString((3.9 + x * 1.6) * inch, (xpos + 2.5 - y * .25) * inch, skilllist[x * 10 + y])
            c.line((3.9 + x * 1.6) * inch, (xpos + 2.45 - y * .25) * inch, (5.4 + x * 1.6) * inch,
                   (xpos + 2.45 - y * .25) * inch)

    # ------------ #
    # Begin Page 2 #
    # ------------ #

    c.showPage()  # finishes writing on current page, starts a new page if more is added

    c.translate(inch, inch)  # moves origin from bottom left to top left
    c.setFont("Helvetica", 10)

    # ------ #
    # Spells #
    # ------ #

    c.rect(-.9 * inch, 7.65 * inch, 8 * inch, 2.85 * inch)
    c.drawString(-.8 * inch, 10.25 * inch, 'Spells Per Day:')

    spd = spellprogression.find(find(charsheet, 'Class:'), find(charsheet, 'Level:'), find(charsheet, 'Wisdom:'))
    spellsperday = '/'.join(spd)

    c.drawString(.4 * inch, 10.25 * inch, spellsperday)

    for x in range(0, 3):
        for y in range(0, 9):
            c.drawString((-.8 + 2.6 * x) * inch, (10 - .25 * y) * inch, spelllist[x * 10 + y + 1])
            c.line((-.8 + 2.6 * x) * inch, (9.95 - .25 * y) * inch, (1.6 + 2.6 * x) * inch, (9.95 - .25 * y) * inch)

    # --------- #
    # Equipment #
    # --------- #

    xpos = 5.9
    c.rect(1.2 * inch, xpos * inch, 5.9 * inch, 1.65 * inch)

    platinum = find(charsheet, 'Platinum:')
    gold = find(charsheet, 'Gold:')
    silver = find(charsheet, 'Silver:')
    copper = find(charsheet, 'Copper:')
    iron = find(charsheet, 'Iron:')
    weight += ((int(gold) + int(silver) + int(copper) + int(iron) + int(platinum)) / 50)

    # ---Wealth Column---#

    c.drawString(1.3 * inch, (xpos + 1.4) * inch, "Platinum:")
    c.drawString(2 * inch, (xpos + 1.4) * inch, str(platinum))

    c.drawString(1.3 * inch, (xpos + 1.15) * inch, "Gold:")
    c.drawString(2 * inch, (xpos + 1.15) * inch, str(gold))

    c.drawString(1.3 * inch, (xpos + .9) * inch, "Silver:")
    c.drawString(2 * inch, (xpos + .9) * inch, str(silver))

    c.drawString(1.3 * inch, (xpos + .65) * inch, "Copper:")
    c.drawString(2 * inch, (xpos + .65) * inch, str(copper))

    c.drawString(1.3 * inch, (xpos + .4) * inch, "Iron:")
    c.drawString(2 * inch, (xpos + .4) * inch, str(iron))

    c.drawString(1.3 * inch, (xpos + .05) * inch, "Weight")

    # Remove Rounding from Float#

    for x in range(0, 2):
        c.drawString((2.5 + x * 2.2) * inch, (xpos + 1.5) * inch, "Item:")
        c.drawString((4 + x * 2.2) * inch, (xpos + 1.5) * inch, "Qty.")
        c.drawString((4.3 + x * 2.2) * inch, (xpos + 1.5) * inch, "Wgt.")
        for y in range(0, 5):
            itemquantity = find(charsheet, 'Item{}:'.format(1 + x * 5 + y)).split(':')
            c.line((2.5 + 2.2 * x) * inch, (xpos + 1.3 - .25 * y) * inch, (4.45 + 2.2 * x) * inch,
                   (xpos + 1.3 - .25 * y) * inch)
            if itemquantity[0] not in ['\n', '']:
                c.drawString((2.5 + 2.2 * x) * inch, (xpos + 1.35 - .25 * y) * inch, itemquantity[0])
                c.drawString((4 + 2.2 * x) * inch, (xpos + 1.35 - .25 * y) * inch, itemquantity[1])
                c.drawString((4.3 + 2.2 * x) * inch, (xpos + 1.35 - .25 * y) * inch, getitem(itemquantity[0], 1))
                weight += float(itemquantity[1]) * float(getitem(itemquantity[0], 1))

    weight += armourweight

    weight = weight * 1000
    top = int(weight / 1000)
    bottom = int(weight) % 1000

    c.drawString(2 * inch, (xpos + .05) * inch, (str(top) + '.' + str(bottom)))

    c.rect(-.9 * inch, xpos * inch, 2 * inch, 1.65 * inch)

    # ------------- #
    # Relationships #
    # ------------- #

    relationships = collectlist(charsheet, 'Relationships')

    c.drawCentredString(.15 * inch, (xpos + 1.5) * inch, 'Relationships')
    for x in range(0, 5):
        c.line((-.8) * inch, (xpos + 1.2 - .25 * x) * inch, (1) * inch,
               (xpos + 1.2 - .25 * x) * inch)
        c.drawString((-.8) * inch, (xpos + 1.25 - .25 * x) * inch, relationships[x])

    # ------------------------ #
    # Rules and Fluff Function #
    # ------------------------ #

    xpos = 12
    inc = 0
    specialweapons = ['Awl Pike', 'Bariche', 'Bec De Corbin', 'Bill', 'Bola', 'Caltrop', 'Fauchard', 'Glaive', 'Lasso',
                      'Long Spear', 'Spear', 'Main-Gauche', 'Mancatcher', 'Military Fork', 'Net', 'Parrying Dagger',
                      'Partisian', 'Ranseur', 'Sap', 'Scimitar', 'Scourge', 'Spear', 'Spetum', 'Staff Sling',
                      'Stiletto', 'Volgue', 'Whip']

    #   listformat=[subfolder,filelocation1,filelocation2,filelocationX...

    c.drawString(2.5 * inch, (7.4 - (xpos * .15)) * inch, "~~~~~Quick Reference~~~~~")
    xpos += 2

    ruleslist = ['rules', 'fulldef', 'running', 'dualwielding', 'morale']
    i = 0
    while i < len(specialweapons):
        if specialweapons[i] in proflist:
            specialweapons[i] = specialweapons[i].lower()
            specialweapons[i] = specialweapons[i].replace(" ", "")
            ruleslist.append(specialweapons[i])
        if (specialweapons[i] + ' Specialist') in proflist:
            specialweapons[i] = specialweapons[i].lower()
            specialweapons[i] = specialweapons[i].replace(" ", "")
            ruleslist.append(specialweapons[i])
        i += 1

    xpos = fluffy(ruleslist, xpos, c)

    c.drawString(2.5 * inch, (7.4 - (xpos * .15)) * inch, "~~~~~Fluff~~~~~")
    xpos += 2
    flufflist = [find(charsheet, "Race:").rstrip('\n'), find(charsheet, "Race:".rstrip('\n')),
                 find(charsheet, "Religion:").rstrip('\n')]
    xpos = fluffy(flufflist, xpos, c)

    c.save()  # finalizes the document
    return 0


# -------------------- #
# Additional Functions #
# -------------------- #

def RateofFire(playerclass, name, RoF):
    if playerclass != "Fighter":  # Re-define RoF
        if RoF == "M":
            RoF = '1'
        elif RoF == "Thrown":
            RoF = '1'
    else:
        if RoF == "M":
            RoF = '3/2'
        elif name == "Light Crossbow":
            RoF = '1'
        elif name == "Heavy Crossbow":
            RoF = '1/2'
        elif name == "Dart":
            RoF = '4'
        elif RoF == "Thrown" or name == "Blowgun" or name == "Staff Sling":
            RoF = '3/2'
    return RoF


def THAC0(missile, melee, spec, based):
    THAC0Value = 20

    if based == "Str":
        if melee.find("-") != -1:
            melee = melee.lstrip('-')
            THAC0Value = THAC0Value + int(melee)
        if melee.find("+") != -1:
            melee = melee.lstrip('+')
            THAC0Value = THAC0Value - int(melee)
    if based == 'Dex':
        if missile.find("-") != -1:
            missile = missile.lstrip('-')
            THAC0Value = THAC0Value + int(missile)
        if missile.find("+") != -1:
            missile = missile.lstrip('+')
            THAC0Value = THAC0Value - int(missile)
    if spec.find("Specialist") != -1:
        THAC0Value = THAC0Value - 1
    return str(THAC0Value)


def DamageAdj(based, stronk, spec):
    damage = 0

    if based == "Str":
        if stronk.find("-") != -1:
            stronk = stronk.lstrip('-')
            damage = damage - int(stronk)
        if stronk.find("+") != -1:
            stronk = stronk.lstrip('+')
            damage = damage + int(stronk)
    if spec.find("Specialist") != -1:
        damage = damage + 2
    return str(damage)


def fluffy(location, xpos, c):
    c.setFont("Helvetica", 9)
    i = 1
    reset = 0
    while i < len(location):
        inc = 0
        file = "/generators/adnd/charactersheet/resources/{}".format(location[0].lower()) + "/{}.txt".format(
            location[i].lower())
        path = os.getcwd() + file
        with open(path, "r") as text_file:
            lines = text_file.readlines()
            text_file.close()
            while len(lines) > inc:
                lines[0 + inc] = lines[0 + inc].rstrip("\n")
                inc += 1

        inc = 0

        while len(lines) > inc:
            c.drawString(-.8 * inch, (7.4 - (xpos * .15)) * inch, lines[inc])
            inc += 1
            xpos += 1
            if (7.4 - (xpos * .15)) <= 0:
                c.drawString(2 * inch, (7.4 - (xpos * .15)) * inch, "~~~~~CONTINUED ON NEXT PAGE~~~~~")
                xpos += 1
                reset = inc
                c.rect(-.9 * inch, (7.4 - (xpos * .15)) * inch, 8 * inch, ((inc + 2) * .15) * inch)
                c.showPage()
                c.translate(inch, inch)
                c.setFont("Helvetica", 8.5)
                xpos = -18
        c.rect(-.9 * inch, (7.4 - (xpos * .15)) * inch, 8 * inch, ((inc + 1 - reset) * .15) * inch)
        reset = 0
        i += 1
        xpos += 2
        if (7.4 - (xpos * .15)) <= 0:
            c.showPage()
            c.translate(inch, inch)
            c.setFont("Helvetica", 9)
    c.setFont("Helvetica", 10)
    return xpos


def find(charsheet, location):
    i = 0
    while i < len(charsheet):
        if charsheet[i].startswith(location):
            return charsheet[i].replace(location, '')
        else:
            i += 1


def getarmour(armour, pos):
    fp = os.getcwd() + "/generators/adnd/charactersheet/resources/equipment/armour/{}.txt".format(armour.rstrip('\n'))
    with open(fp, "r") as text_file:
        stats = text_file.readlines()
    text_file.close()
    for x in range(0, len(stats) - 1):
        stats[x] = stats[x].rstrip('\n')
    return stats[pos]


def getweapon(weapon, pos):
    fp = os.getcwd() + "/generators/adnd/charactersheet/resources/equipment/weapons/{}.txt".format(weapon.rstrip('\n'))
    with open(fp, "r") as text_file:
        stats = text_file.readlines()
    text_file.close()
    for x in range(0, len(stats) - 1):
        stats[x] = stats[x].rstrip('\n')
    return stats[pos]


def getitem(item, pos):
    fp = os.getcwd() + "/generators/adnd/charactersheet/resources/equipment/misc/treasury/{}.txt".format(
        item.rstrip('\n'))
    with open(fp, "r") as text_file:
        stats = text_file.readlines()
    text_file.close()
    for x in range(0, len(stats) - 1):
        stats[x] = stats[x].rstrip('\n')
    return stats[pos]


def collectlist(charsheet, type):
    i = 0
    n = 1
    list = []
    while i < len(charsheet):
        if charsheet[i].startswith(type):
            list.append(charsheet[i].replace(type + '{}:'.format(str(n)), ''))
            n += 1
            i += 1
        else:
            i += 1
    return list
