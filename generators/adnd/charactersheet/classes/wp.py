import random
def roll(playerclass,god):

#After rolling weapon check for validity, do this by listing the numbers of weapons allowed and comparing it to the actuall weapon rolled.

    wplist=[]
    error=0
    wpcount=5
    doublespec=["Composite Longbow","Composite Shortbow","Shortbow","Longbow"]

    if playerclass=="Fighter" or playerclass=="Ranger" or playerclass=="Paladin":
        wpcount=4
    elif playerclass=="Wizard":
        wpcount=1
    elif playerclass=="Cleric":
        wpcount=2
    elif playerclass=="Rogue" or playerclass=="Bard":
        wpcount=2
    while wpcount>0 and error<10:
        legal=True

        roll=random.randint(1,75)
        if roll==1:
            wp="Battleaxe"
        elif roll==2:
            wp="Blowgun"                                
        elif roll==3:
            wp="Composite Longbow"         
        elif roll==4:
            wp="Composite Shortbow"       
        elif roll==5:
            wp="Shortbow"       
        elif roll==6:
            wp="Longbow"         
        elif roll==7:
            wp="Bola"      
        elif roll==8:
            wp="Chain"      
        elif roll==9:
            wp="Club"      
        elif roll==10:
            wp="Hand Crossbow"                                
        elif roll==11:
            wp="Crossbow"                                 
        elif roll==12:
            wp="Heavy Crossbow"                                 
        elif roll==13:
            wp="Dagger"
        elif roll==14:
            wp="Parrying Dagger"
        elif roll==15:
            wp="Dart"                                 
        elif roll==16:
            wp="Footman's Flail" 
        elif roll==17:
            wp="Horseman's Flail"                                
        elif roll==18:
            wp="Gaff/Hook"
        elif roll==19:
            wp="Hand Axe"
        elif roll==20:
            wp="Harpoon"
        elif roll==21:
            wp="Javelin"
        elif roll==22:
            wp="Knife"
        elif roll==23:
            wp="Heavy Horse Lance"
        elif roll==24:
            wp="Jousting Lance"
        elif roll==25:
            wp="Light Horse Lance"
        elif roll==26:
            wp="Medium Horse Lance"
        elif roll==27:
            wp="Lasso"
        elif roll==28:
            wp="Main-Gauche"
        elif roll==29:
            wp="Mancatcher"
        elif roll==30:
            wp="Morning Star"
        elif roll==31:
            wp="Net"
        elif roll==32:
            wp="Awl Pike"
        elif roll==33:
            wp="Bariche"
        elif roll==34:
            wp="Bec De Corbin"
        elif roll==35:
            wp="Bill"
        elif roll==36:
            wp="Fauchard"
        elif roll==36:
            wp="Glaive"
        elif roll==37:
            wp="Guisarme"
        elif roll==38:
            wp="Halberd"
        elif roll==39:
            wp="Military Fork"
        elif roll==40:
            wp="Partisian"
        elif roll==41:
            wp="Ranseur"
        elif roll==42:
            wp="Spetum"
        elif roll==43:
            wp="Volgue"
        elif roll==44:
            wp="Quarterstaff"    
        elif roll==45:
            wp="Sap"
        elif roll==46:
            wp="Scourge"
        elif roll==47:
            wp="Sickle"
        elif roll==48:
            wp="Sling"
        elif roll==49:
            wp="Spear"
        elif roll==50:
            wp="Long Spear"    
        elif roll==51:
            wp="Staff Sling"
        elif roll==52:
            wp="Stiletto"
        elif roll==53:
            wp="Bastard Sword"
        elif roll==54:
            wp="Broadsword"
        elif roll==55:
            wp="Cutlass"
        elif roll==56:
            wp="Falchion"
        elif roll==57:
            wp="Long Sword"
        elif roll==58:
            wp="Rapier"
        elif roll==59:
            wp="Sabre"
        elif roll==60:
            wp="Scimitar"
        elif roll==61:
            wp="Short Sword"
        elif roll==62:
            wp="Zweihander"
        elif roll==63:
            wp="Trident"
        elif roll==64:
            wp="Warhammer"
        elif roll==65:
            wp="Whip"
        elif roll==66:
            wp="Matchlock Cavlier"
        elif roll==67:
            wp="Matchlock Musket"
        elif roll==68:
            wp="Matchlock Pistol"
        elif roll==69:
            wp="Improvised"
        elif roll==70:
            wp="Caltrop"
        elif roll==71:
            wp="Snaplock Cavlier"
        elif roll==72:
            wp="Snaplock Musket"
        elif roll==73:
            wp="Snaplock Pistol"
        elif roll==74:
            wp="Unarmed"
        elif roll==75:
            wp="Wrestling"
        else:
            legal=False

