from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

    #c.line(x1,y1,x2,y2)





def write(header,motive,attributes,proficiencies,weapons,dosh,hp,armour,move,save,miscequ,skills,spelllist,weight,fp):

    c=canvas.Canvas(fp)
    c.translate(inch,inch) #moves origin from bottom left to top left
    c.setFont("Helvetica",10)

    #c.setFillColorRGB(.8,.8,.8)
    #c.rect(-1*inch,-1*inch,9.27*inch,12.69*inch,fill=1) Potential Colours
    #c.setFillColorRGB(0,0,0)
    xpos=0


#-----------------#
# Begin Section 1 #
#-----------------#

#-------#
# Row 1 #
#-------#

#-----Name-----#
    
    c.drawString(-.8*inch,10.5*inch,"Character:")
    c.line(-.1*inch,10.45*inch,3*inch,10.45*inch)
    c.drawString(-.1*inch,10.5*inch,header[0])

#-----Level-----#

    c.drawString(3.1*inch,10.5*inch,"Level:")
    c.line(3.6*inch,10.45*inch,3.8*inch,10.45*inch)
    c.drawString(3.6*inch,10.5*inch,header[1])

#-----Race-----#

    c.drawString(3.9*inch,10.5*inch,"Race:")
    c.line(4.4*inch,10.45*inch,7*inch,10.45*inch)
    c.drawString(4.4*inch,10.5*inch,header[2])

#-------#
# Row 2 #
#-------#

#-----Class-----#

    c.drawString(-.8*inch,10.25*inch,"Class:")
    c.line(-.3*inch,10.20*inch,.5*inch,10.20*inch)
    c.drawString(-.3*inch,10.25*inch,header[3])

#-----Alignment-----#

    c.drawString(.6*inch,10.25*inch,"Alignment:")
    c.line(1.3*inch,10.20*inch,1.5*inch,10.20*inch)
    c.drawString(1.3*inch,10.25*inch,header[4])

#-----Religion-----#

    c.drawString(1.6*inch,10.25*inch,"Religion:")
    c.line(2.2*inch,10.20*inch,3*inch,10.20*inch)
    c.drawString(2.2*inch,10.25*inch,header[5])

#-----Homeland-----#

    c.drawString(3.1*inch,10.25*inch,"Homeland:")
    c.line(3.8*inch,10.20*inch,5.4*inch,10.20*inch)
    c.drawString(3.8*inch,10.25*inch,header[6])

#-----Gender-----#

    c.drawString(5.5*inch,10.25*inch,"Gender:")
    c.line(6*inch,10.20*inch,7*inch,10.20*inch)
    c.drawString(6*inch,10.25*inch,header[7])

#-------#
# Row 3 #
#-------#


#-----Age-----#

    c.drawString(-.8*inch,10*inch,"Age:")
    c.line(-.5*inch,9.95*inch,-.3*inch,9.95*inch)
    c.drawString(-.5*inch,10*inch,header[8])

#-----Height-----#

    c.drawString(-.2*inch,10*inch,"Height:")
    c.line(.3*inch,9.95*inch,.6*inch,9.95*inch)
    c.drawString(.3*inch,10*inch,header[9])

#-----Weight-----#

    c.drawString(.7*inch,10*inch,"Weight:")
    c.line(1.2*inch,9.95*inch,1.5*inch,9.95*inch)
    c.drawString(1.2*inch,10*inch,header[10])

#-----Hair-----#

    c.drawString(1.6*inch,10*inch,"Hair:")
    c.line(1.95*inch,9.95*inch,2.8*inch,9.95*inch)
    c.drawString(1.95*inch,10*inch,header[11])

#-----Eyes-----#

    c.drawString(2.9*inch,10*inch,"Eyes:")
    c.line(3.3*inch,9.95*inch,4.5*inch,9.95*inch)
    c.drawString(3.3*inch,10*inch,header[12])

#-----Appearance-----#

    c.drawString(4.6*inch,10*inch,"Trait:")
    c.line(5*inch,9.95*inch,7*inch,9.95*inch)
    c.drawString(5*inch,10*inch,header[13])



#-------#
# Row 4 #
#-------#

#---Facial Hair---#

    c.drawString(-.8*inch,9.75*inch,"Facial Hair:")
    c.line(0*inch,9.7*inch,1.5*inch,9.7*inch)
    c.drawString(0*inch,9.75*inch,header[14])

#---Previous Occupation---#

    c.drawString(1.6*inch,9.75*inch,"Occupation:")
    c.line(2.4*inch,9.7*inch,4.1*inch,9.7*inch)
    c.drawString(2.4*inch,9.75*inch,header[15])

#---Personality---#

    c.drawString(4.2*inch,9.75*inch,"Personality:")
    c.line(5*inch,9.7*inch,7*inch,9.7*inch)
    c.drawString(5*inch,9.75*inch,header[16])

#-------#
# Row 5 #
#-------#

#---Motivation---#

    c.drawString(-.8*inch,9.50*inch,"Motivation:")
    c.line(-.1*inch,9.45*inch,7*inch,9.45*inch)
    c.drawString(-.1*inch,9.50*inch,motive)
    

    

#------------------#
# End of Section 1 #
#------------------#

    c.line(-.8*inch,9.3*inch,7*inch,9.3*inch)

