"""Emoji
Available Commands:
.rahul_immortal
Credits to @rahul_immortal
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("rahul_immortal"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "rahul_immortal":
    await event.edit("@rahul_immortal")
    animation_chars = [
            "@rahul_immortal tera baap hu"               ,
            "Isme koi shak nhi 😎"                       ,
            "apun hai is bot ka creator"                 ,
            "main tere sath hu aur kya chahyiye tujhe😎" ,
    
           
           
          
           
            


            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
