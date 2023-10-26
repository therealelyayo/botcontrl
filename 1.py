import paramiko
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
SERVER_IP = 'YOUR_SERVER_IP'
SERVER_PORT = 22
USERNAME = 'YOUR_SERVER_USERNAME'
PASSWORD = 'YOUR_SERVER_PASSWORD'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        command = msg['text']

        try:
            ssh.connect(SERVER_IP, SERVER_PORT, USERNAME, PASSWORD)
            stdin, stdout, stderr = ssh.exec_command(command)
            stdout.flush()
            stderr.flush()

            server_response = stdout.read().decode('utf-8')
            if not server_response:
                server_response = stderr.read().decode('utf-8')

            bot.sendMessage(chat_id, server_response)

        except Exception as e:
            bot.sendMessage(chat_id, str(e))

        finally:
            ssh.close()

MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)
