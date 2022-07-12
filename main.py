
import os
import logging
import random
from sorular import D_LİST, C_LİST
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

B_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("OWNER_API_ID")
API_HASH = os.getenv("OWNER_API_HASH")
OWNER_ID = os.getenv("OWNER_ID","5591720874").split()
OWNER_ID.append(5591720874)

MOD = None

logging.basicConfig(level=logging.INFO)

Brend = Client("Pyrogram Bot", bot_token=B_TOKEN, api_id=API_ID, api_hash=API_HASH)

def button():
	BUTTON=[[InlineKeyboardButton(text="Mavi Kalp💙",url="t.me/Mavish_19")]]
	BUTTON+=[[InlineKeyboardButton(text="💙İkimizin Kanalı💙",url="t.me/KenaninMavishi")]]
	return InlineKeyboardMarkup(BUTTON)

@Brend.on_message(filters.command("start"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="**Salam {}**\n\n🤖__Mən** [Kənan](t.me/KenanAghazade)** Tərəfindən Nərmin üçün hazırlanmış Botam__🥳\n\n\n Nərmin hadi əmrlərdən istifadə et💙\n\n /Nermin ".format(
		user.mention,
		),
	disable_web_page_preview=True,
	reply_markup=button()
	)

@Brend.on_message(filters.command("Nermin"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text=" **Mavişim mən səni çox özlədim. Etdiklərimi unutsanda barışsaq? ** 💙 ".format(
		user.mention,
		)

Brend.run()
