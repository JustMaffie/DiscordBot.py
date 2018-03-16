# Setup logging
import logging,logging.handlers,sys;FORMAT='[%(levelname)s] [%(name)s] [%(asctime)s]: %(message)s';logger=logging.getLogger("DiscordBot");format=logging.Formatter(FORMAT, datefmt="%d/%m/%Y %H:%M");stdout_handler=logging.StreamHandler(sys.stdout);stdout_handler.setFormatter(format);fhandler=logging.handlers.RotatingFileHandler(filename='main.log',encoding='utf-8',mode='a',maxBytes=10**7,backupCount=5);fhandler.setFormatter(format);logger.addHandler(stdout_handler);logger.addHandler(fhandler)

# Try to use uvloop if available
try:
    import asyncio
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except:
    # UVLoop can't be imported, it probably isn't installed, you are probably on Windows, UVLoop is optional but recommended for production instances
    logger.warn("UVLoop can't be imported, UVLoop is optional but recommended.")

logger.setLevel(logging.INFO)

from discordbot import make_bot

bot = make_bot(logger)

try:
    bot.run_bot()
except KeyboardInterrupt:
    bot.shutdown()