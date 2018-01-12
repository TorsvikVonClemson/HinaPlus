import random
def roll(dosh,playerclass,weight,enc):

    fault=0

    miscequ=[]
    miscequ.append(dosh)  #set dosh as 0 in the list


    if playerclass=="Rogue" and dosh>=3000:
        dosh=dosh-3000
        miscequ.append("Thieve's Tools")
        miscequ.append(1)
        miscequ.append(1)
    if playerclass=="Cleric":
        dosh=dosh-2500
        miscequ.append("Holy Item")
        miscequ.append(1)
        miscequ.append(.1)

    while fault<=10 and len(miscequ)<30:

#---Switch Statements---#
        additional=0
        blockandtackle=0
        grapplinghook=0
        reroll=0

        purchase=random.randint(1,50)

        if purchase==1 and ("Backpack" not in miscequ) and dosh>=200:
            dosh=dosh-200
            item="Backpack"
            qty=1
            wgt=2

        elif purchase==2 and ("Small Barrel" not in miscequ) and dosh>=200:
            dosh=dosh-200
            item="Small Barrel"
            qty=1
            wgt=30
        
        elif purchase==3 and ("Bell" not in miscequ) and dosh>=5:
            dosh=dosh-5
            item="Bell"
            qty=1
            wgt=.1

        elif purchase==4 and ("Large Wallet" not in miscequ) and dosh>=100:
            dosh=dosh-100
            item="Large Wallet"
            qty=1
            wgt=1

        elif purchase==5 and ("Small Wallet" not in miscequ) and dosh>=20:
            dosh=dosh-5
            item="Small Wallet"
            qty=1
            wgt=.5

#---If there is no rope---#
#        elif purchase==6 and ("Block and Tackle" not in miscequ) and ("Hemp Rope" not in miscequ or "Silk Rope" not in miscequ) and dosh>=500:
#            blockandtackle=1

#---If there is rope---#
#        elif purchase==6 and ("Block and Tackle" not in miscequ) and ("Hemp Rope" in miscequ or "Silk Rope" in miscequ) and dosh>=500:
#            dosh=dosh-500
#            item="Block and Tackle"
#            qty=1
#            wgt=5

#---Purchase First Heavy Chain---#
        elif purchase==7 and ("Heavy Chain" not in miscequ) and dosh>=1200:
            dosh=dosh-1200
            item="Heavy Chain"
            qty=3
            wgt=9

#---Purchase Addtional Heavy Chain---#
        elif purchase==7 and ("Heavy Chain" in miscequ) and dosh>=1200:
            dosh=dosh-1200
            pos=miscequ.index("Heavy Chain")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+3
            miscequ[pos+2]=miscequ[pos+2]+9

#---Purchase First Light Chain---#
        elif purchase==8 and ("Light Chain" not in miscequ) and dosh>=900:
            dosh=dosh-900
            item="Light Chain"
            qty=3
            wgt=3

#---Purchase Addtional Light Chain---#
        elif purchase==8 and ("Light Chain" in miscequ) and dosh>=900:
            dosh=dosh-900
            pos=miscequ.index("Light Chain")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+3
            miscequ[pos+2]=miscequ[pos+2]+3

#---Purchase First Candles---#
        elif purchase==9 and ("Candles" not in miscequ) and dosh>=1:
            dosh=dosh-1
            item="Candles"
            qty=1
            wgt=.1

#---Purchase Addtional Candles---#
        elif purchase==9 and ("Candles" in miscequ) and dosh>=1:
            dosh=dosh-1
            pos=miscequ.index("Candles")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.1

        elif purchase==10 and ("Chalk" not in miscequ) and dosh>=1:
            dosh=dosh-1
            item="Chalk"
            qty=1
            wgt=.1

        elif purchase==11 and ("Crampons" not in miscequ) and dosh>=400:
            dosh=dosh-400
            item="Crampons"
            qty=1
            wgt=2

        elif purchase==12 and ("Fishhook" not in miscequ) and dosh>=10:
            dosh=dosh-10
            item="Fishhook"
            qty=1
            wgt=.01

        elif purchase==13 and ("Fishing Net" not in miscequ) and dosh>=400:
            dosh=dosh-1
            item="Fishing Net"
            qty=1
            wgt=5

        elif purchase==14 and ("Flint and Steel" not in miscequ) and dosh>=50:
            dosh=dosh-50
            item="Flint and Steel"
            qty=1
            wgt=.1

