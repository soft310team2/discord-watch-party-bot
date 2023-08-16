import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import random

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

# Called once bot is ready for further action.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(guild_ids=[GUILD_ID], name="ping", description="pongs the user")
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.slash_command(guild_ids=[GUILD_ID], name="popcorn", description="scoop some popcorn!")
async def popcorn(interaction: nextcord.Interaction):
    popcorn = random.randint(1, 100)
    kernels = random.randint(0, popcorn)
    response = f"{interaction.user.display_name} scooped {popcorn} bits of popcorn, "
    if kernels == 0:
        response += "and no kernels! :popcorn:"
        if popcorn == 100:
            response += " NOW THAT'S A BUTTERY BUCKET :butter:"
    elif kernels == popcorn:
        response += "but ALL OF THEM ARE JUST KERNELS :skull:"
    else:
        response += f"but {kernels} of them are just kernels!"
    await interaction.response.send_message(response)

bot.run(BOT_TOKEN)