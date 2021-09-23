from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup


@Client.on_message(filters.command('start'))
def start(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id,
        "لطفا دستور/DYTسپس لینک را وارد کنید مانند زیر \n /DYT https:\\....."
    )