#---Purchase First Glass Bottle---#
        elif purchase==15 and ("Glass Bottle" not in miscequ) and dosh>=1000:
            dosh=dosh-1000
            item="Glass Bottle"
            qty=1
            wgt=.1

#---Purchase Addtional Glass Bottle---#
        elif purchase==15 and ("Glass Bottle" in miscequ) and dosh>=1000:
            dosh=dosh-1000
            pos=miscequ.index("Glass Bottle")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.1

#---If there is no rope---#
#        elif purchase==16 and ("Grappling Hook" not in miscequ) and ("Hemp Rope" not in miscequ or "Silk Rope" not in miscequ) and dosh>=80:
#            grapplinghook=1

#---If there is rope---#
#        elif purchase==16 and ("Grappling Hook" not in miscequ) and ("Hemp Rope" in miscequ or "Silk Rope" in miscequ) and dosh>=80:
#            dosh=dosh-80
#            item="Grappling Hook"
#            qty=1
#            wgt=4

        elif purchase==17 and ("Holy Item" not in miscequ) and dosh>=2500:
            dosh=dosh-2500
            item="Holy Item"
            qty=1
            wgt=.1

        elif purchase==18 and ("Hourglass" not in miscequ) and dosh>=2500:
            dosh=dosh-2500
            item="Hourglass"
            qty=1
            wgt=1

        elif purchase==19 and ("Iron Pot" not in miscequ) and dosh>=50:
            dosh=dosh-50
            item="Iron Pot"
            qty=1
            wgt=2

        elif purchase==20 and ("Ladder" not in miscequ) and dosh>=5:
            dosh=dosh-5
            item="Ladder"
            qty=10
            wgt=20

        elif purchase==21 and ("Hooded Lantern" not in miscequ) and dosh>=700:
            dosh=dosh-700
            item="Hooded Lantern"
            qty=1
            wgt=2

        elif purchase==22 and ("Bullseye Lantern" not in miscequ) and dosh>=1200:
            dosh=dosh-1200
            item="Bullseye Lantern"
            qty=1
            wgt=3

#---Purchase First Good Lock---#
        elif purchase==23 and ("Good Lock" not in miscequ) and dosh>=10000:
            dosh=dosh-10000
            item="Good Lock"
            qty=1
            wgt=1

#---Purchase Addtional Good Lock---#
        elif purchase==23 and ("Good Lock" in miscequ) and dosh>=10000:
            dosh=dosh-10000
            pos=miscequ.index("Good Lock")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

#---Purchase First Poor Lock---#
        elif purchase==24 and ("Poor Lock" not in miscequ) and dosh>=2000:
            dosh=dosh-2000
            item="Poor Lock"
            qty=1
            wgt=1

#---Purchase Addtional Poor Lock---#
        elif purchase==24 and ("Poor Lock" in miscequ) and dosh>=2000:
            dosh=dosh-2000
            pos=miscequ.index("Poor Lock")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

        elif purchase==25 and ("Magnifying Glass" not in miscequ) and dosh>=10000:
            dosh=dosh-10000
            item="Magnifying Glass"
            qty=1
            wgt=.1

        elif purchase==26 and ("Bronze Mirror" not in miscequ) and dosh>=1000:
            dosh=dosh-1000
            item="Bronze Mirror"
            qty=1
            wgt=.1

#---Purchase First Greek Fire---#
        elif purchase==27 and ("Greek Fire" not in miscequ) and dosh>=1000:
            dosh=dosh-1000
            item="Greek Fire"
            qty=1
            wgt=2

#---Purchase Addtional Greek Fire---#
        elif purchase==27 and ("Greek Fire" in miscequ) and dosh>=1000:
            dosh=dosh-1000
            pos=miscequ.index("Greek Fire")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+2

#---Purchase First Lantern Oil---#
        elif purchase==28 and ("Lantern Oil" not in miscequ) and dosh>=6:
            dosh=dosh-6
            item="Lantern Oil"
            qty=1
            wgt=1

#---Purchase Addtional Lantern Oil---#
        elif purchase==28 and ("Lantern Oil" in miscequ) and dosh>=6:
            dosh=dosh-6
            pos=miscequ.index("Lantern Oil")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

