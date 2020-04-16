from echo.GoogleSheets import writing_data
from telebot import types
from echo.config import TG_TOKEN

import telebot
import datetime
import re

bot = telebot.TeleBot(TG_TOKEN)

user_dict = dict()


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('../stickers/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Курси")
    item2 = types.KeyboardButton("Сезонний табір")
    item3 = types.KeyboardButton("Майстер-клас")
    item4 = types.KeyboardButton("Контакти")
    item5 = types.KeyboardButton("Про нас")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     "Ласкаво просимо, {0.first_name}!\nЯ - <b>{1.first_name}</b>, чим можу бути корисним? 😃.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

    bot.send_message(363707352, "{0.first_name} {0.last_name}".format(message.from_user))


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
                     "Якщо Ви бажаєте отримати більше інформації, виберіть відповідну команду в полі нижще 👇")


@bot.message_handler(content_types=['text'])
def do_message(message):
    if message.chat.type == 'private':
        if message.text == 'Курси':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("STEM-розвиток", callback_data='STEM-розвиток')
            item2 = types.InlineKeyboardButton("WeDo", callback_data='WeDo')
            item3 = types.InlineKeyboardButton("RoboEducation lvl.1", callback_data='RoboEducation lvl.1')
            item4 = types.InlineKeyboardButton("RoboEducation lvl.2", callback_data='RoboEducation lvl.2')
            item5 = types.InlineKeyboardButton("RoboEducation lvl.3", callback_data='RoboEducation lvl.3')
            item6 = types.InlineKeyboardButton("Robo-Python", callback_data='Robo-Python')
            item7 = types.InlineKeyboardButton("EdWeb", callback_data='EdWeb')
            item8 = types.InlineKeyboardButton("ArduinoLab", callback_data='ArduinoLab')
            item9 = types.InlineKeyboardButton("Virtual Reality", callback_data='Virtual Reality')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)

            bot.send_message(message.chat.id, '<b>😊 Який курс Вас цікавить? 🙃</b>', reply_markup=markup,
                             parse_mode='HTML')


        elif message.text == 'Сезонний табір':
            bot.send_message(message.chat.id, '<b>☀️ Вітаємо у зимовому таборі ❄️</b>', parse_mode='HTML')

        elif message.text == 'Майстер-клас':
            bot.send_message(message.chat.id, "<b>Про майстер-класи</b>\n\n\
<i>Пропонуємо вашій увазі майстер-класи за межами банальності та реальності: віртуальні, розважальні та навчальні.\n\n\
Наші викладачі допоможуть вашій дитині зробити перші кроки в доросле програмування та зануритися у світ сучасних технологій. \
На наших майстер класах діти познайомляться з основними алгоритмами робототехніки, технологіями 3D та віртуальної реальності.\n\n\
Ми впевнені, що вам сподобається, адже це інноваційне дозвілля, яке точно запам’ятається.\
Подаруйте своїй дитині та її друзям неперевершені враження та незабутні емоції!</i>\n\n\
Детальна інформація на <a href='https://roboua.org/majster-klasi/'>сайті</a>",
                             parse_mode='HTML')

        elif message.text == 'Контакти':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Номер телефону", callback_data='number')
            item2 = types.InlineKeyboardButton("Відділ з питань маркетингу та реклами", callback_data='marketing')
            item3 = types.InlineKeyboardButton("Для загальних питань", callback_data='question')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, '<b>Контакт-центр працює щоденно з 10:00 до 18:00</b>',
                             reply_markup=markup, parse_mode='HTML')

        elif message.text == 'Про нас':
            bot.send_message(message.chat.id, "<b>ПРО КОМПАНІЮ</b>\n\n\
<i>RoboUA — це лабораторії сучасних технологій, в яких діти отримують інноваційні знання. \
Ми не просто навчаємо, ми зацікавлюємо дитину, адже вчитися з ентузіазмом у рази легше та швидше. \
Наші учні з 7 років здатні самі створювати прості комп’ютерні ігри. \
RoboUA перетворює дітей зі споживачів на творців комп’ютерних продуктів. \
І ми завжди готові довіритися баченню дитини та спробувати втілити її проект, а не нав’язувати постійно лише своє бачення. \
Ми відійшли від застарілих понять «гуру-учень» заради провідних систем виховання за зразком «експерт-команда» і йдемо в ногу зі світовим прогресом, готуючи дітей до життя в умовах нових технологій, де вміння програмувати буде не привілеєм, а необхідністю.\n\n\
RoboUA – не є бізнесом, яким ми його зазвичай звикли бачити в нашій країні. \
Наша мета – зробити лабораторії максимально соціальними, щоб якомога більше дітей мали можливість розвиватися і вчитися не лише користуватися, а й створювати самостійно найсучасніші технології.</i>\n\n\
Більш детальну інформацію дивіться на нашому <a href='https://roboua.org/'>сайті</a>",
                             parse_mode='HTML')
        else:
            user_name(message)


