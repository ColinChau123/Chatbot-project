# This file is for the interface with discord

#import standard modules
import random
import os

#import the discord.py module
import discord
from discord.ext import commands

#import the chatbot and the custom intents editor
import bot.chatbot as cbot
from discordInterface.chatbotMode import chatbot

import com.addRole
import com.ban
import com.createChannel
import com.createRole
import com.kick
import com.mute
import com.toggle

#get the token from token.txt
TOKEN = open("discordInterface\\token.txt", "r").read()
client = discord.Client()

cbot = chatbot()

#<--------------------------------------------------------On Message------------------------------------------------------------>

#this variable sets whether or not the chatbot should be active, this is the default that sets it to true
com.toggle.bToggle = False

#this event runs when a message is sent
@client.event
async def on_message(message):
    #if bToggle is on, act as a chatbot, otherwise act as a standard bot
    print(message.content)
    if com.toggle.bToggle:
        await message.channel.send(chatbot.reply(message.content))

#<--------------------------------------------------------bot prep------------------------------------------------------------>

whitelisted_servers = ['878845591575207966', '732620946300600331']

print("Pyroh is now online")
client.run(TOKEN)