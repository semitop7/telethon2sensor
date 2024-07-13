#!/usr/bin/with-contenv bashio
# ==============================================================================
# Home Assistant Add-on: Telethon2Sensor
# Telegram chatbot messages listener for Home Assistant.
# ==============================================================================

bashio::log.info 'Reading configuration settings...'

API_ID=$(bashio::config 'api_id')
API_HASH=$(bashio::config 'api_hash')
API_SESSION_FILE_PATH=$(bashio::config 'api_session_file_path')
CHAT_BOT_USERNAME=$(bashio::config 'chat_bot_username')

# Setup Auto-Configuration if values are not set.

if [ $(bashio::config 'debug') == true ]; then
	export DEBUG=true
	bashio::log.info 'Debug mode is enabled.'
fi

args=()

bashio::log.info 'Starting telethon-to-sensor...'
args+=( \
	--api_id ${API_ID} \
	--api_hash ${API_HASH} \
	--api_session_file_path ${API_SESSION_FILE_PATH} \
	--chat_bot_username ${CHAT_BOT_USERNAME} \
	--ha_token ${SUPERVISOR_TOKEN})
python telethon-to-sensor.py ${args[@]}