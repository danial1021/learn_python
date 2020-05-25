import discord
import settings

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("성공의 정석 집필")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.content == '성공 설명':
        await msg.channel.send('박건도 is 성공')

client.run(settings.token)