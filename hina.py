from __future__ import unicode_literals

import discord
import asyncio
from discord.ext import commands
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

client = discord.Client()

class Music(object):
    voice=None
    player=None
    channel = client.get_channel('302280204015894549')


    async def initialize(self):
        self.voice = await client.join_voice_channel(client.get_channel('302280204015894549'))
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=ypZThNvKw0g', ytdl_options=None, use_avconv=True)
        self.player.start()

    async def rip(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=kqjVqIYpgak', ytdl_options=None,use_avconv=True)
        self.player.start()

    def stop(self):
        self.player.stop()

    async def next(self):
        if self.player.is_done():
            await Music.rip(self)

x=Music()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await x.initialize()


@client.event
async def on_message(message):

    say='fault'
    image='fault'

    if message.content.startswith('!test'):
        x.stop()
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

#-----------#
# !commands #
#-----------#

    elif message.content.startswith('!rip'):			#Test for blocks
        await x.rip()

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
        
    if say != 'fault':
        await client.send_message(message.channel, '{}'.format(say).format(message.author))
    if image != 'fault':
        await client.send_file(message.channel, '{}'.format(image))

client.run('MzAxNjM4NDg3NjMzODIxNjk3.C9Ahqw.u53J4fjNPW-ODS0XnqZvtlqjJiY')


