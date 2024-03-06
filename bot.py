import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6355149697:AAFJ6YfbbSSnFho40jot049KyM87OQo-V_4")

API_ID = int(os.environ.get("API_ID", "22489880"))

API_HASH = os.environ.get("API_HASH", "03496096c94747bf692313e368c5b74e")

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
