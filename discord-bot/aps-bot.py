import discord
import asyncio
import random

client = discord.Client()

woosh = False
chance = 0/1
woosh_message = ''

def woosh_on(woosh_chance=1/10, input_message='Woosh'):
    global woosh
    global chance
    global woosh_message
    woosh = True
    chance = woosh_chance.split('/')
    woosh_message = input_message

def woosh_off():
    global woosh
    woosh = False

@client.event
async def on_ready():
    print('--------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

@client.event
async def on_message(message):
    print(message.author)
    global woosh
    server = message.channel
    if (message.author != 'aps-bot#8984'):
        print("Message is by someone else")
        if message.content.startswith('!'):
            if message.content.startswith('!test'):
                await client.send_message(server, "Woosh")
            elif message.content.startswith('!woosh on'):
                if woosh:
                    await client.send_message(server, "Woosh is already on")
                else:
                    commands = message.content.split()
                    woosh_on(commands[2], commands[3:])
                    await client.send_message(server, "Woosh has been activated")
            elif message.content.startswith('!woosh off'):
                if not woosh:
                    await client.send_message(server, "Woosh is already off")
                else:
                    woosh_off()
                    await client.send_message(server, "Woosh has been deactivated")           
        elif woosh:
            roll = random.randint(int(chance[0]), int(chance[1]))
            if roll == int(chance[0]):
                await client.send_message(server, woosh_message)
client.run('MzM5NDgwNTI1OTUxNTk4NTky.DFkqAQ.ThGhdO_Ao4Ikxhb3jZr-VGL2sb8')
#client.run('arghalexander3000@gmail.com','D@vid0614')
