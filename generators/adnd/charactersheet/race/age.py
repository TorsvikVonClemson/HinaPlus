import random
def roll(race):
    i=0
    if race=="Human":
        age=18
        while i!=1:
            age=age+random.randint(1,4)
            if (age%4)!=0:
                i +=1
    return (age-1)
