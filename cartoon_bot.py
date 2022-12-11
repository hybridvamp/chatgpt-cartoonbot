import logging
import threading
import asyncio

#from func import game_id, send_score, game_link, check_is_digit, get_checksum, get_token

from telethon import TelegramClient, events, Button
from telethon.events import StopPropagation, NewMessage
from telethon import TelegramClient
from asyncio.exceptions import TimeoutError


# CONFIG
logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
)
log = logging.getLogger("cartoon")
log.info("\n\nStarting...\n")

try:
    bot_token = config("BOT_TOKEN")
    AUTH = [int(i) for i in config("AUTH_USERS").split(" ")]
except Exception as e:
    log.exception(e)
    exit(1)

# connecting the client
try:
    bot = TelegramClient(None, 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
        bot_token=bot_token
    )
except Exception as e:
    log.exception(e)
    exit(1)

# Handle the /start command
@client.on_event(events.NewMessage(pattern='/start'))
async def handle_start_command(event):
    # Send a welcome message to the user
    await event.respond('Hello! I am a cartoon bot. Send me an image and I will convert it to a cartoon for you.')

# Handle the /help command
@client.on_event(events.NewMessage(pattern='/help'))
async def handle_help_command(event):
    # Send a help message to the user
    await event.respond('To use this bot, simply send an image and I will convert it to a cartoon for you.\n\nYou can also use the /start command to get a welcome message.')

# Handle the message event
@client.on(events.NewMessage)
async def handle_message(message):
    # Check if the message contains an image
    if message.photo:
        # Download the image
        image = await message.download_media()
        
        # Convert the image to a cartoon using PIL library
        img = Image.open(image)
        img = img.convert('P', palette=Image.ADAPTIVE, colors=8)
        
        # Save the converted image
        img.save('cartoon.png')
        
        # Send the converted image back to the user
        await client.send_file(message.to_id, 'cartoon.png')

        # Delete the image from storage
        os.remove('cartoon.png')

# Run the bot until interrupted
log.info("Bot has started.\n(c) @HYBRID_VAMP")
bot.run_until_disconnected()