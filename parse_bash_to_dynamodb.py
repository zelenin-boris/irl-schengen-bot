import boto3
from bs4 import BeautifulSoup
import requests

client = boto3.client('dynamodb')


def parse_quotes():
    url = "https://xn--80abh7bk0c.xn--p1ai/random"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    all_quotes = soup.find_all("div", class_="quote__body")
    return filter(lambda q: bool(q.text != ""), all_quotes)


def save_quotes(quotes):
    for index, quote in enumerate(quotes):
        client.put_item(
                TableName='quote',
                Item={
                    'quote_id': {
                        'N': str(index)
                    },
                    'text': {
                        'S': quote.text.strip()
                    }
                }
        )


def print_quotes(quotes):
    for index, quote in enumerate(quotes):
        print("[" + str(index) + "]" + "{" + quote.text.strip() + "}")

# print_quotes(parse_quotes())
