#الملف بحقوق سورس فينوم @Ve_No_m_S 
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from SourceZe import mody
from ..helpers.utils import reply_id


@mody.on(admin_cmd(outgoing=True, pattern="آيه قصيره."))
async def jepvois(vois):
  rl = random.randint(111,210)
  url = f"https://t.me/UIEITI/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @Ve_No_m_S 🌺",parse_mode="html")
  await vois.delete()


@mody.on(admin_cmd(outgoing=True, pattern="سوره الفاتحة$"))
async def jepvois(Voice):
  url = f"https://t.me/Ve_No_m_S/894"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ سوره الفاتحة\n⎊︙ بصوت القارئ ماهر المعيقلي\n⎊︙ BY : @Ve_No_m_S 🌺",parse_mode="html")
  await Voice.delete()
