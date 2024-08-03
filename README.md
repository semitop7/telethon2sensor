[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua/)

![HA Lviv PowerOff Logo](https://github.com/tsdaemon/ha-lviv-poweroff/blob/827c15582bb64c70568f6f7b322e926feeaa2592/icons/icon.png?raw=true)

# ⚡️ Telethon2Sensor
Home Assistant Add-on for send notification and create sensor by Telegram chatbot messages listener by [Telethon](https://github.com/LonamiWebs/Telethon) python library. First of all, this application was developed to interact with the Telegram bot from the energy company [LvivOblEnergo](https://loe.lviv.ua/), but it can be adapted for other Telegram bots.

![update-badge](https://img.shields.io/github/last-commit/semitop7/telethon2sensor?label=Last%20Updated)

## Installation
To add this repository to Home Assistant use the badge below:

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fsemitop7%2Ftelethon2sensor)

or add it manually by navigating to `Settings` > `Add-ons` > `Add-on Store`

Select the three dot menu in the upper right, choose `Repositories`, and add the following url:
```
https://github.com/semitop7/telethon2sensor
```

Refresh the page (hard refresh may be required), scroll down to Telethon2Sensor and install the add-on.

## Creating your Telegram Application

Follow instructions here [documentation](https://core.telegram.org/api/obtaining_api_id).
Then you will have access to the data about the application (App api_id, App api_hash), which is required for the addon.

## Generate Telegram String Session
For generate telegram string session
Use ./utils/session_generator.py

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

## Usage

This integration is configurable via UI.

For testing go to you Telegram chat bot chat and send message like

```
Шановний клієнте!
На період з 03.08.2024 12:00 до 14:00 заплановані стабілізаційні відключення (застосування ГПВ).
```

Go to **Home Assistant** and check **Notifications**.

![Notification](https://github.com/semitop7/telethon2sensor/blob/main/pics/notification.png?raw=true)

Go to **Home Assistant** -> **Developer Tools** -> **TEMPLATE** tab and check sensor value.

```
{{ states('sensor.datetime_scheduled') }}
```

![Sensor](https://github.com/semitop7/telethon2sensor/blob/main/pics/sensor.png?raw=true)

Then you can use this sensor in ***Home Assistant Automations*** in template trigger. 

```
{% set scheduled_time_3_min_before = as_datetime(states('sensor.datetime_scheduled'), '1987-01-01T00:00:00+03:00' | as_datetime ) - timedelta(minutes=3) %}

{% if scheduled_time_3_min_before <= now() <= scheduled_time_3_min_before + timedelta(minutes=1) %}true{% endif %}
```

## Add-ons

This repository contains the following add-ons:

### [Telethon2Sensor](./telethon2sensor)

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg

_Telegram chatbot messages listener for Home Assistant._
