from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = int(input("Enter your API_ID : "))
API_HASH = input("Enter your API_HASH : ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    session_str = client.session.save()
    msg = client.send_message("me", f"`{session_str}`")
    msg.reply("This is your telethon session string.")

print("\nCheck your saved messages for the Telethon String Session")
