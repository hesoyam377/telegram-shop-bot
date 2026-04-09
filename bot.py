from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE"

# === ТОВАРЫ ===
products = {
    "dragon": {
        "name": "🔥 Танец дракона",
        "shots": "25 залпов",
        "caliber": "0.8",
        "price": "6950₸",
        "photo": "dragon.jpg",
        "kaspi": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don633-zalpov-25-142100320/?c=750000000"
    }
}

# === СТАРТ ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Каталог", callback_data="catalog")]
    ]
    await update.message.reply_text(
        "🔥 AYP FIREWORKS\n\nВыберите раздел:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# === КАТАЛОГ ===
async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🔥 Танец дракона", callback_data="dragon")]
    ]

    await query.message.reply_text(
        "📦 Каталог товаров:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# === ТОВАР ===
async def show_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    product = products[query.data]

    keyboard = [
        [InlineKeyboardButton("🛒 Купить в Kaspi", url=product["kaspi"])],
        [InlineKeyboardButton("⬅️ Назад", callback_data="catalog")]
    ]

    text = f"""
{product['name']}

🎆 {product['shots']}
💥 Калибр: {product['caliber']}
💰 Цена: {product['price']}
"""

    with open(product["photo"], "rb") as photo:
        await query.message.reply_photo(
            photo=photo,
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# === ОБРАБОТКА ===
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == "catalog":
        await catalog(update, context)
    elif query.data in products:
        await show_product(update, context)

# === ЗАПУСК ===
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle))

app.run_polling()