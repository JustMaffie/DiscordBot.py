from discord.ext import commands
import discord

def is_admin_check(ctx):
    if is_owner_check(ctx):
        return True
    admins = ctx.bot.config.admins
    return ctx.author.id in admins
    
def is_owner_check(ctx):
    owners = ctx.bot.config.owners
    return ctx.author.id in owners
    
def is_owner():
    def check(ctx):
        return is_owner_check(ctx)
    return commands.check(check)

def is_admin():
    def check(ctx):
        return is_admin_check(ctx)
    return commands.check(check)