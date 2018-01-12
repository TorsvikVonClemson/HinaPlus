import random

def roll(dex,occ):
    PickPockets=15
    OpenLocks=10
    FindRemoveTraps=5
    MoveSilently=10
    HideInShadows=5
    DetectNoise=15
    ClimbWalls=60
    ReadLanguages=0

    if dex==9:
        PickPockets=PickPockets-15
        OpenLocks=OpenLocks-10
        FindRemoveTraps=FindRemoveTraps-10
        MoveSilently=MoveSilently-20
        HideInShadows=HideInShadows-10
    elif dex==10:
        PickPockets=PickPockets-10
        OpenLocks=OpenLocks-5
        FindRemoveTraps=FindRemoveTraps-10
        MoveSilently=MoveSilently-15
        HideInShadows=HideInShadows-5
    elif dex==11:
        PickPockets=PickPockets-5
        FindRemoveTraps=FindRemoveTraps-5
        MoveSilently=MoveSilently-10
    elif dex==12:
        MoveSilently=MoveSilently-5
    elif dex==16:
        OpenLocks=OpenLocks+5
    elif dex==17:
        PickPockets=PickPockets+5
        OpenLocks=OpenLocks+10
        MoveSilently=MoveSilently+5
        HideInShadows=HideInShadows+5
    elif dex==18:
        PickPockets=PickPockets+10
        OpenLocks=OpenLocks+15
        FindRemoveTraps=FindRemoveTraps+5
        MoveSilently=MoveSilently+10
        HideInShadows=HideInShadows+10
    elif dex==19:
        PickPockets=PickPockets+15
        OpenLocks=OpenLocks+20
        FindRemoveTraps=FindRemoveTraps+10
        MoveSilently=MoveSilently+15
        HideInShadows=HideInShadows+15

    if occ=='Street Urchin':
        PickPockets+=20
        OpenLocks+=20
    elif occ=='Pick Pocket':
        PickPockets+=20
        MoveSilently+=20
    elif occ=='Beggar':
        PickPockets+=20
        DetectNoise+=20
    elif occ=='Infiltrator':
        OpenLocks+=20
        ClimbWalls+=20
    elif occ=='Thug':
        OpenLocks+=20
        HideInShadows+=20
    elif occ=='Bandit':
        OpenLocks+=20
        MoveSilently+=20
    elif occ=='Lock Smith':
        OpenLocks+=20
        FindRemoveTraps+=20
    elif occ=='Spelunker':
        FindRemoveTraps+=20
        ReadLanguages+=20
    elif occ=='Saboteur':
        OpenLocks+=20
        FindRemoveTraps+=20
    elif occ=='Assassin':
        MoveSilently+=20
        HideInShadows+=20
    elif occ=='Scout':
        MoveSilently+=20
        DetectNoise+=20
    elif occ=='Spy':
        MoveSilently+=20
        ClimbWalls+=20
    elif occ=='Bounty Hunter':
        HideInShadows+=20
        DetectNoise+=20
    elif occ=='Burglar':
        HideInShadows+=20
        ClimbWalls+=20


    points=20
    while points!=0:
        skill=random.randint(1,8)
        if skill==1:
            PickPockets=PickPockets+1
            points=points-1
        elif skill==2:
            OpenLocks=OpenLocks+1
            points=points-1
        elif skill==3:
            FindRemoveTraps=FindRemoveTraps+1
            points=points-1
        elif skill==4:
            MoveSilently=MoveSilently+1
            points=points-1
        elif skill==5:
            HideInShadows=HideInShadows+1
            points=points-1
        elif skill==6:
            DetectNoise=DetectNoise+1
            points=points-1
        elif skill==7:
            ClimbWalls=ClimbWalls+1
            points=points-1
        elif skill==8:
            ReadLanguages=ReadLanguages+1
            points=points-1

    PickPockets='Pick Pockets: '+str(PickPockets)
    OpenLocks='Open Locks: '+str(OpenLocks)
    FindRemoveTraps='Find/Remove Traps: '+str(FindRemoveTraps)
    MoveSilently='Move Silently: '+str(MoveSilently)
    HideInShadows='Hide in Shadows: '+str(HideInShadows)
    DetectNoise='Detect Noise: '+str(DetectNoise)
    ClimbWalls='Climb Walls: '+str(ClimbWalls)
    ReadLanguages='Read Languages: '+str(ReadLanguages)


    thiefskills=[PickPockets,OpenLocks,FindRemoveTraps,MoveSilently,HideInShadows,DetectNoise,ClimbWalls,ReadLanguages]

    return thiefskills
