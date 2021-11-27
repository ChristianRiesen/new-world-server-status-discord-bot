from config import *
from memberevents import *
from worldupdate import *
from commandsslash import *
from NewWorldCommands import *
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
#Clears console on launch to keep things tidy.
clearConsole()

guild_data = []

@client.event
async def on_ready():

    members = 0

    for guild in client.guilds:
        members += guild.member_count - 1
    #await client.change_presence(activity=discord.Game(name=f"New World with {members} members."))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} members."))
    print(colored (f"{prefix} Ready and Watching {str(members)} members.", 'grey','on_white'))
    print(colored (f"{prefix} Please Wait whilst I gather the server information for {worldname}.", 'grey','on_white'))
    ServerStats.start()

client.run(my_secret)
