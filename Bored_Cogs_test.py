# import discord
# from discord.ext import commands
# from discord_buttons_plugin import *
# from discord_components import *
# from discord_slash import *
# import oauth2
# import os
#
# TOKEN = "NzMzODU2NjYyMzYzOTYzNDMy.XxJPRg.-6OB8rPA0ED-6URRSPgLW1B9CQY"
# auth = oauth2.Oauth.discord_login_url
#
# client = commands.Bot(command_prefix="yada ", case_insensitive=True)
# buttons = ButtonsClient(client)
# slash = SlashCommand(client, sync_commands=True)
# guild_ids = client.get_guild(794964658707890196)
#
#
# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f"cogs.{extension}")
#
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f"cogs.{extension}")
#
#
# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f"cogs.{filename[:-3]}")
#
#
# client.run(TOKEN)