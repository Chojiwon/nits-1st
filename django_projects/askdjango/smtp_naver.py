import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askdjango.settings')

import django
django.setup()

import smtplib
from getpass import getpass
from django.template.loader import render_to_string


def main():
    sender = 'allieuslee@naver.com'  # FIXME
    receiver = 'ask@festi.kr'  # FIXME
    password = getpass('Enter Password : ')

    server = smtplib.SMTP_SSL('smtp.naver.com', 465)
    server.login(sender, password)

    rendered = render_to_string('signup_welcome.txt', {
        'name': '이진석',   # FIXME
        'when': '2016년 12월 5일',   # FIXME
    })
    lines = rendered.splitlines()
    subject = lines[0]
    content = '\n'.join(lines[1:])

    body = '''To: {}
From: {}
Subject: {}
{}'''.format(receiver, sender, subject, content)

    server.sendmail(sender, [receiver], body.encode('utf8'))
    server.quit()

    print('sended!')

if __name__ == '__main__':
    main()
