import os
from telethon import TelegramClient, events
import random
import textimage


BOT_TOKEN = os.environ['BOT_TOKEN']
API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

def random_catfile():
    number = random.randint(1, 9)
    return(f'cats/cat{number}.jpg')
    
@bot.on(events.NewMessage(pattern='/start|привет|Привет|hi|Hi'))
async def start(event):
    """Send a message when the command /start is issued or user say hi."""
    await event.respond('Привет! Я высылаю случаные картинки котов в ответ на твои сообщения!')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='всё|все|Всё|Все|all|All'))
async def echoall(event):
    """Echo all drop."""
    await event.respond(file=textimage.text_to_image(random_catfile(), f'{event.sender.first_name}, проснись, мы всё уронили!'))
    raise events.StopPropagation
    
@bot.on(events.NewMessage(pattern='2021|ZOZI|zozi|2K21|2k21|НГ|Новый год|новый год'))
async def echony(event):
    """Echo new year"""
    await event.respond(file=textimage.text_to_image(random_catfile(), 'Мы подняли 2021 год!'))
    raise events.StopPropagation    

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message + drop."""
    await event.respond(file=textimage.text_to_image(random_catfile(), f'Мы уронили {event.text}'))
   

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()

