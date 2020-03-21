import discord

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("ShiNon이 열심히 코딩중")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("*안녕"):
        await message.channel.send("코딩좀 도와줘ㅠㅠㅠ")


client.run("NjkwODg0MjQ5OTM0MzY0Njkz.XnX7nw.52l7DR25CNEULqM7MZOKFHHYbtQ")
