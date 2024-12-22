from bot import SpyGameBot
import os
from dotenv import load_dotenv
load_dotenv()

# create a bot instance and run it
bot = SpyGameBot(token=os.getenv("BOT_TOKEN"))
bot.run()
