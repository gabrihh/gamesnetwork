# Importar a biblioteca discord.py
import discord
from discord.ext import commands

# Criar uma instância da classe Bot
bot = commands.Bot(command_prefix='/')

# Definir um comando chamado /teste
@bot.command()
async def teste(ctx):
    # Enviar uma mensagem mencionando o autor do comando
    await ctx.send(f'Estou ativo {ctx.author.mention}')

# Conectar o bot usando o token
bot.run('MTIwNzg3Mjk3MDYyMjUwOTE3Nw.GccFmL.dPrnwEuTfBr5R12kxCXnitVEbul5X0XY-7ITx8')
