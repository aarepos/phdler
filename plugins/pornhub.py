from pyrogram import Client, filters
r = "^(https://)?(www.)?pornhub.com/.*viewkey=.*$"

@Client.on_message(filters.private & filters.regex(r))
def get_pornhub_link(client, message):

    pass
    