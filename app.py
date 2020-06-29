# app.py

"""Created by,
    MD Fardeen Ehsan
    fardeen.es7@gmail.com
    github.com/fardeen.es7
"""

import discord
import time

TOKEN = "Bot's Token Here"
AUTHOR = 0000000000  # Your discord id here

client = discord.Client()
PREFIX = "."


@client.event
async def on_ready() :
    for guild in client.guilds :
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')
        print('\n')


@client.event
async def on_message(message):
    sent = []
    if message.author == client.user:
        return
    # Remove the statement below if you want the bot work on only your messages.
    if message.author.id != AUTHOR:
        return

    if message.content.startswith(PREFIX):
        for guild in client.guilds:
            member_list = guild.members
            for member in member_list:
                if member.bot:
                    continue
                elif member in sent:
                    continue
                elif len(sent) >= 1000:
                    print("2000 Messages sent, taking a 10 minutes rest")
                    time.sleep(900)
                try:
                    dm = await member.create_dm()
                    await dm.send(message.content[1:])
                    print(f'message sent to {member}')
                    sent.append(member)
                    if len(sent) % 100 == 0:
                        print(f'{len(sent)} messages sent')
                except discord.Forbidden:
                    pass
            print(f'{len(sent)} messages sent')


client.run(TOKEN)
