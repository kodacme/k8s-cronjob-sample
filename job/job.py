import json
import os

import requests

SLACK_API_URL = os.getenv('SLACK_WEBHOOK_URL')


def execute():
    params = {'text': 'Hello Slack'}
    headers = {'Content-type': 'application/json'}
    requests.post(url=SLACK_API_URL, data=json.dumps(params), headers=headers)


if __name__ == '__main__':
    execute()
