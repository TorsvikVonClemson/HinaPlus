from generators.loot.gems import gem

import random
import os


def roll(x):
    result = []
    intval = [0, 0, 0, 0, 0, 0]
    letters = x.split(',')
    type = ["Iron: ", "Copper: ", "Silver: ", "Gold: ", "Gems: ", "Art Objects:", "Magical Items: "]

    for i in range(0, len(letters)):
        gemcount = 0
        file = "/generators/loot/table/" + letters[i] + ".txt"
        path = os.getcwd() + file
        with open(path, "r") as text_file:
            list = text_file.readlines()
            text_file.close()

        for i in range(0, 6):
            stats = list[i].split(':')
            if int(stats[2]) > random.randint(1, 100):
                number = random.randint(int(stats[0]), int(stats[1]))
                intval[i] += number
                if i == 4:
                    gemcount += number

    for i in range(0, 6):
        result.append(type[i] + str(intval[i]))

    if gemcount != 0:
        gemlist = gem.roll(gemcount)
        result.append('\n')
        result.append(gemlist[1])

    file = "/generators/loot/results.txt"

    list = '\n'.join(result)
    path = os.getcwd() + file

    with open(path, "w") as text_file:
        text_file.writelines(list)
    text_file.close()

    return [path, 'Loot results here:']
