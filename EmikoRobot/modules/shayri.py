import random
import asyncio
from pyrogram import filters
from EmikoRobot import pbot



"""
    |----╒════════════╕----|
          |  Kang with credits |
          |----- Coded by: ----|
          |       @Cute_Boy701      |
          |----(2142595466)----|
          |      on telegram   |
    |----╘════════════╛----|
"""

ROMANTIC_STRINGS = [
                     'Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...',
                     'Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...',
                     'Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...',
                     'Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...',
                     'Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...',
                     'Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...',
                     'Udas shamo me wo lout\nKar aana bhul jate hain..❤️\nKar ke khafa mujhko wo\nManana bhul jate hain....💞😌',
                     'Chalo phir yeha se ghar kaise jaoge...?

🙂🔪Ye humare akhri mulakat h kuch kehna chahoge?🙃❤️


😔❤️M to khr khel rhi thi tum to sacha isq karte the na😓🔪
Kaise karte karke dekhau..😷🤧

🤒❤️Tum to kehte the m bichrungi to mar jaooge marke dekhau😖❤️

😌✨Ek bhola bhala khelta huya dil tut gyi na....🙂❤️

👀❤️....Ladka chup kyu pata ..?

😊❤️ ....ladki to margyi naa',
                   ]

"""
    Hello kangers, 
    How are you all??
    So if you want to add more shyari add it between '', example 'Yes I'm kanging your codes', 
    I hope it's clear to you!

    So if you're really kanging this atleast don't remove this line it takes a lot of time to code things.
    Coded by : @Cute_Boy701 on telegram...
"""

@pbot.on_message(filters.command("romantic"))
async def lel(bot, message):
    ran = random.choice(ROMANTIC_STRINGS)
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)
