
import sys
import csv
import traceback
import time
import random
from telethon import TelegramClient, events, sync

api_id = #your api_id
api_hash = ''#your api_hash

client = TelegramClient('session_name', api_id, api_hash)
client.start()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

word = "کامپیوتر"#keyword you want to find
channel_username = 'channelName'  # your channel
for message in client.get_messages(channel_username, limit=10):
    # print(message.message)
    m = message.message
    if (m.find(word) != -1):
        client.send_message('+19997773333', m)
        break
