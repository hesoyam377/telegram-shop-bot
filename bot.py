from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN", "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE")

WHATSAPP = "https://wa.me/77765999919"
PHONE_LINK = "tel:+77765999919"
MAP = "https://2gis.kz/almaty/geo/70000001103431846"

BANNER = "banner.jpg"

START_TEXT = (
    "AYP FIREWORKS\n\n"
    "Работаем более 4 лет\n"
    "Подберём под любой бюджет\n"
    "Выберите нужный раздел:"
)

# -------------------- ДАННЫЕ --------------------

SALUTES = [
    {
        "title": "До 10 000₸ • для небольшого праздника",
        "url": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don633-zalpov-25-142100320/",
        "group": "low"
    },
    {
        "title": "До 10 000₸ • оптимальный вариант",
        "url": "https://kaspi.kz/shop/p/-raduzhnyi-vzryv-36-zalpov-142101625/",
        "group": "low"
    },
    {
        "title": "До 20 000₸ • яркий салют на праздник",
        "url": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-don623-zalpov-49-142100621/",
        "group": "mid"
    },
    {
        "title": "До 20 000₸ • хороший вариант для компании",
        "url": "https://kaspi.kz/shop/p/raushan-19zarjadov-151817404/",
        "group": "mid"
    },
    {
        "title": "Мощный • насыщенный эффект",
        "url": "https://kaspi.kz/shop/p/feierverk-cake-25-zalpov-1-2-djuima--142141375/",
        "group": "power"
    },
    {
        "title": "Мощный • яркий вау-эффект",
        "url": "https://kaspi.kz/shop/p/nochnoi-impul-s-143082235/",
        "group": "power"
    },
    {
        "title": "Мощный • премиум вариант",
        "url": "https://kaspi.kz/shop/p/venets-ognja-143082487/",
        "group": "power"
    },
    {
        "title": "Выгодный • максимум залпов за цену",
        "url": "https://kaspi.kz/shop/p/prints-festivalja-168-zalp-142399031/",
        "group": "best"
    },
    {
        "title": "Выгодный • длительный и эффектный",
        "url": "https://kaspi.kz/shop/p/godovoi-uspeh-138-zalp-142387958/",
        "group": "best"
    },
    {
        "title": "Хит • компактный и мощный",
        "url": "https://kaspi.kz/shop/p/tanets-strasti-142390794/",
        "group": "hit"
    },
    {
        "title": "Хит • доступный мощный вариант",
        "url": "https://kaspi.kz/shop/p/-nochnoi-bum--142109420/",
        "group": "hit"
    },
    {
        "title": "Хит • яркий 16 залпов",
        "url": "https://kaspi.kz/shop/p/ayp-batareja-saljutov-ayp02016-zalpov-16-151821152/",
        "group": "hit"
    },
    {
        "title": "Премиум • большой салют на событие",
        "url": "https://kaspi.kz/shop/p/korol-stseny-143082089/",
        "group": "power"
    },
    {
        "title": "Премиум • максимум масштаба",
        "url": "https://kaspi.kz/shop/p/-korol-nochi-138-zalpov-142101289/",
        "group": "power"
    },
    {
        "title": "Компактный • мощный 9 залпов",
        "url": "https://kaspi.kz/shop/p/1-2-cake-9-zalpov-142179507/",
        "group": "hit"
    },
    {
        "title": "Средний • хороший выбор по цене",
        "url": "https://kaspi.kz/shop/p/polar-bear-attack-142164788/",
        "group": "mid"
    },
]

ROCKETS = [
    {
        "title": "Римские свечи • 20 выстрелов",
        "url": "https://kaspi.kz/shop/p/rimskie-svechi-20-vystrelov-nabor-12-sht--144108568/",
    },
    {
        "title": "Римская свеча • premium pack",
        "url": "https://kaspi.kz/shop/p/ayp-rimskaja-svecha-premium-pack-4-sht-kalibr-1-2-zalpov-5-149743098/",
    },
    {
        "title": "Ракеты • набор 32",
        "url": "https://kaspi.kz/shop/p/rockets-hf032-152269143/",
    },
    {
        "title": "Ракеты • набор 38",
        "url": "https://kaspi.kz/shop/p/rockets-hf038-152269171/",
    },
    {
        "title": "Ракеты • набор 42",
        "url": "https://kaspi.kz/shop/p/rockets-hf042-152269154/",
    },
]

PETARDS = [
    {
        "title": "Петарды Корсар 1 • блок 10 шт",
        "url": "https://kaspi.kz/shop/p/korsar--1-151817374/",
    },
    {
        "title": "Петарды Gursil • аналог Корсар 4",
        "url": "https://kaspi.kz/shop/p/petardy-gursil-analog-korsar-4-10-sht-v-upakovke-144632182/",
    },
    {
        "title": "Хит • Novel Pack",
        "url": "https://kaspi.kz/shop/p/petardy-gursil-analog-korsar-4-10-sht-v-upakovke-144632182/",
    },
    {
        "title": "Петарды лента • 20 лент по 100",
        "url": "https://kaspi.kz/shop/p/-lenta-petard-100-zarjadov-20-lent-v-upakovke-2000-vzryvov--152309454/",
    },
    {
        "title": "Петарда 3 минуты • яркий эффект",
        "url": "https://kaspi.kz/shop/p/petarda-happy-boom-fountain-3-minuty-jarkii-fontan-iskr-effektnye-hlopki-bezopasnyi-zapusk-144616981/",
    },
    {
        "title": "Свистульки",
        "url": "https://kaspi.kz/shop/p/bai-o-yr-svistul-ki-142401536/",
    },
]

