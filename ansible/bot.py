import requests
import os
# import boturl
from bottle import (
    run, post, response, request as bottle_request
)

# BOT_URL = boturl.BOT_URL
BOT_URL = 'https://api.telegram.org/bot5276323822:AAE8vWnpziUFpyvunwxPOeFacZp3OzQKPaA/'

def get_chat_id(data):
    chat_id = data['message']['chat']['id']
    return chat_id

def get_message(data):
    """
    Method to extract message id from telegram request.
    """
    message_text = data['message']['text']
    return message_text

def send_message(data):
    """
    Prepared data should be json which includes at least `chat_id` and `text`.
    """
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=data)

def reponse_for_answer(data):
    answer = "done"

    json_data = {
        "chat_id": get_chat_id(data),
        "text": answer,
    }
    return json_data

@post('/')
def main():
    data = bottle_request.json
    query = get_message(data)
    answer_data = reponse_for_answer(data)

    if query == "test":
        send_message(answer_data)
    elif query == "start nginx":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml nginx/nginx-start.yml --connection=local")
        send_message(answer_data)
    elif query == "stop nginx":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml nginx/nginx-stop.yml --connection=local")
        send_message(answer_data)
    elif query == "start mysql":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml mysql/mysql-start.yml --connection=local")
        send_message(answer_data)
    elif query == "stop mysql":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml mysql/mysql-stop.yml --connection=local")
        send_message(answer_data)
    elif query == "start cron":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml cron/cron-start.yml --connection=local")
        send_message(answer_data)
    elif query == "stop cron":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml cron/cron-stop.yml --connection=local")
        send_message(answer_data)
    elif query == "start php8":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml php8/php8-start.yml --connection=local")
        send_message(answer_data)
    elif query == "stop php8":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml php8/php8-stop.yml --connection=local")
        send_message(answer_data)
    elif query == "start postgresql":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml postgresql/postgresql-start.yml --connection=local")
        send_message(answer_data)
    elif query == "stop postgresql":
        os.system("cd ~/ajk/ansible && ansible-playbook -i inventory.yml postgresql/postgresql-stop.yml --connection=local")
        send_message(answer_data)

    return response


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)