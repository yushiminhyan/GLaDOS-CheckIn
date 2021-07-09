import os
import requests
import json
import telegram

COOKIES = os.getenv('COOKIES')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telegram.Bot(token=BOT_TOKEN)


def report_success(msg: str, left_days: str):
    bot.send_message(
        CHAT_ID,
        '--------------------\n'
        'GLaDOS CheckIn\n'
        'Msg: ' + msg + '\n' +
        'Left days: ' + str(left_days) + '\n' +
        '--------------------'
    )


def report_cookies_expired():
    bot.send_message(
        CHAT_ID,
        '--------------------\n'
        'GLaDOS CheckIn\n'
        'Msg: Your cookies are expired!\n'
        '--------------------'
    )


def report_checkin_error(msg: str):
    bot.send_message(
        CHAT_ID,
        '--------------------\n'
        'GLaDOS CheckIn\n'
        'Msg: Check in error!\n'
        'Error: ' + msg + '\n' +
        '--------------------'
    )


def report_env_error(msg: str):
    bot.send_message(
        CHAT_ID,
        '--------------------\n'
        'GLaDOS CheckIn\n'
        'Msg: Running environment error!\n'
        'Error: ' + msg + '\n' +
        '--------------------'
    )


def check_in():
    check_in_url = "https://glados.rocks/api/user/checkin"
    status_url = "https://glados.rocks/api/user/status"
    origin_url = "https://glados.rocks"
    referer_url = "https://glados.rocks/console/checkin"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {'token': 'glados_network'}

    check_in_response = requests.post(
        check_in_url,
        headers={'cookie': COOKIES,
                 'referer': referer_url,
                 'origin': origin_url,
                 'user-agent': user_agent,
                 'content-type': 'application/json;charset=UTF-8'},
        data=json.dumps(payload)
    )

    check_in_msg = check_in_response.json()['message']
    check_in_response.close()

    if check_in_msg == '\u6ca1\u6709\u6743\u9650':
        report_cookies_expired()
        return

    status_response = requests.get(
        status_url,
        headers={'cookie': COOKIES,
                 'referer': referer_url,
                 'origin': origin_url,
                 'user-agent': user_agent}
    )

    left_days = status_response.json()['data']['leftDays'].split('.')[0]
    status_response.close()

    report_success(check_in_msg, left_days)


def main():
    try:
        check_in()
    except BaseException as e:
        report_checkin_error(str(e))


if __name__ == '__main__':
    try:
        if COOKIES is None:
            raise EnvironmentError('Environment COOKIES not found!')
        elif BOT_TOKEN is None:
            raise EnvironmentError('Environment BOT_TOKEN not found!')
        elif CHAT_ID is None:
            raise EnvironmentError('Environment CHAT_ID not found!')
        else:
            main()
    except BaseException as err:
        report_env_error(str(err))
