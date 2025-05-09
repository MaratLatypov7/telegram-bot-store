
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.environ.get("YOUR_TOKEN")

products = {
    "Jacket/Skirt": [("Комплект с шерстью", "https://chat.openai.com/mnt/data/jacket_skirt.jpeg", 1200000)],
    "Suit": [("Тёмный костюм", "https://chat.openai.com/mnt/data/suit.jpeg", 1500000)],
    "Dress": [("Трикотажное платье", "https://chat.openai.com/mnt/data/dress.jpeg", 950000)],
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(cat, callback_data=f"cat:{cat}")] for cat in products
    ]
    await update.message.reply_text(
        "Добро пожаловать в Nepovtorimo Bot! Выберите категорию:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    cat = query.data.split(":")[1]
    items = products[cat]

    for name, photo, price in items:
        keyboard = [[InlineKeyboardButton("Купить", callback_data=f"buy:{name}")]]
        await query.message.reply_photo(
            photo=photo,
            caption=f"{name}\nЦена: {price:,} RUB",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def handle_purchase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Ваш заказ принят. Менеджер свяжется с вами в ближайшее время.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_category, pattern="^cat:"))
app.add_handler(CallbackQueryHandler(handle_purchase, pattern="^buy:"))

app.run_polling()
