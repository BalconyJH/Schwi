import random
from nonebot import on_keyword
import os
from utils.message_builder import image
from configs.path_config import IMAGE_PATH
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, MessageEvent
from nonebot.adapters.cqhttp.permission import GROUP
from utils.utils import FreqLimiter
from configs.config import NICKNAME


__zx_plugin_name__ = "基本设置 [Hidden]"
__plugin_usage__ = "用法： 无"
__plugin_version__ = 0.1
__plugin_author__ = 'BalconyJH'


_flmt = FreqLimiter(300)


self_introduction = on_command(
    "自我介绍", aliases={"介绍", "你是谁", "你叫什么"}, rule=to_me(), priority=5, block=True
)


@self_introduction.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    if NICKNAME.find('休比') != -1:
        result = (
            "我叫休比\n编号为Üc207Pr4f57t9\n"
            "你们可以叫我休比，哪怕你们叫我机机我也能接受！\n"
            "年龄的话——我为什么要告诉你这个！\n"
            "身高保密！！！\n"
            "我生日是在7月4号, 能记住的话我会很高兴的\n"
            "可以的话请和我多说说话！\n" + image("xiubi")
        )
        await self_introduction.finish(result)


my_wife = on_keyword({"老婆"}, rule=to_me(), priority=5, block=True)


@my_wife.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):
    await my_wife.finish(image("laopo.jpg", "other"))