#---Purchase First Paper---#
        elif purchase==29 and ("Paper" not in miscequ) and dosh>=200:
            dosh=dosh-200
            item="Paper"
            qty=1
            wgt=.01

#---Purchase Addtional Paper---#
        elif purchase==29 and ("Paper" in miscequ) and dosh>=200:
            dosh=dosh-200
            pos=miscequ.index("Paper")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.01

#---Purchase First Papyrus---#
        elif purchase==30 and ("Papyrus" not in miscequ) and dosh>=80:
            dosh=dosh-80
            item="Papyrus"
            qty=1
            wgt=1

#---Purchase Addtional Papyrus---#
        elif purchase==30 and ("Papyrus" in miscequ) and dosh>=80:
            dosh=dosh-80
            pos=miscequ.index("Papyrus")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.01

#---Purchase First Parchment---#
        elif purchase==31 and ("Parchment" not in miscequ) and dosh>=100:
            dosh=dosh-100
            item="Parchment"
            qty=1
            wgt=.01

#---Purchase Addtional Parchment---#
        elif purchase==31 and ("Parchment" in miscequ) and dosh>=100:
            dosh=dosh-100
            pos=miscequ.index("Parchment")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.01

#---Purchase First Perfume---#
        elif purchase==32 and ("Perfume" not in miscequ) and dosh>=500:
            dosh=dosh-500
            item="Perfume"
            qty=1
            wgt=.1

#---Purchase Addtional Perfume---#
        elif purchase==32 and ("Perfume" in miscequ) and dosh>=500:
            dosh=dosh-500
            pos=miscequ.index("Perfume")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.1

#---Purchase First Piton---#
        elif purchase==33 and ("Piton" not in miscequ) and dosh>=12:
            dosh=dosh-12
            item="Piton"
            qty=3
            wgt=1.5

#---Purchase Addtional Piton---#
        elif purchase==33 and ("Piton" in miscequ) and dosh>=12:
            dosh=dosh-12
            pos=miscequ.index("Piton")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+3
            miscequ[pos+2]=miscequ[pos+2]+1.5

#---Purchase First Hemp Rope---#
        elif purchase==34 and ("Hemp Rope" not in miscequ) and dosh>=100:
            dosh=dosh-100
            item="Hemp Rope"
            qty=50
            wgt=20

#---Purchase Addtional Hemp Rope---#
        elif purchase==34 and ("Hemp Rope" in miscequ) and dosh>=100:
            dosh=dosh-100
            pos=miscequ.index("Hemp Rope")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+50
            miscequ[pos+2]=miscequ[pos+2]+20

#---Purchase First Silk Rope---#
        elif purchase==35 and ("Silk Rope" not in miscequ) and dosh>=1000:
            dosh=dosh-1000
            item="Silk Rope"
            qty=50
            wgt=8

#---Purchase Addtional Silk Rope---#
        elif purchase==35 and ("Silk Rope" in miscequ) and dosh>=1000:
            dosh=dosh-1000
            pos=miscequ.index("Silk Rope")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+50
            miscequ[pos+2]=miscequ[pos+2]+8

#---Purchase First Large Sack---#
        elif purchase==36 and ("Large Sack" not in miscequ) and dosh>=20:
            dosh=dosh-20
            item="Large Sack"
            qty=1
            wgt=.5

#---Purchase Addtional Large Sack---#
        elif purchase==36 and ("Large Sack" in miscequ) and dosh>=20:
            dosh=dosh-20
            pos=miscequ.index("Large Sack")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.5

#---Purchase First Small Sack---#
        elif purchase==37 and ("Small Sack" not in miscequ) and dosh>=5:
            dosh=dosh-5
            item="Small Sack"
            qty=1
            wgt=.1

#---Purchase Addtional Small Sack---#
        elif purchase==37 and ("Small Sack" in miscequ) and dosh>=5:
            dosh=dosh-5
            pos=miscequ.index("Small Sack")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.1

#---Purchase First Wax---#
        elif purchase==38 and ("Wax" not in miscequ) and dosh>=100:
            dosh=dosh-100
            item="Wax"
            qty=1
            wgt=1