#-----------------#
# Begin Section 2 #
#-----------------#

    #-STRENGTH-#

    xpos=8.9
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,(xpos+.1)*inch,"STR")
    c.drawString(-.4*inch,(xpos+.1)*inch,str(attributes[0]))
    c.drawString(0*inch,(xpos+.1)*inch,"Hit Prob:")
    c.drawString(.7*inch,(xpos+.1)*inch,attributes[1])
    c.drawString(1.1*inch,(xpos+.1)*inch,"DMG Adj.:")
    c.drawString(1.8*inch,(xpos+.1)*inch,attributes[2])
    c.drawString(2.2*inch,(xpos+.1)*inch,"Enc.:")
    c.drawString(2.6*inch,(xpos+.1)*inch,attributes[3])
    c.drawString(3.3*inch,(xpos+.1)*inch,"Max Press:")
    c.drawString(4.1*inch,(xpos+.1)*inch,attributes[4])
    c.drawString(4.4*inch,(xpos+.1)*inch,"Open Door:")
    c.drawString(5.2*inch,(xpos+.1)*inch,attributes[5])
    c.drawString(5.5*inch,(xpos+.1)*inch,"B.B./L.G.:")
    c.drawString(6.1*inch,(xpos+.1)*inch,attributes[6])

    #-DEXTERITY-#

    xpos=xpos-.3
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,(xpos+.1)*inch,"DEX")
    c.drawString(-.4*inch,(xpos+.1)*inch,str(attributes[7]))
    c.drawString(0*inch,(xpos+.1)*inch,"Reaction Adj.")
    c.drawString(1*inch,(xpos+.1)*inch,attributes[8])
    c.drawString(3*inch,(xpos+.1)*inch,"Missile Attack Adj.")
    c.drawString(4.5*inch,(xpos+.1)*inch,attributes[9])
    c.drawString(5*inch,(xpos+.1)*inch,"Defensive Adj.")
    c.drawString(6*inch,(xpos+.1)*inch,attributes[10])

    #-CONSTITUTION-#

    xpos=xpos-.3
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,(xpos+.1)*inch,"CON")
    c.drawString(-.4*inch,(xpos+.1)*inch,str(attributes[11]))
    c.drawString(0*inch,(xpos+.1)*inch,"HP Adj.:")
    c.drawString(.6*inch,(xpos+.1)*inch,attributes[12])
    c.drawString(1*inch,(xpos+.1)*inch,"System Shock:")
    c.drawString(2*inch,(xpos+.1)*inch,attributes[13])
    c.drawString(2.5*inch,(xpos+.1)*inch,"Rez Survival:")
    c.drawString(3.5*inch,(xpos+.1)*inch,attributes[14])
    c.drawString(4*inch,(xpos+.1)*inch,"Poison Save:")
    c.drawString(5*inch,(xpos+.1)*inch,attributes[15])
    c.drawString(5.5*inch,(xpos+.1)*inch,"Regeneration:")
    c.drawString(6.5*inch,(xpos+.1)*inch,attributes[16])

    #-Intelligence-#

    xpos=xpos-.3
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,(xpos+.1)*inch,"INT")
    c.drawString(-.4*inch,(xpos+.1)*inch,str(attributes[17]))
    c.drawString(0*inch,(xpos+.1)*inch,"Languages:")
    c.drawString(.8*inch,(xpos+.1)*inch,attributes[18])
    c.drawString(1*inch,(xpos+.1)*inch,"Spell Level:")
    c.drawString(2*inch,(xpos+.1)*inch,attributes[19])
    c.drawString(2.5*inch,(xpos+.1)*inch,"Chance to Learn:")
    c.drawString(3.7*inch,(xpos+.1)*inch,attributes[20])
    c.drawString(4*inch,(xpos+.1)*inch,"Max Spells:")
    c.drawString(5*inch,(xpos+.1)*inch,attributes[21])
    c.drawString(5.5*inch,(xpos+.1)*inch,"Illusion Immune:")
    c.drawString(6.6*inch,(xpos+.1)*inch,attributes[22])

    #-Wisdom-#

    xpos=xpos-.3
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,(xpos+.1)*inch,"WIS")
    c.drawString(-.4*inch,(xpos+.1)*inch,str(attributes[23]))
    c.drawString(0*inch,(xpos+.1)*inch,"Magic Def. Adj.:")
    c.drawString(1*inch,(xpos+.1)*inch,attributes[24])
    c.drawString(2*inch,(xpos+.1)*inch,"Bonus Spells:")
    c.drawString(3*inch,(xpos+.1)*inch,attributes[25])
    c.drawString(4*inch,(xpos+.1)*inch,"Spell Fail:")
    c.drawString(5*inch,(xpos+.1)*inch,attributes[26])
    c.drawString(6*inch,(xpos+.1)*inch,"Spell Immune:")
    c.drawString(7*inch,(xpos+.1)*inch,attributes[27])

    #-Charisma-#

    xpos=xpos-.3
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,(xpos+.1)*inch,"CHA")
    c.drawString(-.4*inch,(xpos+.1)*inch,str(attributes[28]))
    c.drawString(0*inch,(xpos+.1)*inch,"Max Hench:")
    c.drawString(1*inch,(xpos+.1)*inch,str(attributes[29]))
    c.drawString(3*inch,(xpos+.1)*inch,"Loyalty Base:")
    c.drawString(4.5*inch,(xpos+.1)*inch,attributes[30])
    c.drawString(5*inch,(xpos+.1)*inch,"Reaction Adj.:")
    c.drawString(6*inch,(xpos+.1)*inch,attributes[31])

    #Divider#

    c.line(-.1*inch,xpos*inch,-.1*inch,(xpos+1.75)*inch)

#---------------#
# End Section 2 #
#---------------#

#-----------------#
# Begin Section 3 #
#-----------------#

#---Health/Armour---#

#Column 1#

    xpos=xpos-1.1
    c.rect(-.9*inch,xpos*inch,2.8*inch,1*inch)
    c.drawString(-.8*inch,(xpos+.85)*inch,"HP")
    c.drawString(-.1*inch,(xpos+.85)*inch,str(hp))

    c.drawString(-.8*inch,(xpos+.475)*inch,"AC")
    if attributes[10].find('-') != -1:
        attributes[10]=attributes[10].lstrip('-')
        c.drawString(-.1*inch,(xpos+.475)*inch,str(int(armour[2])-int(attributes[10])))
    elif attributes[10].find('+') != -1:
        attributes[10]=attributes[10].lstrip('+')
        c.drawString(-.1*inch,(xpos+.475)*inch,str(int(armour[2])+int(attributes[10])))
    else:
        c.drawString(-.1*inch,(xpos+.475)*inch,str(int(armour[2])))

    c.drawString(-.8*inch,(xpos+.1)*inch,"Flatfoot")
    if str(armour[3])=='':
        c.drawString(-.1*inch,(xpos+.1)*inch,str(armour[2]))
    else:
        c.drawString(-.1*inch,(xpos+.1)*inch,str(armour[2]+1))

