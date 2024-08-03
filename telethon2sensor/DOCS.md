# Telethon2Sensor

This addon is designed to integrate Telegram with the Home Assistant. 

First of all, it is developed for one specific case - when your energy company uses the Telegram bot for advance notification of a temporary power outage.
It allows you to listen to chatbot messages, parse the data about the start of the blackout, and then send a notification to the Home Assistant and create a sensor to set the date of the start of the blackout.
With this new sensor, you can easily set up Home Assistant automation to prepare for a blackout.

# Creating your Telegram Application

Follow instructions here [documentation](https://core.telegram.org/api/obtaining_api_id).
Then you will have access to the data about the application (App api_id, App api_hash), which is required for the addon.

## Generate Telegram String Session
For generate telegram string session
Use ./utils/session_generator.py, see here [Telethon2Sensor](https://github.com/semitop7/telethon2sensor).

Require python and telethon library

```
pip install telethon==1.36.0
python ./utils/session_generator.py
```

If script successfully run you will see request for input. Follow input steps to generate telegram string session.

```
Enter your API_ID : 
```

After finished all steps check telegram "Saved Messages" chat to find you telegram string session.

___

## Configuration

### Required: `api_id`

> Telegram application id.

### Required: `api_hash`

> Telegram application hash.

### Required: `api_session`

> Telegram string session.

### Required: `chat_bot_username`

> Telegram chat name.

### Required: `confirmation_message`

> Home Assistant notification message template.

### Required: `debug`

> Enable debug mode.  Check the log tab for output.
___

## Additional Documentation

For more information, please refer to the following:

- Github repository: [Telethon2Sensor](https://github.com/semitop7/telethon2sensor)