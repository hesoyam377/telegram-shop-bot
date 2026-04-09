from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE")

SHOP_NAME = "AYP"
SHOP_TITLE = "🔥 AYP FIREWORKS"
SHOP_TEXT = (
    "🔥 AYP FIREWORKS\n\n"
    "🎆 Салюты для любого праздника\n"
    "💰 Подбор по бюджету\n"
    "🚀 Быстрый и удобный выбор\n\n"
    "Выберите раздел:"
)

SHOP_ADDRESS_TEXT = "AYP, Алматы"
SHOP_2GIS = "https://2gis.kz/almaty/geo/70000001103431846"
SHOP_PHONE = "+7 776 599 99 19"
SHOP_PHONE_LINK = "tel:+77765999919"
SHOP_WHATSAPP = "https://wa.me/77765999919"

BANNER_FILE = "banner.jpg"

PRODUCTS = [
    {
        "id": 1,
        "name": "Танец Дракона",
        "price": 6950,
        "shots": 25,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don633-zalpov-25-142100320/?c=750000000&sr=4&ref=shared_link",
        "video": "https://youtu.be/94W5GZ6aiAE?si=wnmn0wFhMjZ34k_C",
        "photo": "dragon.jpg",
        "top": True
    },
    {
        "id": 2,
        "name": "Радужный взрыв",
        "price": 9800,
        "shots": 36,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/-raduzhnyi-vzryv-36-zalpov-142101625/?c=750000000&sr=3&ref=shared_link",
        "video": "https://youtu.be/7hQPtWXfxWU?si=1rDx-fR1-_t-hPpK",
        "photo": "raduzhnyi_vzryv.jpg",
        "top": True
    },
    {
        "id": 3,
        "name": "Салют удачи",
        "price": 11000,
        "shots": 49,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don623-zalpov-49-142100621/?c=750000000&sr=5&ref=shared_link",
        "video": "https://youtu.be/lDoNccOoTc8?si=ZSricMqa_xCgE_mY",
        "photo": "salyut_udachi.jpg",
        "top": True
    },
    {
        "id": 4,
        "name": "Raushan",
        "price": 6300,
        "shots": 19,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/raushan-19zarjadov-151817404/?c=750000000&sr=4&ref=shared_link",
        "video": "https://youtu.be/WmKQ2sxRJWY?si=DNgxoKmDTrGskfzw",
        "photo": "raushan.jpg",
        "top": False
    },
    {
        "id": 5,
        "name": "Sholpanai",
        "price": 3000,
        "shots": 7,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/sholpanai-7zarjadov-151695092/?c=750000000&sr=1&ref=shared_link",
        "video": "",
        "photo": "sholpanai.jpg",
        "top": False
    },
    {
        "id": 6,
        "name": "Годовой успех",
        "price": 28000,
        "shots": 138,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/godovoi-uspeh-138-zalp-142387958/?c=750000000&sr=2&ref=shared_link",
        "video": "https://youtu.be/5vvYlOYhHnQ?si=BeQHZ5q6Yxy3opxX",
        "photo": "godovoi_uspeh.jpg",
        "top": True
    },
    {
        "id": 7,
        "name": "Qasqir",
        "price": 3200,
        "shots": 7,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/qasqir-7-zarjadov-151706822/?c=750000000&sr=7&ref=shared_link",
        "video": "https://youtu.be/VI8Fz-SEX00?si=P8F96XtPURD0Ovxk",
        "photo": "qasqir.jpg",
        "top": False
    },
    {
        "id": 8,
        "name": "Батарейный фейерверк",
        "price": 7500,
        "shots": 25,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/batareja-saljutov-139027211-zalpov-25-130933581/?c=750000000&sr=17&ref=shared_link",
        "video": "https://youtu.be/b5_OL8Bc8Q4?si=jfb1_KSp-e-TgL8i",
        "photo": "batareinyi_feierverk.jpg",
        "top": False
    },
    {
        "id": 9,
        "name": "Qar ui",
        "price": 6300,
        "shots": 16,
        "caliber": "0.8",
        "kaspi": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-ayp02016-zalpov-16-151821152/?c=750000000&sr=2&ref=shared_link",
        "video": "https://youtu.be/hKzkTwgUlFU?si=H3jqPyipr6y7MhuY",
        "photo": "qar_ui.jpg",
        "top": False
    }
]


def get_product_by_id(product_id: int):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


def filter_by_budget(min_price: int, max_price: int):
    return [p for p in PRODUCTS if min_price <= p["price"] <= max_price]


def filter_by_shots(min_shots: int, max_shots: int):
    return [p for p in PRODUCTS if min_shots <= p["shots"] <= max_shots]


def top_products():
    return [p for p in PRODUCTS if p.get("top")]


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("💰 По бюджету", callback_data="budget")],
        [InlineKeyboardButton("🎆 По залпам", callback_data="shots")],
        [InlineKeyboardButton("⭐ Топ", callback_data="top")],
        [InlineKeyboardButton("📍 Как нас найти", callback_data="location")],
        [InlineKeyboardButton("📞 Связаться", callback_data="contact")]
    ])


def products_menu(products, back_callback="home"):
    rows = []
    for p in products:
        rows.append([
            InlineKeyboardButton(
                f'{p["name"]} | {p["shots"]} залп. | {p["price"]}₸',
                callback_data=f'product_{p["id"]}'
            )
        ])
    rows.append([
        InlineKeyboardButton("⬅️ Назад", callback_data=back_callback),
        InlineKeyboardButton("🏠 Домой", callback_data="home")
    ])
    return InlineKeyboardMarkup(rows)


