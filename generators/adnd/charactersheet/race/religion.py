import random

def roll(race):

    if race=="Human":
        roll=random.randint(1,12)
        if roll==1:
            relig="Ilmura"
        elif roll==2:
            relig="Makabel"
        elif roll==3:
            relig="Leuchtag"
        elif roll==4:
            relig="Straffherr"
        elif roll==5:
            relig="Tyr"
        elif roll==6:
            relig="Bahamut"
        elif roll==7:
            relig="Hina"
        elif roll==8:
            relig="Reueherr"
        elif roll==9:
            relig="Calandra"
        elif roll==10:
            relig="Cisa"
        elif roll==11:
            relig="Gerdora"
        elif roll==12:
            relig="Kolsten"
    else:
        relig="JESUS"
    return relig
