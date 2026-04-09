import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE")

SHOP_TEXT = (
    "🔥 AYP FIREWORKS\n\n"
    "🎆 Салюты для любого праздника\n"
    "💰 Подбор по цене\n"
    "🚀 Быстрый и удобный выбор\n\n"
    "Выберите раздел:"
)

SHOP_ADDRESS_TEXT = "AYP, Алматы"
SHOP_2GIS = "https://2gis.kz/almaty/geo/70000001103431846"
SHOP_PHONE = "+7 776 599 99 19"
SHOP_PHONE_LINK = "https://wa.me/77765999919?text=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%2C%20%D1%85%D0%BE%D1%87%D1%83%20%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D1%82%D1%8C%20%D0%BF%D0%BE%20%D1%81%D0%B0%D0%BB%D1%8E%D1%82%D0%B0%D0%BC"
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
        "top": True,
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
        "top": True,
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
        "top": True,
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
        "top": False,
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
        "top": False,
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
        "top": True,
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
        "top": False,
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
        "top": False,
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
        "top": False,
    },
]


def file_exists(path: str) -> bool:
    return bool(path and os.path.exists(path))


def get_product_by_id(product_id: int):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)


def filter_by_price(min_price: int, max_price: int):
    return [p for p in PRODUCTS if min_price <= p["price"] <= max_price]


def filter_by_shots(min_shots: int, max_shots: int):
    return [p for p in PRODUCTS if min_shots <= p["shots"] <= max_shots]


def top_products():
    return [p for p in PRODUCTS if p.get("top")]


def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("💰 По цене", callback_data="price_menu")],
        [InlineKeyboardButton("🎆 По залпам", callback_data="shots_menu")],
        [InlineKeyboardButton("⭐ Топ", callback_data="top")],
        [InlineKeyboardButton("📍 Как нас найти", callback_data="location")],
        [InlineKeyboardButton("📞 Связаться", callback_data="contact")],
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
        InlineKeyboardButton("🏠 Домой", callback_data="home"),
    ])
    return InlineKeyboardMarkup(rows)


def price_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 5 000₸", callback_data="price|0|5000")],
        [InlineKeyboardButton("5 000 – 10 000₸", callback_data="price|5000|10000")],
        [InlineKeyboardButton("10 000 – 20 000₸", callback_data="price|10000|20000")],
        [InlineKeyboardButton("20 000 – 40 000₸", callback_data="price|20000|40000")],
        [InlineKeyboardButton("40 000₸ и выше", callback_data="price|40000|999999")],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")],
    ])


def shots_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 10 залпов", callback_data="shots|0|10")],
        [InlineKeyboardButton("11 – 25 залпов", callback_data="shots|11|25")],
        [InlineKeyboardButton("26 – 50 залпов", callback_data="shots|26|50")],
        [InlineKeyboardButton("51 и больше", callback_data="shots|51|999")],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")],
    ])


def location_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📍 Открыть в 2GIS", url=SHOP_2GIS)],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")],
    ])


def contact_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📞 Позвонить / написать", url=SHOP_PHONE_LINK)],
        [InlineKeyboardButton("💬 WhatsApp", url=SHOP_WHATSAPP)],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")],
    ])


def product_buttons(product, back_callback="catalog"):
    rows = []
    if product.get("kaspi"):
        rows.append([InlineKeyboardButton("🛒 Купить в Kaspi", url=product["kaspi"])])
    if product.get("video"):
        rows.append([InlineKeyboardButton("🎥 Смотреть видео", url=product["video"])])
    rows.append([
        InlineKeyboardButton("⬅️ Назад", callback_data=back_callback),
        InlineKeyboardButton("🏠 Домой", callback_data="home"),
    ])
    return InlineKeyboardMarkup(rows)


async def edit_text_safe(query, text: str, reply_markup):
    try:
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    except Exception:
        await query.message.reply_text(text=text, reply_markup=reply_markup)


