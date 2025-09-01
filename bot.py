from pyrogram import Client,filters
import re
from ytmusicapi import YTMusic
import deezer
from pydeezer import Deezer,Downloader
from pydeezer.constants import track_formats
import os
import shutil
import glob

api_id=123456
api_hash="1626636shhshhshhd"
bot_token="166263:AAG9YLmHwbCaEfUZFTuSGCdNqAm83GDyZmw"

app = Client(":memory:",api_id,api_hash,bot_token=bot_token)

@app.on_message(filters.private & filters.private & filters.user(14072628005946))
def hello(client, message):
    message.reply_chat_action("typing")
    text=message.text
    url=re.search("(?P<url>https?://[^\s]+)", text).group("url")
    starti = url.find("=") + len("=")
    endi  = url.find("&")
    id = url[starti:endi]
    ytmusic = YTMusic()
    a=ytmusic.get_song(videoId=id)
    b=a["title"]
    starta = b.find("") + len("")
    enda  = b.find("-")
    c = b[starta:enda]
    d=c.split()
    e=d[0]
    try:
        f=d[1]
    except:
        f=""
    if f=="ft" or f=="Ft" or f=="feat" or f=="Feat" or f=="ft." or f=="Ft." or f=="feat." or f=="Feat." or f=="&":
    	artist=e
    else:
    	artist=e+" "+f
    g=b.split("-")
    h=g[1]
    i=h.split()
    name=i[0]
    client = deezer.Client()
    j=client.advanced_search({"artist":artist,"track":name})
    try:
        song=j[0]
        track_id=song.id
        arl = "26662gshdhhs366#6#6hsg"
        teezer = Deezer(arl=arl)
        track = teezer.get_track(track_id)
        cd=os.getcwd()
        try:
            os.mkdir("Music")
        except:
            pass
        download_dir = os.path.join(cd,"Music")
        message.reply_chat_action("record_audio")
        track["download"](download_dir, quality=track_formats.MP3_320)
        files = glob.glob(os.path.join(download_dir, '*.mp3'))
        path=files[0]
        message.reply_chat_action("upload_audio")
        message.reply_audio(path,quote=True)
        shutil.rmtree(download_dir)
    except:
        message.reply_text(h)
    
app.run()
