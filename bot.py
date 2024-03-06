import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6355149697:AAFJ6YfbbSSnFho40jot049KyM87OQo-V_4")

API_ID = int(os.environ.get("API_ID", "24111429"))

API_HASH = os.environ.get("API_HASH", "41c451e7412d4225f0a5450a166bcf7a")

STRING = os.environ.get("STRING", "BQFv6UUAxagBgU6YTfjqLDNTaNS1aN0dqfGop1Q_mVb0VT3JyXn82GZkxLodD6uMwAgp7lQHV23a9huWjOaHlzDBEFt811w-zuE6Iwi1JwTA59mgeQ30byOuCiancGmE0n0bjv6HPwsi526toliL6ynM1lwNiBIeU-SbMfrbssuGEVjGh9gLsiN1JE6ZKES-h88ow7VVAhyttm2dBC-rhDTCrBgGW1v3okXC0Xq9ytRQFRHzkKxVq-TtC4eTA_RlsVe9BOONN_LE4F_R4BZ4A5wnTCnUnbgsTIvjWfyrP3Rl5d6loqtdxWlVDlGKSoePbUcT0m6e1V2Ju6ItW2VJDtf8WzISnAAAAAFpXGZ7AA")



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
