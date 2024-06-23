#await message.channel.send responde a mensagem no canal 
#await message.author.send responde a mensagem no privado
#{os.linesep} quebra de linha 
import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Habilita a intenção de conteúdo de mensagens
intents.members = True

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!regras':
            await message.channel.send(f'{message.author.name} as regras se encontram no canal de {os.getenv('RULES_CHANNEL')}')
        if message.content == '!bom dia':
            await message.channel.send(f'{message.author.name} https://youtu.be/SuZTzUf3zGI?si=JuZZNd2-I19xF1aT')
        if message.content == 'Whisper':
            await message.author.send('Chamou foi piranha?')
        if message.content == '!bailão':
            await message.channel.send('m!play https://youtu.be/3tdS95YcEOc?si=9npqqIlwlDlay4jj')
        if message.content == '!cola fi':
            if message.author.voice:
                channel = message.author.voice.channel 
                vc = await channel.connect()
                print(f'Bot entrou no canal de voz {channel}')
            else:
                await message.channel.send('tu ta num canal de voz man?')   
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de se fuder na vida entrando na {guild.name}'
            await guild.system_channel.send(mensagem)


client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))