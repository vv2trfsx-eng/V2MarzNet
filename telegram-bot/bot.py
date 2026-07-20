from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN


async def start(update, context):

    await update.message.reply_text(
        "🚀 Welcome to V2MarzNet\n\n"
        "Professional VPN Management Platform"
    )



app = Application.builder().token(
    BOT_TOKEN
).build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


print(
    "V2MarzNet Bot Started"
)


app.run_polling()
