import discord
from random import randint

TOKEN = 'Nzg1NzI3OTc2MDk1NjEyOTI5.X88EMw.H0sDdCjw9Yb60ovDVWORpDxUXJA'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    treasure_roll = randint(1, 100)

    if treasure_roll <= 30:
        await message.channel.send(treasure_roll)
        await message.channel.send("1st range")

    elif treasure_roll <= 60:
        await message.channel.send(treasure_roll)
        await message.channel.send("2nd range")

    elif treasure_roll <= 70:
        await message.channel.send(treasure_roll)
        await message.channel.send("3rd range")

    elif treasure_roll <= 95:
        await message.channel.send(treasure_roll)
        await message.channel.send("4th range")

    elif treasure_roll <= 100:
        await message.channel.send(treasure_roll)
        await message.channel.send("5th range")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
