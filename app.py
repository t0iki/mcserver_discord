import discord
import minestat
import os

client = discord.Client()
TOKEN = os.environ.get('TOKEN')
ADDRESS = os.environ.get('ADDRESS')
PORT = '9933'

def get_server_status():
    # Below is an example using the MineStat class.
    # If server is offline, other instance members will be None.
    print(ADDRESS)
    print(int(PORT))
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
                msg = "サーバーはオンラインです"
            else:
                msg = "サーバーはオフラインです"
            await client.send_message(message.channel,msg)
    elif message.content.startswith("うんこ"):
        if client.user != message.author:
            await client.send_message(message.channel, ':poop:')

client.run(TOKEN)