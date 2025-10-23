from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8499131772:AAHWaiYdcZYSVhdcRVvtiAi38hUjUb1tmwM"  
CHANNEL_LINK = "https://t.me/+W6ptnmSllLY0Zjdk"
MESSAGE_TEXT = "👋 Bem vindo! Entra no nosso canal 100% gratuito e aproveita os melhores prognósticos!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"Hello {user.first_name}! {MESSAGE_TEXT}\n👉 {CHANNEL_LINK}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
