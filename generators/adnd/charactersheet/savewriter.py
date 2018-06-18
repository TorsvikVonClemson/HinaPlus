import os


def save(header, attribs, hp, armour, shield, weaponlist, mint, miscequip, profs, abils, spells):
    # ------ #
    # Header #
    # ------ #

    name = header[0]
    level = header[1]
    exp = header[2]
    race = header[3]
    playerclass = header[4]
    alignment = header[5]
    religion = header[6]
    homeland = header[7]
    gender = header[8]
    age = header[9]
    height = header[10]
    weight = header[11]
    hair = header[12]
    eyes = header[13]
    trait = header[14]
    facialhair = header[15]
    occuptaion = header[16]
    personality = header[17]
    motivation = header[18]

    # ---------- #
    # Attributes #
    # ---------- #

    str = attribs[0]
    dex = attribs[1]
    con = attribs[2]
    int = attribs[3]
    wis = attribs[4]
    cha = attribs[5]

    # --------- #
    # Equipment #
    # --------- #

    # ------------- #
    # Proficiencies #
    # ------------- #

    prof1 = profs[0]
    prof2 = profs[1]
    prof3 = profs[2]
    prof4 = profs[3]
    prof5 = profs[4]
    prof6 = profs[5]
    prof7 = profs[6]
    prof8 = profs[7]
    prof9 = profs[8]
    prof10 = profs[9]
    prof11 = profs[10]
    prof12 = profs[11]
    prof13 = profs[12]
    prof14 = profs[13]
    prof15 = profs[14]
    prof16 = profs[15]
    prof17 = profs[16]
    prof18 = profs[17]
    prof19 = profs[18]
    prof20 = profs[19]

    # --------- #
    # Abilities #
    # --------- #

    abil1 = abils[0]
    abil2 = abils[1]
    abil3 = abils[2]
    abil4 = abils[3]
    abil5 = abils[4]
    abil6 = abils[5]
    abil7 = abils[6]
    abil8 = abils[7]
    abil9 = abils[8]
    abil10 = abils[9]
    abil11 = abils[10]
    abil12 = abils[11]
    abil13 = abils[12]
    abil14 = abils[13]
    abil15 = abils[14]
    abil16 = abils[15]
    abil17 = abils[16]
    abil18 = abils[17]
    abil19 = abils[18]
    abil20 = abils[19]

    # ------ #
    # Spells #
    # ------ #

    spell1 = spells[0]
    spell2 = spells[1]
    spell3 = spells[2]
    spell4 = spells[3]
    spell5 = spells[4]
    spell6 = spells[5]
    spell7 = spells[6]
    spell8 = spells[7]
    spell9 = spells[8]
    spell10 = spells[9]
    spell11 = spells[10]
    spell12 = spells[11]
    spell13 = spells[12]
    spell14 = spells[13]
    spell15 = spells[14]
    spell16 = spells[15]
    spell17 = spells[16]
    spell18 = spells[17]
    spell19 = spells[18]
    spell20 = spells[19]
    spell21 = spells[20]
    spell22 = spells[21]
    spell23 = spells[22]
    spell24 = spells[23]
    spell25 = spells[24]
    spell26 = spells[25]
    spell27 = spells[26]
    spell28 = spells[27]
    spell29 = spells[28]
    spell30 = spells[29]

    title = name + ' ' + race + ' ' + playerclass

    file = "/generators/adnd/charactersheet/saved/trash/{}".format(title)
    path = os.getcwd() + file

    if not os.path.exists(path):
        os.makedirs(path)

    path += "/{}.txt".format(title)

    with open(path, "w") as text_file:
        # ---Print Header--- #

        text_file.write('#------#\n')
        text_file.write('#Header#\n')
        text_file.write('#------#\n\n')

        text_file.write('Name:{}\n'.format(name))
        text_file.write('Level:{}\n'.format(level))
        text_file.write('Exp:{}\n'.format(exp))
        text_file.write('Race:{}\n'.format(race))
        text_file.write('Class:{}\n'.format(playerclass))
        text_file.write('Alignment:{}\n'.format(alignment))
        text_file.write('Religion:{}\n'.format(religion))
        text_file.write('Homeland:{}\n'.format(homeland))
        text_file.write('Gender:{}\n'.format(gender))
        text_file.write('Age:{}\n'.format(age))
        text_file.write('Height:{}\n'.format(height))
        text_file.write('Weight:{}\n'.format(weight))
        text_file.write('Hair:{}\n'.format(hair))
        text_file.write('Eyes:{}\n'.format(eyes))
        text_file.write('Trait:{}\n'.format(trait))
        text_file.write('Facial Hair:{}\n'.format(facialhair))
        text_file.write('Occupation:{}\n'.format(occuptaion))
        text_file.write('Personality:{}\n'.format(personality))
        text_file.write('Motivation:{}\n\n'.format(motivation))

        # ---Print Attibutes--- #

        text_file.write('#----------#\n')
        text_file.write('#Attributes#\n')
        text_file.write('#----------#\n\n')

        text_file.write('Str:{}\n'.format(str))
        text_file.write('Dex:{}\n'.format(dex))
        text_file.write('Con:{}\n'.format(con))
        text_file.write('Int:{}\n'.format(int))
        text_file.write('Wis:{}\n'.format(wis))
        text_file.write('Cha:{}\n\n'.format(cha))

        text_file.write('HP:{}\n\n'.format(hp))

        # ---Print Equipment--- #

        text_file.write('#---------#\n')
        text_file.write('#Equipment#\n')
        text_file.write('#---------#\n\n')

        text_file.write('Armour:{}\n'.format(armour))
        text_file.write('Shield:{}\n\n'.format(shield))

        text_file.write('Weapon1:{}\n'.format(weaponlist[0]))
        text_file.write('Weapon2:{}\n'.format(weaponlist[1]))
        text_file.write('Weapon3:{}\n'.format(weaponlist[2]))
        text_file.write('Weapon4:{}\n'.format(weaponlist[3]))
        text_file.write('Weapon5:{}\n\n'.format(weaponlist[4]))

        text_file.write('Platinum:{}\n'.format(mint[0]))
        text_file.write('Gold:{}\n'.format(mint[1]))
        text_file.write('Silver:{}\n'.format(mint[2]))
        text_file.write('Copper:{}\n'.format(mint[3]))
        text_file.write('Iron:{}\n\n'.format(mint[4]))

        text_file.write('Item1:{}\n'.format(miscequip[0]))
        text_file.write('Item2:{}\n'.format(miscequip[1]))
        text_file.write('Item3:{}\n'.format(miscequip[2]))
        text_file.write('Item4:{}\n'.format(miscequip[3]))
        text_file.write('Item5:{}\n'.format(miscequip[4]))
        text_file.write('Item6:{}\n'.format(miscequip[5]))
        text_file.write('Item7:{}\n'.format(miscequip[6]))
        text_file.write('Item8:{}\n'.format(miscequip[7]))
        text_file.write('Item9:{}\n'.format(miscequip[8]))
        text_file.write('Item10:{}\n\n'.format(miscequip[9]))

        # ---Print Proficiencies--- #

        text_file.write('#-------------#\n')
        text_file.write('#Proficiencies#\n')
        text_file.write('#-------------#\n\n')

        text_file.write('Prof1:{}\n'.format(prof1))
        text_file.write('Prof2:{}\n'.format(prof2))
        text_file.write('Prof3:{}\n'.format(prof3))
        text_file.write('Prof4:{}\n'.format(prof4))
        text_file.write('Prof5:{}\n'.format(prof5))
        text_file.write('Prof6:{}\n'.format(prof6))
        text_file.write('Prof7:{}\n'.format(prof7))
        text_file.write('Prof8:{}\n'.format(prof8))
        text_file.write('Prof9:{}\n'.format(prof9))
        text_file.write('Prof10:{}\n'.format(prof10))
        text_file.write('Prof11:{}\n'.format(prof11))
        text_file.write('Prof12:{}\n'.format(prof12))
        text_file.write('Prof13:{}\n'.format(prof13))
        text_file.write('Prof14:{}\n'.format(prof14))
        text_file.write('Prof15:{}\n'.format(prof15))
        text_file.write('Prof16:{}\n'.format(prof16))
        text_file.write('Prof17:{}\n'.format(prof17))
        text_file.write('Prof18:{}\n'.format(prof18))
        text_file.write('Prof19:{}\n'.format(prof19))
        text_file.write('Prof20:{}\n\n'.format(prof20))

        # ---Print Special Abilities--- #

        text_file.write('#-----------------#\n')
        text_file.write('#Special Abilities#\n')
        text_file.write('#-----------------#\n\n')

        text_file.write('Ability1:{}\n'.format(abil1))
        text_file.write('Ability2:{}\n'.format(abil2))
        text_file.write('Ability3:{}\n'.format(abil3))
        text_file.write('Ability4:{}\n'.format(abil4))
        text_file.write('Ability5:{}\n'.format(abil5))
        text_file.write('Ability6:{}\n'.format(abil6))
        text_file.write('Ability7:{}\n'.format(abil7))
        text_file.write('Ability8:{}\n'.format(abil8))
        text_file.write('Ability9:{}\n'.format(abil9))
        text_file.write('Ability10:{}\n'.format(abil10))
        text_file.write('Ability11:{}\n'.format(abil11))
        text_file.write('Ability12:{}\n'.format(abil12))
        text_file.write('Ability13:{}\n'.format(abil13))
        text_file.write('Ability14:{}\n'.format(abil14))
        text_file.write('Ability15:{}\n'.format(abil15))
        text_file.write('Ability16:{}\n'.format(abil16))
        text_file.write('Ability17:{}\n'.format(abil17))
        text_file.write('Ability18:{}\n'.format(abil18))
        text_file.write('Ability19:{}\n'.format(abil19))
        text_file.write('Ability20:{}\n\n'.format(abil20))

        # ---Print Spells--- #

        text_file.write('#------#\n')
        text_file.write('#Spells#\n')
        text_file.write('#------#\n\n')

        text_file.write('Spell1:{}\n'.format(spell1))
        text_file.write('Spell2:{}\n'.format(spell2))
        text_file.write('Spell3:{}\n'.format(spell3))
        text_file.write('Spell4:{}\n'.format(spell4))
        text_file.write('Spell5:{}\n'.format(spell5))
        text_file.write('Spell6:{}\n'.format(spell6))
        text_file.write('Spell7:{}\n'.format(spell7))
        text_file.write('Spell8:{}\n'.format(spell8))
        text_file.write('Spell9:{}\n'.format(spell9))
        text_file.write('Spell10:{}\n'.format(spell10))
        text_file.write('Spell11:{}\n'.format(spell11))
        text_file.write('Spell12:{}\n'.format(spell12))
        text_file.write('Spell13:{}\n'.format(spell13))
        text_file.write('Spell14:{}\n'.format(spell14))
        text_file.write('Spell15:{}\n'.format(spell15))
        text_file.write('Spell16:{}\n'.format(spell16))
        text_file.write('Spell17:{}\n'.format(spell17))
        text_file.write('Spell18:{}\n'.format(spell18))
        text_file.write('Spell19:{}\n'.format(spell19))
        text_file.write('Spell20:{}\n'.format(spell20))
        text_file.write('Spell21:{}\n'.format(spell21))
        text_file.write('Spell22:{}\n'.format(spell22))
        text_file.write('Spell23:{}\n'.format(spell23))
        text_file.write('Spell24:{}\n'.format(spell24))
        text_file.write('Spell25:{}\n'.format(spell25))
        text_file.write('Spell26:{}\n'.format(spell26))
        text_file.write('Spell27:{}\n'.format(spell27))
        text_file.write('Spell28:{}\n'.format(spell28))
        text_file.write('Spell29:{}\n'.format(spell29))
        text_file.write('Spell30:{}\n\n'.format(spell30))

    # --- Print Relationships --- #

        text_file.write('#-------------#\n')
        text_file.write('#Relationships#\n')
        text_file.write('#-------------#\n\n')

        text_file.write('Relationships1:\n')
        text_file.write('Relationships2:\n')
        text_file.write('Relationships3:\n')
        text_file.write('Relationships4:\n')
        text_file.write('Relationships5:\n')