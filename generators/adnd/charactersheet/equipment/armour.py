import random
def roll(dosh,playerclass,god,weapon):

    if playerclass=='Wizard':
        buy='Unarmoured'
        AC=10
        weight=5

    elif playerclass=='Fighter' or playerclass=='Paladin' or playerclass=='Ranger':
        if dosh>=400 and dosh<500:
            dosh=dosh-400
            buy='Padded'
            AC=9
            weight=10
        elif dosh>=500 and dosh<2000:
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10
        elif dosh>=2000 and dosh<12000:
            dosh=dosh-2000
            buy='Studded Leather'
            AC=7
            weight=25
        elif dosh>=4000 and dosh<7500:
            dosh=dosh-4000
            buy='Brigadine'
            AC=6
            weight=35
        elif dosh>=7500 and dosh<20000:
            dosh=dosh-7500
            buy='Chain Mail'
            AC=5
            weight=40
        elif dosh>=20000 and dosh<60000:
            dosh=dosh-20000
            buy='Banded Mail'
            AC=4
            weight=35
        elif dosh>=60000 and dosh<200000:
            dosh=dosh-60000
            buy='Plate Mail'
            AC=3
            weight=50
        elif dosh>=200000 and dosh<400000:
            dosh=dosh-200000
            buy='Field Plate'
            AC=2
            weight=60
        elif dosh>=400000:
            dosh=dosh-400000
            buy='Full Plate'
            AC=1
            weight=70
        else:
            buy='Unarmoured'
            AC=10
            weight=5

    elif playerclass=='Rogue' or playerclass=='Bard':
        if dosh>=400 and dosh<500:
            dosh=dosh-400
            buy='Padded'
            AC=9
            weight=10
        elif dosh>=500 and dosh<2000:
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10
        elif dosh>=2000 and dosh<12000:
            dosh=dosh-2000
            buy='Studded Leather'
            AC=7
            weight=25
        elif dosh>=4000 and dosh<7500:
            dosh=dosh-4000
            buy='Brigadine'
            AC=6
            weight=35
        elif dosh>=7500 and dosh<20000:
            dosh=dosh-7500
            buy='Chain Mail'
            AC=5
            weight=40
        else:
            buy='Unarmoured'
            AC=10
            weight=5

    elif playerclass=='Cleric':
        if god=="Ilmura":
            dosh=dosh-4000
            buy='Brigadine'
            AC=6
            weight=35

        elif god=="Makabel":
            dosh=dosh-60000
            buy='Plate Mail'
            AC=3
            weight=50

        elif god=="Leuchtag":
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10
    
        elif god=="Strafeherr":
            dosh=dosh-2000
            buy='Spiked Leather'
            AC=7
            weight=25

        elif god=="Tyr":
            dosh=dosh-400000
            buy='Full Plate'
            AC=1
            weight=70

        elif god=="Bahamut":
            dosh=dosh-12000
            buy='Scale'
            AC=6
            weight=40

        elif god=="Hina" and playerclass=='Cleric':
            dosh=dosh-400
            buy='Padded'
            AC=9
            weight=10

        elif god=="Hina" and playerclass=='Paladin':
            dosh=dosh-60000
            buy='Plate Mail'
            AC=3
            weight=50

        elif god=="Reueherr":
            dosh=dosh-7500
            buy='Chain Mail'
            AC=5
            weight=40

        elif god=="Calandra":
            dosh=dosh-1500
            buy='Hide'
            AC=6
            weight=30

        elif god=="Cisa":
            dosh=dosh-12000
            buy='Coin Mail'
            AC=6
            weight=40

        elif god=="Gerdora":
            dosh=dosh-12000
            buy='Cuirass'
            AC=6
            weight=40

        elif god=="Kolsten":
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10



#---Shields---#

    dmgcheck=[weapon[5],weapon[14],weapon[23],weapon[32],weapon[41]] #lists the dmg output for all purchased weapons
    weponname=[weapon[1],weapon[10],weapon[19],weapon[28],weapon[37]]
    largelist=['Chain','Lasso','Mancatcher','Awl Pike','Bardiche',"Bec De Corbin","Bill","Fauchard","Glaive","Guisarme","Halberd","Military Fork","Partisian","Ranseur","Spetum","Volgue","Quarterstaff","Zweihander"]
    i=0
    halfhand=False
    while i<5:
        if dmgcheck[i].find(':')!=-1:
            halfhand=True
            i=5
        i+=1
    i=0
    puredmg=[]
    while i<5:
        add=0
        sub=0
        meddmg=dmgcheck[i].split('/')
        if meddmg[0].find('+')!=-1:
            splitter=meddmg[0].split('+')
            meddmg[0]=splitter[0]
            add=splitter[1]
        elif meddmg[0].find('-')!=-1:
            splitter=meddmg[0].split('-')
            meddmg[0]=splitter[0]
            sub=splitter[1]

        if dmgcheck[i]=='' or dmgcheck[i]=='Ammunition' or (weponname[i] in largelist):
            puredmg.append(0)
        else:    
            maxmin=meddmg[0].split('D')
            puredmg.append(int(maxmin[0])*int(maxmin[1])+int(add)-int(sub))
        i+=1
    
    sortedpuredmg=sorted(puredmg,reverse=True)

    if playerclass=='Wizard':
        shield=''
    elif halfhand==True:
        shield='Body Shield'
        AC=AC-1
    elif sortedpuredmg[0]==0:
        shield=''
    elif sortedpuredmg[0]<=5:
        shield='Buckler'
        AC=AC-1
    elif sortedpuredmg[0]<=8:
        shield='Small Shield'
        AC=AC-1
    elif sortedpuredmg[0]<=10:
        shield='Medium Shield'
        AC=AC-1
    elif sortedpuredmg[0]>10:
        shield='Body Shield'
        AC=AC-1 
    else:
        shield=''    
    

        
    
    stats=[dosh,buy,AC,shield,weight]

    return stats





