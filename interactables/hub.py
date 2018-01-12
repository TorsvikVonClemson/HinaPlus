from interactables.rhunefaust import rhune

def sort(x,author):

    if x.startswith('$rhunefaust'):
      x=rhune.sort(x,author)

    else: x='TODO: Pass "$ Interactive Event" error message'

    return x