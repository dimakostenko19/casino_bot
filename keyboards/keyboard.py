from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

eng = InlineKeyboardButton(
    text="English",
    callback_data="eng"
    )


row = [eng]
rows = [row]
lang_markup = InlineKeyboardMarkup(inline_keyboard=rows)


avio = InlineKeyboardButton(
    text="✈️ AVIATOR ✈️",
    callback_data="avio_eng"
)
mines = InlineKeyboardButton(
    text="🕹 MINES 🕹",
    callback_data="mines_eng"
)

row = [avio, mines]
rows = [row]
cas_markup = InlineKeyboardMarkup(inline_keyboard=rows)


check = InlineKeyboardButton(
    text="🔍 Check Registration",
    callback_data="check_avio_eng"
)
reg = InlineKeyboardButton(
    text="🚀 Register",
    url="https://1wfqtr.life/v3/aviator-fire?p=64ej"
)
row_1 = [check]
row_2 = [reg]

rows = [
    row_2,
    row_1
]
check_avio_markup = InlineKeyboardMarkup(inline_keyboard=rows)


get_signal = InlineKeyboardButton(
    text="GET SIGNAL",
    callback_data="signal_avio_eng"
)

row = [get_signal]
rows=[row]
signal_markup = InlineKeyboardMarkup(inline_keyboard=rows)


signal = InlineKeyboardButton(
    text="❗️ NEXT SIGNAL",
    callback_data="get_sig_avio_eng"
)

game_here_eng = InlineKeyboardButton(
    text="💸 Bet here",
    url="https://1wfqtr.life/v3/aviator-fire?p=64ej"
)
row_1=[signal]
row_2=[game_here_eng]
rows = [
    row_2,
    row_1
]
next_markup = InlineKeyboardMarkup(inline_keyboard=rows)


check = InlineKeyboardButton(
    text="🔍 Check Registration",
    callback_data="check_min_eng"
)
reg = InlineKeyboardButton(
    text="🚀 Register",
    url="https://1wfqtr.life/v3/aviator-fire?p=64ej"
)
row_1 = [check]
row_2 = [reg]

rows = [
    row_2,
    row_1
]
check_min_markup = InlineKeyboardMarkup(inline_keyboard=rows)


get_signal = InlineKeyboardButton(
    text="GET SIGNAL",
    callback_data="signal_min_eng"
)
row = [get_signal]
rows=[row]
signal_min_markup = InlineKeyboardMarkup(inline_keyboard=rows)


signal = InlineKeyboardButton(
    text="❗️ NEXT SIGNAL",
    callback_data="get_sig_min_eng"
)
game_here_eng = InlineKeyboardButton(
    text="💸 Bet here",
    url="https://1wfqtr.life/v3/2158/1win-mines?p=lld8"
)
row_1=[signal]
row_2=[game_here_eng]
rows = [
    row_2,
    row_1
]
next_min_markup = InlineKeyboardMarkup(inline_keyboard=rows)