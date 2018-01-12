import random
import os
import sys
sys.path.insert(0,'/home/torsvik/Music/hina')


def roll(bumptime):
    print("MK2")
    check=bumptime+random.ranint(1,20)
    if check>20:
        bumptime=0
        path = "/home/torsvik/Music/hina/bump.txt"
        fp=open(path,'r+');
        with open(path,"r") as text_file:

            tracklist.extend(text_file.readlines())

            text_file.close()
        song=random.choice(tracklist)
        song=song.rstrip('\n')
    else:
        bumptime=0
        path = "/home/torsvik/Music/hina/bump.txt"
        fp=open(path,'r+');
        with open(path,"r") as text_file:

            tracklist.extend(text_file.readlines())

            text_file.close()
        song=random.choice(tracklist)
        song=song.rstrip('\n')
    track=[bumptime,song]
    return track
