from __future__ import unicode_literals

import discord
import asyncio
import youtube_dl
import commands.testmodule
import commands.hub
import generators.hub
import generators.adnd.adndhub
import interactables.hub
import interactables.rhunefaust.rhune
import os
import random
import sys
import title
sys.path.insert(0,'/home/torsvik/Music/hina')




client = discord.Client()
musicroot=os.path.dirname(__file__)+"/../../Music/hina/"
bumptime=0

async def music():
    channel = client.get_channel('302280204015894549')
    voice = await client.join_voice_channel(channel)
    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=ypZThNvKw0g', ytdl_options=None,use_avconv=True)
    player.start()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await music()
    




@client.event
async def on_message(message):

    say='fault'
    image='fault'

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')





#-------------------------------------------------------------------------------

#---------------#
# TEST COMMANDS #
#---------------#

    elif message.content.startswith('!block'):			#Test for blocks
        await client.send_message(message.channel, '')

    elif message.content.startswith('!loveme'):
        await client.send_message(message.channel, 'no')

    elif message.content.startswith('@Hina'):			#Test for Mentions
        await client.send_message(message.channel, 'I can see @ now, but not anything after. <3')

    #elif message.content.find('!shitposting') != -1:		#Test to find text. May replace startswith
        #await client.send_file(client.get_channel('245151770534346753'), 'Moot_says_ironic_badness_is_badness_nonetheless.png')

    elif message.content.find('patriot') != -1:
        censor=str(message).replace['patriot', 'LaLiLuLeLo']
        await client.edit_message(message,censor)


#-----------#
# !commands #
#-----------#

    elif message.content.startswith('!'):
        image='fault'
        send=message.content
        say=commands.hub.sort(send)
        image=commands.hub.imgsort(send)

    elif message.content.startswith('%'):
        image='fault'
        send=message.content
        data=generators.hub.sort(send)
        say=data[1]
        image=data[0]

    elif message.content.startswith('$'):
        image = 'fault'
        name = message.content[len('$name'):].strip()
        send = message.content
        say = interactables.hub.sort(send,message.author)
        #say = data[1]
        #image = data[0]
        
    if say!='fault':
        await client.send_message(message.channel,'{}'.format(say) ) 
    if image!='fault':
        await client.send_file(message.channel,'{}'.format(image))

client.run('MzAxNjM4NDg3NjMzODIxNjk3.C9Ahqw.u53J4fjNPW-ODS0XnqZvtlqjJiY')
