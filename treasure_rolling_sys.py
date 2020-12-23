import discord
from random import randint
from time import sleep
import asyncio
import dice_roll

TOKEN = 'xxxxxxxxxxxxx'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    treasure_roll = randint(1, 30)

    if treasure_roll <= 30:
        sleep(5)
        asyncio.run(dice_roll)

    elif treasure_roll <= 60:
        await message.channel.send(treasure_roll)
        await message.channel.send("Please roll 4d6 for SP treasure!")

    elif treasure_roll <= 70:
        await message.channel.send(treasure_roll)
        await message.channel.send("Please roll 3d6 for EP treasure!")

    elif treasure_roll <= 95:
        await message.channel.send(treasure_roll)
        await message.channel.send("Please roll 3d6 for GP treasure!")

    elif treasure_roll <= 100:
        await message.channel.send(treasure_roll)
        await message.channel.send("Please roll 1d6 for PP treasure!")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
