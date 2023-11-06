#Bot code

#imports
import discord #IMportamos la libreria discord
from discord.ext import commands
import random #Importamos la libreria random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url(): #Funcion para poder buscar una foto aleatoria de un pato   
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url(): #Funcion para poder buscar una foto aleatoria de un perro  
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.event #Nos indica si el bot de ha logeado (iniciado) correctamente
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command() #Este es el codigo que hace funcionar el comando "$hello" que cuando los ponemos en el chat nos dice: "Hola, mi nombre es: Smok3.#0879!"
async def hello(ctx):
    await ctx.send(f'Hola, mi nombre es: {bot.user}!')

@bot.command() #Codigo que hace funcionar el comando "$heh", que cuando lo ponemos en el chat nos dice: "hehehehehehe"
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command() #Codigo que hace funcionar el comando "$add", que funciona colocando un espacio despues del "add" y colocando 2 numeros que sumara
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description='For when you wanna settle the score some other way') #Codigo que hace funcionar el comando "choose" que tu puedes usar para que eliga entre 2, 3, 4, o todos los datos que tu quieras. No importa si son letras, o numeros, solo tienes que colocar un espacio entre cada dato que quieres que eliga
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command() #Codigo del comando "$joined" que puedes utilizar mencionando a la persona que quieras saber cuando ingreso al servidor en el que estas poniendo el comando
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} Se metio al servidor el: {discord.utils.format_dt(member.joined_at)}')

@bot.group() #Codigo del comando "$cool" que te dice si el usuario mencionado es cool
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Si, {ctx.subcommand_passed} es cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Si, el bot es cool.')

@bot.command() #Comando "$meme" para enviar un meme al servidor de discord
async def meme(ctx):
    img_name = random.choice(os.listdir("memes"))
    with open(f'memes/{img_name}', 'rb') as f: #En donde dice "memes/{img_name}" le colocas tu direccion de tu carpeta de memes, por ejemplo: Si tu carpeta de memes se llama "mis memes" en donde dice memes en "memes/{img_name}" colocas "mis memes", osea quedaria asi: "mis memes/{img_name}". En "img_name = random.choice(os.listdir("memes"))" en donde dice memes pones el nombre de la carpeta de tus memes
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
 
@bot.command('pato') #Codigo del comando "$pato" que envia a tu servidor de discord una foto totalmente aleatoria de un pato
async def pato(ctx):
    '''Una vez que llamamos al comando pato, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('perro') #Codigo del comando "$perro" que envia a tu servidor de discord una foto totalmente aleatoria de un perro
async def perro(ctx):
    '''Una vez que llamamos al comando perro, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command() #Codigo del comando "$emoji" que envia a tu servidor de discord un emoji totalmente aleatorio
async def emoji(ctx):
    await ctx.send(random.choice(["😀","😎","🤑","🥵","🥶","🤬","🤡","👺","🤓","👻","👽","😺"]))

@bot.command() #Codigo del comando "$amb" que envia a tu servidor de discord un consejo sobre como evitar la contaminacion en el planeta tierra
async def amb(ctx):
    await ctx.send(random.choice(["Un consejo que te puedo dar para poder evitar la contaminacion del planeta seria: No botar chicles en la calle", "Recicla toda la basura que puedas o reutilizarla para fabricar algun objeto o algo por el estilo", "Usa productos que puedan reutilizarse", "Cuando llueva y quieras regar tus plantas, pon una cubeta de agua para recolectar el agua de la lluvia", "Siempre apaga cualquier dispositivo electronico cuando no los estes usando, y tambien apagar las luces que no se esten usando", "Consume productos ecológicos y locales", "Evita dejar los aparatos enchufados", "Cerrar los grifos correctamente para que no corra el agua y evitar el mal gasto", "Siempre cuando puedas evita usar automovil que usen gasolina y usa bicicleta para evitar contaminar", "Tener siempre en casa distintos tachos de basura para botellas, plasticos, cajas, etc etc etc"]))

@bot.command() #Codigo del comando "$videos" que envia a tu servidor de discord un video sobre el medio ambiente, la contaminacion, y el cambio climatico en el planeta tierra
async def videos(ctx):
    await ctx.send(random.choice(["Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/1yz0-bEqKLY?si=jU2XcJcvy4JgLZpk", "Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/bR2X6sqsAiY?si=uDRqkU903lPb5HMQ", "Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/5w8cxYdLcCM?si=Nv9xAIoUJJEUmueM", "Esto es un video para que te des cuenta lo que puede provocar la contaminacion: https://youtu.be/e5y7FMCZwKQ?si=2za7P8oo5nlvY1-t"]))



bot.run("TU TOKEN VA AQUI")
