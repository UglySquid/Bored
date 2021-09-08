# import discord
# from discord.ext import commands
# import fonts
# from discord_slash import *
#
#
# class WebhooksCommands(commands.Cog):
#     def __init__(self, client):
#         self.client = client
#
#     # events
#     @commands.Cog.listener()
#     async def on_ready(self):
#         print("LOL I'm here.")
#
#     # commands
#     @commands.command(name="upper")
#     async def upper(self, ctx, *, user_message=None):
#         if user_message is None:
#             await ctx.send(
#                 f'Please provide a message with that!')
#             return
#         member = ctx.author
#         await ctx.message.delete()
#         webhook = await ctx.channel.create_webhook(name=member.name)
#         await webhook.send(
#             str(f"{user_message.upper()}"), username=member.nick, avatar_url=member.avatar_url)
#
#         webhooks = await ctx.channel.webhooks()
#         for webhook in webhooks:
#             await webhook.delete()
#
#     @commands.command(name="lower")
#     async def lower(self, ctx, *, user_message=None):
#         if user_message is None:
#             await ctx.send(
#                 f'Please provide a message with that!')
#             return
#         member = ctx.author
#         await ctx.message.delete()
#         webhook = await ctx.channel.create_webhook(name=member.name)
#         await webhook.send(
#             str(f"{user_message.lower()}"), username=member.nick, avatar_url=member.avatar_url)
#
#         webhooks = await ctx.channel.webhooks()
#         for webhook in webhooks:
#             await webhook.delete()
#
#     @commands.command(name="skyline")
#     async def skyline(self, ctx, *, user_message=None):
#         if user_message is None:
#             await ctx.send(
#                 f'Please provide a message with that!')
#             return
#         member = ctx.author
#         await ctx.message.delete()
#         webhook = await ctx.channel.create_webhook(name=member.name)
#         await webhook.send(
#             str(f"{str(fonts.skyline(user_message))}"), username=member.nick, avatar_url=member.avatar_url)
#
#         webhooks = await ctx.channel.webhooks()
#         for webhook in webhooks:
#             await webhook.delete()
#
#
# def setup(client):
#     client.add_cog(WebhooksCommands(client))

