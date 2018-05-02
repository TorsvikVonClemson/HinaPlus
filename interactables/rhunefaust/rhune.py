import os
import fnmatch
import random

from interactables.rhunefaust import humanoids



def sort(x,author):
    active=0
    x = x.lstrip('$rhunefaust')
    x = x.lstrip()

    file = "/interactables/rhunefaust/saves/{}.txt"
    path = os.getcwd() + file
    authpath=path.format(author)

    nextbiome='null'


    #Check for Save
    active=find(str(author) + '.txt', os.getcwd()+'/interactables/rhunefaust/saves/')

    if x.startswith('begin') and (active == 0):
        biome='Forest'
        biomeedge=False
        with open(authpath, "w") as text_file:
            text_file.write('Move Speed: {}\n'.format(0))
            text_file.write('Current Distance: 0\n')
            text_file.write('Date: 6:00\n')
            text_file.write(biome)

        text_file.close()
        x = 'instance created with 0 values. Please manually set $speed.'

    elif x.startswith('begin') and (active == 1):
        x = 'instance in progress'

    elif x.startswith('next') and (active == 1):
        n=[]

        #Read Save
        with open(authpath, "r") as text_file:
            workingfile=text_file.readlines()
        text_file.close()

        #Read Biome Params
        biomeparamsdir = "/interactables/rhunefaust/" + workingfile[3] + "/params.txt"
        biomeparamspath = os.getcwd() + biomeparamsdir

        with open(biomeparamspath, "r") as text_file:
            params = text_file.readlines()
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
        update(authpath,1,'Current Distance: {}\n'.format(distance))

        currenttime=workingfile[2].lstrip('Date: ')
        currenttime=currenttime.rstrip('\n')
        currenttime=clock(currenttime,timeinterval)
        update(authpath,2,'Date: {}\n'.format(currenttime))

        #Biome Change Check

        if distance>=100 and workingfile[3]=="Forest":
            x='The party enters a cave'
            distance=0
            update(authpath, 1, 'Current Distance: {}\n'.format(distance))
            update(authpath, 3, "Cave")

        if distance>=100 and workingfile[3]=="Cave":
            x='The party enters a kobold farm'
            distance=0
            update(authpath, 1, 'Current Distance: {}\n'.format(distance))
            update(authpath, 3, "Kobold Farm")

        if distance>=100 and workingfile[3]=="Kobold Farm":
            x='BOSS!!'+humanoids.humanoids()
            distance=0
            update(authpath, 1, 'Current Distance: {}\n'.format(distance))

        #No Change
        else:
            roll=random.randint(1, int(params[1].rstrip('\n')))
            if roll<=int(params[2].rstrip('\n')):
                encounter="Benign"
            else:
                roll = random.randint(1, int(params[3].rstrip('\n')))
                encounter="Common"

            biomedir = "/interactables/rhunefaust/"+workingfile[3]+"/"+encounter+"/{}.txt"
            biomepath = os.getcwd() + biomedir

            with open(biomepath.format(str(roll)), "r") as text_file:
                readout=text_file.readlines()
            text_file.close()

            combat=''
            if 'HUMANOID ENCOUNTER' in ''.join(readout):
                combat=humanoids.humanoids()

            x=''.join(workingfile)+'\n\n'+encounter+' Event No.: '+str(roll)+\
                '\n'+''.join(readout)+combat


    elif x.startswith('speed') and (active == 1):
        x=x.lstrip('speed')
        x=x.replace(' ','')
        if x.isdigit():
            update(authpath,0,'Move Speed: {}\n'.format(x))
            x='Party speed set to: '+str(x)
        else:
            x='Last time I checked you can only move at positive integers.'

    elif x.startswith('camp') and (active == 1):
        update(authpath, 2, 'Date: {}\n'.format(clock('6:00',0)))



    elif x.startswith('close'):
        os.remove(authpath)
        x='Run Deleted!'

    else:
        x = 'TODO: Pass "$rhunefaust" error message... Commands are begin,next, speed and close'

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

def update(authpath,line,update):
    with open(authpath, "r") as text_file:
        workingfile = text_file.readlines()
    text_file.close()
    workingfile[line]=update
    with open(authpath, "w") as text_file:
        text_file.writelines(workingfile)
    text_file.close()