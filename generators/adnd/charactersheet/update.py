import os
from generators.adnd.charactersheet import pdfwriter


def main(x):
    characters = os.listdir(os.getcwd() + '/generators/adnd/charactersheet/saved/trash/')
    for x in range(0, len(characters)):
        pdfwriter.write(
            os.getcwd() + '/generators/adnd/charactersheet/saved/trash/{}'.format(characters[x]) + '/{}.txt'.format(
                characters[x]))

    return ['fault', '♥ ♥ ♥ Update Complete! ♥ ♥ ♥']
