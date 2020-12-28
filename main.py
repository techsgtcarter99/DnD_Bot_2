import discord
from random import randint

TOKEN = 'xxxxxxxxxxxxxxxx'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

    elif message.content.startswith('!bot'):
        await message.channel.send("You rang?")

    elif message.content.startswith('@registeruser'):
        await message.channel.send('User Registered! {0.author.mention}'.format(message))

    elif message.content.startswith('tableofcontents'):
        file = discord.File("table_of_contents.png", filename="table_of_contents.png")
        await message.channel.send("table_of_contents.png", file=file)
        await message.channel.send("Just put name of monster to display information!")

    elif message.content.startswith('aboleth'):
        file = discord.File("Monsters/aboleth-1.png", filename="Monsters/aboleth-1.png")
        await message.channel.send("Monsters/aboleth-1.png", file=file)
        file = discord.File("Monsters/aboleth-2.png", filename="Monsters/aboleth-2.png")
        await message.channel.send("Monsters/aboleth-2.png", file=file)

    elif message.content.startswith('angel_deva1'):
        file = discord.File("Monsters/angels_deva-1.png", filename="Monsters/angels_deva-1.png")
        await message.channel.send("Monsters/angels_deva-1.png", file=file)
        file = discord.File("Monsters/angels_deva-2.png", filename="Monsters/angels_deva-2.png")
        await message.channel.send("Monsters/angels_deva-2.png", file=file)

    elif message.content.startswith('animated_armor'):
        file = discord.File("Monsters/animated_armor.png", filename="Monsters/animated_armor.png")
        await message.channel.send("Monsters/animated_armor.png", file=file)

    elif message.content.startswith('rugofsmothering'):
        file = discord.File("Monsters/rug_of_smothering.png", filename="Monsters/rug_of_smothering.png")
        await message.channel.send("Monsters/rug_of_smothering.png", file=file)

    elif message.content.startswith('flyingsword'):
        file = discord.File("Monsters/flying_sword.png", filename="Monsters/flying_sword.ong")
        await message.channel.send("Monsters/flying_sword.png", file=file)

    elif message.content.startswith('Goblins1'):
        file = discord.File("Monsters/GoblinsA.png", filename="Monsters/GoblinsA.png")
        await message.channel.send("Monsters/GoblinsA.png", file=file)
        file = discord.File("Monsters/GoblinsB.png", filename="Monsters/GoblinsB.png")
        await message.channel.send("Monsters/GoblinsB.png", file=file)

    elif message.content.startswith('planetar'):
        file = discord.File("Monsters/planetar-1.png", filename="Monsters/planetar-1.png")
        await message.channel.send("Monsters/planetar-1.png", file=file)

    elif message.content.startswith('solar'):
        file = discord.File("Monsters/solar-1.png", filename="Monsters/solar-1.png")
        await message.channel.send("Monsters/solar-1.png", file=file)

    elif message.content.startswith('mimic'):
        file = discord.File("Monsters/mimic-1.png", filename="Monsters/mimic-1.png")
        await message.channel.send("Monsters/mimic-1.png", file=file)

    elif message.content.startswith('ankheg'):
        file = discord.File("Monsters/ankeg.png", filename="Monsters/ankheg.png")
        await message.channel.send("Monsters/ankheg.png", file=file)

    elif message.content.startswith('azer'):
        file = discord.File("Monsters/azer.png", filename="Monsters/azer.png")
        await message.channel.send("Monsters/azer.png", file=file)

    elif message.content.startswith('banshee'):
        file = discord.File("Monsters/banshee.png", filename="Monsters/banshee.png")
        await message.channel.send("Monsters/banshee.png", file=file)

    elif message.content.startswith('basilisk'):
        file = discord.File("Monsters/basilisk.png", filename="Monsters/basilisk.png")
        await message.channel.send("Monsters/basilisk.png", file=file)

    else:
        pass

    # challenge rating 0-4 treasure rolling

    if message.content.startswith("0-4treasure_roll"):
        treasure_roll = randint(1, 100)

        if treasure_roll <= 30:
            await message.channel.send(treasure_roll)
            dice_roll = randint(1, 6) * 5
            await message.channel.send(dice_roll)
            await message.channel.send("This is CP treasure.")

        elif 30 < treasure_roll <= 60:
            await message.channel.send(treasure_roll)
            dice_roll = randint(1, 6) * 4
            await message.channel.send(dice_roll)
            await message.channel.send("This is SP treasure.")

        elif 60 < treasure_roll <= 70:
            await message.channel.send(treasure_roll)
            dice_roll = randint(1, 6) * 3
            await message.channel.send(dice_roll)
            await message.channel.send("This is EP treasure.")

        elif 70 < treasure_roll <= 95:
            await message.channel.send(treasure_roll)
            dice_roll = randint(1, 6) * 3
            await message.channel.send(dice_roll)
            await message.channel.send("This is GP treasure.")

        elif 95 < treasure_roll <= 100:
            await message.channel.send(treasure_roll)
            dice_roll = randint(1, 6)
            await message.channel.send(dice_roll)
            await message.channel.send("This is PP treasure.")

    else:
        pass

    # 5-10 challenge rating treasure rolling

    if message.content.startswith("5-10treasure_roll"):
        treasure_roll = randint(1, 100)

        if treasure_roll <= 30:
            await message.channel.send(treasure_roll)
            dice_rolla = randint(1, 6) * 4
            await message.channel.send(dice_rolla * 100)
            await message.channel.send("This is CP treasure.")
            dice_rollb = randint(1, 6)
            await message.channel.send(dice_rollb * 10)
            await message.channel.send("This is EP treasure.")

        elif 30 < treasure_roll <= 60:
            await message.channel.send(treasure_roll)
            dice_rolla = randint(1, 6) * 6
            await message.channel.send(dice_rolla * 10)
            await message.channel.send("This is SP treasure.")
            dice_rollb = randint(1, 6) * 2
            await message.channel.send(dice_rollb * 10)
            await message.channel.send("This is GP treasure.")

        elif 60 < treasure_roll <= 70:
            await message.channel.send(treasure_roll)
            dice_rolla = randint(1, 6) * 6
            await message.channel.send(dice_rolla * 10)
            await message.channel.send("This is EP treasure.")
            dice_rollb = randint(1, 6) * 2
            await message.channel.send(dice_rollb * 10)
            await message.channel.send("This is GP treasure.")

        elif 70 < treasure_roll <= 95:
            await message.channel.send(treasure_roll)
            dice_roll = randint(1, 6) * 4
            await message.channel.send(dice_roll * 10)
            await message.channel.send("This is GP treasure.")

        elif 95 < treasure_roll <= 100:
            await message.channel.send(treasure_roll)
            dice_rolla = randint(1, 6) * 2
            await message.channel.send(dice_rolla * 10)
            await message.channel.send("This is GP treasure.")
            dice_rollb = randint(1, 6) * 3
            await message.channel.send(dice_rollb)
            await message.channel.send("This is PP treasure.")

    else:
        pass

        # 11-16 challenge rating treasure rolling

        if message.content.startswith("11-16treasure_roll"):
            treasure_roll = randint(1, 100)

            if treasure_roll <= 20:
                await message.channel.send(treasure_roll)
                dice_rolla = randint(1, 6) * 4
                await message.channel.send(dice_rolla * 100)
                await message.channel.send("This is SP treasure.")
                dice_rollb = randint(1, 6)
                await message.channel.send(dice_rollb * 100)
                await message.channel.send("This is GP treasure.")

            elif 20 < treasure_roll <= 35:
                await message.channel.send(treasure_roll)
                dice_rolla = randint(1, 6)
                await message.channel.send(dice_rolla * 100)
                await message.channel.send("This is EP treasure.")
                dice_rollb = randint(1, 6)
                await message.channel.send(dice_rollb * 100)
                await message.channel.send("This is GP treasure.")

            elif 35 < treasure_roll <= 75:
                await message.channel.send(treasure_roll)
                dice_rolla = randint(1, 6) * 2
                await message.channel.send(dice_rolla * 100)
                await message.channel.send("This is GP treasure.")
                dice_rollb = randint(1, 6)
                await message.channel.send(dice_rollb * 10)
                await message.channel.send("This is PP treasure.")

            elif 75 < treasure_roll <= 100:
                await message.channel.send(treasure_roll)
                dice_rolla = randint(1, 6) * 2
                await message.channel.send(dice_rolla * 100)
                await message.channel.send("This is GP treasure.")
                dice_rollb = randint(1, 6) * 2
                await message.channel.send(dice_rollb * 10)
                await message.channel.send("This is PP treasure.")

        else:
            pass

    # 17+ challenge rating treasure rolling

    if message.content.startswith("17+treasure_roll"):
        treasure_roll = randint(1, 100)

    if treasure_roll <= 15:
        await message.channel.send(treasure_roll)
        dice_rolla = randint(1, 6) * 2
        await message.channel.send(dice_rolla * 1000)
        await message.channel.send("This is EP treasure.")
        dice_rollb = randint(1, 6) * 8
        await message.channel.send(dice_rollb * 100)
        await message.channel.send("This is GP treasure.")

    elif 15 < treasure_roll <= 55:
        await message.channel.send(treasure_roll)
        dice_rolla = randint(1, 6)
        await message.channel.send(dice_rolla * 1000)
        await message.channel.send("This is GP treasure.")
        dice_rollb = randint(1, 6)
        await message.channel.send(dice_rollb * 100)
        await message.channel.send("This is PP treasure.")

    elif 55 < treasure_roll <= 100:
        await message.channel.send(treasure_roll)
        dice_rolla = randint(1, 6)
        await message.channel.send(dice_rolla * 1000)
        await message.channel.send("This is GP treasure.")
        dice_rollb = randint(1, 6) * 2
        await message.channel.send(dice_rollb * 10)
        await message.channel.send("This is PP treasure.")

    else:
        pass

    # treasure gemstone rolling

    if message.content.startswith('10gpgemstones'):
        dice_roll = randint(1, 12)

        if dice_roll == 1:
            await message.channel.send("Azurite (opaque mottled deep blue)")

        elif dice_roll == 2:
            await message.channel.send("Banded agate (translucent stirped (any color))")

        elif dice_roll == 3:
            await message.channel.send("Blue quartz (transparent pale blue)")

        elif dice_roll == 4:
            await message.channel.send("Eye agate (translucent circles of (any color))")

        elif dice_roll == 5:
            await message.channel.send("Hematite (opaque gray-black)")

        elif dice_roll == 6:
            await message.channel.send("Lapis Lazuli (opaque light/dark blue with pecks of yellow)")

        elif dice_roll == 7:
            await message.channel.send("Malachite (opaque striated light and dark green)")

        elif dice_roll == 8:
            await message.channel.send("Moss agate (translucent pink or yellow-white with mossy green)")

        elif dice_roll == 9:
            await message.channel.send("Obsidian (opaque black)")

        elif dice_roll == 10:
            await message.channel.send("Rhodochrosite (opaque light pink)")

        elif dice_roll == 11:
            await message.channel.send("Tiger eye (translucent brown with golden center)")

        elif dice_roll == 12:
            await message.channel.send("Turqouise (opaque light blue-green)")

    else:
        pass

    # Maps Go Here
    if message.content.startswith('?planesmap'):
        file = discord.File("Maps/Planes.png", filename="Maps/Planes.png")
        await message.channel.send("Maps/Planes.png", file=file)

    else:
        pass

    # Combat Rolls Go here

    if message.content.startswith('1d4'):
        dice_roll = randint(1, 4)
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('1d6'):
        dice_roll = randint(1, 6)
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('1d8'):
        dice_roll = randint(1, 8)
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('1d10'):
        dice_roll = randint(1, 10)
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('1d12'):
        dice_roll = randint(1, 12)
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('2d4'):
        dice_roll = randint(1, 4) * 2
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('2d6'):
        dice_roll = randint(1, 6) * 2
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('2d8'):
        dice_roll = randint(1, 8) * 2
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('2d10'):
        dice_roll = randint(1, 10) * 2
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('2d12'):
        dice_roll = randint(1, 12) * 2
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('3d4'):
        dice_roll = randint(1, 4) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('3d6'):
        dice_roll = randint(1, 6) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('3d8'):
        dice_roll = randint(1, 8) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('2d10'):
        dice_roll = randint(1, 10) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('3d12'):
        dice_roll = randint(1, 12) * 3
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('4d4'):
        dice_roll = randint(1, 4) * 4
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('4d6'):
        dice_roll = randint(1, 6) * 4
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('4d8'):
        dice_roll = randint(1, 8) * 4
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('4d10'):
        dice_roll = randint(1, 10) * 4
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('4d12'):
        dice_roll = randint(1, 12) * 4
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('5d4'):
        dice_roll = randint(1, 4) * 5
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('5d6'):
        dice_roll = randint(1, 6) * 5
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('5d8'):
        dice_roll = randint(1, 8) * 5
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('5d10'):
        dice_roll = randint(1, 10) * 5
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('5d12'):
        dice_roll = randint(1, 12) * 5
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('6d4'):
        dice_roll = randint(1, 4) * 6
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('6d6'):
        dice_roll = randint(1, 6) * 6
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('6d8'):
        dice_roll = randint(1, 8) * 6
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('6d10'):
        dice_roll = randint(1, 10) * 6
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('6d12'):
        dice_roll = randint(1, 12) * 6
        await message.channel.send(dice_roll)
        await message.channel.send("damage")

    elif message.content.startswith('1d20'):
        dice_roll = randint(1, 20)
        await message.channel.send(dice_roll)
        await message.channel.send("Your initiative, do you get to go first or last?")

    else:
        pass


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
