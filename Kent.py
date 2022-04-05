from stat import filemode
from typing import Counter
import discord
from discord.enums import MessageType
from discord.ext.commands import errors
import discord.member
import discord.channel
import discord.message
import discord.voice_client
from discord.ext import commands, tasks
from discord_components import Button, ButtonStyle, ComponentsBot
import os
import random
import urllib.request
import re
import pafy
import datetime
import spotipy
from spotipy import SpotifyClientCredentials
from threading import Thread
import emoji

#regex dictionary
#(.*?)    match unspecified length of characters
#(?:.*?)    ignore unspecified length of characters

print('Test file successfully run')

class MainCog(commands.Cog):

    global errorLog
    errorLog = {}

    def __init__(self, bot):
        self.bot = bot

        try:
            os.chdir(os.getcwd() + '\\source\\repos\\Kent')

            for filename in os.listdir(os.path.dirname(__file__) + '\\Kent_Cogs'):

                if filename.endswith('.py'):

                    self.bot.load_extension(f'Kent_Cogs.{filename[:-3]}')
        except:
            pass

        try:
            os.chdir('home/pi/Kent')

            for filename in os.listdir(os.path.dirname(__file__) + '/Kent_Cogs'):

                if filename.endswith('.py'):

                    self.bot.load_extension(f'Kent_Cogs.{filename[:-3]}')
        except:
            pass
        
        print(os.getcwd())
        os.chdir('Users')

        #self.sync.start()
        #self.money.start()

    """@tasks.loop(seconds=60)
    async def sync(self):
        guild = await self.bot.fetch_guild(905228207031197817)

        memberNames = []
        
        async for member in guild.fetch_members():
            if not member.bot:
                memberNames.append(member.name)
                if not os.path.exists("{}.txt".format(member.name)):
                    file = open("{}.txt".format(member.name), 'w')
                    file.write("10 0")

        for file in os.listdir():
            if not str(file)[:-4] in memberNames:
                os.remove(file)

    @tasks.loop(seconds=60 * 15)
    async def money(self):
        for file in os.listdir():
            values = open(file, 'r').read().split()
            open(file, 'w').write(str(int(values[0]) + 1) + ' ' + values[1])
        

    @commands.command()
    async def help(self, ctx):

        embedVar = discord.Embed(title="Commands", color=0x0e41b5)

        embedVar.add_field(name='{0}reset'.format('##'), value='Återställ botten', inline=False)
        embedVar.add_field(name='{0}inv {0}inventory'.format('##'), value='Se ägodelar', inline=False)

        await ctx.send(
            content = None,
            embed = embedVar,
            components=None
        )"""


    @commands.command()
    async def reset(self, ctx):

        if ctx.channel.guild.voice_client:

            if not len(ctx.channel.guild.voice_client.channel.members) - 1 <= 2:
                        
                if not ctx.author.guild_permissions.administrator:
                    
                    temp = False

                    for i in ctx.author.roles:

                        if i.name.lower() == 'Kent dommy':

                            temp = True

                    if not temp:
                        return

        await ctx.send('Resetting')
        errorLog[ctx.guild.id] = ['[{}]   Was reset.'.format(datetime.datetime.now().time())]

        try:

            print('test')

        except:

            pass

        await ctx.send('Please report any problems you find using `{0}report`'.format('##'))


    @commands.command()
    async def reactions(self, ctx):
        if ctx.message.reference:
            print('reactions command')
            ogMessage = await ctx.channel.fetch_message(ctx.message.reference.message_id)

            if ogMessage.author == ctx.message.author:
                
                try:
                    emojis = ['']
                    print(ctx.message.content)
                    for character in ctx.message.content[12:]:
                        
                        if not character == ' ':

                            emojis[len(emojis) - 1] += character

                            if not re.match(r'<|:|[a-ö]|\d', character):
                                emojis.append('')

                    print(emojis)
                    #emojis = ctx.message.content[12:].split()

                    for emoji in emojis:
                        
                        try:
                            if len(emoji) > 1:

                                emojis[emojis.index(emoji)] = (re.findall(r'(\d{18})', emoji)[0])

                                emoji = (re.findall(r'(\d{18})', emoji)[0])

                                await ogMessage.add_reaction(self.bot.get_emoji(int(emoji)))

                            else:
                                await ogMessage.add_reaction(emoji)
                        except:
                            pass

                    print(emojis)

                except:
                    pass

                await ctx.message.delete()

    """@commands.command()
    async def buy(self, ctx):
        for file in os.listdir():
                if str(file)[:-4] == ctx.author.name:
                    values = open(file, 'r').read().split()

                    if int(values[0]) < 10:
                        await ctx.message.reply('F-ord pass kostar 10 kr, du har bara ' + values[0] + ' kr')
                    
                    else:
                        values[0] = str(int(values[0]) - 10)

                        values[1] = str(int(values[1]) + 1)

                        open(file, 'w').write(values[0] + ' ' + values[1])

    @commands.command(aliases=['inventory', 'inv'])
    async def _inventory(self, ctx):
        for file in os.listdir():
                if str(file)[:-4] == ctx.author.name:
                    values = open(file, 'r').read().split()

                    await ctx.message.reply('Kronor: {}\nF-ord pass: {}'.format(values[0], values[1]))



    @commands.Cog.listener() #y = any(x in String for x in List)
    async def on_message(self, message):
        if "folke" in message.content.lower():

            print('Folke detected')

            for file in os.listdir():
                if str(file)[:-4] == message.author.name:
                    values = open(file, 'r').read().split()

                    if int(values[1]) < 1:
                        print('1')
                        try:
                            await message.reply('F-ordet är förbjudet')
                            await message.delete()
                        except:
                            pass
                    else:
                        print('2')
                        
                        values[1] = str(int(values[1]) - 1)

                        print(values[1])

                        open(file, 'w').write(values[0] + ' ' + values[1])"""

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        if re.match(r'.+?#\d{4} (.*?)', message.content):
            
            match = re.match(r'(.+?)#\d{4} (.*?)', message.content)

            for member in self.bot.get_all_members():
                if not member.bot:
                    if member.name == match[1]:
                        print(member.id)
                        await member.create_dm()
                        await member.send(message.content[len(match[0]):])

                        return

            await message.reply('Could not send message')

    

def setup(bot):
    bot.add_cog(MainCog(bot))

