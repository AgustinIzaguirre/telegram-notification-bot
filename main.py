import urllib, requests, time
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def main():
    for i in range(0, 10):
        send_notification("Notification " + str(i + 1))
        time.sleep(10)


def send_notification(message):
    url = prepare_url(message)
    _ = requests.get(url, timeout=10)


def prepare_url(message):
    url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % \
          (TOKEN, CHAT_ID, urllib.parse.quote(message, safe=' '))
    return url


if __name__ == "__main__":
    main()