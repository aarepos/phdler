from __future__ import unicode_literals
from pyrogram import Client, filters
import youtube_dl


def downloadYT(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


@app.on_message(filters=filters.command("DYT"))
def downloadAndSendVideo(client, message):
    chat_id = message.chat.id
    url = message.command[1]
    video = downloadYT(url)
    client.send_video(
        chat_id=chat_id,
        video="Havanna Winter-9wZqI0JKKhk.mp4"
    )



