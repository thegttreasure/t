#Github.com/Vasusen-code

import os

from .. import bot as Worker

from telethon import events, Button, TelegramClient

from config import Config

from pyrogram import idle

from translation import Translation

from main.plugins.main import Bot, userbot

st = "Hoi Buddy ðŸ¤– __Send me Link of any message to clone it here, For private channel message, Send invite link first.__\n\nDEV: @TheCyberWeapon"

@Worker.on(events.NewMessage(incoming=True, pattern="/start"))

async def start(event):
    if str(update.from_user.id) not in Config.AUTH:
        bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NOT_AUTH_USER_TEXT,
            reply_to_message_id=update.message_id
        )
        return
    await event.reply(f'{st}', 

                      buttons=[

                              [Button.inline("SET THUMB.", data="set"),

                               Button.inline("REM THUMB.", data="rem")]

                              ])

    try:

        await Bot.start()

        await userbot.start()

        await idle()

    except Exception as e:

        if 'Client is already connected' in str(e):

            pass

        else:

            return

    

@Worker.on(events.callbackquery.CallbackQuery(data="set"))

async def sett(event):    

    Drone = event.client                    

    button = await event.get_message()

    msg = await button.get_reply_message() 

    await event.delete()

    async with Drone.conversation(event.chat_id) as conv: 

        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")

        x = await conv.get_reply()

        if not x.media:

            xx.edit("No media found.")

        mime = x.file.mime_type

        if not 'png' in mime:

            if not 'jpg' in mime:

                if not 'jpeg' in mime:

                    return await xx.edit("No image found.")

        await xx.delete()

        t = await event.client.send_message(event.chat_id, 'Trying.')

        path = await event.client.download_media(x.media)

        if os.path.exists(f'{event.sender_id}.jpg'):

            os.remove(f'{event.sender_id}.jpg')

        os.rename(path, f'./{event.sender_id}.jpg')

        await t.edit("Temporary thumbnail saved!")

        

@Worker.on(events.callbackquery.CallbackQuery(data="rem"))

async def remt(event):  

    Drone = event.client            

    await event.edit('Trying.')

    try:

        os.remove(f'{event.sender_id}.jpg')

        await event.edit('Removed!')

    except Exception:

        await event.edit("No thumbnail saved.")                        

    

    

