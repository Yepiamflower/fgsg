import discord
from discord.ext import commands
import ollama

# Set up the bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='FlowerAI', intents=intents)

# Memory for storing conversations
memory = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def respond(ctx, *, question):
    # Store the question in memory
    memory.append(question)
    
    # Use Ollama gemma2:3b model to get the response
    response = ollama.chat(question, model='gemma2:3b')
    
    # Send the response back to Discord
    await ctx.send(response)

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')