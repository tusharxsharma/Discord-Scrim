import discord 
import random
from discord.ext import commands 	

client = commands.Bot(command_prefix = '.')

@client.event 
async def on_ready():
	print('Bot is ready.')

@client.event 
async def on_member_join(member):
	print(f'(member) has joined the server.')

@client.event
async def on_member_remove(member):
	print(f'(member) has left the server.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):
	responses = ['It is certaion.',
				 'It is decidely so.',
				 'Without a doubt',
				 'Yes - definitely.']
	await ctx.send(f'Question:{question}\nAnswer: {random.choice(responses)}')
clinent.run('#your bot token')
