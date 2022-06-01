import os

from .. import bot as Beast

from config import Config

from functions.forcesub import handle_force_subscribe

from telethon import events, Button, TelegramClient

from pyrogram import idle

from main.plugins.main import Bot, userbot

st = "Hoi Buddy 🤖 __Send me Link of any message to clone it here, For private channel message, Send invite link first.__\n\nDEV: @Be4STX"

@Beast.on(events.NewMessage(incoming=True, pattern="/start"))

async def start(bot, update):

    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
    if fsub == 400:
        return

    await update.reply(f'{st}', 

                      buttons=[

                              [Button.inline("🆕 SET THUMBNAIL.", data="set"),

                               Button.inline("❗ REMOVE THUMBNAIL.", data="rem")]

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

    

@Beast.on(events.callbackquery.CallbackQuery(data="set"))

async def sett(update, bot):    

    Drone = update.client                    

    button = await update.get_message()

    msg = await button.get_reply_message() 

    await update.delete()

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

        t = await update.client.send_message(event.chat_id, 'Trying.')

        path = await update.client.download_media(x.media)

        if os.path.exists(f'{update.sender_id}.jpg'):

            os.remove(f'{update.sender_id}.jpg')

        os.rename(path, f'./{update.sender_id}.jpg')

        await t.edit("Temporary thumbnail saved!")

        

@Beast.on(events.callbackquery.CallbackQuery(data="rem"))

async def remt(update, bot):  

    Drone = update.client            

    await event.edit('Trying ⌛.')

    try:

        os.remove(f'{event.sender_id}.jpg')

        await update.edit('Removed ❗')

    except Exception:

        await update.edit("No thumbnail saved 🤧.")                        

    

    

