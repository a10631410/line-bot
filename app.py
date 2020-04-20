
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('exCxhQD6tEEHvms/HceXqg3clsd/mFhGr1ihMWOkEp/bvYC6dj854CzaysAYG3mlUL935NHozaV4JCGGgjX+75aVGDT8hAw6nWPGQOt/6sWfJcifrsobfHyTEC3OYa3qpDpD/L1R7ZaxT3zx6MrKfgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c5b91864e463f89852fb190268dbbcc1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
   


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '這個我也不知道欸嘻嘻，你可能要親自問張宇嫻ㄛ'
    if '啦啦' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23'
        )
    elif '晚安' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='26'
        )
     line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return
    if '吃'in msg:
        r = '我最愛吃了 尤其是義大利麵跟甜點!'
    elif msg == '你是誰':
        r = '我是可愛的兔兔兼張宇嫻的分身~'
    elif msg in ['hi', 'Hi', '嗨']:
        r = '哈囉XD'
    elif '嘻' in msg:
        r = '哼~'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
