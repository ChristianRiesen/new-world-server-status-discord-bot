from config import *

@tasks.loop(seconds=300)
async def ServerStats():
    url = "https://nwdb.info/server-status/servers.json?worldId=" + worldid
    headers = CaseInsensitiveDict()
    headers = {'User-agent': user_agent}
    resp = requests.get(url, headers=headers)
    response = resp.text
    output = json.loads(response)

    CategoryName_Var = client.get_channel(CategoryName)
    Playerschannel_Var = client.get_channel(Playerschannel) #Put channel ID You want here.
    QueueChannel_Var = client.get_channel(QueueChannel)#Put channel ID 2 You want here.
    MinutesToWaitChannel_Var = client.get_channel(MinutesToWaitChannel)#Put channel ID 3 You want here.
    LogChannel_Var = client.get_channel(LogChannel) # Logs go here
    await discord.CategoryChannel.edit(CategoryName_Var, name = f"📊 {worldname} Server Stats 📊")

    print(f"Server responded with Status: {resp.status_code}")

    if resp.status_code == 200:
        print(f"{prefix} Status is 200, Updating Stats...")

        players = output['data']['servers'][0][1]
        player_cap = output['data']['servers'][0][0]
        queue = output['data']['servers'][0][2]

        print(colored (f"{prefix} Sucess!!", 'white','on_green'))
        print(f"{prefix} Player Count is {players} / {player_cap}")
        print(f"{prefix} Queue Count is {queue}")

        #Update current player count#
        try:
            if(int(players) >= 1 and int(players) <= 999 ):
                await discord.VoiceChannel.edit(Playerschannel_Var, name = f"🟢 Players: {players} / {player_cap}")
            elif(int(players) >= 1000 and int(players) <= 1499):
                await discord.VoiceChannel.edit(Playerschannel_Var, name = f"🟡 Players: {players} / {player_cap}")
            elif(int(players) >=1500 and int(players) <=1899):
                await discord.VoiceChannel.edit(Playerschannel_Var, name = f"🟠 Players: {players} / {player_cap}")
            elif(int(players) >= 1900):
                await discord.VoiceChannel.edit(Playerschannel_Var, name = f"🔴 Players: {players} / {player_cap}")
            else:
                await discord.VoiceChannel.edit(Playerschannel_Var, name = f"⚙️ Down For Maintenance")

        #Update Queue Size
            if(int(queue) >= 0 and int(queue) <= 34):
                await discord.VoiceChannel.edit(QueueChannel_Var, name = f"🟢 Queue: {queue}")
            elif(int(queue) >= 35 and int(queue) >= 74):
                await discord.VoiceChannel.edit(QueueChannel_Var, name = f"🟡 Queue: {queue}")
            elif(int(queue) >=75 and int(queue) >= 99):
                await discord.VoiceChannel.edit(QueueChannel_Var, name = f"🟠 Queue: {queue}")
            elif(int(queue) >= 100):
                await discord.VoiceChannel.edit(QueueChannel_Var, name = f"🔴 Queue: {queue}")
            else:
                await discord.VoiceChannel.edit(QueueChannel_Var, name = f"❓ Queue: {queue}")

            #Update Queue Wait Times
            #await discord.VoiceChannel.edit(MinutesToWaitChannel_Var, name = f"⏲️ Wait Time: {wait} Mins.")
        except:
            print("Can not update server stats. Please use /help for configuration options.")

        print(f"{prefix} Updated Stats.")
    else:
        if resp.status_code == 429:
            print(colored (f"{prefix} Error!!", 'white','on_red'))
            print(f"{prefix} Status code is {str(statuscode.status_code)} - Too Many Requests - Retrying in {amountofhours} hour")
            hour = 60*60
            amountofhours = 3
            minstowait = hour * amountofhours
            await LogChannel_Var.send(f"I have sent too many requests to the API, I will try again in {amountofhours} hour(s). ")
            await asyncio.sleep(minstowait)
            amountofhours += 0.5

        else:
           # print("Status code is " + str(statuscode.status_code) + " - Retrying in 120 seconds."
           print(colored (f"{prefix} Error!! Status code: {resp.status_code}", 'white','on_red'))
        await LogChannel_Var.send(f"I have encountered an error with updating the server values. Please check the console. ")