#Column 2#

    c.drawString(1.2*inch,(xpos+.85)*inch,"Weight:")
    c.drawString(1.7*inch,(xpos+.85)*inch,(str(armour[4])))

    c.drawString(.5*inch,((xpos+.85))*inch,"Armour")
    c.line(.5*inch,(xpos+.8)*inch,1*inch,(xpos+.8)*inch)
    c.drawString(.5*inch,(xpos+.475)*inch,str(armour[1]))

    c.drawString(.5*inch,(xpos+.1)*inch,str(armour[3]))   #shield


#---Movement---#

    c.rect(2.1*inch,xpos*inch,5*inch,1*inch)

    c.drawString(2.2*inch,(xpos+.85)*inch,"Unencumbered:")
    c.drawString(2.2*inch,(xpos+.65)*inch,"Light:")
    c.drawString(2.2*inch,(xpos+.45)*inch,"Moderate:")
    c.drawString(2.2*inch,(xpos+.25)*inch,"Heavy:")
    c.drawString(2.2*inch,(xpos+.05)*inch,"Severe:")

    c.drawString(3.2*inch,(xpos+.65)*inch,'('+str(move[5])+')') #weight
    c.drawString(3.2*inch,(xpos+.45)*inch,'('+str(move[6])+')')
    c.drawString(3.2*inch,(xpos+.25)*inch,'('+str(move[7])+')')
    c.drawString(3.2*inch,(xpos+.05)*inch,'('+str(move[8])+')')

    c.drawString(3.7*inch,(xpos+.85)*inch,str(move[0])) #speed
    c.drawString(3.7*inch,(xpos+.65)*inch,str(move[1]))
    c.drawString(3.7*inch,(xpos+.45)*inch,str(move[2]))
    c.drawString(3.7*inch,(xpos+.25)*inch,str(move[3]))
    c.drawString(3.7*inch,(xpos+.05)*inch,str(move[4]))

    c.drawString(4.2*inch,(xpos+.1)*inch,"")
    c.drawString(4.2*inch,(xpos+.65)*inch,"Jog")
    c.drawString(4.2*inch,(xpos+.45)*inch,"Charge")
    c.drawString(4.2*inch,(xpos+.25)*inch,"Run")
    c.drawString(4.2*inch,(xpos+.05)*inch,"Sprint")

    c.line(4.3*inch,(xpos+.8)*inch,7*inch,(xpos+.8)*inch)

    c.drawString(4.7*inch,(xpos+.85)*inch,"Speed")
    c.drawString(4.7*inch,(xpos+.65)*inch,"X2")
    c.drawString(4.7*inch,(xpos+.45)*inch,"X3")
    c.drawString(4.7*inch,(xpos+.25)*inch,"X4")
    c.drawString(4.7*inch,(xpos+.05)*inch,"X5")

    c.drawString(5.2*inch,(xpos+.85)*inch,"Atk Adj.")
    c.drawString(5.2*inch,(xpos+.65)*inch,"0")
    c.drawString(5.2*inch,(xpos+.45)*inch,"+2")
    c.drawString(5.2*inch,(xpos+.25)*inch,"+4")
    c.drawString(5.2*inch,(xpos+.05)*inch,"+8")

    c.drawString(5.8*inch,(xpos+.85)*inch,"Dmg Adj.")
    c.drawString(5.8*inch,(xpos+.65)*inch,"0")
    c.drawString(5.8*inch,(xpos+.45)*inch,"0")
    c.drawString(5.8*inch,(xpos+.25)*inch,"+1")
    c.drawString(5.8*inch,(xpos+.05)*inch,"+2")

    c.drawString(6.4*inch,(xpos+.85)*inch,"AC Adj")
    c.drawString(6.4*inch,(xpos+.65)*inch,"Flatfoot")
    c.drawString(6.4*inch,(xpos+.45)*inch,"+1")
    c.drawString(6.4*inch,(xpos+.25)*inch,"+3")
    c.drawString(6.4*inch,(xpos+.05)*inch,"+5")


#------------------#
# Begin Weapon Box # Condense this section to a loop
#------------------#

    xpos=xpos-.15
    c.drawString(2.5*inch,xpos*inch,"Weapons")

    xpos=xpos-.4
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)

    xpos=xpos+.11
    c.drawString(-.8*inch,xpos*inch,"Name")
    c.drawString(1.6*inch,xpos*inch,"RoF")
    c.drawString(2.1*inch,xpos*inch,"THAC0")
    c.drawString(2.8*inch,xpos*inch,"Dmg Adj.")
    c.drawString(3.5*inch,xpos*inch,"Damage")
    c.drawString(4.5*inch,xpos*inch,"Range")
    c.drawString(5.5*inch,xpos*inch,"Type")
    c.drawString(6*inch,xpos*inch,"Speed")
    c.drawString(6.6*inch,xpos*inch,"Weight")
    xpos=xpos+.04

#---Weapon 1---#

    xpos=xpos-.45
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)

    xpos=xpos+.11
    c.drawString(-.8*inch,xpos*inch,weapons[1])
    weapons[2]=RateofFire(header[3],weapons[1],weapons[2])
    c.drawString(1.6*inch,xpos*inch,weapons[2])
    if weapons[1] != '':
        weapons[3]=THAC0(attributes[8],attributes[1],proficiencies[0],weapons[3])
    c.drawString(2.1*inch,xpos*inch,weapons[3])
    if weapons[1] != '':
        weapons[4]=DamageAdj(weapons[4],attributes[2],proficiencies[0])
    c.drawString(2.8*inch,xpos*inch,weapons[4])
    if weapons[5].find(':')!=-1:
            c.setFont("Helvetica",6)
    c.drawString(3.5*inch,xpos*inch,weapons[5])
    c.setFont("Helvetica",10)
    c.drawString(4.5*inch,xpos*inch,weapons[6])
    c.drawString(5.5*inch,xpos*inch,weapons[7])
    c.drawString(6*inch,xpos*inch,weapons[8])
    c.drawString(6.6*inch,xpos*inch,weapons[9])
    xpos=xpos+.04

