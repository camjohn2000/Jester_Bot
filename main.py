import discord
import os
from random import randint

client = discord.Client()

#set to general channel(only channel)
channel = client.get_channel('755969981547544578')

#console logging that bot is logged in and online
@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

def random_joke():
    jester_line = list(open("jester.txt"))
    return jester_line[randint(0, len(jester_line) - 1)]

def tren_special():
    tren_line = list(open("tren.txt"))
    return (tren_line[randint(0, len(tren_line) - 1)])

@client.event
async def on_message(msg):
  
  #ignores it's own messages
  if msg.author == client.user:
    return
    
  #When Trey specifically messages in the Discord server
  elif msg.author.id == ('131971739293843457'):
    await msg.channel.send(tren_special())

  #bot replies when it reads command in text channel
  elif msg.content.startswith("%hey jester"):
    await msg.channel.send("Alright, ready to start!")
  else:
    #Jester talk
    await msg.channel.send(random_joke())
    
#token defined privately in repl.it
client.run(os.environ['TOKEN'])

