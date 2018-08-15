def find(playerclass, level, wisdom):
    if playerclass == 'Cleric':
        if level == '1':
            spd = [1, 0, 0, 0, 0, 0, 0]
        elif level == '2':
            spd = [2, 0, 0, 0, 0, 0, 0]
        elif level == '3':
            spd = [2, 1, 0, 0, 0, 0, 0]
        elif level == '4':
            spd = [3, 2, 0, 0, 0, 0, 0]
        elif level == '5':
            spd = [3, 3, 1, 0, 0, 0, 0]
        elif level == '6':
            spd = [3, 3, 2, 0, 0, 0, 0]
        elif level == '7':
            spd = [3, 3, 2, 1, 0, 0, 0]
        elif level == '8':
            spd = [3, 3, 3, 2, 0, 0, 0]
        elif level == '9':
            spd = [4, 4, 3, 2, 1, 0, 0]
        elif level == '10':
            spd = [4, 4, 3, 3, 2, 0, 0]
        elif level == '11':
            spd = [5, 4, 4, 3, 2, 1, 0]
        elif level == '12':
            spd = [6, 5, 5, 3, 2, 2, 0]
        elif level == '13':
            spd = [6, 6, 6, 4, 2, 2, 0]
        elif level == '14':
            spd = [6, 6, 6, 5, 3, 2, 1]
        elif level == '15':
            spd = [6, 6, 6, 6, 4, 2, 1]
        elif level == '16':
            spd = [7, 7, 7, 6, 4, 3, 1]
        elif level == '17':
            spd = [7, 7, 7, 7, 5, 3, 2]
        elif level == '18':
            spd = [8, 8, 8, 8, 6, 4, 2]
        elif level == '19':
            spd = [9, 9, 8, 8, 6, 4, 2]
        elif level == '20':
            spd = [9, 9, 9, 8, 7, 5, 2]

    elif playerclass == 'Wizard':
        if level == '1':
            spd = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif level == '2':
            spd = [2, 0, 0, 0, 0, 0, 0, 0, 0]
        elif level == '3':
            spd = [2, 1, 0, 0, 0, 0, 0, 0, 0]
        elif level == '4':
            spd = [3, 2, 0, 0, 0, 0, 0, 0, 0]
        elif level == '5':
            spd = [4, 2, 1, 0, 0, 0, 0, 0, 0]
        elif level == '6':
            spd = [4, 2, 2, 0, 0, 0, 0, 0, 0]
        elif level == '7':
            spd = [4, 3, 2, 1, 0, 0, 0, 0, 0]
        elif level == '8':
            spd = [4, 3, 3, 2, 0, 0, 0, 0, 0]
        elif level == '9':
            spd = [4, 3, 3, 2, 1, 0, 0, 0, 0]
        elif level == '10':
            spd = [4, 4, 3, 2, 2, 0, 0, 0, 0]
        elif level == '11':
            spd = [4, 4, 4, 3, 3, 0, 0, 0, 0]
        elif level == '12':
            spd = [4, 4, 4, 4, 4, 1, 0, 0, 0]
        elif level == '13':
            spd = [5, 5, 5, 4, 4, 2, 0, 0, 0]
        elif level == '14':
            spd = [5, 5, 5, 4, 4, 2, 1, 0, 0]
        elif level == '15':
            spd = [5, 5, 5, 5, 5, 2, 1, 0, 0]
        elif level == '16':
            spd = [5, 5, 5, 5, 5, 3, 2, 1, 0]
        elif level == '17':
            spd = [5, 5, 5, 5, 5, 3, 3, 2, 0]
        elif level == '18':
            spd = [5, 5, 5, 5, 5, 3, 3, 2, 1]
        elif level == '19':
            spd = [5, 5, 5, 5, 5, 3, 3, 3, 2]
        elif level == '20':
            spd = [5, 5, 5, 5, 5, 4, 3, 3, 2]

    elif playerclass == 'Bard':
        if level == '1':
            spd = [0, 0, 0, 0, 0, 0]
        elif level == '2':
            spd = [1, 0, 0, 0, 0, 0]
        elif level == '3':
            spd = [2, 0, 0, 0, 0, 0]
        elif level == '4':
            spd = [2, 1, 0, 0, 0, 0]
        elif level == '5':
            spd = [3, 2, 0, 0, 0, 0]
        elif level == '6':
            spd = [3, 2, 0, 0, 0, 0]
        elif level == '7':
            spd = [3, 2, 1, 0, 0, 0]
        elif level == '8':
            spd = [3, 3, 1, 0, 0, 0]
        elif level == '9':
            spd = [3, 3, 2, 0, 0, 0]
        elif level == '10':
            spd = [3, 3, 2, 1, 0, 0]
        elif level == '11':
            spd = [3, 3, 3, 1, 0, 0]
        elif level == '12':
            spd = [3, 3, 3, 2, 0, 0]
        elif level == '13':
            spd = [3, 3, 3, 2, 1, 0]
        elif level == '14':
            spd = [3, 3, 3, 3, 1, 0]
        elif level == '15':
            spd = [3, 3, 3, 3, 2, 0]
        elif level == '16':
            spd = [4, 3, 3, 3, 2, 1]
        elif level == '17':
            spd = [4, 4, 3, 3, 3, 1]
        elif level == '18':
            spd = [4, 4, 4, 3, 3, 2]
        elif level == '19':
            spd = [4, 4, 4, 4, 3, 2]
        elif level == '20':
            spd = [4, 4, 4, 4, 4, 3]

    else:
        spd = []

    if playerclass == 'Cleric':
        if wisdom > 12:
            spd[0] += 1
        if wisdom > 13:
            spd[0] += 1
        if wisdom > 14:
            spd[1] += 1
        if wisdom > 15:
            spd[1] += 1
        if wisdom > 16:
            spd[2] += 1
        if wisdom > 12:
            spd[3] += 1

    for x in range(0, len(spd)):
        spd[x] = str(spd[x])

    return spd