#---Weapon 2---#

    xpos=xpos-.45
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)

    xpos=xpos+.11
    c.drawString(-.8*inch,xpos*inch,weapons[10])
    weapons[11]=RateofFire(header[3],weapons[10],weapons[11])
    c.drawString(1.6*inch,xpos*inch,weapons[11])
    if weapons[10] != '':
        weapons[12]=THAC0(attributes[8],attributes[1],proficiencies[1],weapons[12])
    c.drawString(2.1*inch,xpos*inch,weapons[12])
    if weapons[10] != '':
        weapons[13]=DamageAdj(weapons[13],attributes[2],proficiencies[0])
    c.drawString(2.8*inch,xpos*inch,weapons[13])
    if weapons[14].find(':')!=-1:
            c.setFont("Helvetica",6)
    c.drawString(3.5*inch,xpos*inch,weapons[14])
    c.setFont("Helvetica",10)
    c.drawString(4.5*inch,xpos*inch,weapons[15])
    c.drawString(5.5*inch,xpos*inch,weapons[16])
    c.drawString(6*inch,xpos*inch,weapons[17])
    c.drawString(6.6*inch,xpos*inch,weapons[18])
    xpos=xpos+.04

#---Weapon 3---#

    xpos=xpos-.45
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)

    xpos=xpos+.11
    c.drawString(-.8*inch,xpos*inch,weapons[19])
    weapons[20]=RateofFire(header[3],weapons[19],weapons[20])
    c.drawString(1.6*inch,xpos*inch,weapons[20])
    if weapons[19] != '':
        weapons[21]=THAC0(attributes[8],attributes[1],proficiencies[2],weapons[21])
    c.drawString(2.1*inch,xpos*inch,weapons[21])
    if weapons[19] != '':
        weapons[22]=DamageAdj(weapons[22],attributes[2],proficiencies[0])
    c.drawString(2.8*inch,xpos*inch,weapons[22])
    if weapons[23].find(':')!=-1:
            c.setFont("Helvetica",6)
    c.drawString(3.5*inch,xpos*inch,weapons[23])
    c.setFont("Helvetica",10)
    c.drawString(4.5*inch,xpos*inch,weapons[24])
    c.drawString(5.5*inch,xpos*inch,weapons[25])
    c.drawString(6*inch,xpos*inch,weapons[26])
    c.drawString(6.6*inch,xpos*inch,weapons[27])
    xpos=xpos+.04

#---Weapon 4---#

    xpos=xpos-.45
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)

    xpos=xpos+.11
    c.drawString(-.8*inch,xpos*inch,weapons[28])
    weapons[29]=RateofFire(header[3],weapons[28],weapons[29])
    c.drawString(1.6*inch,xpos*inch,weapons[29])
    if weapons[28] != '':
        weapons[30]=THAC0(attributes[8],attributes[1],proficiencies[3],weapons[30])
    c.drawString(2.1*inch,xpos*inch,weapons[30])
    if weapons[28] != '':
        weapons[31]=DamageAdj(weapons[31],attributes[2],proficiencies[0])
    c.drawString(2.8*inch,xpos*inch,weapons[31])
    if weapons[32].find(':')!=-1:
            c.setFont("Helvetica",6)
    c.drawString(3.5*inch,xpos*inch,weapons[32])
    c.setFont("Helvetica",10)
    c.drawString(4.5*inch,xpos*inch,weapons[33])
    c.drawString(5.5*inch,xpos*inch,weapons[34])
    c.drawString(6*inch,xpos*inch,weapons[35])
    c.drawString(6.6*inch,xpos*inch,weapons[36])
    xpos=xpos+.04

#---Weapon 5---#

    xpos=xpos-.45
    c.rect(-.9*inch,xpos*inch,8*inch,.3*inch)

    xpos=xpos+.11
    c.drawString(-.8*inch,xpos*inch,weapons[37])
    weapons[38]=RateofFire(header[3],weapons[37],weapons[38])
    c.drawString(1.6*inch,xpos*inch,weapons[38])
    if weapons[37] != '':
        weapons[39]=THAC0(attributes[8],attributes[1],proficiencies[4],weapons[39])
    c.drawString(2.1*inch,xpos*inch,weapons[39])
    if weapons[37] != '':
        weapons[40]=DamageAdj(weapons[40],attributes[2],proficiencies[0])
    c.drawString(2.8*inch,xpos*inch,weapons[40])
    if weapons[41].find(':')!=-1:
            c.setFont("Helvetica",6)
    c.drawString(3.5*inch,xpos*inch,weapons[41])
    c.setFont("Helvetica",10)
    c.drawString(4.5*inch,xpos*inch,weapons[42])
    c.drawString(5.5*inch,xpos*inch,weapons[43])
    c.drawString(6*inch,xpos*inch,weapons[44])
    c.drawString(6.6*inch,xpos*inch,weapons[45])
    xpos=xpos+.04

#---Grid Lines---#

    xpos=xpos-.15
    c.line(1.5*inch,xpos*inch,1.5*inch,(xpos+1.8)*inch)		#Name
    c.line(2*inch,xpos*inch,2*inch,(xpos+1.8)*inch)		#RoF
    c.line(2.7*inch,xpos*inch,2.7*inch,(xpos+1.8)*inch)		#atkadj
    c.line(3.4*inch,xpos*inch,3.4*inch,(xpos+1.8)*inch)		#dmgadj
    c.line(4.4*inch,xpos*inch,4.4*inch,(xpos+1.8)*inch)		#dmg
    c.line(5.4*inch,xpos*inch,5.4*inch,(xpos+1.8)*inch)		#range
    c.line(5.9*inch,xpos*inch,5.9*inch,(xpos+1.8)*inch)		#type
    c.line(6.5*inch,xpos*inch,6.5*inch,(xpos+1.8)*inch)		#speed

#-------#
# Saves #
#-------#

    xpos=xpos-1.7
    c.rect(-.9*inch,xpos*inch,2*inch,1.65*inch)

    c.drawCentredString(.15*inch,(xpos+1.5)*inch,"Saving Throws")

    c.drawString(-.8*inch,(xpos+1.3)*inch,"Paralyze/Poison")
    c.drawString(-.8*inch,(xpos+1.1)*inch,"Rod, Staff or Wand")
    c.drawString(-.8*inch,(xpos+.9)*inch,"Petrify/Polymorph")
    c.drawString(-.8*inch,(xpos+.7)*inch,"Breath")
    c.drawString(-.8*inch,(xpos+.5)*inch,"Spell")
    c.drawString(-.8*inch,(xpos+.3)*inch,"Reaction Adj.")
    c.drawString(-.8*inch,(xpos+.1)*inch,"Macabre")

#---Modify Saves Based on Attributes---#

