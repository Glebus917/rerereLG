import telebot, time, sqlite3

file1=open("token.txt", "r", encoding="UTF-8")
token=file1.readline()
file1.close()

bot = telebot.TeleBot(token)

bot.send_message(6765931514, f"Я ЛЮБЛЮ ЛЕРУ!!! ❤️")

tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))

commands = [telebot.types.BotCommand("/start", "Перезапуск бота 🔄️"),
telebot.types.BotCommand("/help", "Помощь 🆘"),
telebot.types.BotCommand("/special", "Что-то секретное 🔥")]

bot.set_my_commands(commands)

def cen_k(mes):

    try:

        markup=telebot.types.InlineKeyboardMarkup(row_width=2)
        b1=telebot.types.InlineKeyboardButton("Назад ⬅️", callback_data="nazad2_inline")
        b2=telebot.types.InlineKeyboardButton("Далее ➡️", callback_data="dalee2_inline")
        markup.add(b1, b2)

        a=mes.text
        a=int(a)
    #=======================
        m1=a/1.5
        m2=m1*2250
    #=======================
        m1r=round(m1, 1)
        m2r=round(m2, 0)
    #=======================
        m1r=str(m1r)
        m2r=int(m2r)
        m2r=str(m2r)
    #=======================
        bot.send_message(mes.chat.id, "Для вашего заказа, потребуется " + m1r + " упаковок плитки 📦, на сумму " + m2r + " рублей! 🪙", reply_markup=markup)

    except:

        markup=telebot.types.InlineKeyboardMarkup(row_width=2)
        b1=telebot.types.InlineKeyboardButton("Заново 🔄️", callback_data="rsc_inline")
        markup.add(b1)
        bot.send_message(mes.chat.id, """Ошибка!
Вы написали не только цифру 👾""", reply_markup=markup)
        

@bot.message_handler(commands=["start"])
def startjoin(mes):
    with sqlite3.connect('mainid.db') as db:
        cursor = db.cursor()
        cursor.execute(f"""SELECT id FROM mine WHERE id = {mes.from_user.id}""")
        users=cursor.fetchall()
        if not users:
            cursor.execute(f"""INSERT INTO mine (id, user_name) VALUES({mes.from_user.id}, '{mes.from_user.username}')""")
            db.commit()

    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
    b1=telebot.types.InlineKeyboardButton("Далее ➡️", callback_data="dalee0_inline")
    markup.add(b1)

    bot.send_message(mes.chat.id, '''
Привет!
Меня зовут impuls 🤖
Я помогу тебе заказать разработку своего личного телеграм бота для бизнеса!
Зачем нужен бот для бизнеса?
Вот преимущества чат бота:
                     
1. Круглосуточное сервисное обслуживание
С помощью чат-ботов, компании могут отвечать на вопросы клиентов, независимо от времени суток

2. Экономность
Чат-боты — это одноразовая инвестиция, которая помогает сократить траты на персонал

3. Генерация, квалификация и взращивание лидов
Чат-боты получают информацию о пользователях, которая позволяет персонализировать общение с клиентом на разных этапах воронки продаж

4. Сбор и анализ данных
Чат-боты являются мощным инструментом для сбора и анализа данных о поведении и предпочтениях клиентов
Эти данные предоставляют компаниям возможность адаптировать свои продукты и услуги к требованиям рынка

5. Чат-боты – отличный инструмент для обработки большого количества типовых запросов
Если компания получает много типовых запросов, нет необходимости увеличивать шаблоны или штат операторов
Хорошо построенный чат-бот позволит предоставить информацию о брэнде по всем запросам одновременно
                     
6. Повышение уровня обслуживания потребителей с помощью сбора и обработки данных
Чат-боты способны записывать данные, тенденции и критерии
для последующего мониторинга взаимодействия с клиентами и оптимизации обработки запросов и реагирования
                     
7. Чат-бот может перенаправить запрос клиента, предоставить любую информацию и сделать предварительный расчет
стоимости товара или услуги!
                     
8. Чат-бот может сделать рассылку всем пользователям!
При необходимости, вы сами можете написать всего лишь одну команду, чтобы сделать рассылку всем, кто хоть раз запускал бота!
Также, после рассылки вы получите количество людей, которые пользовались ботом и количество доставленных сообщений!
Сообщение для рассылки вы тоже пишете сами!
''', reply_markup=markup)

@bot.message_handler(commands=["help"])
def help(mes):
    bot.send_message(mes.chat.id, """Нашли баг или недоработку? 💥

Обратитесь к https://t.me/Impuls_Mironov ✅""")

