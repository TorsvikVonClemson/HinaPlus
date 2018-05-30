from generators.adnd.charactersheet import main


def sort(x):
    x = x.lstrip('%ad&d ')
    if x.startswith('chargen'):
        x = main.main(x.replace("chargen ", ""))

    else:
        x = 'TODO: Pass "%ad&d" error message'

    return x
