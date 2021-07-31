import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, mafiaversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

PM_IMG = "https://telegra.ph/file/b61486075c6ef73dd0d12.png"
pm_caption = "__**🔥🔥𝐗𝐓𝐑𝐄𝐌𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"               👑𝕄𝔸𝕊𝕋𝔼ℝ👑\n**『[{DEFAULTUSER}](tg://user?id={mafia})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"𝐗𝐓𝐑𝐄𝐌𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓😈       : `{mafiaversion}`\n"

pm_caption += f"😱Sudo😱            : `{sudou}`\n"

pm_caption += "😇CHANNEL😇️   : [ᴊᴏɪɴ](https://t.me/MAFIA_USERBOT)\n"

pm_caption += "𝐍𝐨𝐨𝐁 𝐂𝐑𝐄𝐀𝐓𝐎𝐑    : [𝐀𝐍𝐆𝐀𝐃](https://t.me/koi_nahi_apna)\n\n"

#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
