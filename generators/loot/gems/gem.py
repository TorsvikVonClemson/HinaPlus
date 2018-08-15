import random
import os


def roll(number):
    x = []
    total = 0

    for i in range(0, int(number)):
        value = random.randint(1, 100)

        if value <= 25:
            file = "/generators/loot/gems/ornamental.txt"
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                list = text_file.readlines()
                text_file.close()
            choice = random.choice(list)
            choice = choice.rstrip('\n')
            n = choice
            v = 10

        elif value > 25 and value <= 50:
            file = "/generators/loot/gems/semiprecious.txt"
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                list = text_file.readlines()
                text_file.close()
            choice = random.choice(list)
            choice = choice.rstrip('\n')
            n = choice
            v = 50

        elif value > 50 and value <= 70:
            file = "/generators/loot/gems/fancy.txt"
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                list = text_file.readlines()
                text_file.close()
            choice = random.choice(list)
            choice = choice.rstrip('\n')
            n = choice
            v = 100

        elif value > 70 and value <= 90:
            file = "/generators/loot/gems/precious.txt"
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                list = text_file.readlines()
                text_file.close()
            choice = random.choice(list)
            choice = choice.rstrip('\n')
            n = choice
            v = 500

        elif value > 90 and value <= 99:
            file = "/generators/loot/gems/gem.txt"
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                list = text_file.readlines()
                text_file.close()
            choice = random.choice(list)
            choice = choice.rstrip('\n')
            n = choice
            v = 1000

        elif value == 100:
            file = "/generators/loot/gems/jewel.txt"
            path = os.getcwd() + file
            fp = open(path, 'r+');
            with open(path, "r") as text_file:
                list = text_file.readlines()
                text_file.close()
            choice = random.choice(list)
            choice = choice.rstrip('\n')
            n = choice
            v = 5000

        mod = random.randint(1, 6)

        if mod == 1:
            if v == 10:
                v = 50

            elif v == 50:
                v = 100

            elif v == 100:
                v = 500

            elif v == 500:
                v = 1000

            elif v == 1000:
                v = 5000

            elif v == 5000:
                v = 10000

        elif mod == 2:
            v = v * 2

        elif mod == 3:
            mult = random.randint(1, 6) / 10
            v = v + v * mult

        elif mod == 4:
            mult = random.randint(1, 4) / 10
            v = v - v * mult

        elif mod == 5:
            v = v / 2

        elif mod == 6:

            if v == 10:
                v = 5

            elif v == 50:
                v = 10

            elif v == 100:
                v = 50

            elif v == 500:
                v = 100

            elif v == 1000:
                v = 500

            elif v == 5000:
                v = 1000

        if mod == 1 or mod == 6:

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

        x.append(n + ' ' + str(v) + ' Gold')
        total += v

    x.append('\nTotal: '+str(total)+' Gold')
    result = '\n'.join(x)

    return ['fault', result]
