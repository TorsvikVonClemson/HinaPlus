import random
def roll(race,gender):
    i=0
    if race=="Human":
        if gender=="Male":
            weight=140
        if gender=="Female":
            weight=100
        while i!=6:
            weight=weight+random.randint(1,10)
            i +=1


    truweight=str(weight)
    return truweight
