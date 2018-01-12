from . import sorted
from . import emoji
from . import ping
from . import loveme
from . import D20
from . import help
from . import image

def sort(x):

    if x.startswith('!sort'):
      x=sorted.say('fault')

    elif x.startswith('!emoji'):
      x=emoji.say('fault')

    elif x.startswith('!ping'):
      x=ping.say('fault')

    elif x.startswith('!loveme'):
      x=loveme.say('fault')

    elif x.startswith('!help'):
      x=help.say('fault')

    elif x.startswith('!image'):
      x='fault'

    elif x.startswith('!') and ((x.find('D') != -1) or (x.find('K') != -1)):
      x=D20.say(x)

    else:
        x="Sorry, I didn't get that. Either I don't know that command or you misspelled it. " \
          "All commands except for the die rollers use no capitalization. " \
          "Toss up !help for a list of all the things I have been taught how to do!"\
          + '<:Minorochi:248774105342410753>'\
          + '<:Minorochi:248774105342410753>'\
          + '<:Minorochi:248774105342410753>'

    return x

def imgsort(x):

    if x.startswith('!help'):
      x=help.show('fault')
    elif x.startswith('!image'):
      x=image.show('fault')
    else:
      x='fault'
    return x
