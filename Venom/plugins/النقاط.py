import requests
import asyncio
import time
import re
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest

from SourceZe import mody
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import reply_id
estithmar = False
ratp = False
thifts = False
bahsees = False

@mody.ar_cmd(pattern="بوت الجنرال$")
async def _(event):
    await event.edit('@MARKTEBOT')

# Copyright (C) 2023 Ze . All Rights Reserved
@mody.ar_cmd(pattern="الجنرال(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @MARKTEBOT**")
    channel_entity = await mody.get_entity('@MARKTEBOT')
    await mody.send_message('@MARKTEBOT', '/start')
    await asyncio.sleep(3)
    msg0 = await mody.get_messages('@MARKTEBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(3)
    msg1 = await mody.get_messages('@MARKTEBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(2)
        list = await mody(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await mody.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف": #Code by T.me/ELHYBA
            await mody.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await mody(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await mody(ImportChatInviteRequest(bott))
            msg2 = await mody.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/ELHYBA
            msg2 = await mody.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await mody.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@mody.ar_cmd(pattern="بوت المليون$")
async def _(event):
    await event.edit('@qweqwe1919bot')

# Copyright (C) 2023 Ze . All Rights Reserved
@mody.ar_cmd(pattern="المليون(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @qweqwe1919bot**")
    channel_entity = await mody.get_entity('@qweqwe1919bot')
    await mody.send_message('@qweqwe1919bot', '/start')
    await asyncio.sleep(3)
    msg0 = await mody.get_messages('@qweqwe1919bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(3)
    msg1 = await mody.get_messages('@qweqwe1919bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(2)
        list = await mody(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await mody.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف": #Code by T.me/ELHYBA
            await mody.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await mody(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await mody(ImportChatInviteRequest(bott))
            msg2 = await mody.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/ELHYBA
            msg2 = await mody.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await mody.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@mody.ar_cmd(pattern="بوت سمسم$")
async def _(event):
    await event.edit('@SMSMWAbot')

# Copyright (C) 2023 Ze . All Rights Reserved
@mody.ar_cmd(pattern="سمسم(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @SMSMWAbot**")
    channel_entity = await mody.get_entity('@SMSMWAbot')
    await mody.send_message('@SMSMWAbot', '/start')
    await asyncio.sleep(3)
    msgz = await mody.get_messages('@SMSMWAbot', limit=1)
    await msgz[0].click(0)
    await asyncio.sleep(3)
    msg0 = await mody.get_messages('@SMSMWAbot', limit=1)
    await msg0[0].click(3)
    await asyncio.sleep(3)
    msg1 = await mody.get_messages('@SMSMWAbot', limit=1)
    await msg1[0].click(1)
    chs = 1
    for i in range(100):
        await asyncio.sleep(2)
        list = await mody(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await mody.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف": #Code by T.me/ELHYBA
            await mody.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await mody(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await mody(ImportChatInviteRequest(bott))
            msg2 = await mody.get_messages('@SMSMWAbot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/ELHYBA
            msg2 = await mody.get_messages('@SMSMWAbot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await mody.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@mody.ar_cmd(pattern="بوت تناهيد$")
async def _(event):
    await event.edit('@Ncoe_bot')

# Copyright (C) 2023 Ze . All Rights Reserved
@mody.ar_cmd(pattern="تناهيد(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @Ncoe_bot**")
    channel_entity = await mody.get_entity('@Ncoe_bot')
    await mody.send_message('@Ncoe_bot', '/start')
    await asyncio.sleep(3)
    msg0 = await mody.get_messages('@Ncoe_bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(3)
    msg1 = await mody.get_messages('@Ncoe_bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(2)
        list = await mody(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await mody.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف": #Code by T.me/ELHYBA
            await mody.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await mody(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await mody(ImportChatInviteRequest(bott))
            msg2 = await mody.get_messages('@Ncoe_bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/ELHYBA
            msg2 = await mody.get_messages('@Ncoe_bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await mody.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@mody.ar_cmd(pattern="بوت دعمكم$")
async def _(event):
    await event.edit('@DamKombot')

# Copyright (C) 20233 Ze . All Rights Reserved
@mody.ar_cmd(pattern="دعمكم(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @DamKombot**")
    channel_entity = await mody.get_entity('@DamKombot')
    await mody.send_message('@DamKombot', '/start')
    await asyncio.sleep(3)
    msg0 = await mody.get_messages('@DamKombot', limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(3)
    msg1 = await mody.get_messages('@DamKombot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(3)
        list = await mody(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await mody.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف": #Code by T.me/ELHYBA
            await mody.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        msg_text = msgs.message
        if "اشترك فالقناة @" in msg_text:
            the_channel = msg_text.split('@')[1].split()[0]
            try:
                entity = await mody.get_entity(the_channel)
                if entity:
                    await mody(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await mody.get_messages(bot_username6, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    chs += 1
                    await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
            except:
                await mody.send_message(event.chat_id, f"**⎉╎خطـأ , يمكـن تبنـدت ؟!**")
                break
    await mody.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@mody.ar_cmd(pattern="بوت التجميع$")
async def _(event):
    zpoint = gvarstatus("Z_Point")
    if gvarstatus("Z_Point") is None:
        await event.edit("**⎉╎لايوجـد بوت تجميع مضاف بعـد ؟!**\n\n**⎉╎لـ اضافة بوت تجميع جديد**\n**⎉╎ارسـل**  `.اضف بوت التجميع`  **بالـرد ع معـرف البـوت**")
    else:
        await event.edit(f"**⎉╎بوت التجميـع المضـاف حاليـاً**\n**⎉╎هـو** {zpoint}")

# Copyright (C) 2023 Ze . All Rights Reserved
@mody.ar_cmd(pattern="تجميع(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    zpoint = gvarstatus("Z_Point")
    if con in ("المليار", "الجوكر", "الجنرال", "العقاب", "المليون", "سمسم", "تناهيد", "العرب"):
        return await event.edit("**⎉╎عـذراً .. عـزيـزي امـر خاطـئ .\n⎉╎لـ رؤيـة اوامـر التجميـع ارسـل**\n\n`.اوامر التجميع`")
    if gvarstatus("Z_Point") is None:
        return await event.edit("**⎉╎لايوجـد بـوت تجميـع مضـاف للفـارات ؟!\n⎉╎لـ اضافة بـوت تجميـع\n⎉╎ارسـل** `.اضف بوت التجميع` **بالـرد ع معـرف البـوت\n\n⎉╎او استخـدم امر تجميع** `.المليار`")
    await event.edit(f"**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء {zpoint} .**")
    channel_entity = await mody.get_entity(zpoint)
    await mody.send_message(zpoint, '/start')
    await asyncio.sleep(3)
    msg0 = await mody.get_messages(zpoint, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(3)
    msg1 = await mody.get_messages(zpoint, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(2)
        list = await mody(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await mody.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف": #Code by T.me/ELHYBA
            await mody.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await mody(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await mody(ImportChatInviteRequest(bott))
            msg2 = await mody.get_messages(zpoint, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/ELHYBA
            msg2 = await mody.get_messages(zpoint, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await mody.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")
