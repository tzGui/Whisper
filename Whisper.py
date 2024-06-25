#A linha abaixo importa a biblioteca do Discord.py para interagir com a API do discord
import discord

#Os dois imports abaixo tem a função de carregar e acessar as variaveis de um ambiente
from dotenv import load_dotenv
import os

#carrega as variáveis do arquivo .env
load_dotenv()

#Esta área abaixo está configurando as intenções do Bot, neste caso reagindo a mensagens e eventos de membros
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Define uma classe que herda de discord.Client para criação do bot
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #Método chamado quando o Bot está pronto e conectado
    async def on_ready(self):
        #Com intúito de confirmação da ação acima é imprimida uma imagem no console com o nome do Bot
        print('Logged on as {0}!'.format(self.user))

    #Método chamado quando uma mensagem é recebida
    async def on_message(self, message):
        #Imprime no console a mensagem recebida e seu autor
        print('Message from {0.author}: {0.content}'.format(message))
        
        #Esse bloco de codigo abaixo é responsavel por responder de acordo com a mensagem recebida 
        #A unica coisa que os difere é a possibilidade de o Bot te responder pelo próprio canal onde a mensagem foi enviada ou no seu privado
        #sendo especificado pelas diferenças entre "await message.channel/author.send"
        if message.content == '!regras':
            await message.channel.send(f'{message.author.name} as regras se encontram no canal de {os.getenv('RULES_CHANNEL')}')
        if message.content == '!bom dia':
            await message.channel.send(f'{message.author.name} https://youtu.be/SuZTzUf3zGI?si=JuZZNd2-I19xF1aT')
        if message.content == 'Whisper':
            await message.author.send('Seu Bloco de notas pessoal acabou de chegar')
        
        #Se a mensagem for "!join" e o autor estiver em um canal de voz o bot entrará em tal
        if message.content == '!Join':
            if message.author.voice:
                channel = message.author.voice.channel 
                vc = await channel.connect()
                print(f'estamos logados a{channel}')
            else:
                await message.channel.send('Você precisa estar em um canal de voz')   
    
    #Método chamado quando um novo membro se junta ao servidor
    async def on_member_join(self, member):
        guild = member.guild
        #Envia uma mensagem de boas-vindas no canal do sistema, se disponível
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Acabou de se unir a nós. Seja bem vindo a {guild.name}'
            await guild.system_channel.send(mensagem)

#Cria uma instância do bot com as intenções especificadas
client = MyClient(intents=intents)
#Executa o bot usando o token armazenado nas variáveis de ambiente
client.run(os.getenv('TOKEN'))