#---Purchase Addtional Wax---#
        elif purchase==38 and ("Wax" in miscequ) and dosh>=100:
            dosh=dosh-100
            pos=miscequ.index("Wax")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

        elif purchase==39 and ("Sewing Needle" not in miscequ) and dosh>=50:
            dosh=dosh-50
            item="Sewing Needle"
            qty=1
            wgt=.01

        elif purchase==40 and ("Whistle" not in miscequ) and dosh>=80:
            dosh=dosh-80
            item="Whistle"
            qty=1
            wgt=.1

        elif purchase==41 and ("Signet Ring" not in miscequ) and dosh>=500:
            dosh=dosh-500
            item="Signet Ring"
            qty=1
            wgt=.1

#---Purchase First Soap---#
        elif purchase==42 and ("Soap" not in miscequ) and dosh>=50:
            dosh=dosh-50
            item="Soap"
            qty=1
            wgt=1

#---Purchase Addtional Soap---#
        elif purchase==42 and ("Soap" in miscequ) and dosh>=50:
            dosh=dosh-50
            pos=miscequ.index("Soap")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

        elif purchase==43 and ("Spyglass" not in miscequ) and dosh>=100000:
            dosh=dosh-100000
            item="Spyglass"
            qty=1
            wgt=1

        elif purchase==44 and ("Large Tent" not in miscequ) and dosh>=2500:
            dosh=dosh-2500
            item="Large Tent"
            qty=1
            wgt=20

        elif purchase==45 and ("Small Tent" not in miscequ) and dosh>=500:
            dosh=dosh-500
            item="Small Tent"
            qty=1
            wgt=10

        elif purchase==46 and ("Pavilion" not in miscequ) and dosh>=10000:
            dosh=dosh-10000
            item="Pavilion"
            qty=1
            wgt=50

#---Purchase First Torch---#
        elif purchase==47 and ("Torch" not in miscequ) and dosh>=1:
            dosh=dosh-1
            item="Torch"
            qty=1
            wgt=1

#---Purchase Addtional Torch---#
        elif purchase==47 and ("Torch" in miscequ) and dosh>=1:
            dosh=dosh-1
            pos=miscequ.index("Torch")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

#---Purchase First Wineskin---#
        elif purchase==48 and ("Wineskin" not in miscequ) and dosh>=80:
            dosh=dosh-80
            item="Wineskin"
            qty=1
            wgt=1

#---Purchase Addtional Wineskin---#
        elif purchase==48 and ("Wineskin" in miscequ) and dosh>=80:
            dosh=dosh-80
            pos=miscequ.index("Wineskin")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+1

        elif purchase==49 and ("Winter Blanket" not in miscequ) and dosh>=50:
            dosh=dosh-50
            item="Winter Blanket"
            qty=1
            wgt=3

#---Purchase First Ink---#
        elif purchase==50 and ("Ink" not in miscequ) and dosh>=800:
            dosh=dosh-800
            item="Ink"
            qty=1
            wgt=.1

#---Purchase Addtional Ink---#
        elif purchase==50 and ("Ink" in miscequ) and dosh>=800:
            dosh=dosh-800
            pos=miscequ.index("Ink")
            additional=1
            miscequ[pos+1]=miscequ[pos+1]+1
            miscequ[pos+2]=miscequ[pos+2]+.1

        else:
            fault=fault+1
            reroll=1

#---Block and Tackle Code---#
        if blockandtackle==1 and dosh>=600:
            dosh=dosh-600
            miscequ.append("Block and Tackle")
            miscequ.append(1)
            miscequ.append(5)
            miscequ.append("Hemp Rope")
            miscequ.append(50)
            miscequ.append(20)
            blockandtackle=0
            reroll=1


#---Grappling Hook Code---#
        if grapplinghook==1 and dosh>=180:
            dosh=dosh-180
            miscequ.append("Grappling Hook")
            miscequ.append(1)
            miscequ.append(4)
            miscequ.append("Hemp Rope")
            miscequ.append(50)
            miscequ.append(20)
            reroll=1
            grapplinghook=0

#---Append---#

        if additional!=1 and reroll!=1 and float(enc)>=float(weight)+float(wgt):
            miscequ.append(item)
            miscequ.append(qty)
            miscequ.append(wgt)
            weight=float(weight)+float(wgt)
        else:
           addtional=0
           reroll=0


        miscequ[0]=dosh

    while len(miscequ)<31:
        miscequ.append("")

    if playerclass==("Cleric" or "Paladin"):
        miscequ[0]=0

    return miscequ











