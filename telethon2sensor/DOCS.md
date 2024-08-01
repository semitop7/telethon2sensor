# Telethon2Sensor

This addon is designed to integrate Telegram with the Home Assistant. 

First of all, it is developed for one specific case - when your energy company uses the Telegram bot for advance notification of a temporary power outage.
It allows you to listen to chatbot messages, parse the data about the start of the blackout, and then send a notification to the Home Assistant and create a sensor to set the date of the start of the blackout.
With this new sensor, you can easily set up Home Assistant automation to prepare for a blackout.

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

### Required: `debug`

> Enable debug mode.  Check the log tab for output.
___

## Additional Documentation

For more information, please refer to the following:

- Github repository: [Telethon](https://github.com/LonamiWebs/Telethon)