@bot.message_handler(commands=['special'])
def spec(mes):
    if mes.chat.id == 1950291574:

        markup=telebot.types.InlineKeyboardMarkup(row_width=1)
        b1=telebot.types.InlineKeyboardButton("Создать сообщение 💬", callback_data="creatmesras_inline")
        markup.add(b1)

        bot.send_message(mes.chat.id, "Выберите действие 👾", reply_markup=markup)

    else:
        bot.send_message(mes.chat.id, "Недостаточно прав ❌")

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.message:

#===========================================================================================================================
#===========================================================================================================================
        if call.data=="dalee0_inline":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup=telebot.types.InlineKeyboardMarkup(row_width=2)
            b1=telebot.types.InlineKeyboardButton("Магазин 🏪", callback_data="yslyg_inline")
            b2=telebot.types.InlineKeyboardButton("Интернет магазин 🛜", callback_data="yslyg_inline")
            b3=telebot.types.InlineKeyboardButton("Сфера услуг ✂️💅", callback_data="yslyg_inline")
            b4=telebot.types.InlineKeyboardButton("Другое...", callback_data="yslyg_inline")
            markup.add(b1, b2, b3, b4)
            bot.send_message(call.message.chat.id, """
Для какой сферы бизнеса вам нужен чат бот? 💵
""", reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="yslyg_inline":
            markup=telebot.types.InlineKeyboardMarkup(row_width=2)
            b1=telebot.types.InlineKeyboardButton("Назад ⬅️", callback_data="nazad1_inline")
            b2=telebot.types.InlineKeyboardButton("Далее ➡️", callback_data="rsc_inline")
            markup.add(b1, b2)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, """
Отлично!
Чат-бот для вашего бизнеса будет полезен ✅
""", reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="nazad1_inline":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup=telebot.types.InlineKeyboardMarkup(row_width=2)
            b1=telebot.types.InlineKeyboardButton("Далее ➡️", callback_data="dalee0_inline")
            markup.add(b1)
            bot.send_message(call.message.chat.id, '''
Привет!
Меня зовут impuls 🤖
Я помогу тебе заказать разработку своего личного телеграм бота для бизнеса!
Зачем нужен бот для бизнеса?
Вот преимущества чат бота:
                     
1. Круглосуточное сервисное обслуживание
С помощью чат-ботов, компании могут отвечать на вопросы клиентов, независимо от времени суток

2. Экономность
Чат-боты — это одноразовая инвестиция, которая помогает сократить траты на персонал

3. Генерация, квалификация и взращивание лидов
Чат-боты получают информацию о пользователях, которая позволяет персонализировать общение с клиентом на разных этапах воронки продаж

4. Сбор и анализ данных
Чат-боты являются мощным инструментом для сбора и анализа данных о поведении и предпочтениях клиентов
Эти данные предоставляют компаниям возможность адаптировать свои продукты и услуги к требованиям рынка

5. Чат-боты – отличный инструмент для обработки большого количества типовых запросов
Если компания получает много типовых запросов, нет необходимости увеличивать шаблоны или штат операторов
Хорошо построенный чат-бот позволит предоставить информацию о брэнде по всем запросам одновременно
                     
6. Повышение уровня обслуживания потребителей с помощью сбора и обработки данных
Чат-боты способны записывать данные, тенденции и критерии
для последующего мониторинга взаимодействия с клиентами и оптимизации обработки запросов и реагирования
                     
7. Чат-бот может перенаправить запрос клиента, предоставить любую информацию и сделать предварительный расчет
стоимости товара или услуги!
                     
8. Чат-бот может сделать рассылку всем пользователям!
При необходимости, вы сами можете написать всего лишь одну команду, чтобы сделать рассылку всем, кто хоть раз запускал бота!
Также, после рассылки вы получите количество людей, которые пользовались ботом и количество доставленных сообщений!
Сообщение для рассылки вы тоже пишете сами!
''', reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="rsc_inline":

            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, """
Пример, как чат-бот может расчитать предварительную стоимость товара:
                             


Допустим, ваш магазин продает плитку для пола
                         
<b> Все ниже УСЛОВНО ‼️ </b>
                         
<b>Одна упаковка - 1.5 квадратных метра
Цена одной упаковки - 2250 рублей
Покупателю нужно ? квадратных метров плитки </b>
Ваш чат-бот сможет расчитать, сколько клиенту нужно упаковок плитки
и на какую сумму
""", parse_mode="HTML")
            mesg = bot.send_message(call.message.chat.id, "Напишите необходимое количество кв. метров плитки! (Только цифра)")
            bot.register_next_step_handler(mesg, cen_k)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="nazad2_inline":
            markup=telebot.types.InlineKeyboardMarkup(row_width=2)
            b1=telebot.types.InlineKeyboardButton("Назад ⬅️", callback_data="nazad1_inline")
            b2=telebot.types.InlineKeyboardButton("Далее ➡️", callback_data="rsc_inline")
            markup.add(b1, b2)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, """
Отлично!
Чат бот для вашего бизнеса будет полезен ✅
""", reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="dalee2_inline":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup=telebot.types.InlineKeyboardMarkup(row_width=1)
            bURL=telebot.types.InlineKeyboardButton("Ссылка", url="https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D1%81%D0%BE%D0%B1%D0%B5%D1%81%D0%B5%D0%B4%D0%BD%D0%B8%D0%BA")
            b2=telebot.types.InlineKeyboardButton("Далее ➡️", callback_data="dalee3_inline")
            markup.add(bURL, b2)
            bot.send_message(call.message.chat.id, """Также, чат-бот может перенаправить вашего клиента в соц. сети бренда, на сайт с информацией или маркетплейс с вашим товаром!
Как пример, сейчас я перевожу вас на сайт с дополнительной информацией про чат-ботов!""", reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="dalee3_inline":
            
            markup=telebot.types.InlineKeyboardMarkup(row_width=1)
            b1=telebot.types.InlineKeyboardButton("Назад ⬅️", callback_data="nazad4_inline")
            b2=telebot.types.InlineKeyboardButton("Отправить заявку 📤", callback_data="send_inline")
            markup.add(b1, b2)
            bot.send_message(call.message.chat.id, """
<b>СЕЙЧАС ДЕЙСТВУЕТ СКИДКА 20% НА ЗАКАЗ ТЕЛЕЛЕГРАМ ЧАТ-БОТА! 🔥 </b>

В стоимость чат-бота входит:
ПОЛНАЯ разработка чат бота! ‼️
Поддержка бота в течении <b> МЕСЯЦА </b> после покупки! 💥
Учтение <b>ВСЕХ</b> ваших просьб! 👾
Быстрая разработка вашего бота! ✅
Низкая цена! 🔥
Выгрузка на <b>платный</b> хостинг! 💵
""", reply_markup=markup, parse_mode="HTML")
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="nazad4_inline":
            bot.send_message(call.message.chat.id, """
Пример, как чат-бот может расчитать предварительную стоимость товара:
                             


Допустим, ваш магазин продает плитку для пола
                         
<b> Все ниже УСЛОВНО ‼️ </b>
                         
<b>Одна упаковка - 1.5 квадратных метра
Цена одной упаковки - 2250 рублей
Покупателю нужно ? квадратных метров плитки </b>
                             
Ваш чат-бот сможет расчитать, сколько клиенту нужно упаковок плитки
и на какую сумму
""", parse_mode="HTML")
            mesg = bot.send_message(call.message.chat.id, "Напишите необходимое количество кв. метров плитки! (Только цифра)")
            bot.register_next_step_handler(mesg, cen_k)
#---------------------------------------------------------------------------------------------------------------------------
#===========================================================================================================================
#===========================================================================================================================
        if call.data=="send_inline":
            def send(message):
                global id, user_name
                id=message.chat.id
                com = message.text
                user_name=message.from_user.username
                if user_name==None:
                    user_name=""
                    user_name="❌Отсутствует телеграм тег❌"
                else:
                    user_name="@" + user_name
                markup=telebot.types.InlineKeyboardMarkup(row_width=1)
                b1=telebot.types.InlineKeyboardButton("Одобрить ✅", callback_data="odob_inline")
                b2=telebot.types.InlineKeyboardButton("Отправить свои данные ✅", callback_data="odobs_inline")
                b3=telebot.types.InlineKeyboardButton("Отказать ❌", callback_data="otkaz_inline")
                markup.add(b1, b2, b3)
                bot.send_message(1950291574, f"""Вам была отправлена заявка от {user_name} c комментарием '{com}'
chat id пользователя - {id}""", reply_markup=markup, parse_mode="HTML")
            
            bot.delete_message(call.message.chat.id, call.message.message_id)
            mesg = bot.send_message(call.message.chat.id, "Отлично!\nОставьте свой комментарий к заявке ниже! 💬")
            bot.register_next_step_handler(mesg, send)
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="odob_inline":
            def odob():
                bot.delete_message(call.message.chat.id, call.message.message_id)
                global id, user_name
                
                if user_name=="❌Отсутствует телеграм тег❌":
                    bot.send_message(chat_id=id, text=f"""Ваша заявка была одобрена! ✅
Напишите в личные сообщения - @Impuls_Mironov 🔥""")
                    bot.send_message(1950291574, "Ожидайте ответа от пользователя в личных сообщениях‼️")
                else:
                    bot.send_message(chat_id=id, text=f"""Ваша заявка была одобрена! ✅
В ближайшее время с вами свяжутся в личных сообщениях!""")
                    markup=telebot.types.InlineKeyboardMarkup(row_width=1)
                    b1=telebot.types.InlineKeyboardButton("➕", callback_data="plus_inline")
                    markup.add(b1)
                    bot.send_message(1950291574, f"{user_name}", reply_markup=markup)
            odob()
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="odobs_inline":
            def odobs():
                bot.delete_message(call.message.chat.id, call.message.message_id)
                global id, user_name
                bot.send_message(chat_id=id, text=f"""Ваша заявка была одобрена! ✅
Напишите в личные сообщения - @Impuls_Mironov 🔥""")
                bot.send_message(1950291574, "Ожидайте ответа от пользователя в личных сообщениях‼️")
                markup=telebot.types.InlineKeyboardMarkup(row_width=1)
                b1=telebot.types.InlineKeyboardButton("➕", callback_data="plus_inline")
                markup.add(b1)
                bot.send_message(1950291574, f"{user_name}", reply_markup=markup)
            odobs()
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="otkaz_inline":
            def otkaz():
                bot.delete_message(call.message.chat.id, call.message.message_id)
                global id, user_name
                bot.send_message(chat_id=id, text=f"""К сожалению, по неизвестным причинам
вам был октаз в заявка ❌
Попробуйте подать заявку позже ^_^""")
            otkaz()
#---------------------------------------------------------------------------------------------------------------------------
        if call.data=="plus_inline":
            bot.delete_message(call.message.chat.id, call.message.message_id)
#---------------------------------------------------------------------------------------------------------------------------
#===========================================================================================================================
#===========================================================================================================================

        def rassilka():
            def mesras(mes):
                global rasmes
                markup=telebot.types.InlineKeyboardMarkup(row_width=1)
                b1=telebot.types.InlineKeyboardButton("Начать рассылку 📤", callback_data="nachras_unline")
                markup.add(b1)

                rasmes=mes.text
                bot.send_message(call.message.chat.id, "Новое сообщение для рассылки: " + rasmes, reply_markup=markup)

            if call.data=="creatmesras_inline":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                mesg = bot.send_message(call.message.chat.id, "Напишите новое сообщение для рассылки!")
                bot.register_next_step_handler(mesg, mesras)

            def sas():
                global rasmes

                bot.send_message(call.message.chat.id, """Рассылка началась!

    Сообщение рассылки:""")

                with sqlite3.connect('mainid.db') as db:
                    cursor = db.cursor()
                    cursor.execute(f""" SELECT id FROM mine """)
                    i = 0
                    n = 0
                    ress=[]
                while True:
                    try:
                        for res in cursor:
                            bot.send_message(chat_id = res[0], text = rasmes)
                            i += 1

                        break

                    except:
                        n += 1
                        ress.append(res)
                bot.send_message(1950291574, f"""                    
    Всего было отправлено сообщений: {i}

    Не было отправлено сообщений: {n}

    Всего пользователей в базе: {n + i}

    Айди чатов, которым не отправилось сообщение:
    {str(ress)}
    """)


            if call.data=="nachras_unline":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                sas()

        rassilka()
            
#===========================================================================================================================
#===========================================================================================================================


@bot.message_handler(func=lambda m:True)
def dialog(mes):
    if True:
        if mes.chat.id == 6765931514:
            bot.send_sticker(6765931514, sticker="CAACAgIAAxkBAAENsP1nnoVrRDHNYcWDcTp-j3JG4CtJbgACHBYAAojh2Uu1T-m8nBSIOzYE")
        aaa=mes.text
        ab=mes.chat.id
        if ab==6765931514:
            ab="Лерочка (6765931514)"
        elif ab==1950291574:
            ab="Создатель (1950291574)"
        elif ab==6972484444:
            ab=="Степа (6972484444)"
        time=mes.date
        ms=f"message: '{str(aaa)}', chat.id: {str(ab)}, time: {tconv(time)}"
        with open('LogMes.txt', 'a', encoding="UTF-8") as file:
            print(ms, file=file)


bot.infinity_polling()