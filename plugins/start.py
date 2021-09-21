from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup


@Client.on_message(filters.command('start'))
def start(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id,
        "please choose",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["Download from YT", "Download from PH"],  # First row
                ["Communication with Admin(A-Group)"]  # second row
            ],
            resize_keyboard=True
        )
    )
