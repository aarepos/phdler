from pyrogram import Client, filters

@Client.on_message()
def get_pornhub_link(client, message):

    url = message.text
    message.reply_text(str(message))
    # if 'pornhub.com' not in url:
    #     return

    # message.reply_text('I got your url, Thank you.')