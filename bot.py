from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN", "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE")

WHATSAPP = "https://wa.me/77765999919"
MAP = "https://2gis.kz/almaty/geo/70000001103431846"

# --- ТОВАРЫ (упрощенные) ---
PRODUCTS = [
    {"text": "Салют до 7000₸ • 25 залпов", "price": 7000, "tag": "cheap", "url": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don633-zalpov-25-142100320/"},
    {"text": "Салют до 10000₸ • 36 залпов", "price": 10000, "tag": "cheap", "url": "https://kaspi.kz/shop/p/-raduzhnyi-vzryv-36-zalpov-142101625/"},
    {"text": "Салют до 20000₸ • 49 залпов", "price": 20000, "tag": "mid", "url": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don623-zalpov-49-142100621/"},
    {"text": "Мощный салют • 25 залпов 1.2", "price": 38000, "tag": "power", "url": "https://kaspi.kz/shop/p/feierverk-cake-25-zalpov-1-2-djuima--142141375/"},
    {"text": "Мощный салют • 49 залпов 1.2", "price": 68000, "tag": "power", "url": "https://kaspi.kz/shop/p/nochnoi-impul-s-143082235/"},
    {"text": "Выгодный салют • 168 залпов", "price": 55000, "tag": "best", "url": "https://kaspi.kz/shop/p/prints-festivalja-168-zalp-142399031/"},
]

# --- ГЛАВНОЕ МЕНЮ ---
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Салюты", callback_data="salutes")],
        [InlineKeyboardButton("Ракеты", callback_data="rockets")],
        [InlineKeyboardButton("Петарды", callback_data="petards")],
        [InlineKeyboardButton("Фонтаны", callback_data="fountains")],
        [InlineKeyboardButton("Хиты продаж", callback_data="hits")],
        [InlineKeyboardButton("Как нас найти", callback_data="map")],
        [InlineKeyboardButton("Связаться", callback_data="contact")]
    ])

# --- САЛЮТЫ ---
def salutes_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 10 000₸", callback_data="price_low")],
        [InlineKeyboardButton("До 20 000₸", callback_data="price_mid")],
        [InlineKeyboardButton("Мощные", callback_data="power")],
        [InlineKeyboardButton("Выгодные", callback_data="best")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
    ])

# --- ВЫВОД ТОВАРОВ ---
def build_products(filter_tag=None):
    buttons = []
    for p in PRODUCTS:
        if filter_tag is None or p["tag"] == filter_tag:
            buttons.append([InlineKeyboardButton(p["text"], url=p["url"])])
    buttons.append([InlineKeyboardButton("⬅️ Назад", callback_data="home")])
    return InlineKeyboardMarkup(buttons)

# --- START ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AYP FIREWORKS\n\nПодберите салют за 2 клика",
        reply_markup=main_menu()
    )

# --- ОБРАБОТКА ---
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    data = q.data

    if data == "home":
        await q.message.reply_text("Главное меню", reply_markup=main_menu())

    elif data == "salutes":
        await q.message.reply_text("Выберите:", reply_markup=salutes_menu())

    elif data == "price_low":
        await q.message.reply_text("До 10 000₸", reply_markup=build_products("cheap"))

    elif data == "price_mid":
        await q.message.reply_text("До 20 000₸", reply_markup=build_products("mid"))

    elif data == "power":
        await q.message.reply_text("Мощные салюты", reply_markup=build_products("power"))

    elif data == "best":
        await q.message.reply_text("Выгодные варианты", reply_markup=build_products("best"))

    elif data == "hits":
        await q.message.reply_text("🔥 Хиты продаж", reply_markup=build_products())

    elif data == "map":
        await q.message.reply_text("📍 Наш магазин",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Открыть 2GIS", url=MAP)]
            ])
        )

    elif data == "contact":
        await q.message.reply_text("Связаться:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("WhatsApp", url=WHATSAPP)]
            ])
        )

# --- ЗАПУСК ---
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle))

app.run_polling()