async def edit_photo_safe(query, photo_path: str, caption: str, reply_markup):
    if not file_exists(photo_path):
        await edit_text_safe(query, caption, reply_markup)
        return

    try:
        with open(photo_path, "rb") as photo:
            media = InputMediaPhoto(media=photo, caption=caption)
            await query.edit_message_media(media=media, reply_markup=reply_markup)
    except Exception:
        try:
            await query.edit_message_caption(caption=caption, reply_markup=reply_markup)
        except Exception:
            try:
                with open(photo_path, "rb") as photo:
                    await query.message.reply_photo(photo=photo, caption=caption, reply_markup=reply_markup)
            except Exception:
                await query.message.reply_text(text=caption, reply_markup=reply_markup)


async def show_home_callback(query):
    if file_exists(BANNER_FILE):
        await edit_photo_safe(query, BANNER_FILE, SHOP_TEXT, main_menu())
    else:
        await edit_text_safe(query, SHOP_TEXT, main_menu())


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if file_exists(BANNER_FILE):
        with open(BANNER_FILE, "rb") as photo:
            await update.message.reply_photo(photo=photo, caption=SHOP_TEXT, reply_markup=main_menu())
    else:
        await update.message.reply_text(SHOP_TEXT, reply_markup=main_menu())


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "home":
        await show_home_callback(query)
        return

    if data == "catalog":
        await edit_text_safe(query, "🔥 Каталог товаров:", products_menu(PRODUCTS, "home"))
        return

    if data == "price_menu":
        await edit_text_safe(query, "💰 Выберите диапазон цены:", price_menu())
        return

    if data.startswith("price|"):
        _, min_price, max_price = data.split("|")
        items = filter_by_price(int(min_price), int(max_price))

        if not items:
            await edit_text_safe(query, "По этой цене товаров пока нет.", price_menu())
            return

        await edit_text_safe(query, "💰 Подходящие варианты:", products_menu(items, "price_menu"))
        return

    if data == "shots_menu":
        await edit_text_safe(query, "🎆 Выберите количество залпов:", shots_menu())
        return

    if data.startswith("shots|"):
        _, min_shots, max_shots = data.split("|")
        items = filter_by_shots(int(min_shots), int(max_shots))

        if not items:
            await edit_text_safe(query, "По этому количеству залпов товаров пока нет.", shots_menu())
            return

        await edit_text_safe(query, "🎆 Подходящие варианты:", products_menu(items, "shots_menu"))
        return

    if data == "top":
        await edit_text_safe(query, "⭐ Топ товары:", products_menu(top_products(), "home"))
        return

    if data == "location":
        text = f"📍 Наш магазин\n\n{SHOP_ADDRESS_TEXT}\n\nНажмите кнопку ниже:"
        await edit_text_safe(query, text, location_menu())
        return

    if data == "contact":
        text = f"📞 Связаться с нами\n\n{SHOP_PHONE}\n\nВыберите удобный способ:"
        await edit_text_safe(query, text, contact_menu())
        return

    if data.startswith("product_"):
        product_id = int(data.split("_")[1])
        product = get_product_by_id(product_id)

        if not product:
            await edit_text_safe(query, "Товар не найден.", main_menu())
            return

        caption = (
            f'🔥 {product["name"]}\n\n'
            f'💰 Цена: {product["price"]}₸\n'
            f'🎆 Залпы: {product["shots"]}\n'
            f'📏 Калибр: {product["caliber"]}'
        )

        await edit_photo_safe(query, product.get("photo", ""), caption, product_buttons(product, "catalog"))
        return


async def post_init(application: Application):
    await application.bot.delete_webhook(drop_pending_updates=True)


def main():
    if not BOT_TOKEN or BOT_TOKEN == "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН":
        raise ValueError("Не вставлен BOT_TOKEN")

    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling(drop_pending_updates=True, close_loop=False)


if __name__ == "__main__":
    main()