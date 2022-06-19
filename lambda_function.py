import telebot
import os

TRIBE_CHAT_ID = os.environ['TRIBE_CHAT_ID']
BOT_TOKEN = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

def lambda_handler(event, context):
    bot.send_message(TRIBE_CHAT_ID, "TEST")

    return {
        'statusCode': 200,
        'body': "Message sent"
    }