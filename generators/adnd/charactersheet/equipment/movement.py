def roll(race,maxpress):
    maxpress=int(maxpress)
    if race=='Human':
        basemove=12
        lightmove=9
        modmove=6
        heavymove=3
        severemove=1

    else:
        basemove=12
        lightmove=9
        modmove=6
        heavymove=3
        severemove=1

    lightweight=int(maxpress*(2/6))
    modweight=int(maxpress*(3/6))
    heavyweight=int(maxpress*(4/6))
    severeweight=int(maxpress*(5/6))

    lightweight=str(lightweight)
    modweight=str(modweight)
    heavyweight=str(heavyweight)
    severeweight=str(severeweight)

    movement=[basemove,lightmove,modmove,heavymove,severemove,lightweight,modweight,heavyweight,severeweight]

    return movement
