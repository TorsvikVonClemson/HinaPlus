from generators.adnd.charactersheet import main
from generators.adnd.charactersheet import update


def sort(x):
    x = x.lstrip('%ad&d ')
    if x.startswith('chargen'):
        x = main.main(x.replace("chargen ", ""))
    elif x.startswith('update charsheet'):
        x = update.main(x.replace("update charsheet ", ""))

    else:
        x = 'TODO: Pass "%ad&d" error message'

    return x