#Poison#

    if attributes[15].find('-') != -1:
        attributes[15]=attributes[15].lstrip('-')
        save[0]=save[0]+int(attributes[15])
    elif attributes[15].find('+') != -1:
        save[0]=save[0]-int(attributes[15])

#Magic Save#

    if attributes[24].find('-') != -1:
        attributes[24]=attributes[24].lstrip('-')
        save[4]=save[4]+int(attributes[24])
    elif attributes[24].find('+') != -1:
        save[4]=save[4]-int(attributes[24])

#Reaction Adj#

    react=17   
	#dex#
    if attributes[8].find('-') != -1:
        attributes[8]=attributes[8].lstrip('-')
        react=react+int(attributes[8])
    elif attributes[8].find('+') != -1:
        attributes[8]=attributes[8].lstrip('+')
        react=react-int(attributes[8])
	#cha#
    if attributes[31].find('-') != -1:
        attributes[31]=attributes[31].lstrip('-')
        react=react+int(attributes[31])
    elif attributes[31].find('+') != -1:
        attributes[31]=attributes[31].lstrip('+')
        react=react-int(attributes[31])

#Mind that Dwarves get an additional Magic and Poison save.

    c.drawString(.6*inch,(xpos+1.3)*inch,str(save[0]))
    c.drawString(.6*inch,(xpos+1.1)*inch,str(save[1]))
    c.drawString(.6*inch,(xpos+.9)*inch,str(save[2]))
    c.drawString(.6*inch,(xpos+.7)*inch,str(save[3]))
    c.drawString(.6*inch,(xpos+.5)*inch,str(save[4]))
    c.drawString(.6*inch,(xpos+.3)*inch,str(react))
    c.drawString(.6*inch,(xpos+.1)*inch,'0')


#-----------#
# Equipment #
#-----------#

    c.rect(1.2*inch,xpos*inch,5.85*inch,1.65*inch)

#---Begin: Convert Dosh to Currency---#

    gold=int(dosh/100)
    dosh=dosh%100
    silver=int(dosh/10)
    copper=dosh%10
    weight=weight+((gold+silver+copper)/50)

#---Wealth Column---#


    c.drawString(1.3*inch,(xpos+1.4)*inch,"Platinum:")
    c.drawString(2*inch,(xpos+1.4)*inch,"0")

    c.drawString(1.3*inch,(xpos+1.15)*inch,"Gold:")
    c.drawString(2*inch,(xpos+1.15)*inch,str(gold))

    c.drawString(1.3*inch,(xpos+.9)*inch,"Silver:")
    c.drawString(2*inch,(xpos+.9)*inch,str(silver))

    c.drawString(1.3*inch,(xpos+.65)*inch,"Copper:")
    c.drawString(2*inch,(xpos+.65)*inch,str(copper))

    c.drawString(1.3*inch,(xpos+.05)*inch,"Weight")

#Remove Rounding from Float#
    weight=weight*1000
    top=int(weight/1000)
    bottom=int(weight)%1000

    c.drawString(2*inch,(xpos+.05)*inch,(str(top)+'.'+str(bottom))) 

#---Column 1---# 

    c.drawString(2.5*inch,(xpos+1.5)*inch,"Item:")
    c.drawString(4*inch,(xpos+1.5)*inch,"Qty.")
    c.drawString(4.3*inch,(xpos+1.5)*inch,"Wgt.")

    c.drawString(2.5*inch,(xpos+1.35)*inch,str(miscequ[1]))
    c.drawString(4*inch,(xpos+1.35)*inch,str(miscequ[2]))
    c.drawString(4.3*inch,(xpos+1.35)*inch,str(miscequ[3]))
    c.line(2.5*inch,(xpos+1.3)*inch,4.45*inch,(xpos+1.3)*inch)

    c.drawString(2.5*inch,(xpos+1.1)*inch,str(miscequ[4]))
    c.drawString(4*inch,(xpos+1.1)*inch,str(miscequ[5]))
    c.drawString(4.3*inch,(xpos+1.1)*inch,str(miscequ[6]))
    c.line(2.5*inch,(xpos+1.05)*inch,4.45*inch,(xpos+1.05)*inch)

    c.drawString(2.5*inch,(xpos+.85)*inch,str(miscequ[7]))
    c.drawString(4*inch,(xpos+.85)*inch,str(miscequ[8]))
    c.drawString(4.3*inch,(xpos+.85)*inch,str(miscequ[9]))
    c.line(2.5*inch,(xpos+.8)*inch,4.45*inch,(xpos+.8)*inch)

    c.drawString(2.5*inch,(xpos+.6)*inch,str(miscequ[10]))
    c.drawString(4*inch,(xpos+.6)*inch,str(miscequ[11]))
    c.drawString(4.3*inch,(xpos+.6)*inch,str(miscequ[12])) 
    c.line(2.5*inch,(xpos+.55)*inch,4.45*inch,(xpos+.55)*inch)

    c.drawString(2.5*inch,(xpos+.35)*inch,str(miscequ[13]))
    c.drawString(4*inch,(xpos+.35)*inch,str(miscequ[14]))
    c.drawString(4.3*inch,(xpos+.35)*inch,str(miscequ[15]))
    c.line(2.5*inch,(xpos+.3)*inch,4.45*inch,(xpos+.3)*inch) 

