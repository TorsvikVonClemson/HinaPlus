from generators.adnd import adndhub
from generators.loot.gems import gem
from generators.loot import table


def sort(x):
    if x.startswith('%ad&d'):
        x = adndhub.sort(x)

    elif x.startswith('%gem'):
        x = x.replace('%gem', '')
        x = x.lstrip(' ')
        x = gem.roll(x)

    elif x.startswith('%loot'):
        x = x.replace('%loot', '')
        x = x.lstrip(' ')
        x = table.roll(x)

    else:
        x = 'fault'

    return x
