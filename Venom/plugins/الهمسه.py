from telethon import events
from asyncio import sleep
import os, sys, random, re
from zthon import mody
from ..core.managers import edit_delete, edit_or_reply
 

@mody.ar_cmd(pattern="همسة ?(.*)")
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@SI1UBOT"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()
    
