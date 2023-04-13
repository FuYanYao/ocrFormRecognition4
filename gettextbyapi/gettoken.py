import requests
import json


def gettoken():
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=NBIgOasZyKm3Gwc9hmKe8QHP&client_secret=zFciPmvu1cgHk1C6Ct2P5LXeo1FfkCFS&grant_type=client_credentials"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)["access_token"]


if __name__ == '__main__':
    gettoken()



