from parse_bash import get_quote
from telegram import send
from notifications import get_nyc_move_string
from notifications import get_doggo_birthday_string


def lambda_handler(event, context):
    quote = get_quote()

    # send(quote["text"])
    # delete(quote["quote_id"])

    send(quote)
    send(get_nyc_move_string())

    doggo = get_doggo_birthday_string()
    if doggo:
        send(doggo)

    response = {
        'statusCode': 200
    }

    return response
