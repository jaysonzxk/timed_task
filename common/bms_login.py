import requests


def get_token():
    url = "http://192.168.0.201:8041/auth/oauth/token"

    payload='username=miya&password=123456&code=1111&grant_type=password&scope=server'
    headers = {
      'Authorization': 'Basic cGlnOnBpZw==',
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    access_token = response['token_type'] + ' ' + response['access_token']
    return access_token


if __name__ == '__main__':
    res = get_token()
    print(res)