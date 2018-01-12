import random
def roll(playerclass,smarts,god):

    spelllist=[]

#-------------------------#
# 1st Level Wizard Spells #
#-------------------------#


    if playerclass=='Wizard':
        while len(spelllist)<int(smarts):

            number=random.randint(1,53)

            if number==1 and "Affect Normal Fires" not in spelllist:
                spelllist.append("Affect Normal Fires")
            elif number==2 and "Alarm" not in spelllist:
                spelllist.append("Alarm")
            elif number==3 and "Armor" not in spelllist:
                spelllist.append("Armor")
            elif number==4 and "Audible Glamour" not in spelllist:
                spelllist.append("Audible Glamour")
            elif number==5 and "Burning Hands" not in spelllist:
                spelllist.append("Burning Hands")
            elif number==6 and "Cantrip" not in spelllist:
                spelllist.append("Cantrip")
            elif number==7 and "Change Self" not in spelllist:
                spelllist.append("Change Self")
            elif number==8 and "Charm Person" not in spelllist:
                spelllist.append("Charm Person")
            elif number==9 and "Chill Touch" not in spelllist:
                spelllist.append("Chill Touch")
            elif number==10 and "Comprehend Language" not in spelllist:
                spelllist.append("Comprehend Language")
            elif number==11 and "Dancing Lights" not in spelllist:
                spelllist.append("Dancing Lights")
            elif number==12 and "Detect Magic" not in spelllist:
                spelllist.append("Detect Magic")
            elif number==13 and "Detect Undead" not in spelllist:
                spelllist.append("Detect Undead")
            elif number==14 and "Enlarge" not in spelllist:
                spelllist.append("Enlarge")
            elif number==15 and "Color Sprat" not in spelllist:
                spelllist.append("Color Spray")
            elif number==16 and "Erase" not in spelllist:
                spelllist.append("Erase")
            elif number==17 and "Feather Fall" not in spelllist:
                spelllist.append("Feather Fall")
            elif number==18 and "Find Familiar" not in spelllist:
                spelllist.append("Find Familiar")
            elif number==19 and "Friends" not in spelllist:
                spelllist.append("Friends")
            elif number==20 and "Gaze Reflection" not in spelllist:
                spelllist.append("Gaze Reflection")
            elif number==21 and "Grease" not in spelllist:
                spelllist.append("Grease")
            elif number==22 and "Hold Portal" not in spelllist:
                spelllist.append("Hold Portal")
            elif number==23 and "Hypnotism" not in spelllist:
                spelllist.append("Hypnotism")
            elif number==24 and "Identify" not in spelllist:
                spelllist.append("Identify")
            elif number==25 and "Jump" not in spelllist:
                spelllist.append("Jump")
            elif number==26 and "Light" not in spelllist:
                spelllist.append("Light")
            elif number==27 and "Magic Missile" not in spelllist:
                spelllist.append("Magic Missile")
            elif number==28 and "Mend" not in spelllist:
                spelllist.append("Mend")
            elif number==29 and "Message" not in spelllist:
                spelllist.append("Message")
            elif number==30 and "Mount" not in spelllist:
                spelllist.append("Mount")
            elif number==31 and "Nystul's Magic Aura" not in spelllist:
                spelllist.append("Nystul's Magic Aura")
            elif number==32 and "Phantasmal Force" not in spelllist:
                spelllist.append("Phantasmal Force")
            elif number==33 and "Protection from Evil" not in spelllist:
                spelllist.append("Protection from Evil")
            elif number==34 and "Read Magic" not in spelllist:
                spelllist.append("Read Magic")
            elif number==35 and "Shield" not in spelllist:
                spelllist.append("Shield")
            elif number==36 and "Shocking Grasp" not in spelllist:
                spelllist.append("Shocking Grasp")
            elif number==37 and "Sleep" not in spelllist:
                spelllist.append("Sleep")
            elif number==38 and "Spider Climb" not in spelllist:
                spelllist.append("Spider Climb")
            elif number==39 and "Spook" not in spelllist:
                spelllist.append("Spook")
            elif number==40 and "Taunt" not in spelllist:
                spelllist.append("Taunt")
            elif number==41 and "Tenser's Floating Disc" not in spelllist:
                spelllist.append("Tenser's Floating Disc")
            elif number==42 and "Unseen Servant" not in spelllist:
                spelllist.append("Unseen Servant")
            elif number==43 and "Ventriloquism" not in spelllist:
                spelllist.append("Ventriloquism")
            elif number==44 and "Wall of Fog" not in spelllist:
                spelllist.append("Wall of Fog")
            elif number==45 and "Wizard's Mark" not in spelllist:
                spelllist.append("Wizards Mark")
            elif number==46 and "Fire Burst*" not in spelllist:
                spelllist.append("Fire Burst*")
            elif number==47 and "Fist of Stone*" not in spelllist:
                spelllist.append("Fist of Stone*")
            elif number==48 and "Hornung's Guess*" not in spelllist:
                spelllist.append("Hornung's Guess*")
            elif number==49 and "Lasting Breath*" not in spelllist:
                spelllist.append("Lasting Breath*")
            elif number==50 and "Metamorphose Liquid*" not in spelllist:
                spelllist.append("Metamorphose Liquid*")
            elif number==51 and "Murdock's Feathery Flyer*" not in spelllist:
                spelllist.append("Murdock's Feathery Flyer*")
            elif number==52 and "Nahal's Reckless Dweomer*" not in spelllist:
                spelllist.append("Nahal's Reckless Dweomer*")
            elif number==53 and "Patternweave" not in spelllist:
                spelllist.append("Patternweave")