@bot.message_handler(content_types=['text'])
def user_name(message):
    if len(user_dict) < 3:
        bot.send_message(message.chat.id, "Я не знаю такої команди 🤷‍♂️😢", parse_mode='HTML')
    else:
        user_dict["ПІБ"] = message.text
        msg = bot.send_message(message.chat.id, "<b>Введіть свій номер телефону 👇</b>", parse_mode='HTML')
        bot.register_next_step_handler(msg, user_phone)


def user_phone(message):
    try:
        if message.text != '/cancel':
            number = message.text
            numberchek = re.search("^((0|\+38)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{10,12}$", number)
            if "+380" in number or number[0] == "0":
                if numberchek:
                    user_dict["Номер телефону"] = message.text
                    bot.send_message(message.chat.id, "<b>Дякуюємо, найближчим часом ми Вам зателефонуємо ☺️</b>",
                                     parse_mode='HTML')
                    register_data()
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            bot.send_message(message.chat.id, "<b>Виберіть, що Вас цікавить</b>", parse_mode='HTML')

    except ValueError:
        msg = bot.reply_to(message, "<b>Не коректно введений номер телефону, спробуйте ще раз!</b> \n<i>/cancel щоб обрати іншу команду</i>", parse_mode='HTML')
        bot.register_next_step_handler(msg, user_phone)


def register_data():
    now = datetime.datetime.now()
    user_dict["Час"] = now.strftime("%d-%m-%Y %H:%M")

    writing_data(2, user_dict)
    bot.send_message(363707352, "Нова Реєстрація!")


def location():
    markup_local = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Центр", callback_data='Гончара')
    item2 = types.InlineKeyboardButton("Солом'янка", callback_data='КНУБА')
    item3 = types.InlineKeyboardButton("Позняки", callback_data='Мишуги')
    item4 = types.InlineKeyboardButton("Голосіїво", callback_data='Глушкова')
    item5 = types.InlineKeyboardButton("Оболонь", callback_data='Оболонь')

    markup_local.add(item1, item2, item3, item4, item5)

    return markup_local


def class_day():
    markup_day = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Буднього дня", callback_data='Буднього дня')
    item2 = types.InlineKeyboardButton("Вихідного дня", callback_data='Вихідного дня')

    markup_day.add(item1, item2)

    return markup_day


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'STEM-розвиток':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>4-5 років</i>\n\n\
<b>Коротко: </b><i>Конструювання Lego, програмування робота Dash, цікаві математичні вправи,динамічні ігри</i>\n\n\
<b>Кількість дітей в групі: </b><i>6-8 дітей (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>1 год. 30 хв.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 850грн\n\
    Вихідні: 1000грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/stem-rozvitok/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="STEM-розвиток")

                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data


            elif call.data == 'WeDo':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>5-6 років</i>\n\n\
