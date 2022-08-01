from sys import api_version
from telegram.client import Telegram
from telegram.client import AuthorizationState
import time

### ADD ACCOUNT HERE ###
tg = Telegram(api_id="14568556",
              api_hash="4d1ba4f7e664ed2ff20d2d62f0b21dc3",
              phone="+639758809691",
              database_encryption_key="change123")
state = tg.login()

tg2 = Telegram(api_id="11155815",
              api_hash="b6738ff55d04a7d0790ff8f7a1a4775e",
              phone="+639758814842",
              database_encryption_key="change123")
state2 = tg2.login()

tg3 = Telegram(api_id="19561163",
              api_hash="c8c8562a6a323f5fd84e32af241d2efb",
              phone="+639758809742",
              database_encryption_key="change123")
state3 = tg3.login()

tg4 = Telegram(api_id="18438928",
              api_hash="184cae2c347626ef18a8b26ab0722337",
              phone="+639758813062",
              database_encryption_key="change123")
state4 = tg4.login()

tg5 = Telegram(api_id="13264842",
              api_hash="3416647da74b66c6f4c563399e55d2bc",
              phone="+639758809720",
              database_encryption_key="change123")
state5 = tg5.login()

if state == AuthorizationState.READY and state2 == AuthorizationState.READY:
    account_dictionary = {
                        "tg":tg,
                        "tg2":tg2,
                        "tg3":tg3,
                        "tg4":tg4,
                        "tg5":tg5               
                        }

    messages = [
                    ["tg", "so cool", 10],
                    ["tg2", "so cool", 10],
                    ["tg3", "so cool", 10],
                    ["tg4", "so cool", 10],
                    ["tg5", "so cool", 10],
        ]

    while True:
            for data in messages: 
                account, message, seconds = data[0], data[1], data[2]
                tgaccount = account_dictionary[account]
                result1 = tgaccount.get_chats()
                result1.wait()
                result = tgaccount.send_message(chat_id="-1001520502632", text=message,)
                result.wait()
                time.sleep(seconds)
