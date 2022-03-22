from telegram.ext import Updater
from telethon import TelegramClient, events
from multiprocessing import Pool


token = '5283138692:AAGjcpBJHr0FNm6kDfmIVQ4rrcg3v8oK6rU'
api_id = '18665558'
api_hash = 'a1a528f2d5dc2f8aa3a4372facc51e70'

updater = Updater(token, use_context=True)
updater.start_polling()

pool = Pool(2)

try:
    client = TelegramClient('anon', api_id, api_hash)
    print('[SYSTEM]: Ligado com Sucesso! @JF_00Bot')
    
    @client.on(events.NewMessage(chats='Test'))
    async def my_event_handler(event):
        pool.apply()
        updater.bot.send_message(chat_id='-1001233482542', text=event.raw_text)
        print(f'[SYSTEM]: Mensagem enviada: {event.raw_text}')
        
except:
    print('[SYSTEM]: ERROR #06 se isso persistir chamar o desenvolvedor Natã#0711')
    
client.start(bot_token=token)

client.run_until_disconnected()