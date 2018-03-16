from discord.ext import commands


class CustomContext(commands.Context):
    async def send_help(self):
        command = self.invoked_subcommand or self.command
        pages = await self.bot.formatter.format_help_for(self, command)
        ret = []
        for page in pages:
            ret.append(await super().send(page))
        return ret