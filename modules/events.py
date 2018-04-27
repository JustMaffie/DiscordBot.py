from discord.ext import commands
import discord
import traceback
from discordbot.module import Module

class Events(Module):
    async def on_ready(self):
        self.bot.owner = await self.bot.application_info()
        info = [str(self.bot.user), "Discord.py version: {}".format(discord.__version__), 'Shards: {}'.format(self.bot.shard_count), 'Guilds: {}'.format(len(self.bot.guilds)),
            'Users: {}'.format(len(set([m for m in self.bot.get_all_members()]))), '{} modules with {} commands'.format(len(self.bot.cogs), len(self.bot.commands)), 
            'Owner: {}'.format(self.bot.owner.owner)]
        self.bot.logger.info("")
        for f in info:
            self.bot.logger.info(f)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send_help()
        elif isinstance(error, commands.BadArgument):
            await ctx.send_help()
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("It looks like this command is disabled.")
        elif isinstance(error, commands.CommandInvokeError):
            self.bot.logger.exception("An error occurred in the command '{}'"
                          "".format(ctx.command.qualified_name), exc_info=error.original)
            message = ("An error occurred in the command ``{}``. Please contact the bot admins ASAP."
                       "".format(ctx.command.qualified_name))
            await ctx.send(message)
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Hey, I'm sorry, but I can't let you do that!")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("You can't execute this command in Direct Messages!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("This command is on cooldown. "
                           "Try again in {:.2f}s"
                           "".format(error.retry_after))
        else:
            self.bot.logger.exception(error)

def setup(bot):
    bot.load_module(Events)