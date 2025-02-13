import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix="!", self_bot=True, chunk_guilds_at_startup=False)

logs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FILE_NAME")
bot_prefixes = ("!", "g.", ">", "a!") # bot prefixes, add your own here
guild_id = GUILD_ID_HERE
channel_id = CHANNEL_ID_HERE

def NEWFILE(file):
    with open(file, 'w') as f:
        pass
    print(f"New file created: {file}")
#NEWFILE(logs) # comment this when you dont want to overwrite old data, just for testing purposes

def write(file, data):
    try:
        with open(file, 'a', encoding="utf-8") as f:
            f.write(data)
    except:
        pass

def message_cleanup(message):
    "removes newlines, user mentions, custom emojis, role mentions, steamcommunity virus link, and sends back empty if the message has a file attached"
    if message.attachments or message.embeds or message.stickers or message.author.bot: # if message has a file / gif / sticker attached
        return
    if any(x in message.content.lower() for x in ["steamcommunity", "tenor.com", "cdn.discordapp.com", "media.discordapp.net", "a!afk"] or message.startswith(bot_prefixes)): #steamcommunity virus link, tenor gifs, discord media links and bot prefixes
        return
    while any(x in message.content for x in ["<a:", "<:", "<#", "<@", "<!"]):
        try:
            start = message.content.index("<")
            end = message.content.index(">", start)  # if I don't put ", start", the whole thing gets stuck in an infinite loop. I don't know why, but it does and I can't be asked to find out
            message.content = message.content[:start] + message.content[end+1:]
        except ValueError:
                break  # Stop if ">" is missing
    split = message.content.split()
    if split == []:
        return
    print(' '.join(split))
    return ' '.join(split) + "\n"

async def runthrough(guild_id, channel_id):
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    last_message, batch_size, batch_count = None, 1000, 0
    while True:
        try:
            async for message in channel.history(limit=batch_size, before=last_message):
                write(logs, message_cleanup(message))
                last_message = message
            batch_count += 1
            print(f"------------------------------------ NEW BATCH: {batch_count} ------------------------------------")
            await asyncio.sleep(1)
        except discord.HTTPException:
            print(f"Rate limited, waiting 5 seconds.")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Error fetching messages: {e}")
            break

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Selfbot is ready!')
    print("---------------------------------------------------------------------------------------------------")
    await runthrough(guild_id, channel_id)

bot.run('TOKEN')