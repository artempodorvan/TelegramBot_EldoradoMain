from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import telebot
import time
from selenium import webdriver
from bs4 import BeautifulSoup

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

url = 'https://epicentrk.ua/'

chrome_options = Options()
chrome_options.add_argument("--headless")

user_wants_filters = None
topic = None

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Привіт я бот для пошуку різноманітної техніки для пошуку введіть "/search"')

@bot.message_handler(commands=['no'])
def filter_choice_handler(message):
    global user_wants_filters

    bot.send_message(message.chat.id, "Тепер ви можете отримати техніку без фільтрів")
    user_wants_filters = False
    bot.send_message(message.chat.id, "Виберіть категорію техніки знову через команду '/search'")

@bot.message_handler(commands=['yes'])
def filter_choice_handler(message):
    global user_wants_filters

    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Дешево', callback_data='cheap')
    btn2 = telebot.types.InlineKeyboardButton('Дорого', callback_data='expensive')
    markup.row(btn1, btn2)
    btn3 = telebot.types.InlineKeyboardButton('Акції', callback_data='discount')
    markup.row(btn3)
    btn4 = telebot.types.InlineKeyboardButton('Новинки', callback_data='news')
    btn5 = telebot.types.InlineKeyboardButton('Популярні', callback_data='famouse')
    markup.row(btn4, btn5)

    bot.send_message(message.chat.id, 'Виберіть', reply_markup=markup)

    bot.send_message(message.chat.id, "Тепер ви можете отримати техніку з фільтрами")
    user_wants_filters = True
    bot.send_message(message.chat.id, "Виберіть фільтр")

@bot.message_handler(commands=['search'])
def search_command(message):
    bot.send_message(message.chat.id, 'Гаразд, зараз виберіть, що ви шукаєте')
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Ноутбуки', callback_data='laptop')
    btn2 = telebot.types.InlineKeyboardButton('Пральні машини', callback_data='washing_machine')
    markup.row(btn1, btn2)
    btn3 = telebot.types.InlineKeyboardButton('Холодильники', callback_data='fridge')
    markup.row(btn3)
    btn4 = telebot.types.InlineKeyboardButton('Телевізори', callback_data='tv')
    btn5 = telebot.types.InlineKeyboardButton('Пелососи', callback_data='wacum')
    markup.row(btn4, btn5)
    btn6 = telebot.types.InlineKeyboardButton('Телефони', callback_data='phone')
    markup.row(btn6)
    bot.send_message(message.chat.id, 'Виберіть', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_handler(callback):
    chat_id = callback.message.chat.id
    data = callback.data
    global user_wants_filters
    global topic

    bot.send_message(chat_id, "Виберіть чи вам потрібні фльтри '/yes' or '/no' якщо ти вибрав то просто чекай")

    if data == 'laptop':
        try:
            if user_wants_filters == False:
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
                time.sleep(4)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("ноутбуки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(2)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')

                    info1 = soup.find_all('span', class_='font-weight-700 nc')

                    for info in info1:
                        bot.send_message(chat_id, info.text)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'cheap':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("ноутбуки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="asc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'expensive':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("ноутбуки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="desc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'news':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("ноутбуки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="aktsii"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'famouse':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("ноутбуки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="new"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'discount':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("ноутбуки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="rating"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

        except Exception as e:
            bot.send_message(chat_id, f"помилка{e}")

    if data == 'washing_machine':
        try:
            if user_wants_filters == False:
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
                time.sleep(4)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пральні машинки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(2)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')

                    info1 = soup.find_all('span', class_='font-weight-700 nc')

                    for info in info1:
                        bot.send_message(chat_id, info.text)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'cheap':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пральні машинки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="asc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'expensive':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пральні машинки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="desc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'news':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пральні машинки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="aktsii"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'famouse':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пральні машинки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="new"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'discount':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пральні машинки")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="rating"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

        except Exception as e:
            bot.send_message(chat_id, f"помилка{e}")

    if data == 'fridge':
        try:
            if user_wants_filters == False:
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
                time.sleep(4)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("холодильники")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(2)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')

                    info1 = soup.find_all('span', class_='font-weight-700 nc')

                    for info in info1:
                        bot.send_message(chat_id, info.text)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'cheap':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("холодильники")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="asc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'expensive':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("холодильники")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="desc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'news':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("холодильники")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="aktsii"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'famouse':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("холодильники")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="new"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'discount':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("холодильники")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="rating"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

        except Exception as e:
            bot.send_message(chat_id, f"помилка{e}")

    if data == 'phone':
        try:
            if user_wants_filters == False:
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
                time.sleep(4)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("телефони")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(2)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')

                    info1 = soup.find_all('span', class_='font-weight-700 nc')

                    for info in info1:
                        bot.send_message(chat_id, info.text)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'cheap':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("телефони")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="asc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'expensive':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("телефони")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="desc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'news':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("телефони")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="aktsii"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'famouse':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("телефони")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="new"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'discount':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("телефони")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="rating"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

        except Exception as e:
            bot.send_message(chat_id, f"помилка{e}")

    if data == 'wacum':
        try:
            if user_wants_filters == False:
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
                time.sleep(4)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пелесоси")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(2)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')

                    info1 = soup.find_all('span', class_='font-weight-700 nc')

                    for info in info1:
                        bot.send_message(chat_id, info.text)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'cheap':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пелесоси")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="asc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'expensive':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пелесоси")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="desc"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'news':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пелесоси")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="aktsii"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'famouse':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пелесоси")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="new"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

            elif user_wants_filters is True and topic == 'discount':
                driver = webdriver.Chrome()
                driver.get(url)
                time.sleep(2)
                input_field = driver.find_element(by='css selector', value='input[class="_JcImSJ"]')

                if input_field:
                    input_field.send_keys("пелесоси")
                    time.sleep(2)
                    input_field.send_keys(Keys.RETURN)
                    time.sleep(4)
                    # тут ми отримуємо лінк з поточної сторінки де ми зараз
                    html = driver.page_source

                    soup = BeautifulSoup(html, 'html.parser')
                    a = driver.find_element(by='css selector', value='a[data-href="rating"]')
                    a.click()
                    time.sleep(2)

                    spans1 = soup.find_all(
                        'span', class_='font-weight-700 nc'
                    )

                    for span1 in spans1:
                        bot.send_message(chat_id, span1.text)
                        time.sleep(0.2)

                    driver.quit()
                    topic = None
                    user_wants_filters = None

        except Exception as e:
            bot.send_message(chat_id, f"помилка{e}")

# here we have current filters for our product
    elif data == 'cheap':
        topic = 'cheap'
        bot.send_message(chat_id, 'Будь ласка, виберіть повторно свій пристрій та чекайте на пропозиції')

    elif data == 'expensive':
        topic = 'expensive'
        bot.send_message(chat_id, 'Будь ласка, виберіть повторно свій пристрій та чекайте на пропозиції')

    elif data == 'news':
        topic = 'news'
        bot.send_message(chat_id, 'Будь ласка, виберіть повторно свій пристрій та чекайте на пропозиції')

    elif data == 'discount':
        topic = 'discount'
        bot.send_message(chat_id, 'Будь ласка, виберіть повторно свій пристрій та чекайте на пропозиції')

    elif data == 'famouse':
        topic = 'famouse'
        bot.send_message(chat_id, 'Будь ласка, виберіть повторно свій пристрій та чекайте на пропозиції')

bot.polling(none_stop=True)
