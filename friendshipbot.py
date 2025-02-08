import discord
from bot_mantik import sifre_olusturucu , yazi_tura

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('!baybay'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('!şifre'):
        await message.channel.send(sifre_olusturucu(10))
    elif message.content.startswith("!yazıtura"):
        await message.channel.send(yazi_tura())
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
