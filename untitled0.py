from flask import Flask, request
import telepot

secret = "alds{fjpaowe7pq8934wfj"
bot = telepot.Bot('1226664082:AAFGs9AJPGWCuyelft8xBpYhZ8XklvkR_bE')
bot.setWebhook("https://ajayk.pythonanywhere.com/{}".format(secret), max_connections=50)

app = Flask(__name__)
chat_id=0
@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]
    if "message" in update:
        if(text =='/start'):
            bot.sendMessage(chat_id,"Welcome to my bot ... Please type the Phone and its specs In English 😁 "  )
            # bot.sendMessage(chat_id,tr())
             
    return "OK"
