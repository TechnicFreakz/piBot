import discord
import os
from dotenv import load_dotenv
import random

load_dotenv()
bot = discord.Bot()


wrong_citations = ['„Frage nicht, was dein Land für dich tun kann, frage was du für dein Land tun kannst.“ - Kim Jong-il',
                    '„Willst du den Charakter eines Menschen erkennen, so gib ihm Macht.“ - Roland Koch',
                    '„Mister Gorbatschow, tear down this wall!“ - David Hasselhoff',
                    '„Dies ist mein Leib, der für euch hingegeben wird.“ - Gina Wild']


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "answer", description = "What do you get if you multiply six by nine?")
async def answer(ctx):
    await ctx.respond("42")

@bot.slash_command(name = "fzitat", description = "Ein zufälliges falsch zugeordnetes Zitat bitte!")
async def fzitat(ctx):
    await ctx.respond(wrong_citations[random.randint(0, 3)])

bot.run(os.getenv('OLYMP_TOKEN'))
