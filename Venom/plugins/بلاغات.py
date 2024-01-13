# ar-Thon - ZelZal
# Copyright (C) 2023 Source_Ze . All Rights Reserved
#
# PLease read the GNU Affero General Public License in
""" 
Abuse Notifications for Ze™ t.me/Source_Ze
Write file by مودي الهيبه t.me/ELHYBA
ها خماط بعدك تخمط مني .. ماتستحي ؟
متى راح تصير مطور وانت مقضيها خمط تعب وحقوق الناس
ههههههههههههههههههههههههههههههههههههههههههههههههههههههه
"""

import asyncio
import base64
import contextlib

from telethon.errors.rpcerrorlist import ForbiddenError
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from SourceZe import mody

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, unsavegif
from ..helpers.utils import _arutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "الخدمات"
UNSPAM = gvarstatus("Z_UNSPAM") or "ايقاف البلاغ"


# code by t.me/ELHYBA
async def spam_abusear(event, sandy, ar, sleeptimem, sleeptimet, DelaySpam=False):
    # sourcery no-metrics
    counter = int(ar[0])
    if len(ar) == 2:
        spam_message = str(ar[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message('@AbuseNotifications', spam_message) # code by t.me/ELHYBA
            await asyncio.sleep(4)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message('@AbuseNotifications', spam_message) # code by t.me/ELHYBA
            await asyncio.sleep(4)
    else:
        return
    if DelaySpam is not True: # code by t.me/ELHYBA
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**- البلاغـات 📌**\n"
                + f"**- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات**\n"
                + f"**- كليشـة البلاغـات :**\n `{spam_message}`",
            )
            await event.client.send_message(event.chat_id, f"**- بلاغـات_ داخليـه 🚸\n- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات\n- كليشـة البلاغـات :**\n `{spam_message}`")

    elif BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**- البلاغـات 📌**\n"
            + f"**- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات**\n**- وقت التكـرار :** {sleeptimet} **ثانيـه**\n"
            + f"**- كليشـة البلاغـات :**\n `{spam_message}`",
        )
        await event.client.send_message(event.chat_id, f"**- بلاغـات_ داخليـه 🚸\n- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات\n- كليشـة البلاغـات :**\n `{spam_message}`")


# code by t.me/ELHYBA
@mody.ar_cmd(pattern="بلاغ ([\s\S]*)")
async def spammer(event):
    sandy = await event.get_reply_message()
    ar = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(ar[0])
    except Exception:
        return await edit_delete(
            event, "**- ارسـل الامـر بالشكـل التالي**\n\n`.بلاغ` **+ عدد التكرار + الرسالة او بالـرد ع رسالة**\n**- مثـال : .بلاغ 12 بالـرد ع كليشـة البـلاغ**"
        )
    if counter > 50:
        sleeptimet = 4
        sleeptimem = 1
    else:
        sleeptimet = 4
        sleeptimem = 0.3
    await edit_delete(event, f"**⎉╎جـارِ الابـلاغ الداخلـي . . . ⚠️ \n⎉╎لـ الدعم @AbuseNotifications\n⎉╎عـدد البلاغـات ** {ar}", 5)
    addgvar("spamwork", True)
    await spam_abusear(event, sandy, ar, sleeptimem, sleeptimet)


# code by t.me/ELHYBA
@mody.ar_cmd(pattern=f"{UNSPAM} ?(.*)",)
async def spammer(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "**- تم ايقـاف البلاغـات .. بنجـاح ✅**")
    return await edit_delete(event, "**- لايوجـد هنـاك بلاغـات لـ إيقافهـا ؟!**")



