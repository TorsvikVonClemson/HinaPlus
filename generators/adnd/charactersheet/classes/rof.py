def find(rofval, spec, level):
    if 'Melee' in rofval:
        if spec:
            if level < 7:
                rofval = rofval.replace('Melee', '3/2')
            elif 6 < level < 13:
                rofval = rofval.replace('Melee', '2')
            elif level > 12:
                rofval = rofval.replace('Melee', '5/2')
        else:
            rofval = rofval.replace('Melee', '1')
    if 'Heavy' in rofval:
        if spec:
            if level < 7:
                rofval = rofval.replace('Heavy', '1/2')
            elif 6 < level < 13:
                rofval = rofval.replace('Heavy', '1')
            elif level > 12:
                rofval = rofval.replace('Heavy', '3/2')
        else:
            rofval = rofval.replace('Heavy', '1/2')
    if 'Light' in rofval:
        if spec:
            if level < 7:
                rofval = rofval.replace('Light', '1')
            elif 6 < level < 13:
                rofval = rofval.replace('Light', '3/2')
            elif level > 12:
                rofval = rofval.replace('Light', '2')
        else:
            rofval = rofval.replace('Light', '1')
    if 'Dagger' in rofval:
        if spec:
            if level < 7:
                rofval = rofval.replace('Dagger', '3')
            elif 6 < level < 13:
                rofval = rofval.replace('Dagger', '4')
            elif level > 12:
                rofval = rofval.replace('Dagger', '5')
        else:
            rofval = rofval.replace('Dagger', '2')
    if 'Dart' in rofval:
        if spec:
            if level < 7:
                rofval = rofval.replace('Dart', '4')
            elif 6 < level < 13:
                rofval = rofval.replace('Dart', '5')
            elif level > 12:
                rofval = rofval.replace('Dart', '6')
        else:
            rofval = rofval.replace('Dart', '3')

    return rofval