#---Column 2---# 

    c.drawString(4.7*inch,(xpos+1.5)*inch,"Item:")
    c.drawString(6.2*inch,(xpos+1.5)*inch,"Qty.")
    c.drawString(6.5*inch,(xpos+1.5)*inch,"Wgt.")

    c.drawString(4.7*inch,(xpos+1.35)*inch,str(miscequ[16]))
    c.drawString(6.2*inch,(xpos+1.35)*inch,str(miscequ[17]))
    c.drawString(6.5*inch,(xpos+1.35)*inch,str(miscequ[18]))
    c.line(4.7*inch,(xpos+1.3)*inch,6.65*inch,(xpos+1.3)*inch)

    c.drawString(4.7*inch,(xpos+1.1)*inch,str(miscequ[19]))
    c.drawString(6.2*inch,(xpos+1.1)*inch,str(miscequ[20]))
    c.drawString(6.5*inch,(xpos+1.1)*inch,str(miscequ[21]))
    c.line(4.7*inch,(xpos+1.05)*inch,6.65*inch,(xpos+1.05)*inch)

    c.drawString(4.7*inch,(xpos+.85)*inch,str(miscequ[22]))
    c.drawString(6.2*inch,(xpos+.85)*inch,str(miscequ[23]))
    c.drawString(6.5*inch,(xpos+.85)*inch,str(miscequ[24]))
    c.line(4.7*inch,(xpos+.8)*inch,6.65*inch,(xpos+.8)*inch)

    c.drawString(4.7*inch,(xpos+.6)*inch,str(miscequ[25]))
    c.drawString(6.2*inch,(xpos+.6)*inch,str(miscequ[26]))
    c.drawString(6.5*inch,(xpos+.6)*inch,str(miscequ[27]))
    c.line(4.7*inch,(xpos+.55)*inch,6.65*inch,(xpos+.55)*inch) 

    c.drawString(4.7*inch,(xpos+.35)*inch,str(miscequ[28]))
    c.drawString(6.2*inch,(xpos+.35)*inch,str(miscequ[29]))
    c.drawString(6.5*inch,(xpos+.35)*inch,str(miscequ[30]))
    c.line(4.7*inch,(xpos+.3)*inch,6.65*inch,(xpos+.3)*inch)



#----------------#
# Begin Prof Box #
#----------------#

    xpos=xpos-3.1
    c.drawString(1*inch,(xpos+2.7)*inch,"Proficiencies")
    c.rect(-.9*inch,xpos*inch,4.6*inch,2.85*inch)

#---Column 1---#

    i=0
    while i<=9:
       profskill=proficiencies[i].split(":")
       while len(profskill)<2:
           profskill.append('')
       c.drawString(-.8*inch,((xpos+2.5)-(i*.25))*inch,profskill[0])
       c.drawString(.7*inch,((xpos+2.5)-(i*.25))*inch,profskill[1])
       c.line(-.8*inch,((xpos+2.45)-(i*.25))*inch,1.2*inch,((xpos+2.45)-(i*.25))*inch)
       i+=1



#---Column 2---#

    i=0
    while i<=9:
       profskill=proficiencies[i+10].split(":")
       while len(profskill)<2:
           profskill.append('')
       c.drawString(1.4*inch,((xpos+2.5)-(i*.25))*inch,profskill[0])
       c.drawString(2.9*inch,((xpos+2.5)-(i*.25))*inch,profskill[1]) 
       c.line(1.4*inch,((xpos+2.45)-(i*.25))*inch,3.4*inch,((xpos+2.45)-(i*.25))*inch)
       i+=1


#-------------------#
# Begin Special Box #
#-------------------#

    c.drawString(4.9*inch,(xpos+2.7)*inch,"Special Abilities")
    c.rect(3.8*inch,xpos*inch,3.4*inch,2.85*inch)

#---Fill With Special Rules---#
    i=0
    specialweapons=['Awl Pike','Bariche','Bec De Corbin','Bill','Bola','Caltrop','Fauchard','Glaive','Lasso','Long Spear','Spear','Main-Gauche','Mancatcher','Military Fork','Net','Parrying Dagger','Partisian','Ranseur','Sap','Scimitar','Scourge','Spear','Spetum','Staff Sling','Stiletto','Volgue','Whip']
    while i<len(proficiencies):
        if proficiencies[i] in specialweapons:
            skills.append(proficiencies[i])
        i+=1

#---Fill Blank Spaces---#
    while len(skills)<20:
        skills.append("")

#---Column 1---#

    c.drawString(3.9*inch,(xpos+2.5)*inch,skills[0])
    c.drawString(3.9*inch,(xpos+2.25)*inch,skills[1])
    c.drawString(3.9*inch,(xpos+2)*inch,skills[2])
    c.drawString(3.9*inch,(xpos+1.75)*inch,skills[3])
    c.drawString(3.9*inch,(xpos+1.5)*inch,skills[4])
    c.drawString(3.9*inch,(xpos+1.25)*inch,skills[5])
    c.drawString(3.9*inch,(xpos+1)*inch,skills[6])
    c.drawString(3.9*inch,(xpos+.75)*inch,skills[7])
    c.drawString(3.9*inch,(xpos+.5)*inch,skills[8])
    c.drawString(3.9*inch,(xpos+.25)*inch,skills[9])

    c.line(3.9*inch,(xpos+2.45)*inch,5.4*inch,(xpos+2.45)*inch)
    c.line(3.9*inch,(xpos+2.2)*inch,5.4*inch,(xpos+2.2)*inch)
    c.line(3.9*inch,(xpos+1.95)*inch,5.4*inch,(xpos+1.95)*inch)
    c.line(3.9*inch,(xpos+1.7)*inch,5.4*inch,(xpos+1.7)*inch)
    c.line(3.9*inch,(xpos+1.45)*inch,5.4*inch,(xpos+1.45)*inch)
    c.line(3.9*inch,(xpos+1.2)*inch,5.4*inch,(xpos+1.2)*inch)
    c.line(3.9*inch,(xpos+.95)*inch,5.4*inch,(xpos+.95)*inch)
    c.line(3.9*inch,(xpos+.7)*inch,5.4*inch,(xpos+.7)*inch)
    c.line(3.9*inch,(xpos+.45)*inch,5.4*inch,(xpos+.45)*inch)
    c.line(3.9*inch,(xpos+.2)*inch,5.4*inch,(xpos+.2)*inch)

