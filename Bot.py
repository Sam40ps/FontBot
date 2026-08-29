import discord
from bot_logic import gen_pass

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('?morning'):
        await message.channel.send("Bom dia!")
    elif message.content.startswith('?font'):
        await message.channel.send("Qual fonte você quer? (Digite '?' + o nome da fonte)")
    elif message.content.startswith('?password'):
        await message.channel.send("Quantos caracteres você quer na senha? (Digite '?' + o número de caracteres)")
        if message.content.startswith('?' + str):
            characters = int(message.content[str - "?"])
            password = gen_pass(characters)
            await message.channel.send("Senha gerada:" + password)

client.run("SEU TOKEN DE BOT AQUI")
