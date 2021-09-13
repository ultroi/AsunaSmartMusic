from pyrogram import Client, filters
from handlers import check_heroku
from config import OWNER_ID

@Client.on_message(filters.command('rebootmusic') & filters.user(OWNER_ID))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("[Asuna Music] - Restarting")
    hap.restart()
