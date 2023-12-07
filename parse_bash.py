from bs4 import BeautifulSoup
import requests


def get_quote():
    url = "https://xn--80abh7bk0c.xn--p1ai/random"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    quote = soup.find("div", class_="quote__body")
    return '\n'.join(quote.stripped_strings)


def print_quote():
    print(get_quote())

# print_quote()
