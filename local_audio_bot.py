import discord
import os
from discord.ext import commands,tasks
from discord import FFmpegAudio

client = commands.Bot(command_prefix= '!')                                                          # The prefix is ! but it can be changed                                                 
TOKEN = os.getenv('YOUR_BOT_TOKEN')                                                                 # Insert your bot's token in place of "YOUR_BOT_TOKEN"

# Prompt the bot to join a voice channel
@client.command()
async def join(ctx):                                                                                # Name of function (command) is 'join'
    if isinstance(ctx.channel, discord.channel.DMChannel):                                          # Check if the command is being used in a DM channel
        return await ctx.send("Sorry, I can't obey this command in DM.")
    if not ctx.author.voice:                                                                        # Check if message author is connected to a voice channel
       return await ctx.send("You are not currently connected to a voice channel.")
    channel = ctx.author.voice.channel                                                              # Get message author's current voice channel
    voice = get(client.voice_clients, guild=ctx.guild)  
    if voice and voice.is_connected():                                                              # Check if bot is already connected to a voice channel
        await voice.move_to(channel)                                                                # Move to message author's voice channel
    else:                                                                                           # If bot is not connected to a voice channel:
        await channel.connect()                                                                     # Connect to message author's voice channel 
    client_channel = ctx.voice_client.channel                                                       # Get bot's current voice channel 
    if channel and channel == client_channel:                                                       # Check if message author and bot are in the same voice channel
        if voice and voice.is_connected():                                                          # Check if bot is connected to the voice channel
            await ctx.send("I'm already in the channel with you!")

# Prompt the bot to leave a voice channel 
@client.command()
async def leave(ctx):                                                                               # Name of function (command) is 'leave'
    if isinstance(ctx.channel, discord.channel.DMChannel):                                          # Check if the command is being used in a DM channel
        return await ctx.send("Sorry, I can't obey this command in DM.")
    if not ctx.message.guild.voice_client:                                                          # Check if the bot is not connected to a voice channel
       return await ctx.send("I'm not currently connected to any voice channels.")
    await ctx.voice_client.disconnect()                                                             # Leave the current voice channel

# Prompt bot to play local audio file 
@client.command()
async def command_name(ctx):                                                                        # Replace name of function (command_name) with anything you'd like
    if isinstance(ctx.channel, discord.channel.DMChannel):                                          # Check if the command is being used in a DM channel
        return await ctx.send("Sorry, I can't obey this command in DM.")
    if not ctx.author.voice:                                                                        # Check is the message author is not connected to a voice channel
        return await ctx.send("You are not currently connected to a voice channel.")
    channel = ctx.author.voice.channel                                                              # Get message author voice channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:                                                                                   # Check if the bot is not connected to a voice channel
        await ctx.send("I need to be added to a voice channel for this command to work.")
    if voice and voice.is_playing():                                                                # Check if the bot is already playing audio
        return await ctx.send("I am already playing audio.") 
    if voice and voice.is_connected():                                                              # Check if the bot is connected to a voice channel
        await voice.move_to(channel)                                                                # Move to message author's voice channel if needed
        source = FFmpegPCMAudio(executable="C:path_to_ffmpeg.exe", source="C:path_to_audio_file")   # If ffmpeg.exe and the audio file are in the same directory as the script you do not need to specify a path
        player = voice.play(source)                                                                 # Play audio

client.run(TOKEN)
