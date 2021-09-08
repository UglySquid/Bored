import discord
from discord.ext import commands
from discord_buttons_plugin import *
from discord_components import *
from discord_slash import *
from discord_slash.utils.manage_commands import create_choice, create_option
import oauth2
import emoji
import fonts

TOKEN = "NzMzODU2NjYyMzYzOTYzNDMy.XxJPRg.-6OB8rPA0ED-6URRSPgLW1B9CQY"
auth = oauth2.Oauth.discord_login_url

client = commands.Bot(command_prefix="yada ", case_insensitive=True)
buttons = ButtonsClient(client)
slash = SlashCommand(client, sync_commands=True)
guild_ids = client.get_guild(794964658707890196)

client.remove_command("help")


@client.event
async def on_ready():
    channel = client.get_channel(851169143767302154)
    DiscordComponents(client, change_discord_methods=True)
    await channel.send("LOL I'm here.")


@client.event
async def on_disconnect():
    channel = client.get_channel(851169143767302154)
    await channel.send("LOl I'm leaving.")


@client.command(name="hi" or "hello")
async def hi(ctx):
    await ctx.message.channel.send("Hello, Assolotls!")


help_embed = discord.Embed(title="Who am I?", description="I'm Bored, and you?", color=0x3c6e71)
help_embed.add_field(name="Name: ", value="Bored\n(duh)")
help_embed.add_field(name="Pronouns: ", value="it/its/itself")
help_embed.add_field(name="Age: ", value="I'm immortal...the passage of time does not concern me")
help_embed.add_field(name="Occupation: ", value="Unemployed but still richer than you", inline=False)
help_embed.add_field(name="Hobbies: ", value="Collecting debts and spending money.", inline=False)
help_embed.set_footer(text="℗ Copyright I'm bored so why not")

commands_embed = discord.Embed(title="Commands", color=0x3c6e71)
commands_embed.add_field(name="Slash Commands ",
                         value="You can access these commands by typing in a backslash and clicking on the desired commands",
                         inline=False)
commands_embed.add_field(name="Commands using the 'yada' prefix",
                         value="Say Hi : `yada hi`" "\n"
                               "Help page : `yada help`" "\n"
                               "Text/fonts : `yada upper``yada lower``yada skyline`" "\n"
                               "Emoticons : `yada lenny``yada satisfied``yada tt``yada free``yada shock``yada ...`"
                               "`yada ow``yada happy``yada guilty``yada kick`" "\n",
                         inline=False)
commands_embed.add_field(name="Settings",
                         value="Things that you can toggle on or off",
                         inline=False)
commands_embed.set_footer(text="℗ Copyright I'm bored so why not")

settings_embed = discord.Embed(title="Settings", color=0x3c6e71)
settings_embed.add_field(name="Reminders",
                         value="Some things that I say to torment you during every one of your waking hours.",
                         inline=False)
settings_embed.set_footer(text="℗ Copyright I'm bored so why not")

reminders_embed = discord.Embed(title="Reminders", color=0x3c6e71)
reminders_embed.add_field(name="change timezone",
                          value="Will add some options later",
                          inline=False)
reminders_embed.add_field(name="Good morning/night",
                          value="Will add some boolean toggles later",
                          inline=False)
reminders_embed.add_field(name="Drink water?",
                          value="Will add some boolean toggles later",
                          inline=False)
reminders_embed.add_field(name="Move around?",
                          value="Will add some boolean toggles later",
                          inline=False)
reminders_embed.set_footer(text="℗ Copyright I'm bored so why not")

invite_button = Button(style=ButtonStyle.URL, label="Invite button", url=auth)
goback_button = Button(style=ButtonStyle.grey, label="Go back", custom_id="goback_button_id")
previous_button = Button(style=ButtonStyle.blue, label="Previous", custom_id="previous_button_id")
next_button = Button(style=ButtonStyle.blue, label="Next", custom_id="next_button_id")
commands_button = Button(style=ButtonStyle.blue, label="Commands", custom_id="commands_button_id")
settings_button = Button(style=ButtonStyle.blue, label="Settings", custom_id="settings_button_id")
reminders_button = Button(style=ButtonStyle.blue, label="Reminders", custom_id="reminders_button_id")


