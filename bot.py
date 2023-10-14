import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6355149697:AAFJ6YfbbSSnFho40jot049KyM87OQo-V_4")

API_ID = int(os.environ.get("API_ID", "24111429"))

API_HASH = os.environ.get("API_HASH", "41c451e7412d4225f0a5450a166bcf7a")

STRING = os.environ.get("STRING", "BQFv6UUAgbT2vZ9mYKXOMlBkURN9qiMwd_LfjKa6sCO0crgxFG6G_65L2C5-nQO5lQKgwbO2F2_Vg8noySqMUWZ8tDRurBtn7Qbb0Q4xcNaQ7x4V-D5bii3bOfqYUTWAP-s0mimHn4sHz_rBpuZ4-mIZrw4t4MGlhd7clW6UMO3FxIFV6-v4rKBqMyqWxKcBHTq28DYzwe26cYYsO_Lr1kyPdGQ855EHSV5-rD6F5TnZYAhNlH2sK_Jg_xcaBHwWDYfZONZQImlbbZHQc7mVwknGUB16lpRlt3U9LeKcDxIwzw65tqFK7QyE7937ZqZ4IiX9anAA9m8QmY5p7r8HwssadvmWnQAAAAFpXGZ7AA")



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
