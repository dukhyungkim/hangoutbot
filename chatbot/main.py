#!/usr/bin/env python3
from flask import Flask, request, json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def on_event():
    text = ''
    event = request.get_json()

    print(event)

    username = event['user']['displayName']

    if event['type'] == 'ADDED_TO_SPACE':
        if event['space']['type'] == 'ROOM':
            room_name = event['space']['displayName']
            text = '"%s"에 초대해줘서 고맙다!' % room_name
        elif event['space']['type'] == 'DM':
            text = '안녕 "%s"!' % username

    elif event['type'] == 'MESSAGE':
        if event['space']['type'] == 'ROOM':
            message = event['message']['argumentText'].lstrip()
            text = '%s이(가) `%s`(이)라고 말했어.' % (username, message)
        elif event['space']['type'] == 'DM':
            message = event['message']['text']
            text = '넌 이렇게 말했지.. "%s"' % message

    return json.jsonify({'text': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
