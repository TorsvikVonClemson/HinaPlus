import random

def roll(x):
    x=[]

    value=random.randint(1,100)

    if value<=25:
        n="ornamental"
        v=10

    elif value>25 and value<=50:
        n="semi precious"
        v = 50

    elif value > 50 and value <= 70:
        n = "fancy"
        v = 100

    elif value>70 and value<=90:
        n="precious"
        v = 500

    elif value>90 and value<=99:
        n="gem"
        v = 1000

    elif value==100:
        n = "jewel"
        v=5000

    mod=random.randint(1,6)

    if mod==1:
        if v==10:
            v=50

        elif v==50:
            v=100

        elif v==100:
            v=500

        elif v==500:
            v=1000

        elif v == 1000:
            v = 5000

        elif v==5000:
            v=10000

    elif mod==2:
        v=v*2

    elif mod==3:
        mult=random.randint(1,6)/10
        v=v+v*mult

    elif mod==4:
        mult=random.randint(1,4)/10
        v=v-v*mult

    elif mod==5:
        v=v/2

    elif mod==6:

        if v==10:
            v=5

        elif v==50:
            v=10

        elif v==100:
            v=50

        elif v==500:
            v=100

        elif v==1000:
            v=500

        elif v==5000:
            v=1000

    if mod==1 or mod==6:

        mod = random.randint(1, 4)

        if mod == 1:
            v = v * 2

        elif mod == 2:
            mult = random.randint(1, 6) / 10
            v = v + v * mult

        elif mod == 3:
            mult = random.randint(1, 4) / 10
            v = v - v * mult

        elif mod == 4:
            v = v / 2

    x.append("fault")
    x.append(n+' '+str(v)+' Gold')

    return x