import json
from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from channels.sessions import channel_session


@channel_session_user_from_http
def ws_connect(message, post_pk):
    # message.user
    group = Group('post-{}'.format(post_pk))
    group.add(message.reply_channel)


@channel_session_user
def ws_message(message, post_pk):

    obj = json.loads(message.content['text'])

    group = Group('post-{}'.format(post_pk))
    group.send({
        'text': json.dumps({
            'username': message.user.username,
            'chat_text': obj['chat_text'],
        }),
    })


@channel_session_user
def ws_disconnect(message, post_pk):
    group = Group('post-{}'.format(post_pk))
    group.discard(message.reply_channel)

