import json
from channels import Group
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http, http_session
from channels.sessions import channel_session


@channel_session_user_from_http
def ws_connect(message, post_pk):
    # message.user
    group = Group('post-{}'.format(post_pk))
    group.add(message.reply_channel)

    # 접속 유저의 http 세션키로서, 유저별 세션 Group을 생성합니다.
    session_key = message.http_session.session_key
    message.channel_session['session_group_name'] = 'session-{}'.format(session_key)
    group = Group(message.channel_session['session_group_name'])
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


@http_session
@channel_session_user
def ws_disconnect(message, post_pk):
    group = Group('post-{}'.format(post_pk))
    group.discard(message.reply_channel)

    group = Group(message.channel_session['session_group_name'])
    group.discard(message.reply_channel)

