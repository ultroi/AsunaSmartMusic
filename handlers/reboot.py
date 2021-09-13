from pyrogram import Client, filters
from handlers import check_heroku

@Client.on_message(filters.command('rebootmusic') & filters.user(1249591948))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("[Asuna Music] - Restarting")
    hap.restart()
