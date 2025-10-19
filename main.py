from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = AAHI7WEUSgdgm9AVq5aMhgk24dKeJQ8KHM8

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "hola" in texto:
        await update.message.reply_text("¡Hola amigo! ¿Cómo estás?")
    elif "bien y tú" in texto or "bien y tu" in texto:
        await update.message.reply_text("¡Muy bien, gracias!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot de Prueba 1 iniciado...")
app.run_polling()
