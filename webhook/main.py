import requests
import json

URL = ""

def main():
    text = "test"
    data = json.dumps({'text': text})
    response = requests.post(URL, data=data)
    print(response)


if __name__ == '__main__':
    main()
