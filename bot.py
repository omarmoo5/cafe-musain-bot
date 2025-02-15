import asyncio
import discord
from discord.ext import commands
import random
from config import TOKEN, TOKEN2

intents=discord.Intents.all()
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    await member.add_roles(verified)

#fake command error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("there is no command named like that.")

#kick
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
        reason='No reason was provided'
    await ctx.guild.kick(member)
    await ctx.send(f'User {member} has been kicked for {reason}')
#ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
        reason='no reason was provided'
    await ctx.guild.ban(member)
    await ctx.send(f'User {member} has been banned for {reason}')
#unban
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
        reason='no reason was provided'
    await ctx.guild.unban(member)

#mute
@client.command(description="mutes the specified user")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, reason=None):
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name="Muted")
    verified = discord.utils.get(guild.roles, name="verified")

    if not muteRole:
        muteRole = await guild.creat_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(muteRole, send_messages=False, )
    await member.remove_roles(verified)
    await member.add_roles(muteRole, reason=reason)
    await ctx.send(f'Muted {member.mention} for {reason}')    
    await member.send(f'you are muted in {guild.name} for {reason}')      

#unmute
@client.command(description="Unmutes the specifies user")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
    muteRole = discord.utils.get(ctx.guild.roles, name="Muted")
    verified = discord.utils.get(ctx.guild.roles, name="verified")

    await member.remove_roles(muteRole)
    await member.add_roles(verified)
    await ctx.send(f'Unmuted {member.mention}')
    await member.send(f'an admin unmuted in cafe musain')

@client.command()
async def alez(ctx):
    await ctx.send("she is halal waifu to <@766684442940538922> :ring:")

@client.command()
async def iikimo(ctx):
    await ctx.send("<@445245966975500288> you have been summoned")

@client.command()
async def witch(ctx):
    await ctx.send(f'<@332633328114991114> we need you')


client.run(TOKEN + TOKEN2)
