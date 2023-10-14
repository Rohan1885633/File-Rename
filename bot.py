import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6355149697:AAFJ6YfbbSSnFho40jot049KyM87OQo-V_4")

API_ID = int(os.environ.get("API_ID", "24111429"))

API_HASH = os.environ.get("API_HASH", "41c451e7412d4225f0a5450a166bcf7a")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
