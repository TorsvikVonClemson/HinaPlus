import random
def roll(race,gender):
    i=0
    if race=="Human":
        if gender=="Male":
            height=60
        if gender=="Female":
            height=59
        while i!=2:
            height=height+random.randint(1,10)
            i +=1


    feet=int(height/12)
    inches=height%12
    truheight=str(feet)+"'"+str(inches)+'"'
    return truheight
