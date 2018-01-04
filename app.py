import discord
import minestat
from mcstatus import MinecraftServer
import urllib.request
import json

client = discord.Client()
TOKEN = "Mzk4NDAwMjA3Njk3NDc3NjMy.DS-NDQ.MDw5PHrLgyQe9HA47PVANGJ0zFg"
ADDRESS = "192.168.10.43"
PORT = "9933"
URL = "http://minecraft-api.com/v1/get/?server={}:{}".format(ADDRESS,PORT)
def get_server_status():
    # Below is an example using the MineStat class.
    # If server is offline, other instance members will be None.
    ms = minestat.MineStat(ADDRESS, int(PORT))
    print('Minecraft server status of %s on port %d:' % (ms.address, ms.port))
    if ms.online:
        return True
    else:
        return False

@client.event
async def on_ready():
    print("-------------")
    print('Logged in as {} {}'.format(client.user.name,client.user.id))
    print("-------------")
@client.event
async def on_message(message):
    if message.content.startswith("!server"):
        if client.user != message.author:
            status = get_server_status()
            if status == True:
                msg = "Server is ONLINE."
            else:
                msg = "Server is OFFLINE."
            await client.send_message(message.channel,msg)

client.run(TOKEN)