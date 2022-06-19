import telebot
import os

tribe_chat_id = -1001657506369
BOT_TOKEN = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

def lambda_handler(event, context):
    bot.send_message(tribe_chat_id, "TEST")
    return {
        'statusCode': 200
    }