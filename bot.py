import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6736577527:AAFOV3FnWhdMAKPC5DmJ3iEG9Ffm99uYzvo")

API_ID = int(os.environ.get("API_ID", "21593885"))

API_HASH = os.environ.get("API_HASH", "66c868b925a30a3deb21c300a69d1425")

STRING = os.environ.get("STRING", "BQFJfx0AdbB-zrKmh8DmfYoY88e9giXyavSHYecaBvi_xKxp-kOIUEqaY9q07l7t6yINDKHBkM3QBK3BgOe_RKCCAJsBbmTd4SHHU65y4nWXKRBJMquAFmBdhbLHfNox9mhOpbWfRETRTyriAiYCxpyC6LnanAl-MYFGzcmxRR2_9vNL0i4sVZmSVK1hEQzyIwO4qolLadvF0Rx9qXJ-dYngOlyYzphnGQT4b-EnaWTQ3m2mfdQCQ4kf4c-kyjCv24CnP5JKkGz9f64Q7kwhnBbjl5QNNsqxew_MvpstYS-t4M24qXHfdImrqI815oEMdv_6htTlt1zpggbc4Ad81uVLA4_ezQAAAABNuQNpAA")



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
