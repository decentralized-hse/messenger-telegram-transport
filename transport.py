import requests
import base64
import json
import argparse


def _create_parser():
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS, add_help=False)
    subparsers = parser.add_subparsers(title='transport method', dest='method')
    send_parser = subparsers.add_parser(
        'send', description='send message', usage=argparse.SUPPRESS, add_help=False
    )
    send_parser.add_argument(
        '-t', '--token', required=True, help='Telegram bot token'
    )
    send_parser.add_argument(
        '-f', '--from_id', required=True, help='Sender name'
    )
    send_parser.add_argument(
        '-c', '--content', required=True, help='Message content'
    )
    send_parser.add_argument(
        '-n', '--name', required=True, help='Channel name'
    )
    read_parser = subparsers.add_parser(
        'read', description='read message', usage=argparse.SUPPRESS, add_help=False
    )
    read_parser.add_argument(
        '-n', '--name', required=True, help='Telegram channel name for lookup'
    )
    return parser


def send(bot_token, from_id, content, chan_name):
    to_send = {
        'f': from_id,
        'c': content
    }
    chan_name = '@{}'.format(chan_name)
    base_link = 'https://api.telegram.org/bot{}/sendMessage'
    message = base64.b64encode(json.dumps(to_send).encode('ascii'))
    response = requests.post(
        url=base_link.format(bot_token),
        data={
            'chat_id': chan_name,
            'text': message
        }
    )
    if response.status_code != 200:
        raise RuntimeError("Telegram Bot API Error: {}".format(response.status_code))


def read(chan_name):
    response = requests.get(url='https://t.me/s/{0}'.format(chan_name)).text
    response = response.split('<div class="tgme_widget_message_text js-message_text" dir="auto">')[-1]
    response = response.split('</div>')[0]
    decoded_message = json.loads(base64.b64decode(response).decode('ascii'))
    from_id, content = decoded_message['f'], decoded_message['c']
    print('Got message from {0}: {1}'.format(from_id, content))
    return from_id, content


if __name__ == '__main__':
    parser = _create_parser()
    args = parser.parse_args()
    if args.method == 'send':
        send(args.token, args.from_id, args.content, args.name)
    else:
        read(args.name)
