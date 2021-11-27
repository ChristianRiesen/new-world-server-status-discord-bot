# New World Server Status Bot for Discord

This is based on [MrRelliks bot](https://github.com/MrRelliks/New-World---server-status-bot--discord-), in fact most of the code is his. I have expanded upon this slightly to make it work generically with docker and different servers.

This bot fetches every 5 minutes (300 seconds) from the [unofficial status api](https://newworldstatus.com/unofficial-status-api), then updates the names of a category and 3 voice channels so you can use this as a status indicator on your discord server. It uses voice channels so everyone can see them but nobody can write into them. It's a good idea to lock them too.

You can run it locally or as this version is meant to, as a docker container.

You will need the following env variables set for it to work:

`API_TOKEN` is the Bearer token you get from the API. You can [request one here](https://newworldstatus.com/__automata/gtm/request.aspx).
`WORLD_NAME` needs to be one of the names returned from the API call to `/worlds`. It's usually all lower case, so make sure you copy this exactly. Make the first call with some client to ensure you got that right.
`BOT_SECRET` is the secret your bot has on Discord. When you register an app, you get this from Discord.
`CATEGORY_ID` is the id of the category you put the voice channels into. It maybe be a bit tricky to find it, but you can inspect the code if you load Discord in browser and copy the number out there.
`PLAYERS_CHANNEL` is the voice channel that should display the numbers of players (1234 / 2000 for example).
`QUEUE_CHANNEL` is the voice channel to show the number of people in queue.
`WAIT_CHANNEL` is the voice channel to show how long you might have to wait in queue if there is one.
`LOG_CHANNEL` is a text channel you might want to only have visible to you, so the bot can log messages into it if there is an issue.

Your bot needs to have admin permissions as well as intent privileges.

An example on how to run this (replacing each XYZ with actual values) would be this command:
`docker run --env API_TOKEN=XYZ --env WORLD_NAME=XYZ --env BOT_SECRET=XYZ --env CATEGORY_ID=XYZ --env PLAYERS_CHANNEL=XYZ --env QUEUE_CHANNEL=XYZ --env WAIT_CHANNEL=XYZ --env LOG_CHANNEL=XYZ christian-riesen/new-world-server-status-discord-bot`

If you made sure that all works well, you can add `-d` to run it in the background.

If you like this, you can send a thanks to the original author here: https://ko-fi.com/mrrelliks
