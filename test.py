import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


HEADER = {
    'Content-type': 'application/json',
    'Authorization': F'Bearer {config.get("line-bot", "channel_access_token")}'
}

url = "https://api.line.me/v2/bot/message/reply"

payload = {
    "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "messages": [
        {
            "type": "text",
            "text": "Hello, user"
        },
        {
            "type": "text",
            "text": "May I help you?"
        }
    ]
}
res = requests.post(url, headers=HEADER, data=json.dumps(payload))
print(res.text)