#---------------------#
# Weapon Restrictions #
#---------------------#

        if playerclass=="Wizard" and (roll==13 or roll==15 or roll==22 or roll==44 or roll==48):
            legal=True

        elif (playerclass=="Rogue" or playerclass=="Bard") and (roll==2 or roll==5 or roll==7 or roll==8 or roll==9 or roll==10 or roll==11 or roll==13 or roll==13 or roll==14 or roll==15 or roll==19 or roll==22 or roll==27 or roll==28 or roll==29 or roll==31 or roll==44 or roll==45 or roll==46 or roll==47 or roll==48 or roll==51 or roll==52 or roll==55 or roll==56 or roll==58 or roll==59 or roll==60 or roll==61 or roll==65 or roll==68 or roll==68):
            legal=True

        elif (playerclass=="Fighter" or playerclass=="Ranger"):
            legal=True

        elif (playerclass=="Cleric" or playerclass=="Paladin"):


#--------------------#
# Diety Restrictions #
#--------------------#


            if god=="Ilmura" and (roll==47 or roll==48 or roll==16 or roll==35 or roll==36 or roll==37 or roll==38 or roll==63 or roll==11 or roll==69):
                legal=True

            elif god=="Makabel" and (roll==53 or roll==62 or roll==54 or roll==57):
                legal=True

            elif god=="Leuchtag" and (roll==51 or roll==44):
                legal=True
    
            elif god=="Strafeherr" and (roll==1 or roll==8 or roll==29 or roll==31 or roll==42 or roll==46 or roll==65):
                legal=True

            elif god=="Tyr" and (roll==3 or roll==4 or roll==14 or roll==17 or roll==23 or roll==24 or roll==25 or roll==26 or roll==38 or roll==50 or roll==58 or roll==64):
                legal=True

            elif god=="Bahamut" and (roll==18 or roll==20 or roll==63):
                legal=True

            elif god=="Hina" and (roll==2 or roll==15 or roll==7 or roll==70 or roll==14 or roll==22 or roll==28 or roll==45):
                legal=True

            elif god=="Reueherr" and (roll==27 or roll==9 or roll==29 or roll==31 or roll==45):
                legal=True

            elif god=="Calandra" and (roll==5 or roll==6 or roll==19):
                legal=True

            elif god=="Cisa" and (roll==21 or roll==28 or roll==40 or roll==41 or roll==45 or roll==48 or roll==55 or roll==69):
                legal=True

            elif god=="Gerdora" and (roll==12 or roll==33 or roll==67 or roll==72):
                legal=True

            elif god=="Kolsten" and (roll==9 or roll==30 or roll==45 or roll==48 or roll==68 or roll==73 or roll==74 or roll==75):
                legal=True

            else:
                legal=False
        else:
            legal=False

        if wp in wplist:
            legal=False
            error +=1

        if playerclass=="Fighter" and wp not in doublespec and legal==True:
            wp=wp+" Specialist"
            wpcount -= 2
            wplist.append(wp)
        elif playerclass=="Fighter" and wp in doublespec and legal==True:
            wp=wp+" Specialist"
            wpcount -= 3
            wplist.append(wp)
        elif legal==True:
            wplist.append(wp)
            wpcount -= 1
        else:
            legal=True
            roll=random.randint(1,75)
    return wplist
