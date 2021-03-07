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

    elif message.content.startswith('bulette'):
        file = discord.File("Monsters/Bulette.png", filename="Monsters/Bulette.png")
        await message.channel.send("Monsters/Bulette.png", file=file)

    elif message.content.sartswith('bullywug'):
        file = discord.File("Monsters/Bullywug.png", filename="Monsters/Bullywug.png")
        await message.channel.send("Monsters/Bullywug.png", file=file)

    elif message.content.sartswith('cambion'):
        file = discord.File("Monsters/cambion.png", filename="Monsters/cambion.png")
        await message.channel.send("Monsters/cambion.png", file=file)

    elif message.content.sartswith('carrioncrawler'):
        file = discord.File("Monsters/carrion_crawler.png", filename="Monsters/carrion_crawler.png")
        await message.channel.send("Monsters/carrion_crawler.png", file=file)

    elif message.content.sartswith('centaur'):
        file = discord.File("Monsters/centaur.png", filename="Monsters/centaur.png")
        await message.channel.send("Monsters/centaur.png", file=file)

    elif message.content.startswith('chimera'):
        file = discord.File("Monsters/chimera.png", filename="Monsters/chimera.png")
        await message.channel.send("Monsters/chimera.png", file=file)

    elif message.content.startswith('chuul'):
        file = discord.File("Monsters/chuul.png", filename="Monsters/chuul'.png")
        await message.channel.send("Monsters/chuul'.png", file=file)

    elif message.content.startswith('cloaker'):
        file = discord.File("Monsters/cloaker.png", filename="Monsters/cloaker'.png")
        await message.channel.send("Monsters/cloaker'.png", file=file)

    elif message.content.startswith('cockatrice'):
        file = discord.File("Monsters/cockatrice.png", filename="Monsters/cockatrice'.png")
        await message.channel.send("Monsters/cockatrice'.png", file=file)

    elif message.content.startswith('couatl'):
        file = discord.File("Monsters/couatl.png", filename="Monsters/couatl.png")
        await message.channel.send("Monsters/couatl.png", file=file)

    elif message.content.startswith('crawlingclaw'):
        file = discord.File("Monsters/crawling_claw.png", filename="Monsters/crawling_claw.png")
        await message.channel.send("Monsters/crawling_claw.png", file=file)

    elif message.content.startswith('cyclops'):
        file = discord.File("Monsters/cyclops.png", filename="Monsters/cyclops.png")
        await message.channel.send("Monsters/cyclops.png", file=file)

    elif message.content.startswith('darkmantle'):
        file = discord.File("Monsters/darkmantle.png", filename="Monsters/darkmantle.png")
        await message.channel.send("Monsters/darkmantle.png", file=file)

    elif message.content.startswith('death_knight'):
        file = discord.File("Monsters/death_knight.png", filename="Monsters/death_knight.png")
        await message.channel.send("Monsters/death_knight.png", file=file)

    elif message.content.startswith('demilich'):
        file = discord.File("Monsters/demilich-1.png", filename="Monsters/demilich-1.png")
        await message.channel.send("Monsters/demilich-1.png", file=file)
        file = discord.File("Monsters/demilich-2.png", filename="Monsters/demilich-2.png")
        await message.channel.send("Monsters/demilich-2.png", file=file)

    elif message.content.startswith('demons_info'):
        file = discord.File("Monsters/demons_info-1.png", filename="Monsters/demons_info-1.png")
        await message.channel.send("Monsters/demons_info-1.png", file=file)
        file = discord.File("Monsters/demons_info-2.png", filename="Monsters/demons_info-2.png")
        await message.channel.send("Monsters/demons_info-2.png", file=file)
        file = discord.File("Monsters/demons_info-3.png", filename="Monsters/demons_info-3.png")
        await message.channel.send("Monsters/demons_info-3.png", file=file)
        file = discord.File("Monsters/demons_info-4.png", filename="Monsters/demons_info-4.png")
        await message.channel.send("Monsters/demons_info-4.png", file=file)
        file = discord.File("Monsters/demons_info-5.png", filename="Monsters/demons_info-5.png")
        await message.channel.send("Monsters/demons_info-5.png", file=file)

    elif message.content.startswith('balor'):
        file = discord.File("Monsters/balor.png", filename="Monsters/balor.png")
        await message.channel.send("Monsters/balor.png", file=file)

    elif message.content.startswith('barlgura'):
        file = discord.File("Monsters/barlgura.png", filename="Monsters/barlgura.png")
        await message.channel.send("Monsters/barlgura.png", file=file)

    elif message.content.startswith('chasme'):
        file = discord.File("Monsters/chasme.png", filename="Monsters/chasme.png")
        await message.channel.send("Monsters/chasme.png", file=file)

    elif message.content.startswith('dretch'):
        file = discord.File("Monsters/dretch.png", filename="Monsters/dretch.png")
        await message.channel.send("Monsters/dretch.png", file=file)

    elif message.content.startswith('devils_info'):
        file = discord.File("Monsters/devils_info_1.png", filename="Monsters/devils_info_1.png")
        await message.channel.send("Monsters/devils_info_1.png", file=file)
        file = discord.File("Monsters/devils_info_2.png", filename="Monsters/devils_info_2.png")
        await message.channel.send("Monsters/devils_info_2.png", file=file)
        file = discord.File("Monsters/devils_info_3.png", filename="Monsters/devils_info_3.png")
        await message.channel.send("Monsters/devils_info_3.png", file=file)
        file = discord.File("Monsters/devils_info_4.png", filename="Monsters/devils_info_4.png")
        await message.channel.send("Monsters/devils_info_4.png", file=file)

    elif message.content.startswith('barbed_devil'):
        file = discord.File("Monsters/barbed_devil_1.png", filename="Monsters/barbed_devil_1.png")
        await message.channel.send("Monsters/barbed_devil_1.png", file=file)
        file = discord.File("Monsters/barbed_devil_2.png", filename="Monsters/barbed_devil_2.png")
        await message.channel.send("Monsters/barbed_devil_2.png", file=file)

    elif message.content.startswith('bearded_devil'):
        file = discord.File("Monsters/bearded_devil_1.png", filename="Monsters/bearded_devil_1.png")
        await message.channel.send("Monsters/bearded_devil_1.png", file=file)
        file = discord.File("Monsters/bearded_devil_2.png", filename="Monsters/bearded_devil_2.png")
        await message.channel.send("Monsters/bearded_devil_2.png", file=file)

    elif message.content.startswith('bone_devil'):
        file = discord.File("Monsters/bone_devil_1.png", filename="Monsters/bone_devil_1.png")
        await message.channel.send("Monsters/bone_devil_1.png", file=file)
        file = discord.File("Monsters/bone_devil_2.png", filename="Monsters/bone_devil_2.png")
        await message.channel.send("Monsters/bone_devil_2.png", file=file)

    elif message.content.startswith('chain_devil'):
        file = discord.File("Monsters/chain_devil_1.png", filename="Monsters/chain_devil_1.png")
        await message.channel.send("Monsters/chain_devil_1.png", file=file)
        file = discord.File("Monsters/chain_devil_2.png", filename="Monsters/chain_devil_2.png")
        await message.channel.send("Monsters/chain_devil_2.png", file=file)

    elif message.content.startswith('erinyes'):
        file = discord.File("Monsters/erinyes_1.png", filename="Monsters/erinyes_1.png")
        await message.channel.send("Monsters/erinyes_1.png", file=file)
        file = discord.File("Monsters/erinyes_2.png", filename="Monsters_erinyes_2.png")
        await message.channel.send("Monsters/erinyes_2.png", file=file)

    elif message.content.startswith('horned_devil'):
        file = discord.File("Monsters/horned_devil_1.png", filename="Monsters/horned_devil_1.png")
        await message.channel.send("Monsters/horned_devil_1.png", file=file)
        file = discord.File("Monsters/horned_devil_2.png", filename="Monsters/horned_devil_2.png")
        await message.channel.send("Monsters/horned_devil_2.png", file=file)

    elif message.content.startswith('ice_devil'):
        file = discord.File("Monsters/ice_devil_1.png", filename="Monsters/ice_devil_1.png")
        await message.channel.send("Monsters/ice_devil_1.png", file=file)
        file = discord.File("Monsters/ice_devil_2.png", filename="Monsters/ice_devil_2.png")
        await message.channel.send("Monsters/ice_devil_2.png", file=file)

    elif message.content.startswith('imp'):
        file = discord.File("Monsters/imp_1.png", filename="Monsters/imp1.png")
        await message.channel.send("Monsters/imp_1.png", file=file)
        file = discord.File("Monsters/imp_2.png", filename="Monsters/imp_2.png")
        await message.channel.send("Monsters/imp_2.png", file=file)

    elif message.content.startswith('lemure'):
        file = discord.File("Monsters/lemure_1.png", filename="Monsters/lemure_1.png")
        await message.channel.send("Monsters/lemure_1.png", file=file)
        file = discord.File("Monsters/lemure_2.png", filename="Monsters/lemure_2.png")
        await message.channel.send("Monsters/lemure_2.png", file=file)

    elif message.content.startswith('pit_fiend'):
        file = discord.File("Monsters/pit_fiend_1.png", filename="Monsters/pit_fiend_1.png")
        await message.channel.send("Monsters/pit_fiend_1.png", file=file)
        file = discord.File("Monsters/pit_fiend_2.png", filename="Monsters/pit_fiend_2.png")
        await message.channel.send("Monsters/pit_fiend_2.png", file=file)

    elif message.content.startswith('spined_devil'):
        file = discord.File("Monsters/spined_devil_1.png", filename="Monsters/spined_devil_1.png")
        await message.channel.send("Monsters/spined_devil_1.png", file=file)
        file = discord.File("Monsters/spined_devil_2.png", filename="Monsters/spined_devil_2.png")
        await message.channel.send("Monsters/spined_devil_2.png", file=file)

    elif message.content.startswith('allosaurus'):
        file = discord.File("Monsters/allosaurus.png", filename="Monsters/allosaurus.png")
        await message.channel.send("Monsters/allosaurus.png", file=file)

    elif message.content.startswith('ankylosaurus'):
        file = discord.File("Monsters/ankylosaurus.png", filename="Monsters/ankylosaurus.png")
        await message.channel.send("Monsters/ankylosaurus.png", file=file)

    elif message.content.startswith('pleiosaurus'):
        file = discord.File("Monsters/pleiosaurus.png", filename="Monsters/pleiosaurus.png")
        await message.channel.send("Monsters/pleiosaurus.png", file=file)

    elif message.content.startswith('pteranodon'):
        file = discord.File("Monsters/pteranodon.png", filename="Monsters/pteranodon.png")
        await message.channel.send("Monsters/pteranodon.png", file=file)

    elif message.content.startswith('triceratops'):
        file = discord.File("Monsters/triceratops.png", filename="Monsters/triceratops.png")
        await message.channel.send("Monsters/triceratops.png", file=file)

    elif message.content.startswith('tyrannosaurus_rex'):
        file = discord.File("Monsters/tyrannosaurus_rex.png", filename="Monsters/tyrannosaurus_rex.png")
        await message.channel.send("Monsters/tyrannosaurus_rex.png", file=file)

    elif message.content.startswith('displacer_beast'):
        file = discord.File("Monsters/displacer_beast.png", filename="Monsters/displacer_beast.png")
        await message.channel.send("Monsters/displacer_beast.png", file=file)

    elif message.content.startswith('doppleganger'):
        file = discord.File("Monsters/doppleganger.png", filename="Monsters/doppleganger.png")
        await message.channel.send("Monsters/doppleganger.png", file=file)

    elif message.content.startswith('dracolich'):
        file = discord.File("Monsters/dracolich_1.png", filename="Monsters/dracolich_1.png")
        await message.channel.send("Monsters/dracolich_1.png", file=file)
        file = discord.File("Monsters/dracolich_2.png", filename="Monsters/dracolich_2.png")
        await message.channel.send("Monsters/dracolich_2.png", file=file)

    elif message.content.startswith('dragons'):
        file = discord.File("Monsters/dragons.png", filename="Monsters/dragons.png")
        await message.channel.send("Monsters/dragons.png", file=file)

    elif message.content.startswith('shadow_dragons'):
        file = discord.File("Monsters/shadow_dragons_1.png", filename="Monsters/shadow_dragons_1.png")
        await message.channel.send("Monsters/shadow_dragons_1.png", file=file)
        file = discord.File("Monsters/shadow_dragons_2.png", filename="Monsters/shadow_dragons_2.png")
        await message.channel.send("Monsters/shadow_dragons_2.png", file=file)

    elif message.content.startswith('black_dragon'):
        file = discord.File("Monsters/black_dragon.png", filename="Monsters/black_dragon.png")
        await message.channel.send("Monsters/black_dragon.png", file=file)

    elif message.content.startswith('ancient_black_dragon'):
        file = discord.File("Monsters/ancient_black_dragon.png", filename="Monsters/ancient_black_dragon.png")
        await message.channel.send("Monsters/ancient_black_dragon.png", file=file)
        file = discord.File("Monsters/black_dragon.png", filename="Monsters/black_dragon.png")
        await message.channel.send("Monsters/black_dragon.png", file=file)

    elif message.content.startswith('adult_black_dragon'):
        file = discord.File("Monsters/adult_black_dragon.png", filename="Monsters/adult_black_dragon.png")
        await message.channel.send("Monsters/adult_black_dragon.png", file=file)
        file = discord.File("Monsters/black_dragon.png", filename="Monsters/black_dragon.png")
        await message.channel.send("Monsters/black_dragon.png", file=file)

    elif message.content.startswith('young_black_dragon'):
        file = discord.File("Monsters/young_black_dragon.png", filename="Monsters/young_black_dragon.png")
        await message.channel.send("Monsters/young_black_dragon.png", file=file)
        file = discord.File("Monsters/black_dragon.png", filename="Monsters/black_dragon.png")
        await message.channel.send("Monsters/black_dragon.png", file=file)

    elif message.content.startswith('black_dragon_wyrmling'):
        file = discord.File("Monsters/black_dragon_wyrmling.png", filename="Monsters/black_dragon_wyrmling.png")
        await message.channel.send("Monsters/black_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/black_dragon.png", filename="Monsters/black_dragon.png")
        await message.channel.send("Monsters/black_dragon.png", file=file)

    elif message.content.startswith('blue_dragon'):
        file = discord.File("Monsters/blue_dragon.png", filename="Monsters/blue_dragon.png")
        await message.channel.send("Monsters/blue_dragon.png", file=file)

    elif message.content.startswith('ancient_blue_dragon'):
        file = discord.File("Monsters/ancient_blue_dragon.png", filename="Monsters/ancient_blue_dragon.png")
        await message.channel.send("Monsters/ancient_blue_dragon.png", file=file)
        file = discord.File("Monsters/blue_dragon.png", filename="Monsters/blue_dragon.png")
        await message.channel.send("Monsters/blue_dragon.png", file=file)

    elif message.content.startswith('adult_blue_dragon'):
        file = discord.File("Monsters/adult_blue_dragon.png", filename="Monsters/adult_blue_dragon.png")
        await message.channel.send("Monsters/adult_blue_dragon.png", file=file)
        file = discord.File("Monsters/blue_dragon.png", filename="Monsters/blue_dragon.png")
        await message.channel.send("Monsters/blue_dragon.png", file=file)

    elif message.content.startswith('young_blue_dragon'):
        file = discord.File("Monsters/young_blue_dragon.png", filename="Monsters/young_blue_dragon.png")
        await message.channel.send("Monsters/young_blue_dragon.png", file=file)
        file = discord.File("Monsters/blue_dragon.png", filename="Monsters/blue_dragon.png")
        await message.channel.send("Monsters/blue_dragon.png", file=file)

    elif message.content.startswith('blue_dragon_wyrmling'):
        file = discord.File("Monsters/blue_dragon_wyrmling.png", filename="Monsters/blue_dragon_wyrmling.png")
        await message.channel.send("Monsters/blue_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/blue_dragon.png", filename="Monsters/blue_dragon.png")
        await message.channel.send("Monsters/blue_dragon.png", file=file)

    elif message.content.startswith('green_dragon'):
        file = discord.File("Monsters/green_dragon1.png", filename="Monsters/green_dragon1.png")
        await message.channel.send("Monsters/green_dragon1.png", file=file)
        file = discord.File("Monsters/green_dragon2.png", filename="Monsters/green_dragon2.png")
        await message.channel.send("Monsters/green_dragon2.png", file=file)

    elif message.content.startswith('ancient_green_dragon'):
        file = discord.File("Monsters/ancient_green_dragon.png", filename="Monsters/ancient_green_dragon.png")
        await message.channel.send("Monsters/ancient_green_dragon.png", file=file)
        file = discord.File("Monsters/green_dragon1.png", filename="Monsters/green_dragon1.png")
        await message.channel.send("Monsters/green_dragon1.png", file=file)
        file = discord.File("Monsters/green_dragon2.png", filename="Monsters/green_dragon2.png")
        await message.channel.send("Monsters/green_dragon2.png", file=file)

    elif message.content.startswith('adult_green_dragon'):
        file = discord.File("Monsters/adult_green_dragon.png", filename="Monsters/adult_green_dragon.png")
        await message.channel.send("Monsters/adult_green_dragon.png", file=file)
        file = discord.File("Monsters/green_dragon1.png", filename="Monsters/green_dragon1.png")
        await message.channel.send("Monsters/green_dragon1.png", file=file)
        file = discord.File("Monsters/green_dragon2.png", filename="Monsters/green_dragon2.png")
        await message.channel.send("Monsters/green_dragon2.png", file=file)

    elif message.content.startswith('young_green_dragon'):
        file = discord.File("Monsters/young_green_dragon.png", filename="Monsters/young_green_dragon.png")
        await message.channel.send("Monsters/young_green_dragon.png", file=file)
        file = discord.File("Monsters/green_dragon1.png", filename="Monsters/green_dragon1.png")
        await message.channel.send("Monsters/green_dragon1.png", file=file)
        file = discord.File("Monsters/green_dragon2.png", filename="Monsters/green_dragon2.png")
        await message.channel.send("Monsters/green_dragon2.png", file=file)

    elif message.content.startswith('green_dragon_wyrmling'):
        file = discord.File("Monsters/green_dragon_wyrmling.png", filename="Monsters/green_dragon_wyrmling.png")
        await message.channel.send("Monsters/green_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/green_dragon1.png", filename="Monsters/green_dragon1.png")
        await message.channel.send("Monsters/green_dragon1.png", file=file)
        file = discord.File("Monsters/green_dragon2.png", filename="Monsters/green_dragon2.png")
        await message.channel.send("Monsters/green_dragon2.png", file=file)

    elif message.content.startswith('brass_dragon'):
        file = discord.File("Monstes/brass_dragon.png", filename="Monsters/brass_dragon.png")
        await message.channel.send("Monsters/brass_dragon.png", file=file)

    elif message.content.startswith('adult_brass_dragon'):
        file = discord.File("Monsters/adult_brass_dragon.png", filename="Monsters/adult_brass_dragon.png")
        await message.channel.send("Monsters/adult_brass_dragon.png", file=file)
        file = discord.File("Monsters/brass_dragon.png", filename="Monsters/brass_dragon.png")
        await message.channel.send("Monsters/brass_dragon.png", file=file)

    elif message.content.startswith('bronze_dragon'):
        file = discord.File("Monsters/bronze_dragon.png", filename="Monsters/bronze_dragon.png")
        await message.channel.send("Monsters/bronze_dragon.png", file=file)

    elif message.content.startswith('adult_bronze_dragon'):
        file = discord.File("Monsters/adult_bronze_dragon.png", filename="Monsters/adult_bronze_dragon.png")
        await message.channel.send("Monsters/adult_bronze_dragon.png", file=file)
        file = discord.File("Monsters/bronze_dragon.png", filename="Monsters/bronze_dragon.png")
        await message.channel.send("Monsters/bronze_dragon.png", file=file)

    elif message.content.startswith('copper_dragon'):
        file = discord.File("Monsters/copper_dragon.png", filename="Monsters/copper_dragon.png")
        await message.channel.send("Monsters/copper_dragon.png", file=file)

    elif message.content.startswith('adult_copper_dragon'):
        file = discord.File("Monsters/adult_copper_dragon.png", filename="Monsters/adult_copper_dragon.png")
        await message.channel.send("Monsters/adult_copper_dragon.png", file=file)
        file = discord.File("Monsters/copper_dragon.png", filename="Monsters/copper_dragon.png")
        await message.channel.send("Monsters/copper_dragon.png", file=file)

    elif message.content.startswith('red_dragon'):
        file = discord.File("Monsters/red_dragon.png", filename="Monsters/red_dragon.png")
        await message.channel.send("Monsters/red_dragon.png", file=file)

    elif message.content.startswith('adult_red_dragon'):
        file = discord.File("Monsters/adult_brass_red.png", filename="Monsters/adult_red_dragon.png")
        await message.channel.send("Monsters/adult_red_dragon.png", file=file)
        file = discord.File("Monsters/red_dragon.png", filename="Monsters/red_dragon.png")
        await message.channel.send("Monsters/red_dragon.png", file=file)

    elif message.content.startswith('white_dragon'):
        file = discord.File("Monsters/white_dragon_1.png", filename="Monsters/white_dragon_1.png")
        await message.channel.send("Monsters/white_dragon_1.png", file=file)
        file = discord.File("Monsters/white_dragon_2.png", filename="Monsters/white_dragon_2.png")
        await message.channel.send("Monsters/white_dragon_2.png", file=file)

    elif message.content.startswith('adult_white_dragon'):
        file = discord.File("Monsters/adult_white_dragon.png", filename="Monsters/adult_white_dragon.png")
        await message.channel.send("Monsters/adult_white_dragon.png", file=file)
        file = discord.File("Monsters/white_dragon_1.png", filename="Monsters/white_dragon_1.png")
        await message.channel.send("Monsters/white_dragon_1.png", file=file)
        file = discord.File("Monsters/white_dragon_2.png", filename="Monsters/white_dragon_2.png")
        await message.channel.send("Monsters/white_dragon_2.png", file=file)

    elif message.content.startswith('ancient_brass_dragon'):
        file = discord.File("Monsters/ancient_brass_dragon.png", filename="Monsters/ancient_brass_dragon.png")
        await message.channel.send("Monsters/ancient_brass_dragon.png", file=file)
        file = discord.File("Monstes/brass_dragon.png", filename="Monsters/brass_dragon.png")
        await message.channel.send("Monsters/brass_dragon.png", file=file)

    elif message.content.startswith('ancient_bronze_dragon'):
        file = discord.File("Monsters/ancient_bronze_dragon.png", filename="Monsters/ancient_bronze_dragon.png")
        await message.channel.send("Monsters/ancient_bronze_dragon.png", file=file)
        file = discord.File("Monsters/bronze_dragon.png", filename="Monsters/bronze_dragon.png")
        await message.channel.send("Monsters/bronze_dragon.png", file=file)

    elif message.content.startswith('ancient_copper_dragon'):
        file = discord.File("Monsters/ancient_copper_dragon.png", filename="Monsters/ancient_copper_dragon.png")
        await message.channel.send("Monsters/ancient_copper_dragon.png", file=file)
        file = discord.File("Monsters/copper_dragon.png", filename="Monsters/copper_dragon.png")
        await message.channel.send("Monsters/copper_dragon.png", file=file)

    elif message.content.startswith('ancient_red_dragon'):
        file = discord.File("Monsters/ancient_red_dragon.png", filename="Monsters/ancient_red_dragon.png")
        await message.channel.send("Monsters/ancient_red_dragon.png", file=file)
        file = discord.File("Monsters/red_dragon.png", filename="Monsters/red_dragon.png")
        await message.channel.send("Monsters/red_dragon.png", file=file)

    elif message.content.startswith('ancient_white_dragon'):
        file = discord.File("Monsters/ancient_white_dragon.png", filename="Monsters/ancient_white_dragon.png")
        await message.channel.send("Monsters/ancient_white_dragon.png", file=file)
        file = discord.File("Monsters/white_dragon_1.png", filename="Monsters/white_dragon_1.png")
        await message.channel.send("Monsters/white_dragon_1.png", file=file)
        file = discord.File("Monsters/white_dragon_2.png", filename="Monsters/white_dragon_2.png")
        await message.channel.send("Monsters/white_dragon_2.png", file=file)

    elif message.content.startswith('brass_dragon_wyrmling'):
        file = discord.File("Monsters/brass_dragon_wyrmling.png", filename="Monsters/brass_dragon_wyrmling.png")
        await message.channel.send("Monsters/brass_dragon_wyrmling.png", file=file)
        file = discord.File("Monstes/brass_dragon.png", filename="Monsters/brass_dragon.png")
        await message.channel.send("Monsters/brass_dragon.png", file=file)

    elif message.content.startswith('bronze_dragon_wyrmling'):
        file = discord.File("Monsters/bronze_dragon_wyrmling.png", filename="Monsters/bronze_dragon_wyrmling.png")
        await message.channel.send("Monsters/bronze_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/bronze_dragon.png", filename="Monsters/bronze_dragon.png")
        await message.channel.send("Monsters/bronze_dragon.png", file=file)

    elif message.content.startswith('copper_dragon_wyrmling'):
        file = discord.File("Monsters/copper_dragon_wyrmling.png", filename="Monsters/copper_dragon_wyrmling.png")
        await message.channel.send("Monsters/copper_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/copper_dragon.png", filename="Monsters/copper_dragon.png")
        await message.channel.send("Monsters/copper_dragon.png", file=file)

    elif message.content.startswith('red_dragon_wyrmling'):
        file = discord.File("Monsters/red_dragon_wyrmling.png", filename="Monsters/red_dragon_wyrmling.png")
        await message.channel.send("Monsters/red_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/red_dragon.png", filename="Monsters/red_dragon.png")
        await message.channel.send("Monsters/red_dragon.png", file=file)

    elif message.content.startswith('white_dragon_wyrmling'):
        file = discord.File("Monsters/white_dragon_wyrmling.png", filename="Monsters/white_dragon_wyrmling.png")
        await message.channel.send("Monsters/white_dragon_wyrmling.png", file=file)
        file = discord.File("Monsters/white_dragon_1.png", filename="Monsters/white_dragon_1.png")
        await message.channel.send("Monsters/white_dragon_1.png", file=file)
        file = discord.File("Monsters/white_dragon_2.png", filename="Monsters/white_dragon_2.png")
        await message.channel.send("Monsters/white_dragon_2.png", file=file)

    elif message.content.startswith('young_brass_dragon'):
        file = discord.File("Monsters/young_brass_dragon/png", filename="Monsters/young_brass_dragon.png")
        await message.channel.send("Monsters/young_brass_dragon.png", file=file)
        file = discord.File("Monstes/brass_dragon.png", filename="Monsters/brass_dragon.png")
        await message.channel.send("Monsters/brass_dragon.png", file=file)

    elif message.content.startswith('young_bronze_dragon'):
        file = discord.File("Monsters/young_bronze_dragon.png", filename="Monsters/young_bronze_dragon.png")
        await message.channel.send("Monsters/young_bronze_dragon.png", file=file)
        file = discord.File("Monsters/bronze_dragon.png", filename="Monsters/bronze_dragon.png")
        await message.channel.send("Monsters/bronze_dragon.png", file=file)

    elif message.content.startswith('young_copper_dragon'):
        file = discord.File("Monsters/young_copper_dragon.png", filename="Monsters/young_bronze_dragon.png")
        await message.channel.send("Monsters/young_copper_dragon.png", file=file)
        file = discord.File("Monsters/copper_dragon.png", filename="Monsters/copper_dragon.png")
        await message.channel.send("Monsters/copper_dragon.png", file=file)

    elif message.content.startswith('young_red_dragon'):
        file = discord.File("Monsters/young_red_dragon.png", filename="Monsters/young_red_dragon.png")
        await message.channel.send("Monsters/young_red_dragon.png", file=file)
        file = discord.File("Monsters/red_dragon.png", filename="Monsters/red_dragon.png")
        await message.channel.send("Monsters/red_dragon.png", file=file)

    elif message.content.startswith('young_white_dragon'):
        file = discord.File("Monsters/young_white-dragon.png", filename="Monsters/young_white_dragon.png")
        await message.channel.send("Monsters/young_white_dragon.png", file=file)
        file = discord.File("Monsters/white_dragon_1.png", filename="Monsters/white_dragon_1.png")
        await message.channel.send("Monsters/white_dragon_1.png", file=file)
        file = discord.File("Monsters/white_dragon_2.png", filename="Monsters/white_dragon_2.png")
        await message.channel.send("Monsters/white_dragon_2.png", file=file)

    elif message.content.startswith('elemental'):
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswith('air_elemental'):
        file = discord.File("Monsters/air_elemental.png", filename="Monsters/air_elemental.png")
        await message.channel.send("Monsters/air_elemental.png", file=file)
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswtih('earth_elemental'):
        file = discord.File("Monsters/earth_elemental.png", filename="Monsters/earth_elemental.png")
        await message.channel.send("Monsters/earth_elemental.png", file=file)
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswith('fire_elemental'):
        file = discord.File("Monsters/fire_elemental.png", filename="Monsters/fire_elemental.png")
        await message.channel.send("Monsters/fire_elemental.png", file=file)
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswtih('water_elemental'):
        file = discord.File("Monsters/water_elemental.png", filename="Monsters/water_elemental.png")
        await message.channel.send("Monsters/water_elemental.png", file=file)
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswith('dragon_turtle'):
        file = discord.File("Monsters/dragon_turtle.png", filename="Monsters/dragon_turtle.png")
        await message.channel.send("Monsters/dragon_turtle.png", file=file)

    elif message.content.startswith('drider'):
        file = discord.File("Monsters/drider.png", filename="Monsters/drider.png")
        await message.channel.send("Monsters/drider.png", file=file)

    elif message.content.startswith('dryad'):
        file = discord.File("Monsters/dryad.png", filename="Monsters/dryad.png")
        await message.channel.send("Monsters/dryad.png", file=file)

    elif message.content.startswith('duergar'):
        file = discord.File("Monsters/duergar.png", filename="Monsters/duergar.png")
        await message.channel.send("Monsters/duergar.png", file=file)

    elif message.content.startswith('drow_elves'):
        file = discord.File("Monsters/elves_drow_1.png", filename="Monsters/elves_drow_1.png")
        await message.channel.send("Monsters/elves_drow_1.png", file=file)
        file = discord.File("Monsters/elves_drow_2.png", filename="Monsters/elves_drow_2.png")
        await message.channel.send("Monsters/elves_drow_2.png", file=file)

    elif message.content.startswith('drow'):
        file = discord.File("Monsters/drow.png", filename="Monsters/drow.png")
        await message.channel.send("Monsters/drow.png", file=file)
        file = discord.File("Monsters/elves_drow_1.png", filename="Monsters/elves_drow_1.png")
        await message.channel.send("Monsters/elves_drow_1.png", file=file)
        file = discord.File("Monsters/elves_drow_2.png", filename="Monsters/elves_drow_2.png")
        await message.channel.send("Monsters/elves_drow_2.png", file=file)

    elif message.content.startswith("drow_elite_warrior"):
        file = discord.File("Monsters/drow_elite_warrior.png", filename="Monsters/drow_elite_warrior.png")
        await message.channel.send("Monsters/drow_elite_warrior.png", file=file)
        file = discord.File("Monsters/elves_drow_1.png", filename="Monsters/elves_drow_1.png")
        await message.channel.send("Monsters/elves_drow_1.png", file=file)
        file = discord.File("Monsters/elves_drow_2.png", filename="Monsters/elves_drow_2.png")
        await message.channel.send("Monsters/elves_drow_2.png", file=file)

    elif message.content.startswith('drow_mage'):
        file = discord.File("Monsters/drow_mage.png", filename="Monsters/drow_mage.png")
        await message.channel.send("Monsters/drow_mage.png", file=file)
        file = discord.File("Monsters/elves_drow_1.png", filename="Monsters/elves_drow_1.png")
        await message.channel.send("Monsters/elves_drow_1.png", file=file)
        file = discord.File("Monsters/elves_drow_2.png", filename="Monsters/elves_drow_2.png")
        await message.channel.send("Monsters/elves_drow_2.png", file=file)

    elif message.content.startswith('drow_priestess_of_lolth'):
        file = discord.File("Monsters/drow_priestess_of_lolth.png", filename="Monsters/drow_priestess_of_lolth.png")
        await message.channel.send("Monsters/drow_priestess_of_lolth.png", file=file)
        file = discord.File("Monsters/elves_drow_1.png", filename="Monsters/elves_drow_1.png")
        await message.channel.send("Monsters/elves_drow_1.png", file=file)
        file = discord.File("Monsters/elves_drow_2.png", filename="Monsters/elves_drow_2.png")
        await message.channel.send("Monsters/elves_drow_2.png", file=file)

    elif message.content.startswith('empyrean'):
        file = discord.File("Monsters/empyrean.png", filename="Monsters/empyrean.png")
        await message.channel.send("Monsters/empyrean.png", file=file)

    elif message.content.startswith('ettercap'):
        file = discord.File("Monsters/ettercap.png", filename="Monsters/ettercap.png")
        await message.channel.send("Monsters/ettercap.png", file=file)

    elif message.content.startswith('ettin'):
        file = discord.File("Monsters/ettin.png", filename="Monsters/ettin.png")
        await message.channel.send("Monsters/ettin.png", file=file)

    else:
        await message.channel.send("Please try again!")

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
