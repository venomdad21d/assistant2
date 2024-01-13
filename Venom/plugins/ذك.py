import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from SourceZe import mody
from . import mody
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


# code by t.me/ELHYBA
@mody.ar_cmd(pattern="زد إي(?: |$)(.*)")
async def mody_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@V4JRBOT" #code by t.me/ELHYBA
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**𓆰بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**𓆰مثـــال :**\n`.ريفز من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/ELHYBA
        mody = zzz.text
    if not event.reply_to_msg_id: #code by t.me/ELHYBA
        mody = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**𓆰جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n𓆰الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/ELHYBA
        try:
            await conv.send_message(mody)
            sourceze = await conv.get_response()
            ahmed = sourceze.text
            if "another 8 seconds" in sourceze.text: #code by t.me/ELHYBA
                aa = ahmed.replace("⏳ Please wait another 30 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            ze = await conv.get_response()
            malath = ze.text
            if "understanding" in ze.text: #code by t.me/ELHYBA
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {mody}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@Source_Ze • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/ELHYBA
            await mody(unblock("V4JRBOT"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(mody)
            sourceze = await conv.get_response()
            ahmed = sourceze.text
            if "another 8 seconds" in sourceze.text: #code by t.me/ELHYBA
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            ze = await conv.get_response()
            malath = ze.text
            if "understanding" in ze.text: #code by t.me/ELHYBA
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in ze.text: #code by t.me/ELHYBA
                await asyncio.sleep(5)
                ze = await conv.get_response()
                malath = ze.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {mody}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@Source_Ze • ᴼᵖᵉⁿᴬᴵ")


# تخمــط اهينـــك Fuk-You

# code by t.me/ELHYBA
@mody.ar_cmd(pattern="ذك(?: |$)(.*)")
async def mody_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@V4JRBOT" #code by t.me/ELHYBA
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**𓆰بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**𓆰مثـــال :**\n`.ريفز من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/ELHYBA
        mody = zzz.text
    if not event.reply_to_msg_id: #code by t.me/ELHYBA
        mody = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**𓆰جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n𓆰الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/ELHYBA
        try:
            await conv.send_message(mody)
            sourceze = await conv.get_response()
            ahmed = sourceze.text
            if "another 8 seconds" in sourceze.text: #code by t.me/ELHYBA
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            ze = await conv.get_response()
            malath = ze.text
            if "understanding" in ze.text: #code by t.me/ELHYBA
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in ze.text: #code by t.me/ELHYBA
                await asyncio.sleep(5)
                ze = await conv.get_response()
                malath = ze.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {mody}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@Source_Ze • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/ELHYBA
            await mody(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(mody)
            sourceze = await conv.get_response()
            ahmed = sourceze.text
            if "another 8 seconds" in sourceze.text: #code by t.me/ELHYBA
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**𓆰يُرجى الانتظار 8 ثوانٍ ⏳\n𓆰بين إرسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            ze = await conv.get_response()
            malath = ze.text
            if "understanding" in ze.text: #code by t.me/ELHYBA
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذرًا .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**السؤال : {mody}\n\n{malath}**\n\n───────────────────\n𝐙𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓**** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t@Source_Ze • ᴼᵖᵉⁿᴬᴵ")
