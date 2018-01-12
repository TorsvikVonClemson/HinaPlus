from collections import deque

def roll(Dosh,wp):
    wplist=deque(wp)
    weapons=[]
    weapons.append(Dosh)    #sets Dosh as the 0 value

    while len(wplist)>0:
        if wplist[0].find("Specialist")!=-1:
            wplist[0]=wplist[0].replace(" Specialist",'')
        weapons.append(wplist[0])
        if wplist[0]=="Battleaxe" and Dosh>500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D8"
            Range="Melee"
            Type="S"
            SpeeD="7"
            Weight="7"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Blowgun" and Dosh>500:
            RoF="2"
            atkaDj="Dex"
            DmgaDj='0'
            Damage="Ammunition"
            Range="10/20/30"
            Type="N/A"
            SpeeD="5"
            Weight="2"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Composite Longbow" and Dosh>10000:
            RoF="2"
            atkaDj="Dex"
            DmgaDj="Str"
            Damage="Ammunition"
            Range="Ammunition"
            Type="N/A"
            SpeeD="6"
            Weight="3"
            Dosh=Dosh-10000
            wplist.popleft()
        elif wplist[0]=="Composite Shortbow" and Dosh>7500:
            RoF="2"
            atkaDj="Dex"
            DmgaDj="Str"
            Damage="Ammunition"
            Range="50/100/180"
            Type="N/A"
            SpeeD="7"
            Weight="2"
            Dosh=Dosh-7500
            wplist.popleft()
        elif wplist[0]=="Longbow" and Dosh>7500:
            RoF="2"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="Ammunition"
            Range="Ammunition"
            Type="N/A"
            SpeeD="8"
            Weight="3"
            Dosh=Dosh-7500
            wplist.popleft()
        elif wplist[0]=="Shortbow" and Dosh>3000:
            RoF="2"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="Ammunition"
            Range="Ammunition"
            Type="N/A"
            SpeeD="7"
            Weight="2"
            Dosh=Dosh-3000
            wplist.popleft()
        elif wplist[0]=="Bola" and Dosh>50:
            RoF="Thrown"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="1D3/1D2"
            Range="10/20/30"
            Type="N/A"
            SpeeD="8"
            Weight="2"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Caltrop" and Dosh>20:
            RoF="1"
            atkaDj="Dex"
            DmgaDj="Str"
            Damage="1/1D2"
            Range="Thrown"
            Type="P"
            SpeeD="0"
            Weight=".2"
            Dosh=Dosh-20
            wplist.popleft()
        elif wplist[0]=="Chain" and Dosh>50:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4+1/1D4"
            Range="Melee"
            Type="B/Large"
            SpeeD="5"
            Weight="3"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Club" and Dosh>0:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D3"
            Range="Melee"
            Type="B"
            SpeeD="4"
            Weight="3"
            Dosh=Dosh-0
            wplist.popleft()
        elif wplist[0]=="Hand Crossbow" and Dosh>30000:
            RoF="1"
            atkaDj="Dex"
            DmgaDj=""
            Damage="1D3/1D2"
            Range="20/40/60"
            Type="P"
            SpeeD="5"
            Weight="3"
            Dosh=Dosh-30000
            wplist.popleft()
        elif wplist[0]=="Crossbow" and Dosh>3500:
            RoF="1"
            atkaDj="Dex"
            DmgaDj="+1"
            Damage="1D4/1D4"
            Range="60/120/180"
            Type="P"
            SpeeD="7"
            Weight="7"
            Dosh=Dosh-3500
            wplist.popleft()
        elif wplist[0]=="Heavy Crossbow" and Dosh>5000:
            RoF="1/2"
            atkaDj="Dex"
            DmgaDj="+6"
            Damage="1D4+1/1D6+1"
            Range="80/160/240"
            Type="P"
            SpeeD="10"
            Weight="14"
            Dosh=Dosh-5000
            wplist.popleft()
        elif wplist[0]=="Dagger" and Dosh>200:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4/1D3"
            Range="60/120/180"
            Type="P"
            SpeeD="2"
            Weight="1"
            Dosh=Dosh-200
            wplist.popleft()
        elif wplist[0]=="Parrying Dagger" and Dosh>500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D3/1D3"
            Range="Melee"
            Type="P"
            SpeeD="2"
            Weight="1"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Dart" and Dosh>50:
            RoF="3"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="1D3/1D2"
            Range="10/20/30"
            Type="P"
            SpeeD="2"
            Weight=".5"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Footman's Flail" and Dosh>1500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6+1/1D4+1"
            Range="Melee"
            Type="B"
            SpeeD="7"
            Weight="15"
            Dosh=Dosh-1500
            wplist.popleft()
        elif wplist[0]=="Horseman's Flail" and Dosh>800:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4+1/1D4+1"
            Range="Melee"
            Type="B"
            SpeeD="6"
            Weight="5"
            Dosh=Dosh-800
            wplist.popleft()
        elif wplist[0]=="Gaff/Hook" and Dosh>200:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4/1D3"
            Range="Melee"
            Type="S"
            SpeeD="2"
            Weight="2"
            Dosh=Dosh-200
            wplist.popleft()
        elif wplist[0]=="Hand Axe" and Dosh>100:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D4"
            Range="10/20/30"
            Type="S"
            SpeeD="4"
            Weight="5"
            Dosh=Dosh-100
            wplist.popleft()
        elif wplist[0]=="Harpoon" and Dosh>2000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4+1/1D6+1:2D4/2D6"
            Range="Reach"
            Type="P/Large"
            SpeeD="7"
            Weight="6"
            Dosh=Dosh-2000
            wplist.popleft()
        elif wplist[0]=="Javelin" and Dosh>50:
            RoF="M"
            atkaDj="Str/Dex"
            DmgaDj="Str"
            Damage="1D4/1D4:1D6/1D6"
            Range="20/60/80"
            Type="P/Large"
            SpeeD="4"
            Weight="2"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Knife" and Dosh>50:
            RoF="M"
            atkaDj="Str-1"
            DmgaDj="Str-1"
            Damage="1D3/1D2"
            Range="Melee"
            Type="P/S"
            SpeeD="2"
            Weight=".5"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Heavy Horse Lance" and Dosh>1500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8+1/1D6"
            Range="Melee"
            Type="P/Large"
            SpeeD="8"
            Weight="15"
            Dosh=Dosh-1500
            wplist.popleft()
        elif wplist[0]=="Jousting Lance" and Dosh>2000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D3-1/1D2-1"
            Range="Melee"
            Type="P/Large"
            SpeeD="10"
            Weight="20"
            Dosh=Dosh-2000
            wplist.popleft()
        elif wplist[0]=="Light Horse Lance" and Dosh>500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D8"
            Range="Melee"
            Type="P/Large"
            SpeeD="6"
            Weight="5"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Medium Horse Lance" and Dosh>1000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6+1/2D6"
            Range="Melee"
            Type="P/Large"
            SpeeD="7"
            Weight="10"
            Dosh=Dosh-1000
            wplist.popleft()
        elif wplist[0]=="Lasso" and Dosh>50:
            RoF="M"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="-/-"
            Range="10/20/30"
            Type="Large"
            SpeeD="10"
            Weight="3"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Main-Gauche" and Dosh>300:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4/1D3"
            Range="Melee"
            Type="P"
            SpeeD="2"
            Weight="2"
            Dosh=Dosh-300
            wplist.popleft()
        elif wplist[0]=="Mancatcher" and Dosh>3000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="-/-"
            Range="Reach"
            Type="S/P/Large"
            SpeeD="7"
            Weight="8"
            Dosh=Dosh-3000
            wplist.popleft()
        elif wplist[0]=="Morning Star" and Dosh>1000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/1D6+1"
            Range="Melee"
            Type="P"
            SpeeD="7"
            Weight="12"
            Dosh=Dosh-1000
            wplist.popleft()
        elif wplist[0]=="Net" and Dosh>500:
            RoF="Thrown"
            atkaDj="Dex"
            DmgaDj="-"
            Damage="-/-"
            Range="10/20/30"
            Type="-"
            SpeeD="10"
            Weight="10"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Awl Pike" and Dosh>500: #Double Damage when reciving a charge
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D12"
            Range="Reach"
            Type="P/Large"
            SpeeD="13"
            Weight="12"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Bariche" and Dosh>700: #UseD as a mount for guns
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/2D6"
            Range="Reach"
            Type="S/Large"
            SpeeD="9"
            Weight="12"
            Dosh=Dosh-700
            wplist.popleft()
        elif wplist[0]=="Bec De Corbin" and Dosh>800: #poplefts armour on a calleD shot
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D6"
            Range="Reach"
            Type="P/Large"
            SpeeD="9"
            Weight="10"
            Dosh=Dosh-800
            wplist.popleft()
        elif wplist[0]=="Bill" and Dosh>700: #ImproviseD from a machette, supplies can be founD near forrestry inDustries. Dismounts riDers on successful hit.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/1D10"
            Range="Reach"
            Type="P/S/Large"
            SpeeD="10"
            Weight="15"
            Dosh=Dosh-700
            wplist.popleft()
        elif wplist[0]=="Fauchard" and Dosh>500: #ImproviseD from a sickle DesigneD to cut Down fruit. Can be useD to hook objects and enemies.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D10"
            Range="Reach"
            Type="P/S/Large"
            SpeeD="8"
            Weight="7"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Glaive" and Dosh>600: #Double Damage when charging large creatures
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/2D6"
            Range="Reach"
            Type="S/Large"
            SpeeD="8"
            Weight="8"
            Dosh=Dosh-600
            wplist.popleft()
        elif wplist[0]=="Guisarme" and Dosh>500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/2D6"
            Range="Reach"
            Type="P/Large"
            SpeeD="7"
            Weight="8"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Halberd" and Dosh>1000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D10/2D6"
            Range="Reach/Large"
            Type="S/P"
            SpeeD="9"
            Weight="15"
            Dosh=Dosh-1000
            wplist.popleft()
        elif wplist[0]=="Military Fork" and Dosh>500: #Double Damage while charging against large creatures. A moDifieD pitchfork can be useD as a piton to climb walls and lifting objects.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/2D4"
            Range="Reach"
            Type="P/Large"
            SpeeD="9"
            Weight="8"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Partisian" and Dosh>1000: #Double Damage when recieving a charge. Can break weapon on a successful parry. Has a broaD heaD great for engraving
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D6+1"
            Range="Reach"
            Type="P/Large"
            SpeeD="9"
            Weight="8"
            Dosh=Dosh-1000
            wplist.popleft()
        elif wplist[0]=="Ranseur" and Dosh>600: #Double Damage when recieving a charge. On calleD shot -4 can either Disarm or ignore armour
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/2D4"
            Range="Reach"
            Type="P/Large"
            SpeeD="7"
            Weight="8"
            Dosh=Dosh-600
            wplist.popleft()
        elif wplist[0]=="Spetum" and Dosh>500: #Double Damage when reciving a charge. BlaDes on the reverse siDe cause 1D2 after hitting on a roll of 18+ or calleD shot -2
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D6+1"
            Range="Reach"
            Type="P/Large"
            SpeeD="7"
            Weight="8"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Volgue" and Dosh>500: #Double Damage on reciving a charge. SkilleD users can improvise one from any pole and blaDe.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/2D4"
            Range="Reach"
            Type="S/Large"
            SpeeD="10"
            Weight="15"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Quarterstaff" and Dosh>0:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D6"
            Range="Melee"
            Type="B/Large"
            SpeeD="4"
            Weight="4"
            Dosh=Dosh-0
            wplist.popleft()
        elif wplist[0]=="Sap" and Dosh>100: #75% of Damage is non-lethal. -8 calleD shot for knock-out, 5% chance for every Damage Done, 10% for Coup-De-Grace. 
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D2/1D2"
            Range="Melee"
            Type="B"
            SpeeD="5"
            Weight=".1"
            Dosh=Dosh-100
            wplist.popleft()
        elif wplist[0]=="Scourge" and Dosh>100: #forces morale check on creatures on Damage
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4/1D2"
            Range="Melee"
            Type="S"
            SpeeD="5"
            Weight="2"
            Dosh=Dosh-100
            wplist.popleft()
        elif wplist[0]=="Sickle" and Dosh>60:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4+1/1D4"
            Range="Melee"
            Type="S"
            SpeeD="4"
            Weight="3"
            Dosh=Dosh-60
            wplist.popleft()
        elif wplist[0]=="Sling" and Dosh>5:
            RoF="Thrown"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="Ammunition"
            Range="Ammunition"
            Type="B"
            SpeeD="6"
            Weight=".1"
            Dosh=Dosh-5
            wplist.popleft()
        elif wplist[0]=="Spear" and Dosh>80: #If wielDeD two handeD can be set to recieve a charge for Double Damage.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D8:1D8+1/2D6"
            Range="Melee"
            Type="P/Large"
            SpeeD="6"
            Weight="5"
            Dosh=Dosh-80
            wplist.popleft()
        elif wplist[0]=="Long Spear" and Dosh>500: #If wielDeD two handeD can be set to recieve a charge for Double Damage.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D8+1:2D6/3D6"
            Range="Reach"
            Type="P/Large"
            SpeeD="8"
            Weight="8"
            Dosh=Dosh-500
            wplist.popleft()
        elif wplist[0]=="Staff Sling" and Dosh>20: #DesigneD to lob objects like grenaDes, oils and large rocks
            RoF="2/1"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="Ammunition"
            Range="0/30-60/90"
            Type="B/Large"
            SpeeD="11"
            Weight="2"
            Dosh=Dosh-20
            wplist.popleft()
        elif wplist[0]=="Stiletto" and Dosh>50: #Easily concealeD. +2 to attack against metal armoureD enemies.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D3/1D2"
            Range="Melee"
            Type="P"
            SpeeD="2"
            Weight=".5"
            Dosh=Dosh-50
            wplist.popleft()
        elif wplist[0]=="Bastard Sword" and Dosh>2500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D12:2D4/2D8"
            Range="Melee"
            Type="S/Large"
            SpeeD="6"
            Weight="10"
            Dosh=Dosh-2500
            wplist.popleft()
        elif wplist[0]=="Broadsword" and Dosh>1000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="2D4/1D6+1"
            Range="Melee"
            Type="S"
            SpeeD="5"
            Weight="4"
            Dosh=Dosh-1000
            wplist.popleft()
        elif wplist[0]=="Cutlass" and Dosh>1200:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D8"
            Range="Melee"
            Type="S"
            SpeeD="5"
            Weight="4"
            Dosh=Dosh-1200
            wplist.popleft()
        elif wplist[0]=="Falchion" and Dosh>1700:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6+1/2D4"
            Range="Melee"
            Type="S"
            SpeeD="5"
            Weight="8"
            Dosh=Dosh-1700
            wplist.popleft()
        elif wplist[0]=="Long Sword" and Dosh>1500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D12"
            Range="Melee"
            Type="S"
            SpeeD="5"
            Weight="8"
            Dosh=Dosh-1500
            wplist.popleft()
        elif wplist[0]=="Rapier" and Dosh>1500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6+1/1D8+1"
            Range="Melee"
            Type="P"
            SpeeD="4"
            Weight="4"
            Dosh=Dosh-1500
            wplist.popleft()
        elif wplist[0]=="Sabre" and Dosh>1700:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6+1/1D8+1"
            Range="Melee"
            Type="S"
            SpeeD="4"
            Weight="5"
            Dosh=Dosh-1700
            wplist.popleft()
        elif wplist[0]=="Scimitar" and Dosh>1500: #Can be useD to break inanimate objects
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D8/1D8"
            Range="Melee"
            Type="S"
            SpeeD="5"
            Weight="4"
            Dosh=Dosh-1500
            wplist.popleft()
        elif wplist[0]=="Short Sword" and Dosh>1000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6/1D8"
            Range="Melee"
            Type="S"
            SpeeD="2"
            Weight=".5"
            Dosh=Dosh-1000
            wplist.popleft()
        elif wplist[0]=="Zweihander" and Dosh>5000:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D10/3D6"
            Range="Melee"
            Type="S/Large"
            SpeeD="10"
            Weight="15"
            Dosh=Dosh-5000
            wplist.popleft()
        elif wplist[0]=="Trident" and Dosh>1500:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D6+1/3D4:1D8+1/3D4"
            Range="Reach"
            Type="P/Large"
            SpeeD="7"
            Weight="5"
            Dosh=Dosh-1500
            wplist.popleft()
        elif wplist[0]=="Warhammer" and Dosh>200:
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D4+1/1D4"
            Range="Melee"
            Type="B"
            SpeeD="4"
            Weight="6"
            Dosh=Dosh-200
            wplist.popleft()
        elif wplist[0]=="Whip" and Dosh>10: #CalleD shot -4 to Disarm, on any hit a limb may be entangleD.
            RoF="M"
            atkaDj="Str"
            DmgaDj="Str"
            Damage="1D2/1"
            Range="Reach"
            Type="-"
            SpeeD="8"
            Weight="2"
            Dosh=Dosh-10
            wplist.popleft()
        elif wplist[0]=="Matchlock Cavlier" and Dosh>300: #Misfire on roll of a 1. Chance for misfire increases every 3 shots until cleaneD. Explosion on 8's"
            RoF="1/2"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="1D8/1D8"
            Range="40/80/2400"
            Type="B"
            SpeeD="9"
            Weight="11"
            Dosh=Dosh-300
            wplist.popleft()
        elif wplist[0]=="Matchlock Musket" and Dosh>2000: #Misfire on roll of a 1. Chance for misfire increases every 3 shots until cleaneD. Explosion on 8's 10's and 12's"
            RoF="1/2"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="1D12/1D12"
            Range="60/120/360"
            Type="B"
            SpeeD="12"
            Weight="20"
            Dosh=Dosh-2000
            wplist.popleft()
        elif wplist[0]=="Snaplock Pistol" and Dosh>4500: #Misfire on roll of a 3 or lower. Chance for misfire increases every 3 shots until cleaneD. Explosion on 8's"
            RoF="1"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="1D8/1D8"
            Range="15/30/45"
            Type="B"
            SpeeD="6"
            Weight="3"
            Dosh=Dosh-4500
            wplist.popleft()
        elif wplist[0]=="Snaplock Musket" and Dosh>8500: #Misfire on roll of a 3 or lower. Chance for misfire increases every 3 shots until cleaneD. Explosion on 8's, 10' and 12's"
            RoF="1"
            atkaDj="Dex"
            DmgaDj="0"
            Damage="1D12/1D12"
            Range="65/130/390"
            Type="B"
            SpeeD="8"
            Weight="14"
            Dosh=Dosh-8500
            wplist.popleft()
        else:
#            weapons[len(weapons)-1]=''
#            RoF=""
#            atkaDj=""
#            DmgaDj=""
#            Damage=""
#            Range=""
#            Type=""
#            SpeeD=""
#            Weight=""
            wplist.popleft()
            
        
        
        weapons[0]=Dosh
        weapons.append(RoF)
        weapons.append(atkaDj)
        weapons.append(DmgaDj)
        weapons.append(Damage)
        weapons.append(Range)
        weapons.append(Type)
        weapons.append(SpeeD)
        weapons.append(Weight)

    while len(weapons)<46:
        weapons.append("")
    return weapons
