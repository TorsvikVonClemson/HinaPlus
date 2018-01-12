import discord
import asyncio
import os
import fnmatch
import random

client = discord.Client()

def sort(x,author):
    active=0
    x = x.lstrip('$rhunefaust')
    x = x.lstrip()

    file = "/interactables/rhunefaust/saves/{}.txt"
    path = os.getcwd() + file


    active=find(str(author) + '.txt', os.getcwd()+'/interactables/rhunefaust/saves/')

    if x.startswith('begin') and (active == 0):
        CurrentSpeed=question
        with open(path.format(author), "w") as text_file:
            text_file.write('Move Speed: {}\n'.format(0))
            text_file.write('Current Distance: 0\n')
            text_file.write('Date: 0:00\n')

        text_file.close()
        x = 'instance created with 0 values. Please manually set $speed.'

    elif x.startswith('begin') and (active == 1):
        x = 'instance in progress'

    elif x.startswith('next') and (active == 1):
        n=[]

        with open(path.format(author), "r") as text_file:
            workingfile=text_file.readlines()
        text_file.close()

        i=0
        while int(i) < 3:
            roll = random.randint(1, 6)
            n.append(roll)
            i+=1

        n.sort()

        speed=(workingfile[0].lstrip('Move Speed: '))
        displacement = int(speed.rstrip('\n'))

        timeinterval=n[2]*60

        distance=(workingfile[1].lstrip('Current Distance: '))
        distance = int(distance.rstrip('\n'))

        distance=distance+displacement*n[1]

        workingfile[1]='Current Distance: {}\n'.format(distance)

        currenttime=workingfile[2].lstrip('Date: ')
        currenttime=currenttime.rstrip('\n')
        currenttime=clock(currenttime,timeinterval)
        workingfile[2]='Date: '+currenttime+'\n'

        with open(path.format(author), "w") as text_file:
            text_file.writelines(workingfile)
        text_file.close()

        biome = "/interactables/rhunefaust/BenignForest/{}.txt"
        biomepath = os.getcwd() + biome
        roll=random.randint(1, 132)
        with open(biomepath.format(str(roll)), "r") as text_file:
            readout=text_file.readlines()
        text_file.close()

        x=''.join(workingfile)+'\n'+'Event No.: '+str(roll)+\
          '\n'+''.join(readout)

    elif x.startswith('speed') and (active == 1):
        x=x.lstrip('speed')
        x=x.replace(' ','')
        if x.isdigit():
            x='Party speed set to: '+str(x)
        else:
            x='Last time I checked you can only move at positive integers.'

    elif x.startswith('close'):
        os.remove(path.format(author))
        x='Run Deleted!'

    else:
        x = 'TODO: Pass "$rhunefaust" error message'

    return x


def find(pattern, path):
    result = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result=1
    return result

def clock(currenttime,timeinterval):
    hm=currenttime.split(':')
    hm[1]=str(int(hm[1])+int(timeinterval))
    hm[0]=str(int(hm[0])+int(int(hm[1])/60))
    hm[1]=str(int(hm[1])%60)
    return str(hm[0])+':'+str(hm[1])
