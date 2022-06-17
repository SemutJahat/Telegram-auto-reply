from telethon import TelegramClient
import asyncio
import time
from telethon import events

# get from my.telegram.org/apps
api_id = 'api_id'
api_hash = 'api_hash'

client = TelegramClient('username', api_id, api_hash)

def res1():
    return "Response 1\n\n--AutoReply--"
def res2():
    return "Response 2\n\n--AutoReply--"
def res3():
    return "Response 3\n\n--AutoReply--"

switcher = {
    1: res1,
    2: res2,
    3: res3
}

def switch(msg):
    return switcher.get(msg)()
    

def main():

    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if 'pattern1' in event.message.message:
            time.sleep(1)
            await event.respond(switch(1))
        elif 'pattern2' in event.message.message:
            time.sleep(1)
            await event.respond(switch(2))
        elif 'pattern3' in event.message.message:
            time.sleep(1)
            await event.respond(switch(2))
        elif 'pattern4' in event.message.message:
            time.sleep(1)
            await event.respond(switch(3))
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