#---Column 2---#

    c.drawString(5.5*inch,(xpos+2.5)*inch,skills[10])
    c.drawString(5.5*inch,(xpos+2.25)*inch,skills[11])
    c.drawString(5.5*inch,(xpos+2)*inch,skills[12])
    c.drawString(5.5*inch,(xpos+1.75)*inch,skills[13])
    c.drawString(5.5*inch,(xpos+1.5)*inch,skills[14])
    c.drawString(5.5*inch,(xpos+1.25)*inch,skills[15])
    c.drawString(5.5*inch,(xpos+1)*inch,skills[16])
    c.drawString(5.5*inch,(xpos+.75)*inch,skills[17])
    c.drawString(5.5*inch,(xpos+.5)*inch,skills[18])
    c.drawString(5.5*inch,(xpos+.25)*inch,skills[19])

    c.line(5.5*inch,(xpos+2.45)*inch,7*inch,(xpos+2.45)*inch)
    c.line(5.5*inch,(xpos+2.2)*inch,7*inch,(xpos+2.2)*inch)
    c.line(5.5*inch,(xpos+1.95)*inch,7*inch,(xpos+1.95)*inch)
    c.line(5.5*inch,(xpos+1.7)*inch,7*inch,(xpos+1.7)*inch)
    c.line(5.5*inch,(xpos+1.45)*inch,7*inch,(xpos+1.45)*inch)
    c.line(5.5*inch,(xpos+1.2)*inch,7*inch,(xpos+1.2)*inch)
    c.line(5.5*inch,(xpos+.95)*inch,7*inch,(xpos+.95)*inch)
    c.line(5.5*inch,(xpos+.7)*inch,7*inch,(xpos+.7)*inch)
    c.line(5.5*inch,(xpos+.45)*inch,7*inch,(xpos+.45)*inch)
    c.line(5.5*inch,(xpos+.2)*inch,7*inch,(xpos+.2)*inch)


#--------------#
# Begin Page 2 #
#--------------#

    c.showPage() #finishes writing on current page, starts a new page if more is added

    c.translate(inch,inch) #moves origin from bottom left to top left
    c.setFont("Helvetica",10)

#--------#
# Spells #
#--------#

    c.rect(-.9*inch,7.65*inch,8*inch,2.85*inch)
    c.drawString(-.8*inch,10.25*inch,'Spells Per Day:')

    spelllevel=attributes[25].split('/')
    spellsperday=''

    if header[3]=='Wizard':
        spellsperday='1'
    if header[3]=='Cleric':
        startingspell=1

        i=0
        spelllevel[0]=str(int(spelllevel[0])+startingspell)
        while i<len(spelllevel):
            spellsperday=spellsperday+spelllevel[i]+'/'
            i+=1

    c.drawString(.4*inch,10.25*inch,spellsperday)
        

#---Column 1---#
    c.drawString(-.8*inch,10*inch,spelllist[0])
    c.drawString(-.8*inch,9.75*inch,spelllist[1])
    c.drawString(-.8*inch,9.5*inch,spelllist[2])
    c.drawString(-.8*inch,9.25*inch,spelllist[3])
    c.drawString(-.8*inch,9*inch,spelllist[4])
    c.drawString(-.8*inch,8.75*inch,spelllist[5])
    c.drawString(-.8*inch,8.5*inch,spelllist[6])
    c.drawString(-.8*inch,8.25*inch,spelllist[7])
    c.drawString(-.8*inch,8*inch,spelllist[8])
    c.drawString(-.8*inch,7.75*inch,spelllist[9])

    c.line(-.8*inch,9.95*inch,1.6*inch,9.95*inch)
    c.line(-.8*inch,9.7*inch,1.6*inch,9.7*inch)
    c.line(-.8*inch,9.45*inch,1.6*inch,9.45*inch)
    c.line(-.8*inch,9.2*inch,1.6*inch,9.2*inch)
    c.line(-.8*inch,8.95*inch,1.6*inch,8.95*inch)
    c.line(-.8*inch,8.7*inch,1.6*inch,8.7*inch)
    c.line(-.8*inch,8.45*inch,1.6*inch,8.45*inch)
    c.line(-.8*inch,8.2*inch,1.6*inch,8.2*inch)
    c.line(-.8*inch,7.95*inch,1.6*inch,7.95*inch)
    c.line(-.8*inch,7.7*inch,1.6*inch,7.7*inch)


#---Column 2---#
    c.drawString(1.7*inch,10*inch,spelllist[10])
    c.drawString(1.7*inch,9.75*inch,spelllist[11])
    c.drawString(1.7*inch,9.5*inch,spelllist[12])
    c.drawString(1.7*inch,9.25*inch,spelllist[13])
    c.drawString(1.7*inch,9*inch,spelllist[14])
    c.drawString(1.7*inch,8.75*inch,spelllist[15])
    c.drawString(1.7*inch,8.5*inch,spelllist[16])
    c.drawString(1.7*inch,8.25*inch,spelllist[17])
    c.drawString(1.7*inch,8*inch,spelllist[18])
    c.drawString(1.7*inch,7.75*inch,spelllist[19])

    c.line(1.7*inch,9.95*inch,4.2*inch,9.95*inch)
    c.line(1.7*inch,9.7*inch,4.2*inch,9.7*inch)
    c.line(1.7*inch,9.45*inch,4.2*inch,9.45*inch)
    c.line(1.7*inch,9.2*inch,4.2*inch,9.2*inch)
    c.line(1.7*inch,8.95*inch,4.2*inch,8.95*inch)
    c.line(1.7*inch,8.7*inch,4.2*inch,8.7*inch)
    c.line(1.7*inch,8.45*inch,4.2*inch,8.45*inch)
    c.line(1.7*inch,8.2*inch,4.2*inch,8.2*inch)
    c.line(1.7*inch,7.95*inch,4.2*inch,7.95*inch)
    c.line(1.7*inch,7.7*inch,4.2*inch,7.7*inch)

#---Column 3---#
    c.drawString(4.3*inch,10*inch,spelllist[20])
    c.drawString(4.3*inch,9.75*inch,spelllist[21])
    c.drawString(4.3*inch,9.5*inch,spelllist[22])
    c.drawString(4.3*inch,9.25*inch,spelllist[23])
    c.drawString(4.3*inch,9*inch,spelllist[24])
    c.drawString(4.3*inch,8.75*inch,spelllist[25])
    c.drawString(4.3*inch,8.5*inch,spelllist[26])
    c.drawString(4.3*inch,8.25*inch,spelllist[27])
    c.drawString(4.3*inch,8*inch,spelllist[28])
    c.drawString(4.3*inch,7.75*inch,spelllist[29])

    c.line(4.3*inch,9.95*inch,6.8*inch,9.95*inch)
    c.line(4.3*inch,9.7*inch,6.8*inch,9.7*inch)
    c.line(4.3*inch,9.45*inch,6.8*inch,9.45*inch)
    c.line(4.3*inch,9.2*inch,6.8*inch,9.2*inch)
    c.line(4.3*inch,8.95*inch,6.8*inch,8.95*inch)
    c.line(4.3*inch,8.7*inch,6.8*inch,8.7*inch)
    c.line(4.3*inch,8.45*inch,6.8*inch,8.45*inch)
    c.line(4.3*inch,8.2*inch,6.8*inch,8.2*inch)
    c.line(4.3*inch,7.95*inch,6.8*inch,7.95*inch)
    c.line(4.3*inch,7.7*inch,6.8*inch,7.7*inch)


