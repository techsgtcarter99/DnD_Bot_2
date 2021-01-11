import discord
from random import randint

TOKEN = 'xxxxxxxxxxxxxxx'

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

    elif message.content.startswith('behir'):
        file = discord.File("Monsters/behir.png", filename="Monsters/behir.png")
        await message.channel.send("Monsters/behir.png", file=file)

    elif message.content.startswith('beholder'):
        file = discord.File("Monsters/beholder1.png", filename="Monsters/beholder1.png")
        await message.channel.send("Monsters/beholder1.png", file=file)
        file = discord.File("Monsters/beholder2.png", filename="Monsters/beholder2.png")
        await message.channel.send("Monsters/beholder2.png", file=file)

    elif message.content.startswith('deathtyrant'):
        file = discord.File("Monsters/death_tyrant1.png", filename="Monsters/death_tyrant1.png")
        await message.channel.send("Monsters/death_tyrant1.png", file=file)
        file = discord.File("Monsters/death_tyrant2.png", filename="Monsters/death_tyrant2.png")
        await message.channel.send("Monsters/death_tyrant2.png", file=file)

    elif message.content.startswith('spectator'):
        file = discord.File("Monsters/spectator.png", filename="Monsters/spectator.png")
        await message.channel.send("Monsters/spectator.png", file=file)

    elif message.content.startswith('needleblight'):
        file = discord.File("Monsters/Needle_Blight-1.png", filename="Monsters/Needle_Blight-1.png")
        await message.channel.send("Monsters/Needle_Blight-1.png", file=file)
        file = discord.File("Monsters/Needle_Blight-2.png", filename="Monsters/Needle_Blight-2.png")
        await message.channel.send("Monsters/Needle_Blight-2.png", file=file)

    elif message.content.startswith('twigblight'):
        file = discord.File("Monsters/Twig_Blight.png", filename="Monsters/Twig_Blight.png")
        await message.channel.send("Monsters/Twig_Blight.png", file=file)

    elif message.content.startswith('vineblight'):
        file = discord.File("Monsters/Vine_Blight.png", filename="Monsters/Vine_Blight.png")
        await message.channel.send("Monsters/Vine_Blight.png", file=file)

    elif message.content.startswith('bugbear'):
        file = discord.File("Monsters/bugbear.png", filename="Monsters/bugbear.png")
        await message.channel.send("Monsters/bugbear.png", file=file)

    elif message.content.startswith('bugbearchief'):
        file = discord.File("Monsters/bugbearchief.png", filename="Monsters/bugbearchief.png")
        await message.channel.send("Monsters/bugbearchief.png", file=file)


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

    # treasure 10gp gemstone rolling

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

        # 50gp treasure rolling

    if message.content.startswith('50gpgemstones'):
        dice_roll = randint(1, 12)

        if dice_roll == 1:
            await message.channel.send("Bloodstone (opaque dark gray with red flecks)")

        elif dice_roll == 2:
            await message.channel.send("Carnelian (opaque orange to red-brown)")

        elif dice_roll == 3:
            await message.channel.send("Chalcedony (opaque white)")

        elif dice_roll == 4:
            await message.channel.send("Chrysoprase (translucent green)")

        elif dice_roll == 5:
            await message.channel.send("Citrine (transparent pale yellow-brown)")

        elif dice_roll == 6:
            await message.channel.send("Jasper (opaque blue, black, or brown)")

        elif dice_roll == 7:
            await message.channel.send("Moonstone (translucent white with pale blue glow)")

        elif dice_roll == 8:
            await message.channel.send("Onyx (opaque bands of black and white, or pure black or white)")

        elif dice_roll == 9:
            await message.channel.send("Quartz (transparent white, smoky gray, or yellow)")

        elif dice_roll == 10:
            await message.channel.send("Sardonyx (opaque bands of red and white)")

        elif dice_roll == 11:
            await message.channel.send("Star rose quartz (trasnlucent rosy stone with white star-shaped center")

        elif dice_roll == 12:
            await message.channel.send("Zircon (transparent pale blue-green)")

    else:
        pass

    # 100gp gemstones

    if message.content.startswith('100gpgemstones'):
        dice_roll = randint(1, 10)

        if dice_roll == 1:
            await message.channel.send("Amber (transparent watery gold to rich gold)")

        elif dice_roll == 2:
            await message.channel.send("Amethyst (transparent deep purple)")

        elif dice_roll == 3:
            await message.channel.send("Chrysoberyl (transparent yellow-green to pale green)")

        elif dice_roll == 4:
            await message.channel.send("Coral (opaque crimson)")

        elif dice_roll == 5:
            await message.channel.send("Garnet (transparent red, brown-green, or violet)")

        elif dice_roll == 6:
            await message.channel.send("Jade (translucent light green, deep green, or white)")

        elif dice_roll == 7:
            await message.channel.send("Jet (opaque deep black)")

        elif dice_roll == 8:
            await message.channel.send("Pearl (opaque lustrous white, yellow, or pink)")

        elif dice_roll == 9:
            await message.channel.send("Spinel (transparent red, red-brown, or deep green)")

        elif dice_roll == 10:
            await message.channel.send("Tourmaline (transparent pale green, blue, brown, or red")

    else:
        pass

        # 500gp gemstones

    if message.content.startswith('500gpgemstones'):
        dice_roll = randint(1, 6)

        if dice_roll == 1:
            await message.channel.send("Alexandrite (transparent dark green)")

        elif dice_roll == 2:
            await message.channel.send("Aquamarine (transparent pale blue-green)")

        elif dice_roll == 3:
            await message.channel.send("Black pearl (opaque pure black)")

        elif dice_roll == 4:
            await message.channel.send("Blue spinel (transparent deep blue)")

        elif dice_roll == 5:
            await message.channel.send("Peridot (transparent rich olive green)")

        elif dice_roll == 6:
            await message.channel.send("Topaz (transparent golden yellow)")
    else:
        pass

        # 1000gp gemstones

    if message.content.startswith('1000gpgemstones'):
        dice_roll = randint(1, 8)

        if dice_roll == 1:
            await message.channel.send("Black opal (translucent dark green with black mottling and golden flecks")

        elif dice_roll == 2:
            await message.channel.send("Blue sapphire (transparent blue-white to medium blue)")

        elif dice_roll == 3:
            await message.channel.send("Emerald (transparent deep bright green)")

        elif dice_roll == 4:
            await message.channel.send("Fire opal (translucent fiery red)")

        elif dice_roll == 5:
            await message.channel.send("Opal (translucent pale blue with green and gold mottling)")

        elif dice_roll == 6:
            await message.channel.send("Star ruby (translucent ruby with white star-shaped center)")

        elif dice_roll == 7:
            await message.channel.send("Star sapphire (translucent blue sapphire with white star-shaped center)")

        elif dice_roll == 8:
            await message.channel.send("Yellow sapphire (transparent fiery yellow or yellow-green)")

        else:
            pass

        # 5000gp gemstones

    if message.content.startswith('5000gpgemstones'):
        dice_roll = randint(1, 4)

        if dice_roll == 1:
            await message.channel.send("Black sapphire (translucent lustrous black with glowing highlights)")

        elif dice_roll == 2:
            await message.channel.send("Diamond (trasnparent blue-white, canary, pink, brown, or blue)")

        elif dice_roll == 3:
            await message.channel.send("Jacinth (transparent fiery orange)")

        elif dice_roll == 4:
            await message.channel.send("Ruby (transparent clear red to deep crimson)")

        else:
            pass

        # 25gp art

    if message.content.startswith('25gpart'):
        dice_roll = randint(1, 10)

        if dice_roll == 1:
            await message.channel.send("Silver ewer")

        elif dice_roll == 2:
            await message.channel.send("Carved bone statuette")

        elif dice_roll == 3:
            await message.channel.send("Small gold bracelet")

        elif dice_roll == 4:
            await message.channel.send("Cloth-of-gold vestments")

        elif dice_roll == 5:
            await message.channel.send("Black velvet mask stitched with silver thread")

        elif dice_roll == 6:
            await message.channel.send("Copper chalice with silver filigree")

        elif dice_roll == 7:
            await message.channel.send("Pair of engraved bonde dice")

        elif dice_roll == 8:
            await message.channel.send("Small mirror set in a painted wooden frame")

        elif dice_roll == 9:
            await message.channel.send("Embroidered silk handkerchief")

        elif dice_roll == 10:
            await message.channel.send("Gold locket with a painted portrait inside")

    else:
        pass

        # 250gp art

    if message.content.startswith('250gpart'):
        dice_roll = randint(1, 10)

        if dice_roll == 1:
            await message.channel.send("Gold ring set with bloodstones")

        elif dice_roll == 2:
            await message.channel.send("Carved ivory statuette")

        elif dice_roll == 3:
            await message.channel.send("Large gold bracelet")

        elif dice_roll == 4:
            await message.channel.send("Silver necklace with a gemstone pendant")

        elif dice_roll == 5:
            await message.channel.send("Bronze crown")

        elif dice_roll == 6:
            await message.channel.send("Silk robe with gold embroidery")

        elif dice_roll == 7:
            await message.channel.send("Large well-known tapestry")

        elif dice_roll == 8:
            await message.channel.send("Brass mug with jade inlay")

        elif dice_roll == 9:
            await message.channel.send("Box of turquoise animal figurines")

        elif dice_roll == 10:
            await message.channel.send("Gold bird cage with electrum filigree")

        else:
            pass

        # 750gp art

    if message.content.startswith('750gpart'):
        dice_roll = randint(1, 10)

        if dice_roll == 1:
            await message.channel.send("Silver chalice set with moonstones")

        elif dice_roll == 2:
            await message.channel.send("Silver-plated steel longsword with jet set in hilt")

        elif dice_roll == 3:
            await message.channel.send("Carved harp of exotic wood with ivory inlay and zircon gems")

        elif dice_roll == 4:
            await message.channel.send("Small gold idol")

        elif dice_roll == 5:
            await message.channel.send("Gold dragon comb set with red garnet as eyes")

        elif dice_roll == 6:
            await message.channel.send("Bottle stopper cork embossed with gold leaf and set with amethysts")

        elif dice_roll == 7:
            await message.channel.send("Ceremonial electrum dagger with a black pearl in the pommel")

        elif dice_roll == 8:
            await message.channel.send("Silver and gold brooch")

        elif dice_roll == 9:
            await message.channel.send("Obsidian statuette with gold fittings and inlay")

        elif dice_roll == 10:
            await message.channel.send("Painted gold war mask")

        else:
            pass

            # 2500gp art

    if message.content.startswith('2500gpart'):
        dice_roll = randint(1, 10)

        if dice_roll == 1:
            await message.channel.send("Fine gold chain set with fire opal")

        elif dice_roll == 2:
            await message.channel.send("Old masterpiece painting")

        elif dice_roll == 3:
            await message.channel.send("Embroidered silk and velvet mantle set with numerous moonstones")

        elif dice_roll == 4:
            await message.channel.send("Platinum bracelet set with a sapphire")

        elif dice_roll == 5:
            await message.channel.send("Embroidered glove set with jewel chips")

        elif dice_roll == 6:
            await message.channel.send("Jeweled anklet")

        elif dice_roll == 7:
            await message.channel.send("Gold music box")

        elif dice_roll == 8:
            await message.channel.send("Gold circlet set with four aquamarines")

        elif dice_roll == 9:
            await message.channel.send("Eye patch with a mock eye set in blue sapphire and moonstone")

        elif dice_roll == 10:
            await message.channel.send("A necklace string of small pink pearls")

    else:
        pass

        # 7500gp art

    if message.content.startswith('7500gpart'):
        dice_roll = randint(1, 8)

        if dice_roll == 1:
            await message.channel.send("Jeweled gold crown")

        elif dice_roll == 2:
            await message.channel.send("Jeweled platinum ring")

        elif dice_roll == 3:
            await message.channel.send("Small gold statuette set with rubies")

        elif dice_roll == 4:
            await message.channel.send("Gold cup set with emeralds")

        elif dice_roll == 5:
            await message.channel.send("Gold jewelry box with platinum filigree")

        elif dice_roll == 6:
            await message.channel.send("Painted gold child's sarcophagus")

        elif dice_roll == 7:
            await message.channel.send("Jade game board with solid gold playing pieces")

        elif dice_roll == 8:
            await message.channel.send("Bejeweled ivory drinking horn with gold filigree")

    else:
        pass

        # Magic Item Rarity

    if message.content.startswith('MIRC'):
        await message.channel.send("Rarity is common")
        await message.channel.send("Character level required is 1 or higher")
        await message.channel.send("Value is 50 to 100gp")

    elif message.content.startswith('MIRU'):
        await message.channel.send("Rarity is uncommon")
        await message.channel.send("Character level required is 1 or higher")
        await message.channel.send("Value is 101 to 500gp")

    elif message.content.startswith('MIRR'):
        await message.channel.send("Rarity is rare")
        await message.channel.send("Character level required is 5 or higher")
        await message.channel.send("Value is 501 to 5,000gp")

    elif message.content.startwith('MIRVR'):
        await message.channel.send("Rarity is very rare")
        await message.channel.send("Character level required is 11 or higher")
        await message.channel.send("Value is 5,001 to 50,000gp")

    elif message.content.startswith('MIRL'):
        await message.channel.send("Rarity is legendary")
        await message.channel.send("Character level required is 17 or higher")
        await message.channel.send("Value is 50,001gp to higher")

    else:
        pass

    # Maps Go Here
    if message.content.startswith('?planesmap'):
        file = discord.File("Maps/Planes.png", filename="Maps/Planes.png")
        await message.channel.send("Maps/Planes.png", file=file)

    else:
        pass

    # Dice Rolls

    if message.content.startswith('1d4'):
        dice_roll = randint(1, 4)
        await message.channel.send(dice_roll)

    elif message.content.startswith('1d6'):
        dice_roll = randint(1, 6)
        await message.channel.send(dice_roll)

    elif message.content.startswith('1d8'):
        dice_roll = randint(1, 8)
        await message.channel.send(dice_roll)

    elif message.content.startswith('1d10'):
        dice_roll = randint(1, 10)
        await message.channel.send(dice_roll)

    elif message.content.startswith('1d12'):
        dice_roll = randint(1, 12)
        await message.channel.send(dice_roll)

    elif message.content.startswith('2d4'):
        dice_roll = randint(1, 4) * 2
        await message.channel.send(dice_roll)

    elif message.content.startswith('2d6'):
        dice_roll = randint(1, 6) * 2
        await message.channel.send(dice_roll)

    elif message.content.startswith('2d8'):
        dice_roll = randint(1, 8) * 2
        await message.channel.send(dice_roll)

    elif message.content.startswith('2d10'):
        dice_roll = randint(1, 10) * 2
        await message.channel.send(dice_roll)

    elif message.content.startswith('2d12'):
        dice_roll = randint(1, 12) * 2
        await message.channel.send(dice_roll)

    elif message.content.startswith('3d4'):
        dice_roll = randint(1, 4) * 3
        await message.channel.send(dice_roll)

    elif message.content.startswith('3d6'):
        dice_roll = randint(1, 6) * 3
        await message.channel.send(dice_roll)

    elif message.content.startswith('3d8'):
        dice_roll = randint(1, 8) * 3
        await message.channel.send(dice_roll)

    elif message.content.startswith('3d10'):
        dice_roll = randint(1, 10) * 3
        await message.channel.send(dice_roll)

    elif message.content.startswith('3d12'):
        dice_roll = randint(1, 12) * 3
        await message.channel.send(dice_roll)

    elif message.content.startswith('4d4'):
        dice_roll = randint(1, 4) * 4
        await message.channel.send(dice_roll)

    elif message.content.startswith('4d6'):
        dice_roll = randint(1, 6) * 4
        await message.channel.send(dice_roll)

    elif message.content.startswith('4d8'):
        dice_roll = randint(1, 8) * 4
        await message.channel.send(dice_roll)

    elif message.content.startswith('4d10'):
        dice_roll = randint(1, 10) * 4
        await message.channel.send(dice_roll)

    elif message.content.startswith('4d12'):
        dice_roll = randint(1, 12) * 4
        await message.channel.send(dice_roll)

    elif message.content.startswith('5d4'):
        dice_roll = randint(1, 4) * 5
        await message.channel.send(dice_roll)

    elif message.content.startswith('5d6'):
        dice_roll = randint(1, 6) * 5
        await message.channel.send(dice_roll)

    elif message.content.startswith('5d8'):
        dice_roll = randint(1, 8) * 5
        await message.channel.send(dice_roll)

    elif message.content.startswith('5d10'):
        dice_roll = randint(1, 10) * 5
        await message.channel.send(dice_roll)

    elif message.content.startswith('5d12'):
        dice_roll = randint(1, 12) * 5
        await message.channel.send(dice_roll)

    elif message.content.startswith('6d4'):
        dice_roll = randint(1, 4) * 6
        await message.channel.send(dice_roll)

    elif message.content.startswith('6d6'):
        dice_roll = randint(1, 6) * 6
        await message.channel.send(dice_roll)

    elif message.content.startswith('6d8'):
        dice_roll = randint(1, 8) * 6
        await message.channel.send(dice_roll)

    elif message.content.startswith('6d10'):
        dice_roll = randint(1, 10) * 6
        await message.channel.send(dice_roll)

    elif message.content.startswith('6d12'):
        dice_roll = randint(1, 12) * 6
        await message.channel.send(dice_roll)

    elif message.content.startswith('1d20'):
        dice_roll = randint(1, 20)
        await message.channel.send(dice_roll)

    elif message.content.startswith('1d100'):
        dice_roll = randint(1, 100)
        await message.channel.send(dice_roll)

    else:
        pass


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