FOUNTAINS = [
    {
        "title": "Фонтан • упаковка 6 шт",
        "url": "https://kaspi.kz/shop/p/fontan-saljutov-happy-boom-6-sht-v-upakovke-3-effekta-do-25-sek--144733790/",
    },
    {
        "title": "Фонтан Фокусник",
        "url": "https://kaspi.kz/shop/p/happy-boom-fountain-fokusnik-142713834/",
    },
    {
        "title": "Ручной фонтан",
        "url": "https://kaspi.kz/shop/p/ayp-fontan-happy-boom-glow-of-sunset-lcm-ew-301-zalpov-1-142409289/",
    },
    {
        "title": "Фонтан 6 в 1",
        "url": "https://kaspi.kz/shop/p/fontan-happy-boom-fountian-142298382/",
    },
]

HITS = [
    {
        "title": "Хит • до 10 000₸",
        "url": "https://kaspi.kz/shop/p/-raduzhnyi-vzryv-36-zalpov-142101625/",
    },
    {
        "title": "Хит • до 20 000₸",
        "url": "https://kaspi.kz/shop/p/tanets-strasti-142390794/",
    },
    {
        "title": "Хит • выгодный салют",
        "url": "https://kaspi.kz/shop/p/prints-festivalja-168-zalp-142399031/",
    },
    {
        "title": "Хит • петарды Novel Pack",
        "url": "https://kaspi.kz/shop/p/petardy-gursil-analog-korsar-4-10-sht-v-upakovke-144632182/",
    },
]

# -------------------- МЕНЮ --------------------

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

def salutes_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("До 10 000₸", callback_data="salutes_low")],
        [InlineKeyboardButton("До 20 000₸", callback_data="salutes_mid")],
        [InlineKeyboardButton("Мощные", callback_data="salutes_power")],
        [InlineKeyboardButton("Выгодные", callback_data="salutes_best")],
        [InlineKeyboardButton("Хиты", callback_data="salutes_hit")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="home")]
    ])

def build_url_buttons(items, back_callback):
    buttons = []
    for item in items:
        buttons.append([InlineKeyboardButton(item["title"], url=item["url"])])
    buttons.append([InlineKeyboardButton("⬅️ Назад", callback_data=back_callback)])
    return InlineKeyboardMarkup(buttons)

def contact_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("WhatsApp", url=WHATSAPP)],
        [InlineKeyboardButton("Позвонить", url=PHONE_LINK)],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")]
    ])

def map_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Открыть 2GIS", url=MAP)],
        [InlineKeyboardButton("🏠 Домой", callback_data="home")]
    ])

# -------------------- ВЫВОД --------------------

async def show_home_message(message):
    if os.path.exists(BANNER):
        with open(BANNER, "rb") as photo:
            await message.reply_photo(
                photo=InputFile(photo),
                caption=START_TEXT,
                reply_markup=main_menu()
            )
    else:
        await message.reply_text(
            START_TEXT,
            reply_markup=main_menu()
        )

# -------------------- START --------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await show_home_message(update.message)

# -------------------- CALLBACK --------------------

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == "home":
        await q.message.reply_text("Главная", reply_markup=main_menu())

    elif data == "salutes":
        await q.message.reply_text("Выберите раздел салютов:", reply_markup=salutes_menu())

    elif data == "salutes_low":
        items = [x for x in SALUTES if x["group"] == "low"]
        await q.message.reply_text("До 10 000₸", reply_markup=build_url_buttons(items, "salutes"))

    elif data == "salutes_mid":
        items = [x for x in SALUTES if x["group"] == "mid"]
        await q.message.reply_text("До 20 000₸", reply_markup=build_url_buttons(items, "salutes"))

    elif data == "salutes_power":
        items = [x for x in SALUTES if x["group"] == "power"]
        await q.message.reply_text("Мощные салюты", reply_markup=build_url_buttons(items, "salutes"))

    elif data == "salutes_best":
        items = [x for x in SALUTES if x["group"] == "best"]
        await q.message.reply_text("Выгодные варианты", reply_markup=build_url_buttons(items, "salutes"))

    elif data == "salutes_hit":
        items = [x for x in SALUTES if x["group"] == "hit"]
        await q.message.reply_text("Хиты", reply_markup=build_url_buttons(items, "salutes"))

    elif data == "rockets":
        await q.message.reply_text("Ракеты", reply_markup=build_url_buttons(ROCKETS, "home"))

    elif data == "petards":
        await q.message.reply_text("Петарды", reply_markup=build_url_buttons(PETARDS, "home"))

    elif data == "fountains":
        await q.message.reply_text("Фонтаны", reply_markup=build_url_buttons(FOUNTAINS, "home"))

    elif data == "hits":
        await q.message.reply_text("Хиты продаж", reply_markup=build_url_buttons(HITS, "home"))

    elif data == "map":
        await q.message.reply_text("Наш магазин", reply_markup=map_menu())

    elif data == "contact":
        await q.message.reply_text(
            "Связаться с нами\n\n+7 776 599 99 19",
            reply_markup=contact_menu()
        )

# -------------------- ЗАПУСК --------------------

async def post_init(application: Application):
    try:
        await application.bot.delete_webhook(drop_pending_updates=True)
    except:
        pass

def main():
    if not TOKEN or TOKEN == "8660444999:AAEQkb-iwqFR-YI821DyhK84DYtxvscjXpE":
        raise ValueError("Не вставлен BOT_TOKEN")

    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle))

    print("Bot started...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()