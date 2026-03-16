import argparse
import asyncio
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import aiohttp
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# -------------------------------
# Parse command-line arguments
# -------------------------------
parser = argparse.ArgumentParser(description='Telegram messages listener for Home Assistant.')
parser.add_argument('--api_id', required=True, help='API ID for Telegram client')
parser.add_argument('--api_hash', required=True, help='API Hash for Telegram client')
parser.add_argument('--api_session', required=True, help='API string session for Telegram client')
parser.add_argument('--chat_bot_username', required=True, help='Username of the bot to listen to')
parser.add_argument('--confirmation_message', required=True, help='Home Assistant notification message')
parser.add_argument('--ha_token', required=True, help='Home Assistant Long-Lived Access Token')
parser.add_argument('--timezone', default='Europe/Kiev', help='Server timezone for automation')
args = parser.parse_args()

# -------------------------------
# Constants
# -------------------------------
API_ID = args.api_id
API_HASH = args.api_hash
API_STRING_SESSION = args.api_session
CHAT_BOT_USERNAME = args.chat_bot_username
CONFIRMATION_MESSAGE = args.confirmation_message
HA_BASE_URL = 'http://supervisor/core/api'
HA_TOKEN = args.ha_token
SERVER_TZ = ZoneInfo(args.timezone)
KEYWORDS = ['відсутня електроенергія', 'відключення']

NOTIFICATION_URL = f'{HA_BASE_URL}/services/persistent_notification/create'
HTTP_SENSOR_URL = f'{HA_BASE_URL}/states/sensor.datetime_scheduled'

HEADERS = {
    'Authorization': f'Bearer {HA_TOKEN}',
    'content-type': 'application/json',
}

# -------------------------------
# Telegram client
# -------------------------------
client = TelegramClient(StringSession(API_STRING_SESSION), API_ID, API_HASH)

# -------------------------------
# Helper functions
# -------------------------------
async def send_notification(session, message, title):
    data = {'message': message.replace('\\n', '\n'), 'title': title}
    async with session.post(NOTIFICATION_URL, json=data) as resp:
        if 200 <= resp.status <= 202:
            print('Confirmation message sent to Home Assistant')
        else:
            text = await resp.text()
            print(f'Failed to send confirmation message: {text}')

async def create_sensor(session, automation_time: datetime):
    sensor_body = {
        "state": automation_time.isoformat(),
        "attributes": {"friendly_name": "AC200MAX Turn on AC inverter at time"}
    }
    async with session.post(HTTP_SENSOR_URL, json=sensor_body) as resp:
        if 200 <= resp.status <= 202:
            print('Automation created/updated successfully.')
            # Send notification
            automation_time_str = automation_time.strftime("%Y-%m-%d %H:%M")
            confirmation_message = CONFIRMATION_MESSAGE.format(time=automation_time_str)
            await send_notification(session, confirmation_message, 'Automation Created')
        else:
            text = await resp.text()
            print(f'Failed to create automation: {text}')

# -------------------------------
# Main async function
# -------------------------------
async def main():
    bot = await client.get_entity(CHAT_BOT_USERNAME)

    async with aiohttp.ClientSession(headers=HEADERS) as session:

        @client.on(events.NewMessage(chats=bot))
        async def handler(event):
            message = event.message.message.lower()
            if any(keyword.lower() in message for keyword in KEYWORDS):
                match = re.search(r'з (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2})', message)
                if match:
                    start_time_str = match.group(1).strip()
                    start_time = datetime.strptime(start_time_str, '%d.%m.%Y %H:%M')
                    start_time = start_time.replace(tzinfo=SERVER_TZ)
                    print(f'Start time automation: {start_time}')
                    await create_sensor(session, start_time)

        print('Listening for new messages...')
        await client.run_until_disconnected()

# -------------------------------
# Entry point
# -------------------------------
async def run():
    async with client:
        await main()

if __name__ == "__main__":
    asyncio.run(run())