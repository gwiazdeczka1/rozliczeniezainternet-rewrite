import discord

intents = discord.Intents.all() #Lol

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'jajoajojoajoajoajoajoajoajo3fffff: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: # useleleseses
        return

    if message.content.startswith('roaming'):
        await message.reply('Rozpoczales transmisje danych w roamingu w Strefie 1 (UE). Za korzystanie z internetu w roamingu naliczymy oplaty 10,24 gr/MB', mention_author=True)
    elif message.content.startswith('wlacz roaming'):
        await message.reply('Rozpoczales transmisje danych w roamingu w Strefie 1 (UE). Za korzystanie z internetu w roamingu naliczymy oplaty 10,24 gr/MB', mention_author=True)
    elif message.content.startswith('wylacz roaming'):
        await message.reply('Rozpoczales transmisje danych w roamingu w Strefie 1 (UE). Za korzystanie z internetu w roamingu naliczymy oplaty 10,24 gr/MB', mention_author=True)

client.run('MTAxOTY3NTEyMDM4MzU3ODE0Mg.GwnB7E._xdYYH5Ux7BBtB55lc6SVPrD00PGRuCrN80Rns') #please do not login to my bot :sob:
