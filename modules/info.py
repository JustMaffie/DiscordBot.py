from discord.ext import commands
import discord
import platform
import datetime
from discordbot.module import Module

class Info(Module):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, user:discord.User=None):
        """Grab information about a user"""
        if not ctx.message.guild:
            return await ctx.send("You can only execute this command in a guild")
        guild = ctx.message.guild
        if not user:
            user = ctx.author
        member = guild.get_member(user.id)
        _roles = member.roles
        roles = []
        for role in _roles:
            roles.append(role.name)
        embed = discord.Embed(color=discord.Colour.green(), timestamp=datetime.datetime.utcnow())
        joined_at = member.joined_at
        since_joined = (ctx.message.created_at - joined_at).days
        since_created = (ctx.message.created_at - user.created_at).days
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        joined_at = joined_at.strftime("%d %b %Y %H:%M")
        embed.set_author(name="{}#{}".format(user.name, user.discriminator), icon_url=member.avatar_url)
        embed.add_field(name="ID", value="{}".format(user.id), inline=True)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="Game", value=member.activity.name, inline=True)
        embed.add_field(name="Roles", value=", ".join(roles))
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name="Created At", value="{} (Thats over {} days ago)".format(user_created, since_created), inline=True)
        embed.add_field(name="Joined At", value="{} (Thats over {} days ago)".format(joined_at, since_joined), inline=True)
        embed.set_footer(text='Requested by: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=embed)

    @commands.command(aliases=["info","botinfo"])
    async def about(self, ctx):
        """Get more information about the bot"""
        bot = self.bot
        if not hasattr(bot, "owner"):
            return await ctx.send("Hey, I'm sorry, but I am not ready yet, please try again in a few seconds.") # You won't often have to see this, this is only when the bot hasn't yet started up
        embed = discord.Embed(color=discord.Colour.green(), timestamp=datetime.datetime.utcnow())
        discord_version = discord.__version__
        python_version = platform.python_version()
        embed.add_field(name="Discord.py Version", value=discord_version, inline=True)
        embed.add_field(name="Python Version", value=python_version, inline=True)
        embed.add_field(name="Latency", value=str(round(bot.latency, 3)), inline=True)
        embed.add_field(name="Guilds", value=str(len(bot.guilds)), inline=True)
        embed.add_field(name="Users", value=str(len(bot.users)), inline=True)
        if ctx.message.guild:
            embed.add_field(name="Shard ID", value=str(ctx.message.guild.shard_id), inline=True)
        embed.add_field(name="Developers", value="JustMaffie#0420, {}".format(bot.owner.owner))
        embed.set_footer(text='Requested by: {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=embed)

def setup(bot):
    bot.load_module(Info)