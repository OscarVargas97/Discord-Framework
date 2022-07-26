import os #biblioteca que permite interactuar con el sistema operativo
import sys #Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete. Siempre está disponible.
from src import index as allcommand
from dotenv import load_dotenv #carga variables de entorno desde un archivo .env
from discord.ext import commands


def main():
  
  bot = commands.Bot(command_prefix='$', description='Esta es la ayuda del bot')
  
  load_dotenv()
  
  allcommand.chargecogs(bot)
  allcommand.load(bot)

  bot.run(os.getenv('TOKEN'))


if __name__ == "__main__":
  main()