from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8314351622:AAF4ZJarBizUVHt4_59vJaj2b7LU08K3IOM"  
CHANNEL_LINK = "https://t.me/+Ixg34cVsJH9hMzU0"
MESSAGE_TEXT = "👋 Bem vindo! Entra no nosso canal gratiis e aproveita as nossas dicas com analise escrita!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{MESSAGE_TEXT}\n👉 {CHANNEL_LINK}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

