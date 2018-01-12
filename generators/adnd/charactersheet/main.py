import os
from reportlab.pdfgen import canvas
from generators.adnd.charactersheet import pdfwriter

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

    x=[]
    skills=[]
    spelllist=[]
    equipweight=0    #weight is maintained as a FLOAT


#---Chargen Headers---#

    race=""
    playerclass=""		#
    while race!="Human":	#Temporary Code to force Race
        race=races.roll()	#
    gender=genders.roll(race)
    name=names.roll(race,gender)
    while playerclass!="Rogue":		#Force Class
        playerclass=classes.roll(race)
    save=saves.roll(playerclass)
    god=religion.roll(race)
    years=age.roll(race)
    alt=height.roll(race,gender)
    lbs=weight.roll(race,gender)
    beard=facialhair.roll(race,gender)
    hairs=hair.roll(race)
    person=personality.roll(race)
    eye=eyes.roll(eyes)
    motive=motivation.roll(race,god,playerclass)
    app=appearence.roll(race,gender)
    occ=occupation.roll(race,playerclass)

#---Chargen Attributes---#
    attributes=attribute.roll(race,playerclass)
    stronk=strength.roll(attributes[0])
    move=movement.roll(race,stronk[3])
    dex=dexterity.roll(attributes[1])
    con=constitution.roll(attributes[2])
    smarts=intelligence.roll(attributes[3])
    wis=wisdom.roll(attributes[4])
    cha=charisma.roll(attributes[5])
    hp=hitdie.roll(playerclass,con[0])

#---Proficencies and Special Skills---#

    wplist=wp.roll(playerclass,god)
    profs=proficiencies.roll(race,playerclass,attributes[3])

    if playerclass=='Rogue':
        skills=skills+rogue.roll(attributes[1],occ)
    if playerclass=='Wizard' or playerclass=='Cleric':
        spelllist=spelllist+spells.roll(playerclass,smarts[0],god)
    else:
        while len(spelllist)<31:
            spelllist.append("")



#---Equipment---#

#Money#
    rolleddosh=dosh.roll(playerclass)

#Weapons#
    pdfweapons=weapons.roll(rolleddosh,wplist)
    remainingdosh=pdfweapons[0]
    loop=0
    while loop<=4:
        if pdfweapons[9+(loop*9)]!='':
            equipweight=equipweight+float(pdfweapons[9+(loop*9)])
        loop +=1

#Armour#
    playerarmour=armour.roll(remainingdosh,playerclass,god,pdfweapons)
    remainingdosh=playerarmour[0]
    equipweight=equipweight+float(playerarmour[4])

#Misc#
    miscequ=miscequip.roll(remainingdosh,playerclass,equipweight,move[6])
    remainingdosh=miscequ[0]
    loop=0
    while loop<=9:
        if miscequ[3+(loop*3)]!='':
            equipweight=equipweight+float(miscequ[3+(loop*3)])
        loop +=1

#---Metadata---#

    title=name+' '+race+' '+playerclass

    file = "/generators/adnd/charactersheet/saved/trash/{}.txt"
    pdffile =  "/generators/adnd/charactersheet/saved/trash/{}.pdf"
    path=os.getcwd()+file
    pdfpath=os.getcwd()+pdffile
    with open(path.format(title),"w") as text_file:

#-------------------------------#
#    Character Sheet Headers    #
#-------------------------------#

        text_file.write(str(pdfweapons[0]))
        text_file.write(pdfweapons[1])
        text_file.write(pdfweapons[2])
        text_file.write(pdfweapons[3])
        text_file.write(pdfweapons[4])
        text_file.write(pdfweapons[5])
        text_file.write(pdfweapons[6])
        text_file.write(pdfweapons[7])
        text_file.write(pdfweapons[8])
        text_file.write(pdfweapons[9])
        text_file.write(pdfweapons[10])
        text_file.write(pdfweapons[11])
        text_file.write(pdfweapons[12])
        text_file.write(pdfweapons[13])
        text_file.write(pdfweapons[14])

#-------------------------------------#
#    Attributes and Related Values    #
#-------------------------------------#

#Strength

        text_file.write("Str: {}\n".format(attributes[0]))
        text_file.write("Hit Adj: {}\n".format(stronk[0]))
        text_file.write("Dmg Adj: {}\n".format(stronk[1]))
        text_file.write("Weight Allowed:{}\n".format(stronk[2]))
        text_file.write("Max Press: {}\n".format(stronk[3]))
        text_file.write("Open Door:{}\n".format(stronk[4]))
        text_file.write("Bend Bar Lift Gate: {}\n".format(stronk[5]))

#Dexterity
        text_file.write("Dex: {}\n".format(attributes[1]))

#Constitution
        text_file.write("Con: {}\n".format(attributes[2]))

#Intelligence
        text_file.write("Int: {}\n".format(attributes[3]))

#Wisdom
        text_file.write("Wis: {}\n".format(attributes[4]))

#Constitution
        text_file.write("Cha: {}\n".format(attributes[5]))


        text_file.write(str(hp))


    text_file.close()

#-------------#
# PDF Writing #
#-------------#

    pdfheader=[]
    pdfattributes=[]
    pdfproficiencies=[]

#-----Header-----#

    pdfheader.append(name)
    pdfheader.append("1") #TEMP SPACE FOR LEVEL
    pdfheader.append(race)
    pdfheader.append(playerclass)
    pdfheader.append("TN")#TEMP SPACE FOR ALIGNMENT
    pdfheader.append(god)
    pdfheader.append("HOME")#TEMP SPACE FOR HOME
    pdfheader.append(gender)
    pdfheader.append(str(years))
    pdfheader.append(alt)
    pdfheader.append(lbs)
    pdfheader.append(str(hairs))
    pdfheader.append(eye)
    pdfheader.append(app)
    pdfheader.append(beard)
    pdfheader.append(occ)
    pdfheader.append(person)


#-----Attributes-----#

    pdfattributes.append(attributes[0])
    pdfattributes=pdfattributes+stronk
    pdfattributes.append(attributes[1])
    pdfattributes=pdfattributes+dex
    pdfattributes.append(attributes[2])
    pdfattributes=pdfattributes+con
    pdfattributes.append(attributes[3])
    pdfattributes=pdfattributes+smarts
    pdfattributes.append(attributes[4])
    pdfattributes=pdfattributes+wis
    pdfattributes.append(attributes[5])
    pdfattributes=pdfattributes+cha

#-----Proficiencies-----#

    pdfproficiencies=wplist+profs
    while len(pdfproficiencies)<20:
        pdfproficiencies.append("")

#----Inventory---#



    pdfwriter.write(pdfheader,motive,pdfattributes,pdfproficiencies,pdfweapons,remainingdosh,hp,playerarmour,move,save,miscequ,skills,spelllist,equipweight,pdfpath.format(title))

#--------#
# Return #
#--------#

    x.append(pdfpath.format(title))

    x.append("\n\n**Character Sheets are automatically saved to a trash folder that will be occasionally cleared, notify me if there is one you want to keep.**\n\n**The only race that can be rolled right now is 'Human' while tests are being conducted**\n\n**Right now proficiencies sometimes get rolled twice. If its non-weapon treat it as specialized, if its a weapon proficincy you're just out of luck for now**\n\n**I encourage contributions, it means alot more can get done.**\n\n**Tell me if an error occurs!**\n\n**        -Love, Hina**")

    return x
