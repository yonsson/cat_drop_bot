import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
import random

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

def random_catfile():
    number = random.randint(1, 4)
    return(f'cat{number}.jpg')
    
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Привет! Я высылаю случаные картинки котов в ответ на твои сообщения!')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='всё|все|Всё|Все|all|All'))
async def echoall(event):
    """Echo the user message."""
    await event.respond(message=f'Наташ, проснись, мы всё уронили!', file=random_catfile())
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    await event.respond(message=f'Мы уронили {event.text}', file=random_catfile())
        

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