@client.event
async def on_button_click(itractn):
    if itractn.component.label.startswith("Go back"):
        await itractn.message.edit(type=InteractionType.ChannelMessageWithSource,
                                   embed=help_embed,
                                   components=[[commands_button, settings_button]])
    elif itractn.component.label.startswith("Settings"):
        await itractn.message.edit(type=InteractionType.ChannelMessageWithSource,
                                   embed=settings_embed,
                                   components=[[goback_button, previous_button, next_button]])
    elif itractn.component.label.startswith("Previous"):
        await itractn.message.edit(type=InteractionType.ChannelMessageWithSource,
                                   embed=commands_embed,
                                   components=[[goback_button, previous_button, next_button]])
    elif itractn.component.label.startswith("Next"):
        await itractn.message.edit(type=InteractionType.ChannelMessageWithSource,
                                   embed=commands_embed,
                                   components=[[goback_button, previous_button, next_button]])
    elif itractn.component.label.startswith("Settings"):
        await itractn.message.edit(type=InteractionType.ChannelMessageWithSource,
                                   embed=settings_embed,
                                   components=[[goback_button, reminders_button]])
    elif itractn.component.label.startswith("Reminders"):
        await itractn.message.edit(type=InteractionType.ChannelMessageWithSource,
                                   embed=reminders_embed,
                                   components=[[goback_button]])


@client.command(name="help")
async def help_func(ctx):
    await ctx.message.channel.send(embed=help_embed,
                                   components=[[invite_button, commands_button, settings_button]])


@client.command(name="?")
async def help_func(ctx, itractn):
    await ctx.message.channel.send(embed=help_embed,
                                   components=[invite_button, commands_button, settings_button])


# SLASH COMMANDS


# Allow people to choose which emojis? if no emoji chosen, assign one for them (maybe shuffle the list of emojis)
# person can only vote once, if they vote twice "Sorry! you can't vote twice!" leader board will show the choice with most votes
# Option(un-required): Approval voting description: you can vote more than once (Don't just ask for the favorite, ask for all the OKs.)
# if user reacts to a message, that option_count+1 += 1
# if user reacts to a message more than once, await ctx.message.channel.send("Sorry! You can't react more than once!")
# use buttons instead of reactions,create a button with a count function for each time the button is pressed,etc.

all_reactions = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "⚪",
                 "🟥", "🟧",
                 "🟨", "🟩", "🟦", "🟪", "🟫", "⬛", "⬜"]


@slash.slash(name="poll", description="Create a poll (separate the poll choices with ',   ')",
             guild_ids=guild_ids, )
async def poll(ctx, title: str, poll_choices):
    poll_embed = discord.Embed(title=title, description=f"This is a poll created by @{ctx.author}")
    choices_list = poll_choices.split(", ")
    how_many_choices = len(choices_list)
    reactions_list = all_reactions[0:how_many_choices]
    for choice in choices_list:
        index_num = choices_list.index(choice)
        emoji_name = reactions_list[index_num]
        reaction = emoji.emojize(emoji_name, use_aliases=True)
        poll_embed.add_field(name=choice, value=f'- react with ({reaction})', inline=False)

    msg = await ctx.send(embed=poll_embed)

    for reaction in reactions_list:
        await msg.add_reaction(reaction)


@slash.slash(name="emoticons", description="Send some of your favorite emoticons. DM for requests",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="emoticon",
                     description="Choose an emoticon",
                     required=True,
                     option_type=3,
                     choices=[
                         create_choice(name="( ͡° ͜ʖ ͡°)", value="( ͡° ͜ʖ ͡°)"),
                         create_choice(name="^ω^", value="^ω^"),
                         create_choice(name="(ToT)", value="(ToT)"),
                         create_choice(name="⊂二二二（＾ω＾）二⊃", value="⊂二二二（＾ω＾）二⊃"),
                         create_choice(name="Σ(ﾟДﾟ)", value="Σ(ﾟДﾟ)"),
                         create_choice(name="(￣ー￣)", value="(￣ー￣)"),
                         create_choice(name="＿|￣|○", value="＿|￣|○"),
                         create_choice(name="(≧ロ≦)", value="(≧ロ≦)"),
                         create_choice(name="(ΘεΘ;)", value="(ΘεΘ;)"),
                         create_choice(name="＼| ￣ヘ￣|／＿＿＿＿＿＿＿θ☆( *o*)/", value="＼| ￣ヘ￣|／＿＿＿＿＿＿＿θ☆( *o*)/"),
                     ])
             ])
async def emoticons(ctx, emoticon: str):
    await ctx.send(content="emoticon sent", delete_after=1)
    member = ctx.author
    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
        str(emoticon), username=member.nick, avatar_url=member.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()


