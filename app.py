from flask import Flask, render_template
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import threading
import time

app = Flask(__name__)

api_id = '26401329'
api_hash = '96d89beca5696a77e0cc4e3c7c0ffe4c'
phone = '+923551996176'
user_name = "ENM"

def update_name(client):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        client(UpdateProfileRequest(first_name=f'{user_name} {current_time}'))
        time.sleep(60)

def start_telegram_client():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start(phone)
    update_name(client)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=start_telegram_client).start()
    app.run(debug=True)