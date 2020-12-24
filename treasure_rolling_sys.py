import discord
from random import randint


TOKEN = 'xxxxxxxxxxx'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    treasure_roll = randint(1, 100)

    if treasure_roll <= 30:
        await message.channel.send(treasure_roll)
        dice_roll = randint(1, 6) * 5
        await message.channel.send(dice_roll)
        await message.channel.send("This is CP treasure.")

    elif treasure_roll > 30 and treasure_roll <= 60:
        await message.channel.send(treasure_roll)
        dice_roll = randint(1, 6) * 4
        await message.channel.send(dice_roll)
        await message.channel.send("This is SP treasure.")

    elif treasure_roll > 60 and treasure_roll <= 70:
        await message.channel.send(treasure_roll)
        dice_roll = randint(1, 6) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("This is EP treasure.")

    elif treasure_roll > 70 and treasure_roll <= 95:
        await message.channel.send(treasure_roll)
        dice_roll = randint(1, 6) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("This is GP treasure.")

    elif treasure_roll > 95 and treasure_roll <= 100:
        await message.channel.send(treasure_roll)
        dice_roll = randint(1, 6)
        await message.channel.send(dice_roll)
        await message.channel.send("This is PP treasure.")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
