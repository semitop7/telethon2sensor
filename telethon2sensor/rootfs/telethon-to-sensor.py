import argparse
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
import requests
import re
from datetime import datetime

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Telegram chatbot messages listener for Home Assistant.')
parser.add_argument('--api_id', required=True, help='API ID for Telegram client')
parser.add_argument('--api_hash', required=True, help='API Hash for Telegram client')
parser.add_argument('--api_session', required=True, help='API string session for Telegram client')
parser.add_argument('--chat_bot_username', required=True, help='Username of the bot to listen to')
parser.add_argument('--confirmation_message', required=True, help='Home Assistant notification message')
parser.add_argument('--ha_token', required=True, help='Home Assistant Long-Lived Access Token')
args = parser.parse_args()

# Constants
API_ID = args.api_id
API_HASH = args.api_hash
API_STRING_SESSION = args.api_session
CHAT_BOT_USERNAME = args.chat_bot_username
CONFIRMATION_MESSAGE = args.confirmation_message
HA_BASE_URL = 'http://supervisor/core/api'
HA_TOKEN = args.ha_token
KEYWORDS = ['відсутня електроенергія', 'відключення']

NOTIFICATION_URL = f'{HA_BASE_URL}/services/persistent_notification/create'
HTTP_SENSOR_URL = f'{HA_BASE_URL}/states/sensor.datetime_scheduled'

HEADERS = {
    'Authorization': f'Bearer {HA_TOKEN}',
    'content-type': 'application/json',
}

client = TelegramClient(StringSession(API_STRING_SESSION), API_ID, API_HASH)


def send_notification(message, title):
    data = {
        'message': message.replace('\\n', '\n'),
        'title': title,
    }
    response = requests.post(NOTIFICATION_URL, json=data, headers=HEADERS)

    if response.status_code == 200:
        print('Confirmation message sent to Home Assistant')
    else:
        print(f'Failed to send confirmation message: {response.text}')


def create_sensor(automation_time):
    sensor_body = {
        "state": automation_time.isoformat(),
        "attributes": {
            "friendly_name": "AC200MAX Turn on AC inverter at time"
        }
    }

    response = requests.post(HTTP_SENSOR_URL, json=sensor_body, headers=HEADERS)

    if 200 <= response.status_code <= 202:
        print('Automation created/updated successfully.')

        # Send notification
        automation_time_str = automation_time.strftime("%Y-%m-%d %H:%M")
        confirmation_message = CONFIRMATION_MESSAGE.format(time=automation_time_str)
        send_notification(confirmation_message, 'Automation Created')
    else:
        print(f'Failed to create automation: {response.text}')


async def main():
    bot = await client.get_entity(CHAT_BOT_USERNAME)

    @client.on(events.NewMessage(chats=bot))
    async def handler(event):
        message = event.message.message

        if any(keyword in message for keyword in KEYWORDS):
            # Parse message
            match = re.search(r'з (\d{2}:\d{2})(?: до (\d{2}:\d{2}))?', message)
            if match:
                start_time_str = match.group(1)

                start_time = datetime.strptime(start_time_str, '%d.%m.%Y %H:%M')

                server_timezone = datetime.now().astimezone().tzinfo
                start_time = start_time.replace(tzinfo=server_timezone)

                print(f'Start time automation: {start_time}')

                # Create sensor
                create_sensor(start_time)

    print('Listening for new messages...')
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