<b>Коротко: </b><i>Конструювання роботів на базі наборів Lego WEDO</i>\n\n\
<b>Кількість дітей в групі: </b><i>6-10 дітей (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/wedo/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="WeDo")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'RoboEducation lvl.1':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>7+ років</i>\n\n\
<b>Коротко: </b><i>Конструювання роботів на базі наборів Mindstorms EV3.</i>\n\n\
<b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/roboeducation-lvl-1/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="RoboEducation lvl.1")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'RoboEducation lvl.2':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>8+ років</i>\n\n\
<b>Коротко: </b><i>Програмування та робототехніка Lego Mindstorms, 3D-моделювання і 3D-друк</i>\n\n\
<b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/roboeducation-lvl-2/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="RoboEducation lvl.2")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'RoboEducation lvl.3':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>9+ років</i>\n\n\
<b>Коротко: </b><i>Створення складних алгоритмів та їх практичне застосування з використанням наборів Lego Mindstorms EV3</i>\n\n\
<b>Кількість дітей в групі: </b><i>6-8 дітей (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/roboeducation-lvl-3/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="RoboEducation lvl.3")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'Robo-Python':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>9+ років</i>\n\n\
<b>Коротко: </b><i>Конструювання Lego Mindstorms EV3, вивчення мови програмування PYTHON3</i>\n\n\
<b>Кількість дітей в групі: </b><i>6-14 дітей (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/robopython/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Robo-Python")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'EdWeb':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>10+ років</i>\n\n\
<b>Коротко: </b><i>Вивчення HTML5, Основи CSS3, JavaScript</i>\n\n\
<b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/edweb-junior/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="EdWeb")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'ArduinoLab':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>10+ років</i>\n\n\
<b>Коротко: </b><i>Робота з контролером Arduino, проектування електричних схем, програмування С++</i>\n\n\
<b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
<b>Тривалість заняття: </b><i>2 год.</i>\n\n\
<b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
__________________________________\n\n\
<b>ЦІНИ: </b><i>Будні: 1300грн\n\
    Вихідні: 1500грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/arduinolab-1-0/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="ArduinoLab")
                bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
                                 reply_markup=location(), parse_mode='HTML')

                user_dict['Курс'] = call.data

            elif call.data == 'Virtual Reality':
                bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
__________________________________\n\
<b>Вік: </b><i>8+ років</i>\n\n\
<b>VR: </b><i>Зона віртуальної реальності, з великою кількістю ігор та якісним обладнанням</i>\n\n\
<b>Тривалість: </b><i>30-120 хв.</i>\n\n\
<b>Адреса: </b><i>вул. Преображенська, 2 (КНУБА)</i>\n\
__________________________________\n\n\
<b>Вартість: </b><i>75-250 грн</i>\n\n\
Детальна інформація на <a href='https://roboua.org/vr/'>сайті</a>",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Virtual Reality")

                bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
                                 reply_markup=class_day(), parse_mode='HTML')

                user_dict['Курс'] = call.data
                user_dict['Локація'] = 'КНУБА'



            elif call.data == 'number':
                bot.send_contact(call.message.chat.id, +380955877070, "RoboUa")

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Номер телефону:")


            elif call.data == 'marketing':
                bot.send_message(call.message.chat.id, "pr@roboua.org",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Відділ з питань маркетингу та реклами:")

            elif call.data == 'question':
                bot.send_message(call.message.chat.id, "contact@roboua.org",
                                 parse_mode='HTML')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Для загальних питань:")

            elif call.data == 'Гончара':
                bot.send_message(call.message.chat.id,
                                 "<i>вул. Олеся Гончара, 37А, 1 поверх, офіс №10. Найближча станція метро: Золоті Ворота</i>",
                                 parse_mode='HTML')

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Гончара")

                bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
                                 reply_markup=class_day(), parse_mode='HTML')

                user_dict['Локація'] = call.data

            elif call.data == 'КНУБА':
                bot.send_message(call.message.chat.id,
                                 "<i>вул. Преображенська 2, 1 поверх. Між Солом’янською і Севастопольскою площами. В будівлі корпусу КНУБА, 1 поверх. Найближча станція метро: Вокзальна</i>",
                                 parse_mode='HTML')

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="КНУБА")

                bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
                                 reply_markup=class_day(), parse_mode='HTML')

                user_dict['Локація'] = call.data

            elif call.data == 'Мишуги':
                bot.send_message(call.message.chat.id,
                                 "<i>вул. Мішуги 3В, 4 поверх. Найближчі станції метро: Позняки (5 хв. пішки) та Харківська (20 хв. пішки)</i>",
                                 parse_mode='HTML')

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Мишуги")

                bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
                                 reply_markup=class_day(), parse_mode='HTML')

                user_dict['Локація'] = call.data

            elif call.data == 'Глушкова':
                bot.send_message(call.message.chat.id,
                                 "<i>пр-т. Глушкова 6, 2 поверх. В будівлі Фізико-математичного ліцею КНУ ім. Шевченка, 2 поверх. Найближчі станції метро: Виставковий центр, Іподром</i>",
                                 parse_mode='HTML')

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Глушкова")

                bot.send_message(call.message.chat.id, '<b><i>Яка група курсів більше підходить? 🤔</i></b>',
                                 reply_markup=class_day(), parse_mode='HTML')

                user_dict['Локація'] = call.data

            elif call.data == 'Оболонь':
                bot.send_message(call.message.chat.id,
                                 "<i>пр-т. Героїв Сталінграду 20, 1 поверх. В будівлі Дитячої Академії Футболу. Найближча станція метро: Мінська (10 хв. пішки)</i>",
                                 parse_mode='HTML')

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Оболонь")

                bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
                                 reply_markup=class_day(), parse_mode='HTML')

                user_dict['Локація'] = call.data

            elif call.data == 'Буднього дня':

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Буднього дня")
                bot.send_message(call.message.chat.id, "<b> Напишіть будь ласка своє ім'я та прізвище </b>",
                                 parse_mode='HTML')

                user_dict['День'] = call.data

            elif call.data == 'Вихідного дня':

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Вихідного дня")
                bot.send_message(call.message.chat.id, "<b> Напишіть будь ласка своє ім'я та прізвище </b>",
                                 parse_mode='HTML')

                user_dict['День'] = call.data

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