def budget_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 5 000₸", callback_data="budget_0_5000")],
        [InlineKeyboardButton("5 000 – 10 000₸", callback_data="budget_5000_10000")],
        [InlineKeyboardButton("10 000 – 20 000₸", callback_data="budget_10000_20000")],
        [InlineKeyboardButton("20 000 – 40 000₸", callback_data="budget_20000_40000")],
        [InlineKeyboardButton("40 000₸ и выше", callback_data="budget_40000_999999")],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")]
    ])


def shots_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 10 залпов", callback_data="shots_0_10")],
        [InlineKeyboardButton("11 – 25 залпов", callback_data="shots_11_25")],
        [InlineKeyboardButton("26 – 50 залпов", callback_data="shots_26_50")],
        [InlineKeyboardButton("51 и больше", callback_data="shots_51_999")],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")]
    ])


def location_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📍 Открыть в 2GIS", url=SHOP_2GIS)],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")]
    ])


def contact_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📞 Позвонить", url=SHOP_PHONE_LINK)],
        [InlineKeyboardButton("💬 WhatsApp", url=SHOP_WHATSAPP)],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")]
    ])


def product_buttons(product, back_callback="catalog"):
    rows = []

    if product.get("kaspi"):
        rows.append([InlineKeyboardButton("🛒 Купить в Kaspi", url=product["kaspi"])])

    if product.get("video"):
        rows.append([InlineKeyboardButton("🎥 Смотреть видео", url=product["video"])])

    rows.append([
        InlineKeyboardButton("⬅️ Назад", callback_data=back_callback),
        InlineKeyboardButton("🏠 Домой", callback_data="home")
    ])
    return InlineKeyboardMarkup(rows)


async def send_new_text(chat_id: int, bot, text: str, markup):
    return await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)


async def send_new_photo(chat_id: int, bot, photo_path: str, caption: str, markup):
    with open(photo_path, "rb") as photo:
        return await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=markup)


async def replace_with_text(query, text: str, markup):
    chat_id = query.message.chat_id
    try:
        await query.message.delete()
    except:
        pass
    await send_new_text(chat_id, query.bot, text, markup)


async def replace_with_photo(query, photo_path: str, caption: str, markup):
    chat_id = query.message.chat_id
    try:
        await query.message.delete()
    except:
        pass
    try:
        await send_new_photo(chat_id, query.bot, photo_path, caption, markup)
    except:
        await send_new_text(chat_id, query.bot, caption, markup)


async def show_home(chat_id: int, bot):
    if os.path.exists(BANNER_FILE):
        try:
            await send_new_photo(chat_id, bot, BANNER_FILE, SHOP_TEXT, main_menu())
            return
        except:
            pass
    await send_new_text(chat_id, bot, SHOP_TEXT, main_menu())


async def show_product(query, product, back_callback="catalog"):
    caption = (
        f'🔥 {product["name"]}\n\n'
        f'💰 Цена: {product["price"]}₸\n'
        f'🎆 Залпы: {product["shots"]}\n'
        f'📏 Калибр: {product["caliber"]}'
    )

    photo_path = product.get("photo", "").strip()
    if photo_path and os.path.exists(photo_path):
        await replace_with_photo(query, photo_path, caption, product_buttons(product, back_callback))
    else:
        await replace_with_text(query, caption, product_buttons(product, back_callback))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_home(update.effective_chat.id, context.bot)


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "home":
        await replace_with_text(query, SHOP_TEXT, main_menu())
        return

    if data == "catalog":
        await replace_with_text(query, "🔥 Каталог товаров:", products_menu(PRODUCTS, "home"))
        return

    if data == "budget":
        await replace_with_text(query, "💰 Выберите бюджет:", budget_menu())
        return

    if data.startswith("budget_"):
        _, min_price, max_price = data.split("_")
        items = filter_by_budget(int(min_price), int(max_price))

        if not items:
            await replace_with_text(query, "По этому бюджету товаров пока нет.", budget_menu())
            return

        await replace_with_text(query, "💰 Подходящие варианты:", products_menu(items, "budget"))
        return

    if data == "shots":
        await replace_with_text(query, "🎆 Выберите количество залпов:", shots_menu())
        return

    if data.startswith("shots_"):
        _, min_shots, max_shots = data.split("_")
        items = filter_by_shots(int(min_shots), int(max_shots))

        if not items:
            await replace_with_text(query, "По этому количеству залпов товаров пока нет.", shots_menu())
            return

        await replace_with_text(query, "🎆 Подходящие варианты:", products_menu(items, "shots"))
        return

    if data == "top":
        await replace_with_text(query, "⭐ Топ товары:", products_menu(top_products(), "home"))
        return

    if data == "location":
        text = f"📍 Наш магазин\n\n{SHOP_ADDRESS_TEXT}\n\nНажмите кнопку ниже:"
        await replace_with_text(query, text, location_menu())
        return

    if data == "contact":
        text = f"📞 Связаться с нами\n\n{SHOP_PHONE}\n\nВыберите удобный способ:"
        await replace_with_text(query, text, contact_menu())
        return

    if data.startswith("product_"):
        product_id = int(data.split("_")[1])
        product = get_product_by_id(product_id)

        if not product:
            await replace_with_text(query, "Товар не найден.", main_menu())
            return

        await show_product(query, product, "catalog")
        return


def main():
    if not BOT_TOKEN or BOT_TOKEN == "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН":
        raise ValueError("Не вставлен BOT_TOKEN")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()