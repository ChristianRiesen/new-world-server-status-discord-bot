from config import *
from worldupdate import *


@client.event
async def on_ready():
    print(colored (f"{prefix} Please Wait whilst I gather the server information for {worldname}.", 'grey','on_white'))
    ServerStats.start()

client.run(my_secret)
