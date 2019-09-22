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

line_bot_api = LineBotApi('QPbdjZugpGl0WpGXy3b5QS2n5CYXPIGL4SZueo6eCYDFOxcY9UVg28kwKDmdJe7UlfYlvuqnYYVhRCLRSY6BwLanxHqwXyJ9aZPRMBUv1j9FTJkckcT43w2iTIB9BrJysrBLaxOnXnfl3t1N6PpBKAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('63425eec6ea7a2153c27a0ca0fc768a1')


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
    s = '母鯊大，公鯊?'

    if msg in ['給我貼圖', '貼圖', 'sticker']:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        
    if msg in ['哈囉', 'hi', 'Hi']:
        s = '哈囉模投'
    elif msg in ['你是誰', '你是']:
        s = '大家好，我是人工智障機器人'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=s
        ))
        return


if __name__ == "__main__":
    app.run()