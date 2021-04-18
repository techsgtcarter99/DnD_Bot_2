import discord
from random import randint


TOKEN = '-------------------'

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

    elif message.content.startswith('bullywug'):
        file = discord.File("Monsters/Bullywug.png", filename="Monsters/Bullywug.png")
        await message.channel.send("Monsters/Bullywug.png", file=file)

    elif message.content.startswith('cambion'):
        file = discord.File("Monsters/cambion.png", filename="Monsters/cambion.png")
        await message.channel.send("Monsters/cambion.png", file=file)

    elif message.content.startswith('carrioncrawler'):
        file = discord.File("Monsters/carrion_crawler.png", filename="Monsters/carrion_crawler.png")
        await message.channel.send("Monsters/carrion_crawler.png", file=file)

    elif message.content.startswith('centaur'):
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

    elif message.content.startswith('earth_elemental'):
        file = discord.File("Monsters/earth_elemental.png", filename="Monsters/earth_elemental.png")
        await message.channel.send("Monsters/earth_elemental.png", file=file)
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswith('fire_elemental'):
        file = discord.File("Monsters/fire_elemental.png", filename="Monsters/fire_elemental.png")
        await message.channel.send("Monsters/fire_elemental.png", file=file)
        file = discord.File("Monsters/elementals.png", filename="Monsters/elementals.png")
        await message.channel.send("Monsters/elementals.png", file=file)

    elif message.content.startswith('water_elemental'):
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

    elif message.content.startswith('faerie_dragon'):
        file = discord.File("Monsters/faerie_dragon.png", filename="Monsters/faerie_dragon.png")
        await message.channel.send("Monsters/faerie_dragon.png", file=file)

    elif message.content.startswith('flameskull'):
        file = discord.File("Monsters/flameskull.png", filename="Monsters/flameskull.png")
        await message.channel.send("Monsters/flameskull.png", file=file)

    elif message.content.startswith('flumph'):
        file = discord.File("Monsters/flumph.png", filename="Monsters/flumph.png")
        await message.channel.send("Monsters/flumph.png", file=file)

    elif message.content.startswith('fomorian'):
        file = discord.File("Monsters/fomorian.png", filename="Monsters/fomorian.png")
        await message.channel.send("Monsters/fomorian.png", file=file)

    elif message.content.startswith('fungi'):
        file = discord.File("Monsters/fungi.png", filename="Monsters/fungi.png")
        await message.channel.send("Monsters/fungi.png", file=file)

    elif message.content.startswith('shrieker'):
        file = discord.File("Monsters/shrieker.png", filename="Monsters/shrieker.png")
        await message.channel.send("Monsters/shrieker.png", file=file)
        file = discord.File("Monsters/fungi.png", filename="Monsters/fungi.png")
        await message.channel.send("Monsters/fungi.png", file=file)

    elif message.content.startswith('gas_spore'):
        file = discord.File("Monsters/gas_spore.png", filename="Monsters/gas_spore.png")
        await message.channel.send("Monsters/gas_spore.png", file=file)
        file = discord.File("Monsters/fungi.png", filename="Monsters/fungi.png")
        await message.channel.send("Monsters/fungi.png", file=file)

    elif message.content.startswith('violet_fungus'):
        file = discord.File("Monsters/violet_fungus.png", filename="Monsters/violet_fungus.png")
        await message.channel.send("Monsters/violet_fungus.png", file=file)
        file = discord.File("Monsters/fungi.png", filename="Monsters/fungi.png")
        await message.channel.send("Monsters/fungi.png", file=file)

    elif message.content.startswith('galeb_duhr'):
        file = discord.File("Monsters/galeb_duhr.png", filename="Monsters/galeb_duhr.png")
        await message.channel.send("Monsters/galeb_duhr.png", file=file)

    elif message.content.startswith('gargoyle'):
        file = discord.File("Monsters/gargoyle.png", filename="Monsters/gargoyle.png")
        await message.channel.send("Monsters/gargoyle.png", file=file)

    elif message.content.startswith('genie'):
        file = discord.File("Monsters/genies_1.png", filename="Monsters/genies_1.png")
        await message.channel.send("Monsters/genies_1.png", file=file)
        file = discord.File("Monsters/genies_2.png", filename="Monsters/genies_2.png")
        await message.channel.send("Monsters/genies_2.png", file=file)

    elif message.content.startswith('dao'):
        file = discord.File("Monsters/dao.png", filename="Monsters/dao.png")
        await message.channel.send("Monsters/dao.png", file=file)
        file = discord.File("Monsters/genies_1.png", filename="Monsters/genies_1.png")
        await message.channel.send("Monsters/genies_1.png", file=file)
        file = discord.File("Monsters/genies_2.png", filename="Monsters/genies_2.png")
        await message.channel.send("Monsters/genies_2.png", file=file)

    elif message.content.startswith('djinni'):
        file = discord.File("Monsters/djinni.png", filename="Monsters/djinni.png")
        await message.channel.send("Monsters/djinni.png", file=file)
        file = discord.File("Monsters/genies_1.png", filename="Monsters/genies_1.png")
        await message.channel.send("Monsters/genies_1.png", file=file)
        file = discord.File("Monsters/genies_2.png", filename="Monsters/genies_2.png")
        await message.channel.send("Monsters/genies_2.png", file=file)

    elif message.content.startswith('efreeti'):
        file = discord.File("Monsters/efreeti.png", filename="Monsters/efreeti.png")
        await message.channel.send("Monsters/efreeti.png", file=file)
        file = discord.File("Monsters/genies_1.png", filename="Monsters/genies_1.png")
        await message.channel.send("Monsters/genies_1.png", file=file)
        file = discord.File("Monsters/genies_2.png", filename="Monsters/genies_2.png")
        await message.channel.send("Monsters/genies_2.png", file=file)

    elif message.content.startswith('marid'):
        file = discord.File("Monsters/marid.png", filename="Monsters/marid.png")
        await message.channel.send("Monsters/marid.png", file=file)
        file = discord.File("Monsters/genies_1.png", filename="Monsters/genies_1.png")
        await message.channel.send("Monsters/genies_1.png", file=file)
        file = discord.File("Monsters/genies_2.png", filename="Monsters/genies_2.png")
        await message.channel.send("Monsters/genies_2.png", file=file)

    elif message.content.startswith('ghost'):
        file = discord.File("Monsters/ghost.png", filename="Monsters/ghost.png")
        await message.channel.send("Monsters/ghost.png", file=file)

    elif message.content.startswith('ghast'):
        file = discord.File("Monsters/ghast.png", filename="Monsters/ghast.png")
        await message.channel.send("Monsters/ghast.png", file=file)

    elif message.content.startswith('ghoul'):
        file = discord.File("Monsters/ghoul.png", filename="Monsters/ghoul.png")
        await message.channel.send("Monsters/ghoul.png", file=file)

    elif message.content.startswith('giants'):
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('cloud_giants'):
        file = discord.File("Monsters/cloud_giants_1.png", filename="Monsters/cloud_giants_1.png")
        await message.channel.send("Monsters/cloud_giants_1.png", file=file)
        file = discord.File("Monsters/cloud_giants_2.png", filename="Monsters/cloud_giants_2.png")
        await message.channel.send("Monsters/cloud_giants_2.png", file=file)
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('fire_giants'):
        file = discord.File("Monsters/fire_giants_1.png", filename="Monsters'/fire_giants_1.png")
        await message.channel.send("Monsters/fire_giants_1.png", file=file)
        file = discord.File("Monsters/fire_giants_2.png", filename="Monsters'/fire_giants_2.png")
        await message.channel.send("Monsters/fire_giants_2.png", file=file)
        file = discord.File("Monsters/fire_giants_3.png", filename="Monsters'/fire_giants_3.png")
        await message.channel.send("Monsters/fire_giants_3.png", file=file)
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('frost_giants'):
        file = discord.File("Monsters/frost_giants_1.png", filename="Monsters/frost_giants_1.png")
        await message.channel.send("Monsters/fronts_giants_1.png", file=file)
        file = discord.File("Monsters/frost_giants_2.png", filename="Monsters/frost_giants_2.png")
        await message.channel.send("Monsters/fronts_giants_2.png", file=file)
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('hill_giants'):
        file = discord.File("Monsters/hill_giants_1.png", filename="Monsters/hill_giants_1.png")
        await message.channel.send("Monsters/hill_giants_1.png", file=file)
        file = discord.File("Monsters/hill_giants_2.png", filename="Monsters/hill_giants_2.png")
        await message.channel.send("Monsters/hill_giants_2.png", file=file)
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('stone_giants'):
        file = discord.File("Monsters/stone_giants_1.png", filename="Monsters'/stone_giants_1.png")
        await message.channel.send("Monsters/stone_giants_1.png", file=file)
        file = discord.File("Monsters/stone_giants_2.png", filename="Monsters'/stone_giants_2.png")
        await message.channel.send("Monsters/stone_giants_2.png", file=file)
        file = discord.File("Monsters/stone_giants_3.png", filename="Monsters'/stone_giants_3.png")
        await message.channel.send("Monsters/stone_giants_3.png", file=file)
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('storm_giants'):
        file = discord.File("Monsters/storm_giants_1.png", filename="Monsters/storm_giants_1.png")
        await message.channel.send("Monsters/storm_giants_1.png", file=file)
        file = discord.File("Monsters/storm_giants_2.png", filename="Monsters/storm_giants_2.png")
        await message.channel.send("Monsters/storm_giants_2.png", file=file)
        file = discord.File("Monsters/giants_general.png", filename="Monsters/giants_general.png")
        await message.channel.send("Monsters/giants_general.png", file=file)

    elif message.content.startswith('gibbering_mouth'):
        file = discord.File("Monsters/gibbering_mouth.png", filename="Monsters/gibbering_mouth.png")
        await message.channel.send("Monsters/gibbering_mouth.png", file=file)

    elif message.content.startswith('githyanki'):
        file = discord.File("Monsters/githyanki_1.png", filename="Monsters/githyanki_1.png")
        await message.channel.send("Monsters/githyanki_1.png", file=file)
        file = discord.File("Monsters/githyanki_2.png", filename="Monsters/githyanki_2.png")
        await message.cannel.send("Monsters/githyanki_2.png", file=file)

    elif message.content.startswith('githyanki_warrior'):
        file = discord.File("Monsters/githyanki_warrior.png", filename="Monsters/githyanki_warrior.png")
        await message.channel.send("Monsters/githyanki_warrior.png", file=file)
        file = discord.File("Monsters/githyanki_1.png", filename="Monsters/githyanki_1.png")
        await message.channel.send("Monsters/githyanki_1.png", file=file)
        file = discord.File("Monsters/githyanki_2.png", filename="Monsters/githyanki_2.png")
        await message.cannel.send("Monsters/githyanki_2.png", file=file)

    elif message.content.startswith('githyanki_knight'):
        file = discord.File("Monsters/githyanki_knight.png", filename="Monsters/githyanki_knight.png")
        await message.channel.send("Monsters/githyanki_knight.png", file=file)
        file = discord.File("Monsters/githyanki_1.png", filename="Monsters/githyanki_1.png")
        await message.channel.send("Monsters/githyanki_1.png", file=file)
        file = discord.File("Monsters/githyanki_2.png", filename="Monsters/githyanki_2.png")
        await message.cannel.send("Monsters/githyanki_2.png", file=file)

    elif message.content.startswith('githzerai'):
        file = discord.File("Monsters/githzerai.png", filename="Monsters/githzerai.png")
        await message.channel.send("Monsters/githzerai.png", file=file)

    elif message.content.startswith('githzerai_monk'):
        file = discord.File("Monsters/githzerai_monk.png", filename="Monsters/githzerai_monk.png")
        await message.channel.send("Monsters/githzerai_monk.png", file=file)
        file = discord.File("Monsters/githzerai.png", filename="Monsters/githzerai.png")
        await message.channel.send("Monsters/githzerai.png", file=file)

    elif message.content.startswith('githzerai_zerith'):
        file = discord.File("Monsters/githzerai_zerith.png", filename="Monsters/githzerai_zerith.png")
        await message.channel.send("Monsters/githzerai_zerith.png", file=file)
        file = discord.File("Monsters/githzerai.png", filename="Monsters/githzerai.png")
        await message.channel.send("Monsters/githzerai.png", file=file)

    elif message.content.startswith('gnoll'):
        file = discord.File("Monsters/gnoll_1.png", filename="Monsters/gnoll_1.png")
        await message.channel.send("Monsters/gnoll_1.png", file=file)
        file = discord.File("Monsters/gnoll_2.png", filename="Monsters/gnoll_2.png")
        await message.channel.send("Monsters/gnoll_2.png", file=file)

    elif message.content.startswith('gnoll_pack_lord'):
        file = discord.File("Monsters/gnoll_pack_lord_1.png", filename="Monsters/gnoll_pack_lord_1.png")
        await message.channel.send("Monsters/gnoll_pack_lord_1.png", file=file)
        file = discord.File("Monsters/gnoll_pack_lord_2.png", filename="Monsters/gnoll_pack_lord_2.png")
        await message.channel.send("Monsters/gnoll_pack_lord_2.png", file=file)

    elif message.content.startswith('gnoll_fang_of_yeenoghu'):
        file = discord.File("Monsters/gnoll_fang_of_yeenoghu_1.png", filename="Monsters/gnoll_fang_of_yeenoghu_1.png")
        await message.channel.send("Monsters/gnoll_fang_of_yeenoghu_1.png", file=file)
        file = discord.File("Monsters/gnoll_fang_of_yeenoghu_2.png", filename="Monsters/gnoll_fang_of_yeenoghu_2.png")
        await message.channel.send("Monsters/gnoll_fang_of_yeenoghu_2.png", file=file)

    elif message.content.startswith('goblins'):
        file = discord.File("Monsters/goblins.png", filename="Monsters/goblins.png")
        await message.channel.send("Monsters/goblins.png", file=file)

    elif message.content.startswith('goblin'):
        file = discord.File("Monsters/goblin.png", filename="Monsters/goblin.png")
        await message.channel.send("Monsters/goblin.png", file=file)
        file = discord.File("Monsters/goblins.png", filename="Monsters/goblins.png")
        await message.channel.send("Monsters/goblins.png", file=file)

    elif message.content.startswith('goblin_boss'):
        file = discord.File("Monsters/goblin_boss.png", filename="Monsters/goblin_boss.png")
        await message.channel.send("Monsters/goblin_boss.png", file=file)
        file = discord.File("Monsters/goblins.png", filename="Monsters/goblins.png")
        await message.channel.send("Monsters/goblins.png", file=file)

    elif message.content.startswith('golems'):
        file = discord.File("Monsters/golems.png", filename="Monsters/golems.png")
        await message.channel.send("Monsters/golems.png", file=file)

    elif message.content.startswith('clay_golem'):
        file = discord.File("Monsters/clay_golem_1.png", filename="Monsters/clay_golem_1.png")
        await message.channel.send("Monsters/clay_golem_1.png", file=file)
        file = discord.File("Monsters/clay_golem_2.png", filename="Monsters/clay_golem_2.png")
        await message.channel.send("Monsters/clay_golem_2.png", file=file)
        file = discord.File("Monsters/golems.png", filename="Monsters/golems.png")
        await message.channel.send("Monsters/golems.png", file=file)

    elif message.content.startswith('flesh_golem'):
        file = discord.File("Monsters/flesh_golem_1.png", filename="Monsters/flesh_golem_1.png")
        await message.channel.send("Monsters/flesh_golem_1.png", file=file)
        file = discord.File("Monsters/flesh_golem_2.png", filename="Monsters/flesh_golem_2.png")
        await message.channel.send("Monsters/flesh_golem_2.png", file=file)
        file = discord.File("Monsters/golems.png", filename="Monsters/golems.png")
        await message.channel.send("Monsters/golems.png", file=file)

    elif message.content.startswith('iron_golem'):
        file = discord.File("Monsters/iron_golem_1.png", filename="Monsters/iron_golem_1.png")
        await message.channel.send("Monsters/iron_golem_1.png", file=file)
        file = discord.File("Monsters/iron_golem_2.png", filename="Monsters/iron_golem_2.png")
        await message.channel.send("Monsters/iron_golem_2.png", file=file)
        file = discord.File("Monsters/golems.png", filename="Monsters/golems.png")
        await message.channel.send("Monsters/golems.png", file=file)

    elif message.content.startswith('stone_golem'):
        file = discord.File("Monsters/stone_golem_1.png", filename="Monsters/stone_golem_1.png")
        await message.channel.send("Monsters/stone_golem_1.png", file=file)
        file = discord.File("Monsters/stone_golem_2.png", filename="Monsters/stone_golem_2.png")
        await message.channel.send("Monsters/stone_golem_2.png", file=file)
        file = discord.File("Monsters/golems.png", filename="Monsters/golems.png")
        await message.channel.send("Monsters/golems.png", file=file)

    elif message.content.startswith('gorgon'):
        file = discord.File("Monsters/gorgon.png", filename="Monsters/gorgon.png")
        await message.channel.send("Monsters/gorgon.png", file=file)

    elif message.content.startswith('hags'):
        file = discord.File("Monsters/hags.png", filename="Monsters/hags.png")
        await message.channel.send("Monsters/hags.png", file=file)

    elif message.content.startswith('green_hag'):
        file = discord.File("Monsters/green_hag.png", filename="Monsters/green_hag.png")
        await message.channel.send("Monsters/green_hag.png", file=file)
        file = discord.File("Monsters/hags.png", filename="Monsters/hags.png")
        await message.channel.send("Monsters/hags.png", file=file)

    elif message.content.startswith('sea_hag'):
        file = discord.File("Monsters/sea_hag.png", filename="Monsters/sea_hag.png")
        await message.channel.send("Monsters/sea_hag.png", file=file)
        file = discord.File("Monsters/hags.png", filename="Monsters/hags.png")
        await message.channel.send("Monsters/hags.png", file=file)

    elif message.content.startswith('night_hag'):
        file = discord.File("Monsters/night_hag_1.png", filename="Monsters/night_hag_1.png")
        await message.channel.send("Monsters/night_hag_1.png", file=file)
        file = discord.File("Monsters/night_hag_2.png", filename="Monsters/night_hag_2.png")
        await message.channel.send("Monsters/night_hag_2.png", file=file)
        file = discord.File("Monsters/hags.png", filename="Monsters/hags.png")
        await message.channel.send("Monsters/hags.png", file=file)

    elif message.content.startswith('grell'):
        file = discord.File("Monsters/grell.png", filename="Monsters/grell.png")
        await message.channel.send("Monsters/grell.png", file=file)

    elif message.content.startswith('grick'):
        file = discord.File("Monsters/grick.png", filename="Monsters/grick.png")
        await message.channel.send("Monsters/grick.png", file=file)

    elif message.content.startswith('grick_alpha'):
        file = discord.File("Monsters/grick_alpha.png", filename="Monsters/grick_alpha.png")
        await message.channel.send("Monsters'grick_alpha.png", file=file)

    elif message.content.startswith('griffon'):
        file = discord.File("Monsters/griffon.png", filename="Monsters/griffon.png")
        await message.channel.send("Monsters/griffon.png", file=file)

    elif message.content.startswith('grimlock'):
        file = discord.File("Monsters/grimlock.png", filename="Monsters/grimlock.png")
        await message.channel.send("Monsters/grimlock.png", file=file)

    elif message.content.startswith('harpy'):
        file = discord.File("Monsters/harpy.png", filename="Monsters/harpy.png")
        await message.channel.send("Monsters/harpy.png", file=file)

    elif message.content.startswith('hell_hound'):
        file = discord.File("Monsters/hell_hound.png", filename="Monsters/hell_hound.png")
        await message.channel.send("Monsters/hell_hound.png", file=file)

    elif message.content.startswith('helmed_horror'):
        file = discord.File("Monsters/helmed_horror.png", filename="Monsters/helmed_horror.png")
        await message.channel.send("Monsters/helmed_horror.png", file=file)

    elif message.content.startswith('hippogriff'):
        file = discord.File("Monsters/hippogriff.png", filename="Monsters/hippogriff.png")
        await message.channel.send("Monsters/hippogriff.png", file=file)

    elif message.content.startswith('half_dragon'):
        file = discord.File("Monsters/half_dragon.png", filename="Monsters/half_dragon.png")
        await message.channel.send("Monsters/half_dragon.png", file=file)

    elif message.content.startswith('hobgoblins'):
        file = discord.File("Monsters/hobgoblins_1.png", filename="Monsters/hobgoblins_1.png")
        await message.channel.send("Monsters/hobgoblins_1.png", file=file)
        file = discord.File("Monsters/hobgoblins_2.png", filename="Monsters/hobgoblins_2.png")
        await message.channel.send("Monsters/hobgoblins_2.png", file=file)

    elif message.content.startswith('hobgoblin'):
        file = discord.File("Monsters/hobgoblin.png", filename="Monsters/hobgoblin.png")
        await message.channel.send("Monsters/hobgoblin.png", file=file)
        file = discord.File("Monsters/hobgoblins_1.png", filename="Monsters/hobgoblins_1.png")
        await message.channel.send("Monsters/hobgoblins_1.png", file=file)
        file = discord.File("Monsters/hobgoblins_2.png", filename="Monsters/hobgoblins_2.png")
        await message.channel.send("Monsters/hobgoblins_2.png", file=file)

    elif message.content.startswith('hobgoblin_captain'):
        file = discord.File("Monsters/hobgoblin_captain.png", filename="Monsters/hobgoblin_captain.png")
        await message.channel.send("Monsters/hobgoblin_captain.png", file=file)
        file = discord.File("Monsters/hobgoblins_1.png", filename="Monsters/hobgoblins_1.png")
        await message.channel.send("Monsters/hobgoblins_1.png", file=file)
        file = discord.File("Monsters/hobgoblins_2.png", filename="Monsters/hobgoblins_2.png")
        await message.channel.send("Monsters/hobgoblins_2.png", file=file)

    elif message.content.startswith('hobgoblin_warlord'):
        file = discord.File("Monsters/hobgoblin_warlord.png", filename="Monsters/hobgoblin_warlord.png")
        await message.channel.send("Monsters/hobgoblin_warlord.png", file=file)
        file = discord.File("Monsters/hobgoblins_1.png", filename="Monsters/hobgoblins_1.png")
        await message.channel.send("Monsters/hobgoblins_1.png", file=file)
        file = discord.File("Monsters/hobgoblins_2.png", filename="Monsters/hobgoblins_2.png")
        await message.channel.send("Monsters/hobgoblins_2.png", file=file)

    elif message.content.startswith('homunculus'):
        file = discord.File("Monsters/homunculus.png", filename="Monsters/homunculus.png")
        await message.channel.send("Monsters/homunculus.png", file=file)

    elif message.content.startswith('hook_horror'):
        file = discord.File("Monsters/hook_horror.png", filename="Monsters/hook_horror.png")
        await message.channel.send("Monsters/hook_horror.png", file=file)

    elif message.content.startswith('hydra'):
        file = discord.File("Monsters/hydra.png", filename="Monsters/hydra.png")
        await message.channel.send("Monsters/hydra.png", file=file)

    elif message.content.startswith('intellect_devourer'):
        file = discord.File("Monsters/intellect_devourer.png", filename="Monsters/intellect_devourer.png")
        await message.channel.send("Monsters/intellect_devourer.png", file=file)

    elif message.content.startswith('invisible_stalker'):
        file = discord.File("Monsters/invisible_stalker.png", filename="Monsters/invisible_stalker.png")
        await message.channel.send("Monsters/invisible_stalker.png", file=file)

    elif message.content.startswith('jackalwere'):
        file = discord.File("Monsters/jackalwere.png", filename="Monsters/jackalwere.png")
        await message.channel.send("Monsters/jackalwere.png", file=file)

    elif message.content.startswith('kenku'):
        file = discord.File("Monsters/kenku.png", filename="Monsters/kenku.png")
        await message.channel.send("Monsters/kenku.png", file=file)

    elif message.content.startswith('kobold'):
        file = discord.File("Monsters/kobold.png", filename="Monsters/kobold.png")
        await message.channel.send("Monsters/kobold.png", file=file)

    elif message.content.startswith('kuo_toa'):
        file = discord.File("Monsters/kuo_toa.png", filename="Monsters/kuo_toa.png")
        await message.channel.send("Monsters/kuo_toa.png", file=file)
        file = discord.File("Monsters/kuo_toas_1.png", filename="Monsters/kuo_toas_1.png")
        await message.channel.send("Monsters/kuo_toas_1.png", file=file)
        file = discord.File("Monsters/kuo_toas_2.png", filename="Monsters/kuo_toas_2.png")
        await message.channel.send("Monsters/kuo_toas_2.png", file=file)

    elif message.content.startswith('kuo_toas'):
        file = discord.File("Monsters/kuo_toas_1.png", filename="Monsters/kuo_toas_1.png")
        await message.channel.send("Monsters/kuo_toas_1.png", file=file)
        file = discord.File("Monsters/kuo_toas_2.png", filename="Monsters/kuo_toas_2.png")
        await message.channel.send("Monsters/kuo_toas_2.png", file=file)

    elif message.content.startswith('kuo_toa_whip'):
        file = discord.File("Monsters/kuo_toa_whip.png", filename="Monsters/kuo_toa_whip.png")
        await message.channel.send("Monsters/kuo_toa_whip.png", file=file)
        file = discord.File("Monsters/kuo_toas_1.png", filename="Monsters/kuo_toas_1.png")
        await message.channel.send("Monsters/kuo_toas_1.png", file=file)
        file = discord.File("Monsters/kuo_toas_2.png", filename="Monsters/kuo_toas_2.png")
        await message.channel.send("Monsters/kuo_toas_2.png", file=file)

    elif message.content.startswith('kuo_toa_archpriest'):
        file = discord.File("Monsters/kuo_toa_archpries.png", filename="Monsters/kuo_toa_archpriest.png")
        await message.channel.send("Monsters/kuo_toa_archpriest.png", file=file)
        file = discord.File("Monsters/kuo_toas_1.png", filename="Monsters/kuo_toas_1.png")
        await message.channel.send("Monsters/kuo_toas_1.png", file=file)
        file = discord.File("Monsters/kuo_toas_2.png", filename="Monsters/kuo_toas_2.png")
        await message.channel.send("Monsters/kuo_toas_2.png", file=file)

    elif message.content.startswith('kraken'):
        file = discord.File("Monsters/kraken_1.png", filename="Monsters/kraken_1.png")
        await message.channel.send("Monsters/kraken_1.png", file=file)
        file = discord.File("Monsters/kraken_2.png", filename="Monsters/kraken_2.png")
        await message.channel.send("Monsters/kraken_2.png", file=file)

    elif message.content.startswith('lamia'):
        file = discord.File("Monsters/lamia.png", filename="Monsters/lamia.png")
        await message.channel.send("Monsters/lamia.png", file=file)

    elif message.content.startswith('lizardfolk'):
        file = discord.File("Monsters/lizardfolk.png", filename="Monsters/lizardfolk.png")
        await message.channel.send("Monsters/lizardfolk.png", file=file)

    elif message.content.startswith('lizardfolk_king_queen'):
        file = discord.File("Monsters/lizardfolk_king_queen.png", filename="Monsters/lizardfolk_king_queen.png")
        await message.channel.send("Monsters/lizardfolk_king_queen.png", file=file)

    elif message.content.startswith('lizardfolk_shaman'):
        file = discord.File("Monsters/lizardfolk_shaman.png", filename="Monsters/lizardfolk_shaman.png")
        await message.channel.send("Monsters/lizardfolk_shaman.png", file=file)

    elif message.content.startswith('lich'):
        file = discord.File("Monsters/lich_1.png", filename="Monsters/lich_1.png")
        await message.channel.send("Monsters/lich_1.png", file=file)
        file = discord.File("Monsters/lich_2.png", filename="Monsters/lich_2.png")
        await message.channel.send("Monsters/lich_2.png", file=file)

    elif message.content.startswith('lycanthropes'):
        file = discord.File("Monsters/lycanthropes_1.png", filename="Monsters/lycanthropes_1.png")
        await message.channel.send("Monsters/lycanthropes_1.png", file=file)
        file = discord.File("Monsters/lycanthropes_2.png", filename="Monsters/lycanthropes_2.png")
        await message.channel.send("Monsters/lycanthropes_2.png", file=file)

    elif message.content.startswith('werebear'):
        file = discord.File("Monsters/werebear.png", filename="Monsters/werebear.png")
        await message.channel.send("Monsters/werebear.png", file=file)
        file = discord.File("Monsters/lycanthropes_1.png", filename="Monsters/lycanthropes_1.png")
        await message.channel.send("Monsters/lycanthropes_1.png", file=file)
        file = discord.File("Monsters/lycanthropes_2.png", filename="Monsters/lycanthropes_2.png")
        await message.channel.send("Monsters/lycanthropes_2.png", file=file)

    elif message.content.startswith('wererat'):
        file = discord.File("Monsters/wererat.png", filename="Monsters/wererat.png")
        await message.channel.send("Monsters/wererat.png", file=file)
        file = discord.File("Monsters/lycanthropes_1.png", filename="Monsters/lycanthropes_1.png")
        await message.channel.send("Monsters/lycanthropes_1.png", file=file)
        file = discord.File("Monsters/lycanthropes_2.png", filename="Monsters/lycanthropes_2.png")
        await message.channel.send("Monsters/lycanthropes_2.png", file=file)

    elif message.content.startswith('weretiger'):
        file = discord.File("Monsters/weretiger.png", filename="Monsters/weretiger.png")
        await message.channel.send("Monsters/weretiger.png", file=file)
        file = discord.File("Monsters/lycanthropes_1.png", filename="Monsters/lycanthropes_1.png")
        await message.channel.send("Monsters/lycanthropes_1.png", file=file)
        file = discord.File("Monsters/lycanthropes_2.png", filename="Monsters/lycanthropes_2.png")
        await message.channel.send("Monsters/lycanthropes_2.png", file=file)

    elif message.content.startswith('werewolf'):
        file = discord.File("Monsters/werewolf.png", filename="Monsters/werewolf.png")
        await message.channel.send("Monsters/werewolf.png", file=file)
        file = discord.File("Monsters/lycanthropes_1.png", filename="Monsters/lycanthropes_1.png")
        await message.channel.send("Monsters/lycanthropes_1.png", file=file)
        file = discord.File("Monsters/lycanthropes_2.png", filename="Monsters/lycanthropes_2.png")
        await message.channel.send("Monsters/lycanthropes_2.png", file=file)

    elif message.content.startswith('wereboar'):
        file = discord.File("Monsters/wereboar.png", filename="Monsters/wereboar.png")
        await message.channel.send("Monsters/wereboar.png", file=file)
        file = discord.File("Monsters/lycanthropes_1.png", filename="Monsters/lycanthropes_1.png")
        await message.channel.send("Monsters/lycanthropes_1.png", file=file)
        file = discord.File("Monsters/lycanthropes_2.png", filename="Monsters/lycanthropes_2.png")
        await message.channel.send("Monsters/lycanthropes_2.png", file=file)

    elif message.content.startswith('magmin'):
        file = discord.File("Monsters/magmin.png", filename="Monsters/magmin.png")
        await message.channel.send("Monsters/magmin.png", file=file)

    elif message.content.startswith('medusa'):
        file = discord.File("Monsters/medusa.png", filename="Monsters/medusa.png")
        await message.channel.send("Monsters/medusa.png", file=file)

    elif message.content.startswith('manticore'):
        file = discord.File("Monsters/manticore.png", filename="Monsters/manticore.png")
        await message.channel.send("Monsters/manticore.png", file=file)

    elif message.content.startswith('winged_kobold'):
        file = discord.File("Monsters/winged_kobold.png", filename="Monsters/winged_kobold.png")
        await message.channel.send("Monsters/winged_kobold.png", file=file)

    elif message.content.startswith('mephits'):
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('dust_mephit'):
        file = discord.File("Monsters/dust_mephit.png", filename="Monsters/dust_mephit.png")
        await message.channel.send("Monsters/dust_mephit.png", file=file)
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('ice_mephit'):
        file = discord.File("Monsters/ice_mephit.png", filename="Monsters/ice_mephit.png")
        await message.channel.send("Monsters/ice_mephit.png", file=file)
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('mud_mephit'):
        file = discord.File("Monsters/mud_mephit.png", filename="Monsters/mud_mephit.png")
        await message.channel.send("Monsters/mud_mephit.png", file=file)
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('smoke_mephit'):
        file = discord.File("Monsters/smoke_mephit.png", filename="Monsters/smoke_mephit.png")
        await message.channel.send("Monsters/smoke_mephit.png", file=file)
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('steam_mephit'):
        file = discord.File("Monsters/steam_mephit.png", filename="Monsters/steam_mephit.png")
        await message.channel.send("Monsters/steam_mephit.png", file=file)
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('magma_mephit'):
        file = discord.File("Monsters/magma_mephit.png", filename="Monsters/magma_mephit.png")
        await message.channel.send("Monsters/magma_mephit.png", file=file)
        file = discord.File("Monsters/mephits.png", filename="Monsters/mephits.png")
        await message.channel.send("Monsters/mephits.png", file=file)

    elif message.content.startswith('merrow'):
        file = discord.File("Monsters/merrow.png", filename="Monsters/merror.png")
        await message.channel.send("Monsters/merrow.png", file=file)

    elif message.content.startswith('mimic'):
        file = discord.File("Monsters/mimic.png", filename="Monsters/mimic.png")
        await message.channel.send("Monsters/mimic.png", file=file)

    elif message.content.startswith('minotaur'):
        file = discord.File("Monsters/minotaur.png", filename="Monsters/minotaur.png")
        await message.channel.send("Monsters/minotaur.png", file=file)

    elif message.content.startswith('merfolk'):
        file = discord.File("Monsters/merfolk.png", filename="Monsters/merfolk.png")
        await message.channel.send("Monsters/merfolk.png", file=file)

    elif message.content.startswith('mind_flayer'):
        file = discord.File("Monsters/mind_flayer_1.png", filename="Monsters/mind_flayer_1.png")
        await message.channel.send("Monsters/mind_flayer_1.png", file=file)
        file = discord.File("Monsters/mind_flayer_2.png", filename="Monsters/mind_flayer_2.png")
        await message.channel.send("Monsters/mind_flayer_2.png", file=file)

    elif message.content.startswith('modrones'):
        file = discord.File("Monsters/modrones.png", filename="Monsters/modrones.png")
        await message.channel.send("Monsters/modrones.png", file=file)

    elif message.content.startswith('quadrone'):
        file = discord.File("Monsters/quadrone.png", filename="Monsters/quadrone.png")
        await message.channel.send("Monsters/quadrone.png", file=file)

    elif message.content.startswith('duodrone'):
        file = discord.File("Monsters/duodrone.png", filename="Monsters/duodrone.png")
        await message.channel.send("Monsters/duodrone.png", file=file)

    elif message.content.startswith('pentadrone'):
        file = discord.File("Monsters/pentadrone.png", filename="Monsters/pentadrone.png")
        await message.channel.send("Monsters/pentadrone.png", file=file)

    elif message.content.startswith('tridrone'):
        file = discord.File("Monsters/tridrone.png", filename="Monsters/tridrone.png")
        await message.channel.send("Monsters/tridrone.png", file=file)

    elif message.content.startswith('mummies'):
        file = discord.File("Monsters/mummies.png", filename="Monsters/mummies.png")
        await message.channel.send("Monsters/mummies.png", file=file)

    elif message.content.startswith('mummy'):
        file = discord.File("Monsters/mummy.png", filename="Monsters/mummy.png")
        await message.channel.send("Monsters/mummy.png", file=file)

    elif message.content.startswith('mummy_lord'):
        file = discord.File("Monsters/mummy_lord_1.png", filename="Monsters/mummy_lord_1.png")
        await message.channel.send("Monsters/mummy_lord_1.png", file=file)
        file = discord.File("Monsters/mummy_lord_2.png", filename="Monsters/mummy_lord_2.png")
        await message.channel.send("Monsters/mummy_lord_2.png", file=file)
        file = discord.File("Monsters/mummy_lord_3.png", filename="Monsters/mummy_lord_3.png")
        await message.channel.send("Monsters/mummy_lord_3.png", file=file)

    elif message.content.startswith('myconids'):
        file = discord.File("Monsters/myconids_1.png", filename="Monsters/myconids_1.png")
        await message.channel.send("Monsters/myconids_1.png", file=file)
        file = discord.File("Monsters/myconids_2.png", filename="Monsters/myconids_2.png")
        await message.channel.send("Monsters/myconids_2.png", file=file)

    elif message.content.startswith('myconid_sprout'):
        file = discord.File("Monsters/myconid_sprout.png", filename="Monsters/myconid_sprout.png")
        await message.channel.send("Monsters/myconid_sprout.png", file=file)
        file = discord.File("Monsters/myconids_1.png", filename="Monsters/myconids_1.png")
        await message.channel.send("Monsters/myconids_1.png", file=file)
        file = discord.File("Monsters/myconids_2.png", filename="Monsters/myconids_2.png")
        await message.channel.send("Monsters/myconids_2.png", file=file)

    elif message.content.startswith('myconid_adult'):
        file = discord.File("Monsters/myconid_adult.png", filename="Monsters/myconid_adult.png")
        await message.channel.send("Monsters/myconid_adult.png", file=file)
        file = discord.File("Monsters/myconids_1.png", filename="Monsters/myconids_1.png")
        await message.channel.send("Monsters/myconids_1.png", file=file)
        file = discord.File("Monsters/myconids_2.png", filename="Monsters/myconids_2.png")
        await message.channel.send("Monsters/myconids_2.png", file=file)

    elif message.content.startswith('myconid_sovereign'):
        file = discord.File("Monsters/myconid_sovereign.png", filename="Monsters/myconid_sovereign.png")
        await message.channel.send("Monsters/myconid_sovereign.png", file=file)
        file = discord.File("Monsters/myconids_1.png", filename="Monsters/myconids_1.png")
        await message.channel.send("Monsters/myconids_1.png", file=file)
        file = discord.File("Monsters/myconids_2.png", filename="Monsters/myconids_2.png")
        await message.channel.send("Monsters/myconids_2.png", file=file)

    elif message.content.startswith('quaggoth_spore_servant'):
        file = discord.File("Monsters/quaggoth_spore_servant.png", filename="Monsters/quaggoth_spore_servant.png")
        await message.channel.send("Monsters/quaggoth_spore_servant.png", file=file)
        file = discord.File("Monsters/myconids_1.png", filename="Monsters/myconids_1.png")
        await message.channel.send("Monsters/myconids_1.png", file=file)
        file = discord.File("Monsters/myconids_2.png", filename="Monsters/myconids_2.png")
        await message.channel.send("Monsters/myconids_2.png", file=file)

    elif message.content.startswith('nagas'):
        file = discord.File("Monsters/nagas.png", filename="Monsters/nagas.png")
        await message.channel.send("Monsters/nagas.png", file=file)

    elif message.content.startswith('bone_naga'):
        file = discord.File("Monsters/bone_naga.png", filename="Monsters/bone_naga.png")
        await message.channel.send("Monsters/bone_naga.png", file=file)
        file = discord.File("Monsters/nagas.png", filename="Monsters/nagas.png")
        await message.channel.send("Monsters/nagas.png", file=file)

    elif message.content.startswith('spirit_naga'):
        file = discord.File("Monsters/spirit_naga.png", filename="Monsters/spirit_naga.png")
        await message.channel.send("Monsters/spirit_naga.png", file=file)
        file = discord.File("Monsters/nagas.png", filename="Monsters/nagas.png")
        await message.channel.send("Monsters/nagas.png", file=file)

    elif message.content.startswith('guardian_naga'):
        file = discord.File("Monsters/guardian_naga.png", filename="Monsters/guardian_naga.png")
        await message.channel.send("Monsters/guardian_naga.png", file=file)
        file = discord.File("Monsters/nagas.png", filename="Monsters/nagas.png")
        await message.channel.send("Monsters/nagas.png", file=file)

    elif message.content.startswith('nightmare'):
        file = discord.File("Monsters/nightmare.png", filename="Monsters/nightmare.png")
        await message.channel.send("Monsters/nightmare.png", file=file)

    elif message.content.startswith('nothic'):
        file = discord.File("Monsters/nothic.png", filename="Monsters/nothic.png")
        await message.channel.send("Monsters/nothic.png", file=file)

    elif message.content.startswith('oozes'):
        file = discord.File("Monsters/oozes.png", filename="Monsters/oozes.png")
        await message.channel.send("Monsters/oozes.png", file=file)

    elif message.content.startswith('black_pudding'):
        file = discord.File("Monsters/black_pudding.png", filename="Monsters/black_pudding.png")
        await message.channel.send("Monsters/black_pudding.png", file=file)
        file = discord.File("Monsters/oozes.png", filename="Monsters/oozes.png")
        await message.channel.send("Monsters/oozes.png", file=file)

    elif message.content.startswith('gelatinous_cube'):
        file = discord.File("Monsters/gelatinous_cube_1.png", filename="Monsters/gelatinous_cube_1.png")
        await message.channel.send("Monsters/gelatinous_cube_1.png", file=file)
        file = discord.File("Monsters/gelatinous_cube_2.png", filename="Monsters/gelatinous_cube_2.png")
        await message.channel.send("Monsters/gelatinous_cube_2.png", file=file)
        file = discord.File("Monsters/oozes.png", filename="Monsters/oozes.png")
        await message.channel.send("Monsters/oozes.png", file=file)

    elif message.content.startswith('ochre_jelly'):
        file = discord.File("Monsters/ochre_jelly_1.png", filename="Monsters/ochre_jelly_1.png")
        await message.channel.send("Monsters/ochre_jelly_1.png", file=file)
        file = discord.File("Monsters/ochre_jelly_2.png", filename="Monsters/ochre_jelly_2.png")
        await message.channel.send("Monsters/ochre_jelly_2.png", file=file)
        file = discord.File("Monsters/oozes.png", filename="Monsters/oozes.png")
        await message.channel.send("Monsters/oozes.png", file=file)

    elif message.content.startswith('gray_jelly'):
        file = discord.File("Monsters/gray_jelly_1.png", filename="Monsters/gray_jelly_1.png")
        await message.channel.send("Monsters/gray_jelly_1.png", file=file)
        file = discord.File("Monsters/gray_jelly_2.png", filename="Monsters/gray_jelly_2.png")
        await message.channel.send("Monsters/gray_jelly_2.png", file=file)
        file = discord.File("Monsters/oozes.png", filename="Monsters/oozes.png")
        await message.channel.send("Monsters/oozes.png", file=file)

    elif message.content.startswith('ogres'):
        file = discord.File("Monsters/ogres_1.png", filename="Monsters/ogres_1.png")
        await message.channel.send("Monsters/ogres_1.png", file=file)
        file = discord.File("Monsters/ogres_2.png", filename="Monsters/ogres_2.png")
        await message.channel.send("Monsters/ogres_2.png", file=file)

    elif message.content.startswith('half_ogre'):
        file = discord.File("Monsters/half_ogre.png", filename="Monsters/half_ogre.png")
        await message.channel.send("Monsters/half_ogre.png", file=file)
        file = discord.File("Monsters/ogres_1.png", filename="Monsters/ogres_1.png")
        await message.channel.send("Monsters/ogres_1.png", file=file)
        file = discord.File("Monsters/ogres_2.png", filename="Monsters/ogres_2.png")
        await message.channel.send("Monsters/ogres_2.png", file=file)

    elif message.content.startswith('oni'):
        file = discord.File("Monsters/oni.png", filename="Monsters/oni.png")
        await message.channel.send("Monsters/oni.png", file=file)
        
    elif message.content.startswith('orc'):
        file = discord.File("Monsters/orc.png", filename="Monsters/orc.png")
        await message.channel.send("Monsters/orc.png", file=file)
        file = discord.File("Monsters/orcs_1.png", filename="Monsters/orcs_1.png")
        await message.channel.send("Monsters/orcs_1.png", file=file)
        file = discord.File("Monsters/orcs_2.png", filename="Monsters/orcs_2.png")
        await message.channel.send("Monsters/orcs_2.png", file=file)

    elif message.content.startswith('orcs'):
        file = discord.File("Monsters/orcs_1.png", filename="Monsters/orcs_1.png")
        await message.channel.send("Monsters/orcs_1.png", file=file)
        file = discord.File("Monsters/orcs_2.png", filename="Monsters/orcs_2.png")
        await message.channel.send("Monsters/orcs_2.png", file=file)

    elif message.content.startswith('orc_war_chief'):
        file = discord.File("Monsters/orc_war_chief.png", filename="Monsters/orc_war_chief.png")
        await message.channel.send("Monsters/orc_war_chief.png", file=file)
        file = discord.File("Monsters/orcs_1.png", filename="Monsters/orcs_1.png")
        await message.channel.send("Monsters/orcs_1.png", file=file)
        file = discord.File("Monsters/orcs_2.png", filename="Monsters/orcs_2.png")
        await message.channel.send("Monsters/orcs_2.png", file=file)

    elif message.content.startswith('orc_eye_of_gruumsh'):
        file = discord.File("Monsters/orc_eye_of_gruumsh.png", filename="Monsters/orc_eye_of_gruumsh.png")
        await message.channel.send("Mosnters/orc_eye_of_gruumsh.png", file=file)
        file = discord.File("Monsters/orcs_1.png", filename="Monsters/orcs_1.png")
        await message.channel.send("Monsters/orcs_1.png", file=file)
        file = discord.File("Monsters/orcs_2.png", filename="Monsters/orcs_2.png")
        await message.channel.send("Monsters/orcs_2.png", file=file)

    elif message.content.startswith('orog'):
        file = discord.File("Monsters/orog.png", filename="Monsters/orog.png")
        await message.channel.send("Monsters/orog.png", file=file)
        file = discord.File("Monsters/orcs_1.png", filename="Monsters/orcs_1.png")
        await message.channel.send("Monsters/orcs_1.png", file=file)
        file = discord.File("Monsters/orcs_2.png", filename="Monsters/orcs_2.png")
        await message.channel.send("Monsters/orcs_2.png", file=file)

    elif message.content.startswith('otyugh'):
        file = discord.File("Monsters/otyugh.png", filename="Monsters/otyugh.png")
        await message.channel.send("Monsters/otyugh.png", file=file)

    elif message.content.startswith('owlbear'):
        file = discord.File("Monsters/owlbear.png", filename="Monsters/owlbear.png")
        await message.channel.send("Monsters/owlbear.png", file=file)

    elif message.content.startswith('pegasus'):
        file = discord.File("Monsters/pegasus.png", filename="Monsters/pegasus.png")
        await message.channel.send("Monsters/pegasus.png", file=file)

    elif message.content.startswith('peryton'):
        file = discord.File("Monsters/peryton.png", filename="Monsters/peryton.png")
        await message.channel.send("Monsters/peryton.png", file=file)

    elif message.content.startswith('piercer'):
        file = discord.File("Monsters/piercer.png", filename="Monsters/piercer.png")
        await message.channel.send("Monsters/piercequagr.png", file=file)

    elif message.content.startswith('pixie'):
        file = discord.File("Monsters/pixie.png", filename="Monsters/pixie.png")
        await message.channel.send("Monsters/pixie.png", file=file)

    elif message.content.startswith('pseudodragon'):
        file = discord.File("Monsters/pseudodragon.png", filename="Monsters/pseudodragon.png")
        await message.channel.send("Mosnters/pseudodragon.png", file=file)

    elif message.content.startswith('purple_worm'):
        file = discord.File("Monsters/purple_worm.png", filename="Monsters/purple_worm.png")
        await message.channel.send("Monsters/purple_worm.png", file=file)

    elif message.content.startswith('quaggoth'):
        file = discord.File("Monsters/quaggoth.png", filename="Monsters/quaggoth.png")
        await message.channel.send("Monsters/quaggoth.png", file=file)

    elif message.content.startswith('rakshasa'):
        file = discord.File("Monsters/rakshasa.png", filename="Monsters/rakshasa.png")
        await message.channel.send("Monsters/rakshasa.png", file=file)

    elif message.content.startswith('remorhazes'):
        file = discord.File("Monsters/remorhazes.png", filename="Monsters/remorhazes.png")
        await message.channel.send("Monsters/remorhazes.png", file=file)

    elif message.content.startswith('fire_snake'):
        file = discord.File("Monsters/fire_snake.png", filename="Monsters/fire_snake.png")
        await message.channel.send("Monsters/fire_snake.png", file=file)

    elif message.content.startswith('salamanders'):
        file = discord.File("Monsters/salamanders.png", filename="Monsters/salamanders.png")
        await message.channel.send("Monsters/salamanders.png", file=file)

    elif message.content.startswith('salamander'):
        file = discord.File("Monsters/salamander.png", filename="Monsters/salamander.png")
        await message.channel.send("Monsters/slamander.png", file=file)
        file = discord.File("Monsters/salamanders.png", filename="Monsters/salamanders.png")
        await message.channel.send("Monsters/salamanders.png", file=file)

    elif message.content.startswith('sahuagin'):
        file = discord.File("Monsters/sahuagin.png", filename="Monsters/sahuagin.png")
        await message.channel.send("Monsters/sahuagin.png", file=file)

    elif message.content.startswith('sahuagin_baron'):
        file = discord.File("Monsters/sahuagin_baron.png", filename="Monsters/sahuagin_baron.png")
        await message.channel.send("Monsters/sahuagin_baron.png", file=file)
        file = discord.File("Monsters/sahuagin.png", filename="Monsters/sahuagin.png")
        await message.channel.send("Monsters/sahuagin.png", file=file)

    elif message.content.startswith('sahuagin_priestess'):
        file = discord.File("Monsters/sahuagin_priestess.png", filename="Monsters/sahuagin_priestess.png")
        await message.channel.send("Monsters/sahuagin_priestess.png", file=file)
        file = discord.File("Monsters/sahuagin.png", filename="Monsters/sahuagin.png")
        await message.channel.send("Monsters/sahuagin.png", file=file)

    elif message.content.startswith('satyr'):
        file = discord.File("Monsters/satyr.png", filename="Monsters/satyr.png")
        await message.channel.send("Monsters/satyr.png", file=file)

    elif message.content.startswith('shadow'):
        file = discord.File("Monsters/shadow.png", filename="Monsters/shadow.png")
        await message.channel.send("Monsters/shadow.png", file=file)

    elif message.content.startswith('scarecrow'):
        file = discord.File("Monsters/scarecrow.png", filename="Monsters/scarecrow.png")
        await message.channel.send("Monsters/scarecrow.png", file=file)

    elif message.content.startswith('shambling_mound'):
        file = discord.File("Monsters/shambling_mound.png", filename="Monsters/shambling_mound.png")
        await message.channel.send("Monsters/shambling_mound.png", file=file)

    elif message.content.startswith('shield_guardian'):
        file = discord.File("Monsters/shield_guardian.png", filename="Monsters/shield_guardian.png")
        await message.channel.send("Monsters/shield_guardian.png", file=file)

    elif message.content.startswith('skeleton'):
        file = discord.File("Monsters/skeleton.png", filename="Monsters/skeleton.png")
        await message.channel.send("Monsters/skeleton.png", file=file)

    elif message.content.startswith('slaadi'):
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('red_slaad'):
        file = discord.File("Monsters/red_slaad.png", filename="Monsters/red_slaad.png")
        await message.channel.send("Monsters/red_slaad.png", file=file)
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('blue_slaad'):
        file = discord.File("Monsters/blue_slaad.png", filename="Monsters/blue_slaad.png")
        await message.channel.send("Monsters/blue_slaad.png", file=file)
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('grey_slaad'):
        file = discord.File("Monsters/grey_slaad.png", filename="Monsters/grey_slaad.png")
        await message.channel.send("Monsters/grey_slaad.png", file=file)
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('death_slaad'):
        file = discord.File("Monsters/death_slaad.png", filename="Monsters/death_slaad.png")
        await message.channel.send("Monsters/death_slaad.png", file=file)
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('green_slaad'):
        file = discord.File("Monsters/green_slaad.png", filename="Monsters/green_slaad.png")
        await message.channel.send("Monsters/green_slaad.png", file=file)
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('slaad_tadpole'):
        file = discord.File("Monsters/slaad_tadpole.png", filename="Monsters/slaad_tadpole.png")
        await message.channel.send("Monsters/slaad_tadpole.png", file=file)
        file = discord.File("Monsters/slaadi_1.png", filename="Monsters/slaadi_1.png")
        await message.channel.send("Monsters/slaadi_1.png", file=file)
        file = discord.File("Monsters/slaadi_2.png", filename="Monsters/slaadi_2.png")
        await message.channel.send("Monsters/slaadi_2.png", file=file)

    elif message.content.startswith('warhorse_skeleton'):
        file = discord.File("Monsters/warhorse_skeleton.png", filename="Monsters/warhorse_skeleton.png")
        await message.channel.send("Monsters/warhorse_skeleton.png", file=file)

    elif message.content.startswith('minotaur_skeleton'):
        file = discord.File("Monsters/minotaur_skeleton.png", filename="Monsters/minotaur_skeleton.png")
        await message.channel.send("Monsters/minotaur_skeleton.png", file=file)

    elif message.content.startswith('roper'):
        file = discord.File("Monsters/roper.png", filename="Monsters/roper.png")
        await message.channel.send("Monsters/roper.png", file=file)

    elif message.content.startswith('roc'):
        file = discord.File("Monsters/roc.png", filename="Monsters/roc.png")
        await message.channel.send("Monsters/roc.png", file=file)

    elif message.content.startswith('revenant'):
        file = discord.File("Monsters/revenant.png", filename="Monsters/revenant.png")
        await message.channel.send("Monsters/revenant.png", file=file)

    elif message.content.startswith('rust_monster'):
        file = discord.File("Monsters/rust_monster.png", filename="Monsters/rust_monster.png")
        await message.channel.send("Monsters/rust_monster.png", file=file)

    elif message.content.startswith('sphinxes'):
        file = discord.File("Monsters/sphinxes.png", filename="Monsters/sphinxes.png")
        await message.channel.send("Monsters/sphinxes.pnd", file=file)

    elif message.content.startswith('androsphinx'):
        file = discord.File("Monsters/androsphinx.png", filename="Monsters/andropshinx.png")
        await message.channel.send("Monsters/androsphinx.png", file=file)
        file = discord.File("Monsters/sphinxes.png", filename="Monsters/sphinxes.png")
        await message.channel.send("Monsters/sphinxes.pnd", file=file)

    elif message.content.startswith('gynosphinx'):
        file = discord.File("Monsters/gynosphinx.png", filename="Monsters/gynosphinx.png")
        await message.channel.send("Monsters/gynosphinx.png", file=file)
        file = discord.File("Monsters/sphinxes.png", filename="Monsters/sphinxes.png")
        await message.channel.send("Monsters/sphinxes.pnd", file=file)

    elif message.content.startswith('sprite'):
        file = discord.File("Monsters/sprite.png", filename="Monsters/sprite.png")
        await message.channel.send("Monsters/sprite.png", file=file)

    elif message.content.startswith('spectre'):
        file = discord.File("Monsters/spectre.png", filename="Monsters/spectre.png")
        await message.channel.send("Monsters/spectre.png", file=file)

    elif message.content.startswith('succubus'):
        file = discord.File("Monsters/succubus.png", filename="Monsters/succubus.png")
        await message.channel.send("Monsters/succubus.png", file=file)

    elif message.content.startswith('stirge'):
        file = discord.File("Monsters/stirge.png", filename="Monsters/stirgre.png")
        await message.channel.send("Monsters/stirge.png", file=file)

    elif message.content.startswith('incubus'):
        file = discord.File("Monsters/incubus.png", filename="Monsters/incubus.png")
        await message.channel.send("Monsters/incubus.png", file=file)

    elif message.content.startswith('thri_kreen'):
        file = discord.File("Monsters/thri-kreen.png", filename="Monsters/thri-kreen.png")
        await message.channel.send("Monsters/thri-kreen.png", file=file)

    elif message.content.startswith('tarrasque'):
        file = discord.File("Monsters/tarrasque_1.png", filename="Monsters/tarrasque_1.png")
        await message.channel.send("Monsters/tarrasque_1.png", file=file)
        file = discord.File("Monsters/tarrasque_2.png", filename="Monsters/tarrasque_2.png")
        await message.channel.send("Monsters/tarrasque_2.png", file=file)

    elif message.content.startswith('troll'):
        file = discord.File("Monsters/troll.png", filename="Monsters/troll.png")
        await message.channel.send("Monsters/troll.png", file=file)

    elif message.content.startswith('troglodyte'):
        file = discord.File("Monsters/troglodyte.png", filename="Monsters/troglodyte.png")
        await message.channel.send("Monsters/troglodyte.png", file=file)

    elif message.content.startswith('treant'):
        file = discord.File("Monsters/treant.png", filename="Monsters/treant.png")
        await message.channel.send("Monsters/treant.png", file=file)

    elif message.content.startswith('umber_hulk'):
        file = discord.File("Monsters/umber_hulk.png", filename="Monsters/umber_hulk.png")
        await message.channel.send("Monsters/umber_hulk.png", file=file)

    elif message.content.startswith('unicorn'):
        file = discord.File("Monsters/unicorn_1.png", filename="Monsters/unicorn_1.png")
        await message.channel.send("Monsters/unicorn_1.png", file=file)
        file = discord.File("Monsters/unicorn_2.png", filename="Monsters/unicorn_2.png")
        await message.channel.send("Monsters/unicorn_2.png", file=file)

    elif message.content.startswith('vampires'):
        file = discord.File("Monsters/vampires_1.png", filename="Monsters/vampires_1.png")
        await message.channel.send("Monsters/vampires_1.png", file=file)
        file = discord.File("Monsters/vampires_2.png", filename="Monsters/vampires_2.png")
        await message.channel.send("Monsters/vampires_2.png", file=file)

    elif message.content.startswith('vampire'):
        file = discord.File("Monsters/vampire.png", filename="Monsters/vampire.png")
        await message.channel.send("Monsters/vampire.png", file=file)
        file = discord.File("Monsters/vampires_1.png", filename="Monsters/vampires_1.png")
        await message.channel.send("Monsters/vampires_1.png", file=file)
        file = discord.File("Monsters/vampires_2.png", filename="Monsters/vampires_2.png")
        await message.channel.send("Monsters/vampires_2.png", file=file)

    elif message.content.startswith("vampire_spawn"):
        file = discord.File("Monsters/vampire_spawn.png", filename="Monsters/vampire_spawn.png")
        await message.channel.send("Monsters/vampire_spawn.png", file=file)
        file = discord.File("Monsters/vampires_1.png", filename="Monsters/vampires_1.png")
        await message.channel.send("Monsters/vampires_1.png", file=file)
        file = discord.File("Monsters/vampires_2.png", filename="Monsters/vampires_2.png")
        await message.channel.send("Monsters/vampires_2.png", file=file)

    elif message.content.startswith('water_weird'):
        file = discord.File("Monsters/water_weird.png", filename="Monsters/water_weird.png")
        await message.channel.send("Monsters/water_weird.png", file=file)

    elif message.content.startswith('wight'):
        file = discord.File("Monsters/wight.png", filename="Monsters/wight.png")
        await message.channel.send("Monsters/wight.png", file=file)

    elif message.content.startswith('will_o_wisp'):
        file = discord.File("Monsters/will-o'-wisp.png", filename="Monsters/will-o'-wisp.png")
        await message.channel.send("Monsters/will-o'-wisp.png", file=file)

    elif message.content.startswith('wraith'):
        file = discord.File("Monsters/wraith.png", filename="Monsters/wraith.png")
        await message.channel.send("Monsters/wraith.png", file=file)

    elif message.content.startswith('wyvern'):
        file = discord.File("Monsters/wyvern.png", filename="Monsters/wyvern.png")
        await message.channel.send("Monsters/wyvern.png", file=file)

    elif message.content.startswith('xorn'):
        file = discord.File("Monsters/xorn.png", filename="Monsters/xorn.png")
        await message.channel.send("Monsters/xorn.png", file=file)

    elif message.content.startswith('yeti'):
        file = discord.File("Monsters/yeti_1.png", filename="Monsters/yeti_1.png")
        await message.channel.send("Monsters/yeti_1.png", file=file)
        file = discord.File("Monsters/yeti_2.png", filename="Monsters/yeti_2.png")
        await message.channel.send("Monsters/yeti_2.png", file=file)

    elif message.content.startswith('yuan_ti'):
        file = discord.File("Monsters/yuan_ti.png", filename="Monsters/yuan_ti.png")
        await message.channel.send("Monsters/yuan_ti.png", file=file)

    elif message.content.startswith('yuan_ti_abomination'):
        file = discord.File("Monsters/yuan_ti_abomination.png", filename="Monsters/yuan_ti_abomination.png")
        await message.channel.send("Monsters/yuan_ti_abomination.png", file=file)
        file = discord.File("Monsters/yuan_ti.png", filename="Monsters/yuan_ti.png")
        await message.channel.send("Monsters/yuan_ti.png", file=file)

    elif message.content.startswith('yuan_ti_malison'):
        file = discord.File("Monsters/yuan_ti_malison.png", filename="Monsters/yuan_ti_malison.png")
        await message.channel.send("Monsters/yuan_ti_malison.png", file=file)
        file = discord.File("Monsters/yuan_ti.png", filename="Monsters/yuan_ti.png")
        await message.channel.send("Monsters/yuan_ti.png", file=file)

    elif message.content.startswith('yuan_ti_pureblood'):
        file = discord.File("Monsters/yuan_ti_pureblood.png", filename="Monsters/yuan_ti_pureblood.png")
        await message.channel.send("Monsters/yuan_ti_pureblood.png", file=file)
        file = discord.File("Monsters/yuan_ti.png", filename="Monsters/yuan_ti.png")
        await message.channel.send("Monsters/yuan_ti.png", file=file)

    elif message.content.startswith('yugoloths'):
        file = discord.File("Monsters/yugoloths_1.png", filename="Monsters/yugoloths_1.png")
        await message.channel.send("Monsters/yugoloths_1.png", file=file)
        file = discord.File("Monsters/yugoloths_2.png", filename="Monsters/yugoloths_2.png")
        await message.channel.send("Monsters/yugoloths_2.png", file=file)

    elif message.content.startswith('arcanaloth'):
        file = discord.File("Monsters/arcanaloth.png", filename="Monsters/arcanaloth.png")
        await message.channel.send("Monsters/arcanaloth.png", file=file)
        file = discord.File("Monsters/yugoloths_1.png", filename="Monsters/yugoloths_1.png")
        await message.channel.send("Monsters/yugoloths_1.png", file=file)
        file = discord.File("Monsters/yugoloths_2.png", filename="Monsters/yugoloths_2.png")
        await message.channel.send("Monsters/yugoloths_2.png", file=file)

    elif message.content.startswith('nycaloth'):
        file = discord.File("Monsters/nycaloth.png", filename="Monsters/nycaloth.png")
        await message.channel.send("Monsters/nycaloth.png", file=file)
        file = discord.File("Monsters/yugoloths_1.png", filename="Monsters/yugoloths_1.png")
        await message.channel.send("Monsters/yugoloths_1.png", file=file)
        file = discord.File("Monsters/yugoloths_2.png", filename="Monsters/yugoloths_2.png")
        await message.channel.send("Monsters/yugoloths_2.png", file=file)

    elif message.content.startswith('zombies'):
        file = discord.File("Monsters/zombies.png", filename="Monsters/zombies.png")
        await message.channel.send("Monsters/zombies.png", file=file)

    elif message.content.startswith('zombie'):
        file = discord.File("Monsters/zombie.png", filename="Monsters/zombie.png")
        await message.channel.send("Monsters/zombie.png", file=file)
        file = discord.File("Monsters/zombies.png", filename="Monsters/zombies.png")
        await message.channel.send("Monsters/zombies.png", file=file)

    elif message.content.startswith('mezzoloth'):
        file = discord.File("Monsters/mezzoloth.png", filename="Monsters/mezzoloth.png")
        await message.channel.send("Monsters/mezzoloth.png", file=file)
        file = discord.File("Monsters/yugoloths_1.png", filename="Monsters/yugoloths_1.png")
        await message.channel.send("Monsters/yugoloths_1.png", file=file)
        file = discord.File("Monsters/yugoloths_2.png", filename="Monsters/yugoloths_2.png")
        await message.channel.send("Monsters/yugoloths_2.png", file=file)

    elif message.content.startswith('ultroloth'):
        file = discord.File("Monsters/utlroloth.png", filename="Monsters/ultroloth.png")
        await message.channel.send("Monsters/ultroloth.png", file=file)
        file = discord.File("Monsters/yugoloths_1.png", filename="Monsters/yugoloths_1.png")
        await message.channel.send("Monsters/yugoloths_1.png", file=file)
        file = discord.File("Monsters/yugoloths_2.png", filename="Monsters/yugoloths_2.png")
        await message.channel.send("Monsters/yugoloths_2.png", file=file)

    elif message.content.startswith('beholder_zombie'):
        file = discord.File("Monsters/beholder_zombie.png", filename="Monsters/beholder_zombie.png")
        await message.channel.send("Monsters/beholder_zombie.png", file=file)
        file = discord.File("Monsters/zombies.png", filename="Monsters/zombies.png")
        await message.channel.send("Monsters/zombies.png", file=file)

    elif message.content.startswith('ogre_zombie'):
        file = discord.File("Monsters/ogre_zombie.png", filename="Monsters/ogre_zombie.png")
        await message.channel.send("Monsters/ogre_zombie.png", file=file)
        file = discord.File("Monsters/zombies.png", filename="Monsters/zombies.png")
        await message.channel.send("Monsters/zombies.png", file=file)

    # challenge rating 0-4 treasure rolling

    elif message.content.startswith("0-4treasure_roll"):
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

    # 5-10 challenge rating treasure rolling

    elif message.content.startswith("5-10treasure_roll"):
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

        # 11-16 challenge rating treasure rolling

    elif message.content.startswith("11-16treasure_roll"):
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


    # 17+ challenge rating treasure rolling
    elif message.content.startswith("17+treasure_roll"):
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

    # treasure 10gp gemstone rolling

    elif message.content.startswith('10gpgemstones'):
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



        # 50gp treasure rolling

    elif message.content.startswith('50gpgemstones'):
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



    # 100gp gemstones

    elif message.content.startswith('100gpgemstones'):
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



        # 500gp gemstones

    elif message.content.startswith('500gpgemstones'):
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


        # 1000gp gemstones

    elif message.content.startswith('1000gpgemstones'):
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



        # 5000gp gemstones

    elif message.content.startswith('5000gpgemstones'):
        dice_roll = randint(1, 4)

        if dice_roll == 1:
            await message.channel.send("Black sapphire (translucent lustrous black with glowing highlights)")

        elif dice_roll == 2:
            await message.channel.send("Diamond (trasnparent blue-white, canary, pink, brown, or blue)")

        elif dice_roll == 3:
            await message.channel.send("Jacinth (transparent fiery orange)")

        elif dice_roll == 4:
            await message.channel.send("Ruby (transparent clear red to deep crimson)")


        # 25gp art

    elif message.content.startswith('25gpart'):
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


        # 250gp art

    elif message.content.startswith('250gpart'):
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

        # 750gp art

    elif message.content.startswith('750gpart'):
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



            # 2500gp art

    elif message.content.startswith('2500gpart'):
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



        # 7500gp art

    elif message.content.startswith('7500gpart'):
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


        # Magic Item Rarity

    elif message.content.startswith('MIRC'):
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



    # Maps Go Here
    elif message.content.startswith('?planesmap'):
        file = discord.File("Maps/Planes.png", filename="Maps/Planes.png")
        await message.channel.send("Maps/Planes.png", file=file)


    # Dice Rolls

    elif message.content.startswith('1d4'):
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
