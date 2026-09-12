import discord
import random
import requests

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
    elif message.content.startswith('?evening'):
        await message.channel.send("Boa tarde!")
    elif message.content.startswith('?night'):
        await message.channel.send("Boa noite!")
    elif message.content.startswith('?desc'):
            await message.channel.send("Olá! Eu sou um bot de fontes personalizadas para o Discord. No momento, eu ainda estou em desenvolvimento. Logo, eu talvez não entregue sempre os resultados esperados. Caso encontre algum erro ou tenha alguma sugestão ou melhoria, por favor contate através de um dos meios a seguir: Telefone: +55 (46) 98821-6205; E-mail: samuelsieminkoski@gmail.com; Discord: samuelviski.")
    elif message.content.startswith('?compliment'):
        compliment = random.randint(1, 5)
        if compliment == 1:
            await message.channel.send("Você é incrível!")
        elif compliment == 2:
            await message.channel.send("Você é muito inteligente!")
        elif compliment == 3:
            await message.channel.send("Você é muito bonito(a)!")
        elif compliment == 4:
            await message.channel.send("Você é muito talentoso(a)!")
        elif compliment == 5:
            await message.channel.send("Você é muito engraçado(a)!")
    elif message.content.startswith("?joke"):
        joke = random.randint(1, 10)
        if joke == 1:
            await message.channel.send("Por que o livro de matemática se suicidou? Porque ele tinha muitos problemas.")
        elif joke == 2:
            await message.channel.send("Por que o computador foi ao médico? Porque ele estava com um vírus.")
        elif joke == 3:
            await message.channel.send("Havia um pintinho que se chamava Relam. Toda vez que chovia, 'relampiava'")
        elif joke == 4:
            await message.channel.send("Havia dois bolinhos em um forno. Um deles disse: 'Nossa, está quente aqui!'. E o outro respondeu: 'Minha nossa! Um bolinho falante!'")
        elif joke == 5:
            await message.channel.send("Por que, quando a plantinha foi ao méico, ela não foi atendida? Porque lá só tinha médico de plantão!")
        elif joke == 6:
            await message.channel.send("Era uma vez o AB e o C. O C veio e disse: 'Bom dia AB! Como você está?'. Porém, o AB não respondeu. O C tentou de novo e disse: 'AB! Bom dia! Como andam as linhas?'. Mesmo assim o AB não respondeu. O C, irritado, disse: 'Mas que ABsurdo!'")
        elif joke == 7:
            await message.channel.send("Porque o espermatozoide é o pior inquilino? Por que o prédio é um ovo, o vizinho é um cu e, quando o dono fica duro, bota todo mundo pra fora!")
        elif joke == 8:
            await message.channel.send("Por que o pinheiro não se perde na floresta? Porque ele tem uma pinha!")
        elif joke == 9:
            await message.channel.send("Por que o peixe foi para o circo? Porque ele era um peixe-palhaço!")
        elif joke == 10:
            await message.channel.send("Qual o contrário de volátil? Vemcásobrinho!")
    elif message.content.startswith("?suggest_musics"):
        music = random.randint(1, 10)
        if music == 1:
            await message.channel.send("Escuta essa: 'Bohemian Rhapsody' - Queen")
        elif music == 2:
            await message.channel.send("Escuta essa: 'La Bamba' - Los Lobos")
        elif music == 3:
            await message.channel.send("Escuta essa: 'Hotel California' - Eagles")
        elif music == 4:
            await message.channel.send("Escuta essa: 'YMCA' - Village People")
        elif music == 5:
            await message.channel.send("Escuta essa: 'Billie Jean' - Michael Jackson")
        elif music == 6:
            await message.channel.send("Escuta essa: 'Smooth Criminal' - Michael Jackson")
        elif music == 7:
            await message.channel.send("Escuta essa: 'Never Gonna Give You Up' - Rick Astley")
        elif music == 8:
            await message.channel.send("Escuta essa: 'Smells Like Teen Spirit' - Nirvana")
        elif music == 9:
            await message.channel.send("Escuta essa: 'What a Wonderful World' - Louis Armstrong")
        elif music == 10:
            await message.channel.send("Escuta essa: 'Somebody That I Used to Know' - Gotye")

@client.event
async def on_message(message):

    with open('FontBot.jpeg', 'rb') as image:
        image = discord.File(image)
        if message.content.startswith("?profile_image"):
            await message.channel.send("Olha a minha foto de perfil!", file = image)

client.run("SEU TOKEN DE BOT AQUI")
