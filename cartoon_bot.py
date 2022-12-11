# Import necessary libraries
from telethon import TelegramClient, sync, events
from telethon.tl.enums import MessageParseMode
from telethon.sync import Client
from PIL import Image

# Set BOT_TOKEN and API ID/HASH as environment variables
import os

bot_token = os.environ['BOT_TOKEN']
api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']

# Create a client for your bot
client = Client('cartoon_bot', api_id, api_hash, parse_mode=MessageParseMode.MARKDOWNV2)

# Start the client
client.start(bot_token=bot_token)

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
client.run_until_disconnected()
