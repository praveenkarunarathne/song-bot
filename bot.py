from pyrogram import Client,filters
import re
from ytmusicapi import YTMusic
import deezer
from pydeezer import Deezer
import os
import shutil

api_id=2940667
api_hash="8590c88aca3638eb321979577ddb53d3"
bot_token="1846486129:AAG9YLmHwbCaEfUZFTuSGCdNqAm83GDyZmw"

app = Client(":memory:",api_id,api_hash,bot_token=bot_token)

@app.on_message(filters.private & filters.private & filters.user(1407800946))
def hello(client, message):
    message.reply_chat_action("typing")
    text=message.text
    url=re.search("(?P<url>https?://[^\s]+)", text).group("url")
    starti = url.find("=") + len("=")
    endi  = url.find("&")
    id = url[starti:endi]
    a=YTMusic.get_song(videoId=id)
    b=a["title"]
    starta = b.find("") + len("")
    enda  = b.find("-")
    c = b[starta:enda]
    d=c.split()
    e=d[0]
    f=d[1]
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
    song=j[0]
    track_id=song.id
    arl = "5896d2a9fc5b0e010aa4c2795cb9933ba70d4ef518bc565907a7f2f168ed893749eb4c898ab35628428f486c87a8a814c3241be83c43668352e3a3914cbd35bbb055a3d35ab332bf8780354c142bfdd37f84e89156c674c2521ff4c9349c692d"
    deezer = Deezer(arl=arl)
    track = deezer.get_track(track_id)
    cd=os.getcwd()
    os.mkdir("Music")
    download_dir = os.path.join(cd,"Music")
    message.reply_chat_action("record_audio")
    track["download"](download_dir, quality=track_formats.MP3_320)
    k=os.listdir(download_dir)
    sname=k[0]
    path=os.path.join(download_dir,sname)
    message.reply_chat_action("upload_audio")
    message.reply_audio(path,quote=True,caption=sname)
    shutil.rmtree(download_dir)
    
app.run()