#--------------------------#
# Rules and Fluff Function #
#--------------------------#

    xpos=0
    inc=0
    specialweapons=['Awl Pike','Bariche','Bec De Corbin','Bill','Bola','Caltrop','Fauchard','Glaive','Lasso','Long Spear','Spear','Main-Gauche','Mancatcher','Military Fork','Net','Parrying Dagger','Partisian','Ranseur','Sap','Scimitar','Scourge','Spear','Spetum','Staff Sling','Stiletto','Volgue','Whip']

#   listformat=[subfolder,filelocation1,filelocation2,filelocationX...  

    c.drawString(2.5*inch,(7.4-(xpos*.15))*inch,"~~~~~Quick Reference~~~~~")
    xpos+=2

    ruleslist=['rules','fulldef','running','dualwielding']
    i=0
    while i<len(specialweapons):
        if specialweapons[i] in proficiencies:
            specialweapons[i]=specialweapons[i].lower()
            specialweapons[i]=specialweapons[i].replace(" ", "")
            ruleslist.append(specialweapons[i])
        if (specialweapons[i]+' Specialist') in proficiencies:
            specialweapons[i]=specialweapons[i].lower()
            specialweapons[i]=specialweapons[i].replace(" ", "")
            ruleslist.append(specialweapons[i])
        i+=1

    xpos=fluffy(ruleslist,xpos,c)

    c.drawString(2.5*inch,(7.4-(xpos*.15))*inch,"~~~~~Fluff~~~~~")
    xpos+=2
    flufflist=[header[2],header[2],header[5]]
    xpos=fluffy(flufflist,xpos,c)


#    i=0
#    while i<len(flufflist):
#        inc=0
#        file = "/generators/adnd/charactersheet/resources/{}".format(header[2].lower())+"/{}.txt".format(flufflist[i].lower())
#        path=os.getcwd()+file
#        fp=open(path,'r+');
#        with open(path,"r") as text_file:
#            lines=text_file.readlines()
#            text_file.close()
#            while len(lines)>inc:
#                lines[0+inc]=lines[0+inc].rstrip("\n")
#                inc+=1
#
#        inc=0
#
#        while len(lines)>inc:
#            c.drawString(-.8*inch,(7.4-(xpos*.15))*inch,lines[0+inc])
#            inc+=1
#            xpos+=1
#
#        c.rect(-.9*inch,(7.4-(xpos*.15))*inch,8*inch,((inc+1)*.15)*inch)
#        i +=1
#        xpos+=2










    c.save() #finalizes the document
    return 0

#----------------------#
# Additional Functions #
#----------------------#

def RateofFire(playerclass,name,RoF):

    if playerclass!= "Fighter":   #Re-define RoF
        if RoF=="M":
            RoF='1'
        elif RoF=="Thrown":      
            RoF='1'
    else:
        if RoF=="M":
            RoF='3/2'
        elif name=="Light Crossbow":
            RoF='1'
        elif name=="Heavy Crossbow":      
            RoF='1/2'
        elif name=="Dart":
            RoF='4'
        elif RoF=="Thrown" or name=="Blowgun" or name=="Staff Sling":
            RoF='3/2'
    return RoF

def THAC0(missile,melee,spec,based):
    THAC0Value=20


    if based=="Str":
        if melee.find("-")!=-1:
            melee=melee.lstrip('-')
            THAC0Value=THAC0Value+int(melee)
        if melee.find("+")!=-1:
            melee=melee.lstrip('+')
            THAC0Value=THAC0Value-int(melee)
    if based=='Dex':
        if missile.find("-")!=-1:
            missile=missile.lstrip('-')
            THAC0Value=THAC0Value+int(missile)
        if missile.find("+")!=-1:
            missile=missile.lstrip('+')
            THAC0Value=THAC0Value-int(missile)
    if spec.find("Specialist") != -1:
        THAC0Value=THAC0Value-1
    return str(THAC0Value)

def DamageAdj(based,stronk,spec):
    damage=0

    if based=="Str":
        if stronk.find("-")!=-1:
            stronk=stronk.lstrip('-')
            damage=damage-int(stronk)
        if stronk.find("+")!=-1:
            stronk=stronk.lstrip('+')
            damage=damage+int(stronk)
    if spec.find("Specialist") != -1:
        damage=damage+2
    return str(damage)

def fluffy(location,xpos,c):

    c.setFont("Helvetica",9)
    i=1
    reset=0
    while i<len(location):
        inc=0
        file = "/generators/adnd/charactersheet/resources/{}".format(location[0].lower())+"/{}.txt".format(location[i].lower())
        path=os.getcwd()+file
        fp=open(path,'r+');
        with open(path,"r") as text_file:
            lines=text_file.readlines()
            text_file.close()
            while len(lines)>inc:
                lines[0+inc]=lines[0+inc].rstrip("\n")
                inc+=1

        inc=0

        while len(lines)>inc:
            c.drawString(-.8*inch,(7.4-(xpos*.15))*inch,lines[inc])
            inc+=1
            xpos+=1
            if (7.4-(xpos*.15))<=0:
                c.drawString(2*inch,(7.4-(xpos*.15))*inch,"~~~~~CONTINUED ON NEXT PAGE~~~~~")
                xpos+=1
                reset=inc
                c.rect(-.9*inch,(7.4-(xpos*.15))*inch,8*inch,((inc+2)*.15)*inch)
                c.showPage()
                c.translate(inch,inch)
                c.setFont("Helvetica",8.5)
                xpos=-18
        c.rect(-.9*inch,(7.4-(xpos*.15))*inch,8*inch,((inc+1-reset)*.15)*inch)
        reset=0
        i +=1
        xpos+=2
        if (7.4-(xpos*.15))<=0:
            c.showPage()
            c.translate(inch,inch)
            c.setFont("Helvetica",9)
    c.setFont("Helvetica",10)
    return xpos
