from generators.adnd import adndhub
from generators.loot.gems import gem

def sort(x):

    if x.startswith('%ad&d'):
      x=adndhub.sort(x)

    elif x.startswith('%gem'):
        x=gem.roll(x)

    else: x='fault'


    return x
