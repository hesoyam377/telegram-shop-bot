from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE")

SHOP_NAME = "AYP Fireworks Shop"
SHOP_TEXT = "🔥 Магазин пиротехники AYP\n\nВыберите раздел:"

PRODUCTS = [
    {"id": 1, "name": "Танец Дракона", "price": 6950, "shots": 25, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 2, "name": "Радужный взрыв", "price": 9800, "shots": 36, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 3, "name": "Салют удачи", "price": 11000, "shots": 49, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 4, "name": "Raushan", "price": 6300, "shots": 19, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 5, "name": "Батарея салютов", "price": 7500, "shots": 25, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 6, "name": "Sholpanai", "price": 3000, "shots": 7, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 7, "name": "Qasqir", "price": 3200, "shots": 7, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 8, "name": "Ночной бум", "price": 11000, "shots": 12, "caliber": "1,2", "kaspi": "", "video": ""},
    {"id": 9, "name": "Cake", "price": 38000, "shots": 25, "caliber": "1,2", "kaspi": "", "video": ""},
    {"id": 10, "name": "Polar bear attack", "price": 15000, "shots": 16, "caliber": "1,2", "kaspi": "", "video": ""},
    {"id": 11, "name": "Годовой успех", "price": 28000, "shots": 138, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 12, "name": "Qarui", "price": 6300, "shots": 16, "caliber": "0,8", "kaspi": "", "video": ""},
    {"id": 13, "name": "Танец страсти", "price": 21000, "shots": 19, "caliber": "1,2", "kaspi": "", "video": ""}
]

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("💰 По бюджету", callback_data="budget")],
        [InlineKeyboardButton("🎆 По залпам", callback_data="shots")],
        [InlineKeyboardButton("⭐ Топ", callback_data="top")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contacts")]
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
    rows.append([InlineKeyboardButton("⬅️ Назад", callback_data=back_callback)])
    return InlineKeyboardMarkup(rows)

def budget_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 5 000₸", callback_data="budget_0_5000")],
        [InlineKeyboardButton("5 000 – 10 000₸", callback_data="budget_5000_10000")],
        [InlineKeyboardButton("10 000 – 20 000₸", callback_data="budget_10000_20000")],
        [InlineKeyboardButton("20 000 – 40 000₸", callback_data="budget_20000_40000")],
        [InlineKeyboardButton("40 000₸ и выше", callback_data="budget_40000_999999")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
    ])

def shots_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 10 залпов", callback_data="shots_0_10")],
        [InlineKeyboardButton("11 – 25 залпов", callback_data="shots_11_25")],
        [InlineKeyboardButton("26 – 50 залпов", callback_data="shots_26_50")],
        [InlineKeyboardButton("51 и больше", callback_data="shots_51_999")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
    ])

def product_buttons(product):
    rows = []

    if product.get("kaspi"):
        rows.append([InlineKeyboardButton("🛒 Купить в Kaspi", url=product["kaspi"])])

    if product.get("video"):
        rows.append([InlineKeyboardButton("🎥 Смотреть видео", url=product["video"])])

    rows.append([InlineKeyboardButton("⬅️ Назад", callback_data="catalog")])
    return InlineKeyboardMarkup(rows)

def get_product_by_id(product_id):
    return next((p for p in PRODUCTS if p["id"] == product_id), None)

def filter_by_budget(min_price, max_price):
    return [p for p in PRODUCTS if min_price <= p["price"] <= max_price]

def filter_by_shots(min_shots, max_shots):
    return [p for p in PRODUCTS if min_shots <= p["shots"] <= max_shots]

def top_products():
    top_ids = [11, 9, 3, 13]
    return [p for p in PRODUCTS if p["id"] in top_ids]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        SHOP_TEXT,
        reply_markup=main_menu()
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "home":
        await query.message.reply_text(
            SHOP_TEXT,
            reply_markup=main_menu()
        )
        return

    if data == "catalog":
        await query.message.reply_text(
            "🔥 Каталог товаров:",
            reply_markup=products_menu(PRODUCTS, "home")
        )
        return

    if data == "budget":
        await query.message.reply_text(
            "💰 Выберите бюджет:",
            reply_markup=budget_menu()
        )
        return

    if data.startswith("budget_"):
        _, min_price, max_price = data.split("_")
        items = filter_by_budget(int(min_price), int(max_price))

        if not items:
            await query.message.reply_text(
                "По этому бюджету товаров пока нет.",
                reply_markup=budget_menu()
            )
            return

        await query.message.reply_text(
            "💰 Подходящие варианты:",
            reply_markup=products_menu(items, "budget")
        )
        return

    if data == "shots":
        await query.message.reply_text(
            "🎆 Выберите количество залпов:",
            reply_markup=shots_menu()
        )
        return

    if data.startswith("shots_"):
        _, min_shots, max_shots = data.split("_")
        items = filter_by_shots(int(min_shots), int(max_shots))

        if not items:
            await query.message.reply_text(
                "По этому количеству залпов товаров пока нет.",
                reply_markup=shots_menu()
            )
            return

        await query.message.reply_text(
            "🎆 Подходящие варианты:",
            reply_markup=products_menu(items, "shots")
        )
        return

    if data == "top":
        await query.message.reply_text(
            "⭐ Топ товары:",
            reply_markup=products_menu(top_products(), "home")
        )
        return

    if data == "contacts":
        await query.message.reply_text(
            "📞 Контакты\n\n"
            "AYP Fireworks Shop\n"
            "📍 Алматы\n"
            "📱 +7 777 000 00 00",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
            ])
        )
        return

    if data.startswith("product_"):
        product_id = int(data.split("_")[1])
        product = get_product_by_id(product_id)

        if not product:
            await query.message.reply_text("Товар не найден.")
            return

        text = (
            f'🔥 {product["name"]}\n\n'
            f'💰 Цена: {product["price"]}₸\n'
            f'🎆 Залпы: {product["shots"]}\n'
            f'📏 Калибр: {product["caliber"]}'
        )

        await query.message.reply_text(
            text,
            reply_markup=product_buttons(product)
        )
        return

def main():
    if not BOT_TOKEN or BOT_TOKEN == "СЮДА_ВСТАВЬ_СВОЙ_ТОКЕН":
        raise ValueError("Не вставлен BOT_TOKEN")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущен...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()