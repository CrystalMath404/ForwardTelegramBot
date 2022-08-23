from pyrogram import Client
from pyrogram import filters
import config

ACCOUNT = config.acc
PHONE = config.phone
API_ID = config.api_id 
API_HASH = config.hash_id
SOURCE_CHAT = config.source_chat
TARGET_CHAT = config.target_chat

app = Client(
    ACCOUNT,
    phone_number=PHONE,
    api_id=API_ID,
    api_hash=API_HASH
)

filters.chat(SOURCE_CHAT)
@app.on_message(filters.chat(SOURCE_CHAT))
def my_handler(client, message):
    message.copy(  # copy() so there's no "forwarded from" header
        chat_id=TARGET_CHAT,  # the channel you want to post to
        caption="Copied from XYZ"  # Caption
    )
'''Uncomment this and comment the funcrion above to get all your chats values'''
# @app.on_message()
# def my_handler(client, message):
#     print(message)

if __name__ == '__main__':
    app.run()