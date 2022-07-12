import os
import logging
import random
from sorular import 12, 13
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
	BUTTON=[[InlineKeyboardButton(text="👨🏻‍💻 Sahibim ",url="t.me/KenanAghazade")]]
	BUTTON+=[[InlineKeyboardButton(text="🤖 Əsas Kanalımız",url="t.me/KenaninMavishi")]]
	return InlineKeyboardMarkup(BUTTON)

@Brend.on_message(filters.command("start"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="**Salam {}**\n\n🤖__Mən** [Kənan](t.me/KenanAghazade)** Tərəfindən Nərmin üçün hazırlanmış Botam__🥳\n\n\n Nərmin hadi əmrlərdən istifadə et💙\n\n /NerminÖzledimSeni ".format(
		user.mention,
		),
	disable_web_page_preview=True,
	reply_markup=button()
	)

def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="💙", callback_data = " ".join(["d_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="🖤", callback_data = " ".join(["c_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)

@Brend.on_message(filters.command("NerminÖzledimSeni"))
async def _(client, message):
	user = message.from_user
     

	await message.reply_text(text="{} İstədiyin sual növünü seç🖤".format(user.mention),
		reply_markup=d_or_c(user.id)
		)

@Brend.on_callback_query()
async def _(client, callback_query):
	d_soru=random.choice(12)
	c_soru=random.choice(13)
	user = callback_query.from_user

	c_q_d, user_id = callback_query.data.split()

	if str(user.id) == str(user_id):
		if c_q_d == "d_data":
			await callback_query.answer(text="🌚 Doğruluq sualı istədin", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)

			await callback_query.message.reply_text("**📣{user} Doğruluq seçdi:\n\nSəmimi olacağına inanırıq**\n\n `{d_soru}`".format(user=user.mention, d_soru=d_soru))
			return

		if c_q_d == "c_data":
			await callback_query.answer(text="Cəsarət Sualı İstədiniz", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text("**👻{user} Cəsarət seçdi:**\n\n `{c_soru}`".format(user=user.mention, c_soru=c_soru))
			return

	else:
		await callback_query.answer(text="😡Hey özünü ağıllı sayma! Sənin sıran deyil!", show_alert=False)
		return

@Brend.on_message(filters.command("csual"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID: 
    await message.reply_text("**[?]** **Sən icazəli şəxs deyilsən!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Əlavə olunmasını istədiyiniz cəsarət sualını yazın!**")
  
@Brend.on_message(filters.command("dsual"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID: 
    await message.reply_text("**[?]** **Sən icazəli şəxs deyilsən!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Əlavə olunmasını istədiyiniz doğruluq sualını yazın!**")

@Brend.on_message(filters.private)
async def _(client, message):
  global MOD
  global 13
  global 12
  
  user = message.from_user
  
  if user.id in OWNER_ID: 
    if MOD=="csual":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Sual Cəsarət suallarına əlavə olundu✅__")
      return
    if MOD=="dsual":
      C_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Sual Doğruluq suallarına əlavə olundu✅__")
      return

Brend.run()
