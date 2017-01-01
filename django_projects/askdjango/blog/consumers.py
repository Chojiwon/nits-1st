import json
import time
from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from channels.sessions import channel_session


# Connected to websocket.connect
@channel_session_user_from_http  # http session 을 channel session 으로 이동
def ws_connect(message, post_pk):
    # message.user
    group = Group('post-{}'.format(post_pk))
    group.add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_message(message, post_pk):
    # message.content  # dict
    # - {'text': '{"text":"3423"}', 'reply_channel': 'websocket.send!ZBuZwnkqIeNi',
    #    'order': 1, 'path': '/blog/20/chat/'}
    # message.user
    print(message.content)

    obj = json.loads(message.content['text'])

    group = Group('post-{}'.format(post_pk))
    group.send({
        'text': json.dumps({
            'username': message.user.username,
            'chat_text': obj['chat_text'],
        }),
    })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message, post_pk):
    group = Group('post-{}'.format(post_pk))
    group.discard(message.reply_channel)

