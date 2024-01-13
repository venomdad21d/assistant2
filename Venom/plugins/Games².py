#تم اضافة الالعاب بواسطة سورس زد إي @Source_Ze
import asyncio
from collections import deque
from random import choice

from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from SourceZe import mody 
from ..core.managers import edit_delete, edit_or_reply

async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call

def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]

R = [
    "𓆰العـاب الاحترافيه²** 🎮𓆪 \n"
    "  ❶ ⪼  [SQUARES](https://t.me/gamee?game=Squares)   \n"
    "  ❷ ⪼  [CORSAIRS](https://t.me/gamebot?game=Corsairs)   \n"
    "  ❸ ⪼  [Little Plane](https://t.me/gamee?game=LittlePlane)   \n"
    "  ❹ ⪼  [ATOMIC](https://t.me/gamee?game=AtomicDrop1)   \n"
    "  ❺ ⪼  [LumberJack](https://t.me/gamebot?game=LumberJack)   \n"
    "  ❻ ⪼  [RollerDisco](https://t.me/gamee?game=RollerDisco)   \n"
    "  ❼ ⪼  [GravityNinja](https://t.me/gamee?game=GravityNinjaEmeraldCity)   \n"
    "  ❽ ⪼  [Astrocat](https://t.me/gamee?game=Astrocat)   \n"
    "  ❾ ⪼  [WorldCup](https://t.me/gamee?game=PocketWorldCup)   \n"
    "  ❿ ⪼  [Ten2One](https://t.me/gamee?game=Ten2One)   \n"
    "  ⓫ ⪼  [Paintio](https://t.me/gamee?game=Paintio)   \n"
    "  ⓬ ⪼  [BrickStacker](https://t.me/gamee?game=BrickStacker)   \n"
    "  ⓭ ⪼  [LoadTheVan](https://t.me/gamee?game=LoadTheVan)   \n"
    "  ⓮ ⪼  [GravityNinja21](https://t.me/gamee?game=GravityNinja21)   \n"
    "  ⓯ ⪼  [PaintioTeams](https://t.me/gamee?game=PaintioTeams)   \n"
    "  ⓰ ⪼  [SunshineSolitaire](https://t.me/gamee?game=SunshineSolitaire)   \n"
    "  ⓱ ⪼  [PenaltyShooter2](https://t.me/gamee?game=PenaltyShooter2)   \n"
    "  ⓲ ⪼  [GroovySki](https://t.me/gamee?game=GroovySki)   \n"
    "  ⓳ ⪼  [SpaceTraveler](https://t.me/gamee?game=SpaceTraveler)   \n"
    "⎊ مطور السورس **⪼ [ᯓ𓆩˹ َتــــٓــايــــٓــســــٓــون ،ِّّ⸙⛥َٰ⏤͟͟͞͞𓆃](t.me/S_Ml10)   \n"
    "⎊ قناة السورس **⪼ [Source V](t.me/Ve_No_m_S)   "
]

@mody.on(admin_cmd(pattern="الالعاب2$"))
async def ithker(knopis):
    await knopis.edit(choice(R))
