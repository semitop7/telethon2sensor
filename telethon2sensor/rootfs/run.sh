#!/usr/bin/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: Telethon2Sensor
# Telegram chatbot messages listener for Home Assistant.
# ==============================================================================

bashio::log.info 'Reading configuration settings...'

API_ID=$(bashio::config 'api_id')
API_HASH=$(bashio::config 'api_hash')
CHAT_BOT_USERNAME=$(bashio::config 'chat_bot_username')

# Setup Auto-Configuration if values are not set.

if [ $(bashio::config 'debug') == true ]; then
	export DEBUG=true
	bashio::log.info 'Debug mode is enabled.'
fi

args=()

bashio::log.info 'Starting telethon-to-sensor...'
bashio::log.info "Directory $(dirname "$0")"
args+=( \
	--api_id ${API_ID} \
	--api_hash ${API_HASH} \
	--chat_bot_username ${CHAT_BOT_USERNAME} \
	--ha_token ${SUPERVISOR_TOKEN})
python $(dirname "$0")/telethon-to-sensor.py ${args[@]}