# # show alert
# # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
# # #                           text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")



#----------RoboUA----------
# from echo.GoogleSheets import writing_data
# from telebot import types
# from echo.config import TG_TOKEN
#
# import telebot
# import datetime
# import re
#
# bot = telebot.TeleBot(TG_TOKEN)
#
# user_dict = dict()
#
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     sti = open('../stickers/hello.webp', 'rb')
#     bot.send_sticker(message.chat.id, sti)
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     item1 = types.KeyboardButton("Курси")
#     item2 = types.KeyboardButton("Сезонний табір")
#     item3 = types.KeyboardButton("Майстер-клас")
#     item4 = types.KeyboardButton("Контакти")
#     item5 = types.KeyboardButton("Про нас")
#
#     markup.add(item1, item2, item3, item4, item5)
#
#     bot.send_message(message.chat.id,
#                      "Ласкаво просимо, {0.first_name}!\nЯ - <b>{1.first_name}</b>, чим можу бути корисним? 😃.".format(
#                          message.from_user, bot.get_me()),
#                      parse_mode='html', reply_markup=markup)
#
#     bot.send_message(363707352, "{0.first_name} {0.last_name}".format(message.from_user))
#
#
# @bot.message_handler(commands=['help'])
# def help_command(message):
#     bot.send_message(message.chat.id,
#                      "Якщо Ви бажаєте отримати більше інформації, виберіть відповідну команду в полі нижще 👇")
#
#
# @bot.message_handler(content_types=['text'])
# def do_message(message):
#     if message.chat.type == 'private':
#         if message.text == 'Курси':
#             markup = types.InlineKeyboardMarkup(row_width=2)
#             item1 = types.InlineKeyboardButton("STEM-розвиток", callback_data='STEM-розвиток')
#             item2 = types.InlineKeyboardButton("WeDo", callback_data='WeDo')
#             item3 = types.InlineKeyboardButton("RoboEducation lvl.1", callback_data='RoboEducation lvl.1')
#             item4 = types.InlineKeyboardButton("RoboEducation lvl.2", callback_data='RoboEducation lvl.2')
#             item5 = types.InlineKeyboardButton("RoboEducation lvl.3", callback_data='RoboEducation lvl.3')
#             item6 = types.InlineKeyboardButton("Robo-Python", callback_data='Robo-Python')
#             item7 = types.InlineKeyboardButton("EdWeb", callback_data='EdWeb')
#             item8 = types.InlineKeyboardButton("ArduinoLab", callback_data='ArduinoLab')
#             item9 = types.InlineKeyboardButton("Virtual Reality", callback_data='Virtual Reality')
#
#             markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
#
#             bot.send_message(message.chat.id, '<b>😊 Який курс Вас цікавить? 🙃</b>', reply_markup=markup,
#                              parse_mode='HTML')
#
#
#         elif message.text == 'Сезонний табір':
#             bot.send_message(message.chat.id, '<b>☀️ Вітаємо у зимовому таборі ❄️</b>', parse_mode='HTML')
#
#         elif message.text == 'Майстер-клас':
#             bot.send_message(message.chat.id, "<b>Про майстер-класи</b>\n\n\
# <i>Пропонуємо вашій увазі майстер-класи за межами банальності та реальності: віртуальні, розважальні та навчальні.\n\n\
# Наші викладачі допоможуть вашій дитині зробити перші кроки в доросле програмування та зануритися у світ сучасних технологій. \
# На наших майстер класах діти познайомляться з основними алгоритмами робототехніки, технологіями 3D та віртуальної реальності.\n\n\
# Ми впевнені, що вам сподобається, адже це інноваційне дозвілля, яке точно запам’ятається.\
# Подаруйте своїй дитині та її друзям неперевершені враження та незабутні емоції!</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/majster-klasi/'>сайті</a>",
#                              parse_mode='HTML')
#
#         elif message.text == 'Контакти':
#             markup = types.InlineKeyboardMarkup(row_width=2)
#             item1 = types.InlineKeyboardButton("Номер телефону", callback_data='number')
#             item2 = types.InlineKeyboardButton("Відділ з питань маркетингу та реклами", callback_data='marketing')
#             item3 = types.InlineKeyboardButton("Для загальних питань", callback_data='question')
#
#             markup.add(item1, item2, item3)
#
#             bot.send_message(message.chat.id, '<b>Контакт-центр працює щоденно з 10:00 до 18:00</b>',
#                              reply_markup=markup, parse_mode='HTML')
#
#         elif message.text == 'Про нас':
#             bot.send_message(message.chat.id, "<b>ПРО КОМПАНІЮ</b>\n\n\
# <i>RoboUA — це лабораторії сучасних технологій, в яких діти отримують інноваційні знання. \
# Ми не просто навчаємо, ми зацікавлюємо дитину, адже вчитися з ентузіазмом у рази легше та швидше. \
# Наші учні з 7 років здатні самі створювати прості комп’ютерні ігри. \
# RoboUA перетворює дітей зі споживачів на творців комп’ютерних продуктів. \
# І ми завжди готові довіритися баченню дитини та спробувати втілити її проект, а не нав’язувати постійно лише своє бачення. \
# Ми відійшли від застарілих понять «гуру-учень» заради провідних систем виховання за зразком «експерт-команда» і йдемо в ногу зі світовим прогресом, готуючи дітей до життя в умовах нових технологій, де вміння програмувати буде не привілеєм, а необхідністю.\n\n\
# RoboUA – не є бізнесом, яким ми його зазвичай звикли бачити в нашій країні. \
# Наша мета – зробити лабораторії максимально соціальними, щоб якомога більше дітей мали можливість розвиватися і вчитися не лише користуватися, а й створювати самостійно найсучасніші технології.</i>\n\n\
# Більш детальну інформацію дивіться на нашому <a href='https://roboua.org/'>сайті</a>",
#                              parse_mode='HTML')
#         else:
#             user_name(message)
#
#
# @bot.message_handler(content_types=['text'])
# def user_name(message):
#     if len(user_dict) < 3:
#         bot.send_message(message.chat.id, "Я не знаю такої команди 🤷‍♂️😢", parse_mode='HTML')
#     else:
#         user_dict["ПІБ"] = message.text
#         msg = bot.send_message(message.chat.id, "<b>Введіть свій номер телефону 👇</b>", parse_mode='HTML')
#         bot.register_next_step_handler(msg, user_phone)
#
#
# def user_phone(message):
#     try:
#         if message.text != '/cancel':
#             number = message.text
#             numberchek = re.search("^((0|\+38)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{10,12}$", number)
#             if "+380" in number or number[0] == "0":
#                 if numberchek:
#                     user_dict["Номер телефону"] = message.text
#                     bot.send_message(message.chat.id, "<b>Дякуюємо, найближчим часом ми Вам зателефонуємо ☺️</b>",
#                                      parse_mode='HTML')
#                     register_data()
#                 else:
#                     raise ValueError
#             else:
#                 raise ValueError
#         else:
#             bot.send_message(message.chat.id, "<b>Виберіть, що Вас цікавить</b>", parse_mode='HTML')
#
#     except ValueError:
#         msg = bot.reply_to(message, "<b>Не коректно введений номер телефону, спробуйте ще раз!</b> \n<i>/cancel щоб обрати іншу команду</i>", parse_mode='HTML')
#         bot.register_next_step_handler(msg, user_phone)
#
#
# def register_data():
#     now = datetime.datetime.now()
#     user_dict["Час"] = now.strftime("%d-%m-%Y %H:%M")
#
#     writing_data(2, user_dict)
#     bot.send_message(363707352, "Нова Реєстрація!")
#
#
# def location():
#     markup_local = types.InlineKeyboardMarkup(row_width=2)
#     item1 = types.InlineKeyboardButton("Центр", callback_data='Гончара')
#     item2 = types.InlineKeyboardButton("Солом'янка", callback_data='КНУБА')
#     item3 = types.InlineKeyboardButton("Позняки", callback_data='Мишуги')
#     item4 = types.InlineKeyboardButton("Голосіїво", callback_data='Глушкова')
#     item5 = types.InlineKeyboardButton("Оболонь", callback_data='Оболонь')
#
#     markup_local.add(item1, item2, item3, item4, item5)
#
#     return markup_local
#
#
# def class_day():
#     markup_day = types.InlineKeyboardMarkup(row_width=2)
#     item1 = types.InlineKeyboardButton("Буднього дня", callback_data='Буднього дня')
#     item2 = types.InlineKeyboardButton("Вихідного дня", callback_data='Вихідного дня')
#
#     markup_day.add(item1, item2)
#
#     return markup_day
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'STEM-розвиток':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>4-5 років</i>\n\n\
# <b>Коротко: </b><i>Конструювання Lego, програмування робота Dash, цікаві математичні вправи,динамічні ігри</i>\n\n\
# <b>Кількість дітей в групі: </b><i>6-8 дітей (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>1 год. 30 хв.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 850грн\n\
#     Вихідні: 1000грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/stem-rozvitok/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="STEM-розвиток")
#
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#
#             elif call.data == 'WeDo':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>5-6 років</i>\n\n\
# <b>Коротко: </b><i>Конструювання роботів на базі наборів Lego WEDO</i>\n\n\
# <b>Кількість дітей в групі: </b><i>6-10 дітей (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/wedo/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="WeDo")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'RoboEducation lvl.1':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>7+ років</i>\n\n\
# <b>Коротко: </b><i>Конструювання роботів на базі наборів Mindstorms EV3.</i>\n\n\
# <b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/roboeducation-lvl-1/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="RoboEducation lvl.1")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'RoboEducation lvl.2':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>8+ років</i>\n\n\
# <b>Коротко: </b><i>Програмування та робототехніка Lego Mindstorms, 3D-моделювання і 3D-друк</i>\n\n\
# <b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/roboeducation-lvl-2/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="RoboEducation lvl.2")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'RoboEducation lvl.3':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>9+ років</i>\n\n\
# <b>Коротко: </b><i>Створення складних алгоритмів та їх практичне застосування з використанням наборів Lego Mindstorms EV3</i>\n\n\
# <b>Кількість дітей в групі: </b><i>6-8 дітей (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/roboeducation-lvl-3/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="RoboEducation lvl.3")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'Robo-Python':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>9+ років</i>\n\n\
# <b>Коротко: </b><i>Конструювання Lego Mindstorms EV3, вивчення мови програмування PYTHON3</i>\n\n\
# <b>Кількість дітей в групі: </b><i>6-14 дітей (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/robopython/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Robo-Python")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'EdWeb':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>10+ років</i>\n\n\
# <b>Коротко: </b><i>Вивчення HTML5, Основи CSS3, JavaScript</i>\n\n\
# <b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/edweb-junior/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="EdWeb")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'ArduinoLab':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>10+ років</i>\n\n\
# <b>Коротко: </b><i>Робота з контролером Arduino, проектування електричних схем, програмування С++</i>\n\n\
# <b>Кількість дітей в групі: </b><i>10-14 (залежно від локації)</i>\n\n\
# <b>Тривалість заняття: </b><i>2 год.</i>\n\n\
# <b>Кількість занять: </b><i>1 на тиждень (всього 32 заняття)</i>\n\
# __________________________________\n\n\
# <b>ЦІНИ: </b><i>Будні: 1300грн\n\
#     Вихідні: 1500грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/arduinolab-1-0/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="ArduinoLab")
#                 bot.send_message(call.message.chat.id, "<b><i>Виберіть локацію яка вас цікавить 👇</i></b>",
#                                  reply_markup=location(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#
#             elif call.data == 'Virtual Reality':
#                 bot.send_message(call.message.chat.id, "<b>ПРО КУРС:</b>\n\
# __________________________________\n\
# <b>Вік: </b><i>8+ років</i>\n\n\
# <b>VR: </b><i>Зона віртуальної реальності, з великою кількістю ігор та якісним обладнанням</i>\n\n\
# <b>Тривалість: </b><i>30-120 хв.</i>\n\n\
# <b>Адреса: </b><i>вул. Преображенська, 2 (КНУБА)</i>\n\
# __________________________________\n\n\
# <b>Вартість: </b><i>75-250 грн</i>\n\n\
# Детальна інформація на <a href='https://roboua.org/vr/'>сайті</a>",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Virtual Reality")
#
#                 bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
#                                  reply_markup=class_day(), parse_mode='HTML')
#
#                 user_dict['Курс'] = call.data
#                 user_dict['Локація'] = 'КНУБА'
#
#
#
#             elif call.data == 'number':
#                 bot.send_contact(call.message.chat.id, +380955877070, "RoboUa")
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Номер телефону:")
#
#
#             elif call.data == 'marketing':
#                 bot.send_message(call.message.chat.id, "pr@roboua.org",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Відділ з питань маркетингу та реклами:")
#
#             elif call.data == 'question':
#                 bot.send_message(call.message.chat.id, "contact@roboua.org",
#                                  parse_mode='HTML')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Для загальних питань:")
#
#             elif call.data == 'Гончара':
#                 bot.send_message(call.message.chat.id,
#                                  "<i>вул. Олеся Гончара, 37А, 1 поверх, офіс №10. Найближча станція метро: Золоті Ворота</i>",
#                                  parse_mode='HTML')
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Гончара")
#
#                 bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
#                                  reply_markup=class_day(), parse_mode='HTML')
#
#                 user_dict['Локація'] = call.data
#
#             elif call.data == 'КНУБА':
#                 bot.send_message(call.message.chat.id,
#                                  "<i>вул. Преображенська 2, 1 поверх. Між Солом’янською і Севастопольскою площами. В будівлі корпусу КНУБА, 1 поверх. Найближча станція метро: Вокзальна</i>",
#                                  parse_mode='HTML')
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="КНУБА")
#
#                 bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
#                                  reply_markup=class_day(), parse_mode='HTML')
#
#                 user_dict['Локація'] = call.data
#
#             elif call.data == 'Мишуги':
#                 bot.send_message(call.message.chat.id,
#                                  "<i>вул. Мішуги 3В, 4 поверх. Найближчі станції метро: Позняки (5 хв. пішки) та Харківська (20 хв. пішки)</i>",
#                                  parse_mode='HTML')
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Мишуги")
#
#                 bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
#                                  reply_markup=class_day(), parse_mode='HTML')
#
#                 user_dict['Локація'] = call.data
#
#             elif call.data == 'Глушкова':
#                 bot.send_message(call.message.chat.id,
#                                  "<i>пр-т. Глушкова 6, 2 поверх. В будівлі Фізико-математичного ліцею КНУ ім. Шевченка, 2 поверх. Найближчі станції метро: Виставковий центр, Іподром</i>",
#                                  parse_mode='HTML')
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Глушкова")
#
#                 bot.send_message(call.message.chat.id, '<b><i>Яка група курсів більше підходить? 🤔</i></b>',
#                                  reply_markup=class_day(), parse_mode='HTML')
#
#                 user_dict['Локація'] = call.data
#
#             elif call.data == 'Оболонь':
#                 bot.send_message(call.message.chat.id,
#                                  "<i>пр-т. Героїв Сталінграду 20, 1 поверх. В будівлі Дитячої Академії Футболу. Найближча станція метро: Мінська (10 хв. пішки)</i>",
#                                  parse_mode='HTML')
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Оболонь")
#
#                 bot.send_message(call.message.chat.id, "<b><i>Яка група курсів більше підходить? 🤔</i></b>",
#                                  reply_markup=class_day(), parse_mode='HTML')
#
#                 user_dict['Локація'] = call.data
#
#             elif call.data == 'Буднього дня':
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Буднього дня")
#                 bot.send_message(call.message.chat.id, "<b> Напишіть будь ласка своє ім'я та прізвище </b>",
#                                  parse_mode='HTML')
#
#                 user_dict['День'] = call.data
#
#             elif call.data == 'Вихідного дня':
#
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Вихідного дня")
#                 bot.send_message(call.message.chat.id, "<b> Напишіть будь ласка своє ім'я та прізвище </b>",
#                                  parse_mode='HTML')
#
#                 user_dict['День'] = call.data
#
#     except Exception as e:
#         print(repr(e))
#
#
# # RUN
# bot.polling(none_stop=True)
#
# # # show alert
# # # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
# # # #                           text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