@slash.slash(name="pseudo", description="Sends a message under someone else's name",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="message_input",
                     description="Choose an emoticon",
                     required=True,
                     option_type=str),
                 create_option(
                     name="user",
                     description="Choose a user to imposter?",
                     required=False,
                     option_type=6),
             ])
async def pseudo(ctx, message_input: str, user: id):
    if user is None:
        user = ctx.author
    await ctx.send(content="pseudo message sent")
    webhook = await ctx.channel.create_webhook(name=user.name)
    await webhook.send(
        str(message_input), username=user.nick, avatar_url=user.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()


@slash.slash(name="upper", description="Send something in UPPERCASE",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="message_input",
                     description="Message you would like to send in uppercase",
                     required=True,
                     option_type=str)
             ])
async def upper(ctx, message_input: str):
    await ctx.send(content="UPPER message sent")
    member = ctx.author

    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
        str(f"{message_input.upper()}"), username=member.nick, avatar_url=member.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()


@slash.slash(name="lower", description="Send something in lower",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="message_input",
                     description="Message you would like to send in lowercase",
                     required=True,
                     option_type=str)
             ])
async def lower(ctx, message_input: str):
    await ctx.send(content="lower message sent")
    member = ctx.author

    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
        str(f"{message_input.lower()}"), username=member.nick, avatar_url=member.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()
        
        
@slash.slash(name="skyline", description="Send something in sKyLiNe",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="message_input",
                     description="Message you would like to send in lowercase",
                     required=True,
                     option_type=str)
             ])
async def skyline(ctx, message_input: str):
    await ctx.send(content="sKyLiNe message sent")
    member = ctx.author

    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
        str(f"{str(fonts.skyline(message_input))}"), username=member.nick, avatar_url=member.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()


@slash.slash(name="case-fonts", description="Sends a message in UPPERCASE, lowercase, or sKyLiNe fonts.",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="font",
                     description="Choose UPPERCASE, lowercase, or sKyLiNe.",
                     required=True,
                     option_type=str,
                     choices=[
                         create_choice(name="uppercase", value="upper"),
                         create_choice(name="lowercase", value="lower"),
                         create_choice(name="skyline", value="skyline")]),
                 create_option(
                     name="message_input",
                     description="Message you would like to send in case-font",
                     required=True,
                     option_type=str)
             ])
async def case_font(ctx, font: str, message_input: str):
    if font == "upper":
        font_message = message_input.upper()
    elif font == "lower":
        font_message = message_input.lower()
    elif font == "skyline":
        font_message = fonts.skyline(message_input)

    await ctx.send(content="case-font message sent")
    member = ctx.author

    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
        str(f"{str(font_message)}"), username=member.nick, avatar_url=member.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()


@slash.slash(name="spam", description="Send something you said more than once",
             guild_ids=guild_ids,
             options=[
                 create_option(
                     name="spam_number",
                     description="Choose an emoticon",
                     required=True,
                     option_type=int,
                     choices=[
                         create_choice(name="1", value=1),
                         create_choice(name="2", value=2),
                         create_choice(name="3", value=3),
                         create_choice(name="4", value=4),
                         create_choice(name="5", value=5),
                         create_choice(name="6", value=6),
                         create_choice(name="7", value=7),
                         create_choice(name="8", value=8),
                         create_choice(name="9", value=9),
                         create_choice(name="10", value=10)]),
                 create_option(
                     name="message_input",
                     description="Choose an emoticon",
                     required=True,
                     option_type=str)
             ])
async def spam(ctx, spam_number: int, message_input: str):
    await ctx.send(content="spam message sent")
    spam_message = f"{spam_number * message_input}"

    member = ctx.author
    webhook = await ctx.channel.create_webhook(name=member.name)
    await webhook.send(
        str(f"{spam_message}"), username=member.nick, avatar_url=member.avatar_url)

    webhooks = await ctx.channel.webhooks()
    for webhook in webhooks:
        await webhook.delete()


# it can take a message, and search on youtube, and pick the first video, and play it (if no message input, send this: https://www.youtube.com/watch?v=7NuaK29J1fM)
# it can take a message, and search on google images, and pick the first image and send it (if no message input, send this: https://media1.giphy.com/media/l2JhpjWPccQhsAMfu/200.gif)
# it can take your message word, and return a list of synonyms and antonyms
# make a calculator

client.run(TOKEN)
