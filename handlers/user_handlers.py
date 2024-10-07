from aiogram import Router, types, F
from aiogram.filters.command import Command, CommandStart
from aiogram.types.input_file import FSInputFile

import random
import os

from bot import Bot
import keyboards.keyboard as kb

router = Router()

@router.message(CommandStart)
async def start(message: types.Message):
    
    await message.answer(text="Choose a language | Выберите язык", reply_markup=kb.lang_markup)

#########################################################
# ENGLISH #
@router.callback_query(F.data == "eng")
async def english_bot(call: types.callback_query):
    photo_kino = FSInputFile("E:\\DimaPy\\casino_bot\\aiogram_casino\\photo\\cas_aio.jpg")
    
    await call.message.answer_photo(
        photo=photo_kino,
        reply_markup=kb.cas_markup,
        caption="Choose a game ⤵️"
        )


@router.callback_query(F.data == "avio_eng")
async def call_jet(callback_data: types.callback_query):
    photo_av = FSInputFile("E:\\DimaPy\\casino_bot\\aiogram_casino\\photo\\avio.jpg")
    await callback_data.message.answer_photo(
        photo=photo_av,
        reply_markup=kb.check_avio_markup,
        caption="""Welcome to AVIATOR 🚀

🌐Step 1 - Register.

✦ To synchronize with our bot, you must register a NEW account using a previously unused phone number on this site, and without using social media.  

If you already have an account and when you click on the button "🚀 Register " you get to the old one, you need to exit it and click on the button "🚀 Register " again, and then register again!

● After completing the registration, click the "🔍 Check Registration " button."""
)

@router.callback_query(F.data=="check_avio_eng")
async def call_check(callback_data: types.callback_query):
    await callback_data.message.answer(
        text="""
        Account confirmed ✅
Congratulations, you can now make money🤑 
But there are only 12 signals available per day ❗️❗️
        """,
        reply_markup=kb.signal_markup)
    

@router.callback_query(F.data=="signal_avio_eng")
async def signal(call: types.callback_query):
    
    rand = random.uniform(1.2, 5.46)
    form_num = "{:.2f}".format(rand)
    await call.message.answer(
        text=f"""
        ❗️ ATTENTION ❗️

    🚀 SIGNAL - <b>{form_num}</b>x
    🎯 In <b>1 MINUTE</b> place your bet.
    ➖➖➖➖➖➖➖➖➖➖➖➖

        """,
        reply_markup=kb.next_markup,
        )
    

@router.callback_query(F.data=="get_sig_avio_eng")
async def new_signal(call: types.callback_query):
    rand = random.uniform(1.2, 5.46)
    form_num = "{:.2f}".format(rand)
    await call.message.answer(
        text=f"""
        ❗️ ATTENTION ❗️

    🚀 SIGNAL - <b>{form_num}</b>x
    🎯 In <b>1 MINUTE</b> place your bet.
    ➖➖➖➖➖➖➖➖➖➖➖➖

        """,
        reply_markup=kb.next_markup,
        )

#####################################################################################
# Mines #
#####################################################################################

@router.callback_query(F.data == "mines_eng")
async def call_min(callback_data: types.callback_query):
    
    photo_mn = FSInputFile("E:\\DimaPy\\casino_bot\\aiogram_casino\\photo\\mines_logo.jpg")
    await callback_data.message.answer_photo(
        photo=photo_mn,
        reply_markup=kb.check_min_markup,
        caption="""Welcome to MINES 💣 

🌐Step 1 - Register.

✦ To synchronize with our bot, you must register a NEW account using a previously unused phone number on this site, and without using social media.  

If you already have an account and when you click on the button "🚀 Register " you get to the old one, you need to exit it and click on the button "🚀 Register " again, and then register again!

● After completing the registration, click the "🔍 Check Registration " button."""
)
    
@router.callback_query(F.data=="check_min_eng")
async def call_check(callback_data: types.callback_query):
    await callback_data.message.answer(
        text="""
        Account confirmed ✅
Congratulations, you can now make money🤑 
But there are only 12 signals available per day ❗️❗️
        """,
        reply_markup=kb.signal_min_markup
        )


@router.callback_query(F.data=="signal_min_eng")
async def signal_min(call: types.callback_query):
    
    mines_dir = os.listdir("mines_signals")
    photo_mn = FSInputFile(f"E:\\DimaPy\\casino_bot\\aiogram_casino\\mines_signals\\{random.choice(mines_dir)}")
    await call.message.answer_photo(
        caption=f"""
        
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

    """,
        reply_markup=kb.next_min_markup,
        photo=photo_mn
        )

@router.callback_query(F.data=="get_sig_min_eng")
async def signal_mins(call: types.callback_query):
    
    mines_dir = os.listdir("mines_signals")
    photo_mn = FSInputFile(f"E:\\DimaPy\\casino_bot\\aiogram_casino\\mines_signals\\{random.choice(mines_dir)}")
    await call.message.answer_photo(
        caption=f"""
        
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

        """,
        reply_markup=kb.next_min_markup,
        photo=photo_mn
        )