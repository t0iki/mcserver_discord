import discord
import minestat
import os
import urllib.request
import json
from riotwatcher import RiotWatcher

client = discord.Client()
TOKEN = os.environ.get('TOKEN')
ADDRESS = os.environ.get('ADDRESS')
#TOKEN = 'Mzk4NDM2NzE3OTQzODQ4OTYw.DS-hSg.PMR2Gdj88dMeEuCGRs_xcHTKPIk'
#ADDRESS = '180.16.218.228'
RIOTAPI = os.environ.get('RIOTAPI')
#RIOTAPI = 'RGAPI-d9519528-a4ce-429c-9311-030d4e91ed84'
PORT = '9933'
connection = RiotWatcher(RIOTAPI)


def get_summonerlevel(name):
    summoner = connection.summoner.by_name('jp1', name)
    print(summoner)
    return summoner['summonerLevel']


def get_server_status():
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
    elif message.content.startswith("!help"):
        if client.user != message.author:
            await client.send_message(message.channel, 'Commands: !server , うんこ')
    elif message.content.startswith("!lollvl"):
        words = message.content.split(' ')
        if len(words) >= 3:
            name = ' '.join(words[1:])
        else:
            name = words[1]
        level = get_summonerlevel(name)
        msg = "{}のサモナーレベルは{}です".format(name,level)
        await client.send_message(message.channel, msg)

client.run(TOKEN)