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
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=34UutDrXV2Q', ytdl_options=None, use_avconv=True)
        self.player.start()

    async def rip(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=kqjVqIYpgak', ytdl_options=None,use_avconv=True)
        self.player.volume=.05
        self.player.start()

    async def traka(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=XCiDuy4mrWU',
                                                              ytdl_options=None, use_avconv=True)
        self.player.volume = .05
        self.player.start()

    async def trakb(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://youtu.be/8kqscI_c1mY',
                                                              ytdl_options=None, use_avconv=True)
        self.player.volume = .05
        self.player.start()

    async def trakc(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://youtu.be/1wG33sjUSi8',
                                                              ytdl_options=None, use_avconv=True)
        self.player.volume = .05
        self.player.start()

    async def trakd(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://youtu.be/8q0alRhsVgE',
                                                              ytdl_options=None, use_avconv=True)
        self.player.volume = .05
        self.player.start()

    async def trake(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=saVZRj1qiKw',
                                                              ytdl_options=None, use_avconv=True)
        self.player.volume = .05
        self.player.start()

    async def trakf(self):
        self.player.stop()
        await self.voice.disconnect()
        self.voice = await client.join_voice_channel(client.get_channel('245323860344438784'))
        self.player = await self.voice.create_ytdl_player('https://www.youtube.com/watch?v=34UutDrXV2Q',
                                                              ytdl_options=None, use_avconv=True)
        self.player.volume = .05
        self.player.start()

    def stop(self):
        self.player.stop()

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

    elif message.content.startswith('!rip'):
        await x.rip()

    elif message.content.startswith('!traka'):
        await x.traka()

    elif message.content.startswith('!trakb'):
        await x.trakb()

    elif message.content.startswith('!trakc'):
        await x.trakc()

    elif message.content.startswith('!trakd'):
        await x.trakd()

    elif message.content.startswith('!trake'):
        await x.trake()

    elif message.content.startswith('!trakf'):
        await x.trakf()

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
        say = interactables.hub.sort(send, message.author)

        #data = interactables.hub.sort(send,message.author)
        #say = data[1]
        #image = data[0]

        
    if say != 'fault':
        await client.send_message(message.channel, '{}'.format(say).format(message.author))
    if image != 'fault':
        await client.send_file(message.channel, '{}'.format(image))

client.run('MzAxNjM4NDg3NjMzODIxNjk3.C9Ahqw.u53J4fjNPW-ODS0XnqZvtlqjJiY')


