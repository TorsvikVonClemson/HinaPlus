from generators.adnd import adndhub

def sort(x):

    if x.startswith('%ad&d'):
      x=adndhub.sort(x)

    else: x='fault'

    return x