#-------------------------#
# 1st Level Cleric Spells #
#-------------------------#

    allsphere=["Bless","Combine","Detect Evil","Purify Food & Drink"]
    animal=["Animal Friendship","Invisibility to Animals","Locate Animals"]
    charm=["Command","Remove Fear"]
    water=["Create Water"]
    healing=["Cure Light Wounds"]
    divination=["Detect Magic","Detect Poison","Detect Snares and Pits","Locate Animals or Plants","Analyze Balance"]
    protection=["Endure Cold/Heat","Protection from Evil","Sanctuary","Ring of Hands"]
    plant=["Entangle","Locate Plants","Pass Without Trace","Shillelagh","Log of Everburning"]
    weather=["Faerie Fire"]
    necromantic=["Invisibility to Undead"]
    sun=["Light"]
    combat=["Magic Stone","Shillelagh"]
    numbers=["Analyze Balance","Personal Reading"]
    wards=["Anti-Vermin Barrier","Weighty Chest"]
    summoning=["Call Upon Faith"]
    war=["Courage","Morale"]
    thought=["Emotion Read","Thought Capture"]
    time=["Know Age","Know Time"]
    travelers=["Know Direction"]
    fire=["Log of Everburning"]
    chaos=["Mistaken Missive"]
    guardian=["Sacred Guardian"]
    astral=["Speak with Astral Traveler"]
    creation=[]
    law=[]

    if playerclass=='Cleric':
        if god=='Ilmura':
            spelllist=spelllist+allsphere+plant+sun+weather+divination+summoning+charm
        elif god=='Makabel':
            spelllist=spelllist+allsphere+necromantic+protection+astral+summoning+healing+combat
        elif god=='Leuchtag':
            spelllist=spelllist+allsphere+fire+sun+healing+chaos+wards+law+necromantic+summoning
        elif god=='Straffeherr':
            spelllist=spelllist+allsphere+law+charm+thought+healing+protection+combat
        elif god=='Tyr':
            spelllist=spelllist+allsphere+combat+war+travelers+healing+divination+summoning
        elif god=='Bahamut':
            spelllist=spelllist+allsphere+protection+guardian+law+charm+sun+summoning
        elif god=='Hina':
            spelllist=spelllist+allsphere+chaos+healing+necromantic+protection+wards+divination
        elif god=='Reueherr':
            spelllist=spelllist+allsphere+protection+wards+guardian+law+healing+charm
        elif god=='Calandra':
            spelllist=spelllist+allsphere+summoning+plant+animal+healing+necromantic+weather
        elif god=='Cisa':
            spelllist=spelllist+allsphere+chaos+travelers+divination+sun+combat+numbers
        elif god=='Gerdora':
            spelllist=spelllist+allsphere+wards+charm+numbers+fire+water+law+protection
        elif god=='Kolsten':
            spelllist=spelllist+allsphere+numbers+creation+time+fire+water+law+healing

    while len(spelllist)<31:
        spelllist.append("")

    return spelllist
