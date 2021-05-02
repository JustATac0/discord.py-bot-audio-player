import discord
import os
from discord.ext import commands,tasks
from discord import FFmpegAudio

# The prefix is ! but it can be changed
client = commands.Bot(command_prefix= '!')
# Insert your bot's token in place of "YOUR_BOT_TOKEN"
TOKEN = os.getenv('YOUR_BOT_TOKEN')

# Prompt the bot to join a voice channel
@client.command()
# Name of function (command) is 'join'
async def join(ctx):
    # Check if the command is being used in a DM channel
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Sorry, I can't obey this command in DM.")
    # Check if message author is connected to a voice channel
    if not ctx.author.voice:
       return await ctx.send("You are not currently connected to a voice channel.")
    # Get message author's current voice channel
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    # Check if bot is already connected to a voice channel  
    if voice and voice.is_connected():
        # Move to message author's voice channel
        await voice.move_to(channel)
    # If bot is not connected to a voice channel
    else:
        # Connect to message author's voice channel 
        await channel.connect()
    # Get bot's current voice channel 
    client_channel = ctx.voice_client.channel
    # Check if message author and bot are in the same voice channel 
    if channel and channel == client_channel:
        # Check if bot is connected to the voice channel
        if voice and voice.is_connected():
            await ctx.send("I'm already in the channel with you!")

# Prompt the bot to leave a voice channel 
@client.command()
# Name of function (command) is 'leave'
async def leave(ctx):
    # Check if the command is being used in a DM channel
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Sorry, I can't obey this command in DM.")
    # Check if the bot is not connected to a voice channel
    if not ctx.message.guild.voice_client:
       return await ctx.send("I'm not currently connected to any voice channels.")
    # Leave the current voice channel
    await ctx.voice_client.disconnect()

# Play local audio file 
@client.command()
# Replace name of function (command_name) with anything you'd like
async def command_name(ctx):
    # Check if the command is being used in a DM channel
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Sorry, I can't obey this command in DM.")
    # Check is the message author is not connected to a voice channel
    if not ctx.author.voice:
        return await ctx.send("You are not currently connected to a voice channel.")
    # Get message author voice channel
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    # Check if the bot is not connected to a voice channel
    if not voice:
        await ctx.send("I need to be added to a voice channel for this command to work.")
    # Check if the bot is already playing audio
    if voice and voice.is_playing():
        return await ctx.send("I am already playing audio. Please wait until I am done before using another voice channel command.")
    # Check if the bot is connected to a voice channel 
    if voice and voice.is_connected():
        # Move to message author's voice channel if needed
        await voice.move_to(channel)
        # If ffmpeg.exe and the audio file are in the same directory as the script you do not need to specify a path
        source = FFmpegPCMAudio(executable="C:path_to_ffmpeg.exe", source="C:path_to_audio_file")
        # Play audio
        player = voice.play(source)

client.run(TOKEN)
