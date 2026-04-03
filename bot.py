from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE"

# ===== ТОВАРЫ =====
PRODUCTS = [
    {"id":1,"name":"Танец Дракона","price":25000,"shots":25,"video":"https://youtube.com","kaspi":"https://kaspi.kz"},
    {"id":2,"name":"QASQIR","price":15000,"shots":7,"video":"https://youtube.com","kaspi":"https://kaspi.kz"},
    {"id":3,"name":"Радужный Взрыв","price":36000,"shots":36,"video":"https://youtube.com","kaspi":"https://kaspi.kz"},
    {"id":4,"name":"Рыцарь","price":42000,"shots":36,"video":"https://youtube.com","kaspi":"https://kaspi.kz"},
]

# ===== МЕНЮ =====
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("💰 По бюджету", callback_data="budget")],
        [InlineKeyboardButton("🎆 По залпам", callback_data="shots")],
        [InlineKeyboardButton("⭐ Топ", callback_data="top")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contacts")]
    ])

# ===== СТАРТ =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 AYP PYRO SHOP\n\nВыберите раздел:",
        reply_markup=main_menu()
    )

# ===== КНОПКИ =====
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # каталог
    if data == "catalog":
        buttons = []
        for p in PRODUCTS:
            buttons.append([InlineKeyboardButton(f'{p["name"]} - {p["price"]}₸', callback_data=f'product_{p["id"]}')])
        buttons.append([InlineKeyboardButton("⬅️ Назад", callback_data="home")])
        await query.message.reply_text("🔥 Каталог:", reply_markup=InlineKeyboardMarkup(buttons))

    # бюджет
    elif data == "budget":
        await query.message.reply_text("💰 Выбери бюджет:", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("до 15000", callback_data="b_0_15000")],
            [InlineKeyboardButton("15000-30000", callback_data="b_15000_30000")],
            [InlineKeyboardButton("30000+", callback_data="b_30000_999999")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
        ]))

    elif data.startswith("b_"):
        _, min_p, max_p = data.split("_")
        min_p, max_p = int(min_p), int(max_p)

        res = [p for p in PRODUCTS if min_p <= p["price"] <= max_p]

        buttons = []
        for p in res:
            buttons.append([InlineKeyboardButton(f'{p["name"]} - {p["price"]}₸', callback_data=f'product_{p["id"]}')])

        buttons.append([InlineKeyboardButton("⬅️ Назад", callback_data="budget")])
        await query.message.reply_text("Подходящие варианты:", reply_markup=InlineKeyboardMarkup(buttons))

    # залпы
    elif data == "shots":
        await query.message.reply_text("🎆 Выбери залпы:", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("до 10", callback_data="s_0_10")],
            [InlineKeyboardButton("10-30", callback_data="s_10_30")],
            [InlineKeyboardButton("30+", callback_data="s_30_999")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
        ]))

    elif data.startswith("s_"):
        _, min_s, max_s = data.split("_")
        min_s, max_s = int(min_s), int(max_s)

        res = [p for p in PRODUCTS if min_s <= p["shots"] <= max_s]

        buttons = []
        for p in res:
            buttons.append([InlineKeyboardButton(f'{p["name"]} ({p["shots"]} залпов)', callback_data=f'product_{p["id"]}')])

        buttons.append([InlineKeyboardButton("⬅️ Назад", callback_data="shots")])
        await query.message.reply_text("Подходящие варианты:", reply_markup=InlineKeyboardMarkup(buttons))

    # топ
    elif data == "top":
        await query.message.reply_text("⭐ Лучшие:", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔥 Танец Дракона", callback_data="product_1")],
            [InlineKeyboardButton("🔥 Радужный Взрыв", callback_data="product_3")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
        ]))

    # контакты
    elif data == "contacts":
        await query.message.reply_text(
            "📞 Контакты\n\nАлматы\n+7 777 000 00 00",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
            ])
        )

    # товар
    elif data.startswith("product_"):
        pid = int(data.split("_")[1])
        p = next((x for x in PRODUCTS if x["id"] == pid), None)

        await query.message.reply_text(
            f'🔥 {p["name"]}\n\n💰 {p["price"]}₸\n🎆 {p["shots"]} залпов',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📲 Купить (Kaspi)", url=p["kaspi"])],
                [InlineKeyboardButton("🎬 Смотреть видео", url=p["video"])],
                [InlineKeyboardButton("⬅️ Назад", callback_data="catalog")]
            ])
        )

    # назад
    elif data == "home":
        await query.message.reply_text("Главное меню:", reply_markup=main_menu())

# ===== ЗАПУСК =====
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    print("Бот запущен...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()