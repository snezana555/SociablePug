import telebot
from telebot import types
import sqlite3
bot = telebot.TeleBot('6060536100:AAGHX4tNaLUqDzQ3x2of_6pAMyVIWGYGzJE')
levels = ['знакомы', 'вроде дружим', 'точно дружим', 'что-то большее чем друзья', 'мы с тобой будет вечно вместе']
conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()
def db_table_val(id: int, level: str, points: int):
	cursor.execute('INSERT INTO users (id, level, points) VALUES (?, ?, ?)', (id, level, points))
	conn.commit()

def btn(message):
    user = conn.execute(f'SELECT * FROM users WHERE id ={message.from_user.id}').fetchone()
    markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = []
    if user[1] == levels[0]:
        buttons = ["Погулять (+ 1 очко)", "Покормить (+ 2 очка)", "Статус", "Перейти на новый уровень"]
    elif user[1] == levels[1]:
        buttons = ["Погулять (+ 1 очко)", "Покормить (+ 2 очка)", "Дрессировать (+ 3 очка)", "Статус",
                   "Перейти на новый уровень"]
    elif user[1] == levels[2]:
        buttons = ["Погулять (+ 1 очко)", "Покормить (+ 2 очка)", "Дрессировать (+ 3 очка)",
                   "Почесать за ушком (+ 3 очка)", "Статус", "Перейти на новый уровень"]
    elif user[1] == levels[3]:
        buttons = ["Погулять (+ 1 очко)", "Покормить (+ 2 очка)", "Дрессировать (+ 3 очка)",
                   "Почесать за ушком (+ 3 очка)", "Поспать рядом (+ 4 очка)", "Статус", "Перейти на новый уровень"]
    elif user[1] == levels[4]:
        buttons = ["Погулять (+ 1 очко)", "Покормить (+ 2 очка)", "Дрессировать (+ 3 очка)",
                   "Почесать за ушком (+ 3 очка)", "Поспать рядом (+ 4 очка)", "Поговорить по душам (+ 4 очка)",
                   "Статус", "Перейти на новый уровень"]
    markup_2.add(*buttons)
    return markup_2


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('Дружить')
    markup.add(start)
    bot.send_message(message.chat.id, "Привет, я Федя, будем дружить?", reply_markup=markup)
    user = conn.execute(f'SELECT * FROM users WHERE id ={message.from_user.id}').fetchone()
    if user is None:
        db_table_val(id=message.from_user.id, level=levels[0], points=0)
@bot.message_handler(content_types=['text'])
def index(message):
    user = conn.execute(f'SELECT * FROM users WHERE id ={message.from_user.id}').fetchone()
    if message.text == 'Дружить':
        markup_2 = btn(message)
        bot.send_photo(message.chat.id, photo="https://sun9-63.userapi.com/impg/Pwk7oyZqGHf63iKSnQ3nAWq0UNOXFrhcAUZwEg/uokDDKvejZM.jpg?size=600x800&quality=96&sign=1c62416e7ec3a79565dc8702be100f21&type=album")
        bot.send_message(message.chat.id, 'Привет, чем займёмся?', reply_markup=markup_2)

    if message.text == 'Погулять (+ 1 очко)':
        points = user[2] + 1
        cursor.execute(f"UPDATE users SET points = {points} WHERE id = {message.from_user.id} ")
        conn.commit()
        bot.send_photo(message.chat.id, photo="https://sun9-73.userapi.com/impg/pr_7EEy117mncz8ZBn1ub147ONDhHQheErBl6w/S7dRy5rHTH0.jpg?size=810x1080&quality=96&sign=65b7128e7a5c0c32d4ad7ce876d321a6&type=album")
        bot.send_message(message.chat.id, 'эх, хорошо погуляли')
    elif message.text == 'Покормить (+ 2 очка)':
        points = user[2] + 2
        cursor.execute(f"UPDATE users SET points = {points} WHERE id = {message.from_user.id} ")
        conn.commit()
        bot.send_photo(message.chat.id, photo="https://sun9-77.userapi.com/impg/bBsGqgDgQkDsQjibI63Oc5ugkY3vAjPBH6LubA/-M5Jl7Ifcb8.jpg?size=1280x960&quality=96&sign=08f202c8bff095c74e0fa8fbdc9af9f7&type=album")
        bot.send_message(message.chat.id, 'очень вкусно, спасибо')
    elif message.text == 'Дрессировать (+ 3 очка)':
        points = user[2] + 3
        cursor.execute(f"UPDATE users SET points = {points} WHERE id = {message.from_user.id} ")
        conn.commit()
        bot.send_photo(message.chat.id, photo="https://sun9-80.userapi.com/impg/IsLb6weAwN_Wo8dd-FjpSg-706I7VIikKUKHyg/uJjDzuyLxsI.jpg?size=509x1080&quality=96&sign=7308cb324bf8b3b7282bde87071d55e5&type=album")
        bot.send_message(message.chat.id, 'фух, устал')
    elif message.text == 'Почесать за ушком (+ 3 очка)':
        points = user[2] + 3
        cursor.execute(f"UPDATE users SET points = {points} WHERE id = {message.from_user.id} ")
        conn.commit()
        bot.send_photo(message.chat.id,photo="https://sun9-24.userapi.com/impg/Jy1bGYKip6E0ruhEbfRyNECwS9v7Shfq38sPcg/vu4n0dbntj8.jpg?size=1280x960&quality=96&sign=2a3584b2d6b884cb17492b6a290fd5b3&type=album")
        bot.send_message(message.chat.id, 'хехе, хорошо то как')
    elif message.text == 'Поспать рядом (+ 4 очка)':
        points = user[2] + 4
        cursor.execute(f"UPDATE users SET points = {points} WHERE id = {message.from_user.id} ")
        conn.commit()
        bot.send_photo(message.chat.id, photo="https://sun9-1.userapi.com/impg/ZXilAOxqBaZIECxpHzbFK_e1Wjglz5NPltSgMw/BTE4i5X9oWA.jpg?size=1280x960&quality=96&sign=d00d96a7dceb5d6d8a99204a35c9b318&type=album")
        bot.send_message(message.chat.id, 'zzzzzzzzzzzz')
    elif message.text == 'Поговорить по душам (+ 4 очка)':
        points = user[2] + 4
        cursor.execute(f"UPDATE users SET points = {points} WHERE id = {message.from_user.id} ")
        conn.commit()
        bot.send_photo(message.chat.id, photo="https://sun1-91.userapi.com/impg/ygaK1SjXoqWTXzVTncede6ynBG4ldBfafxY9Rw/VZRrpZO8pHA.jpg?size=810x1080&quality=96&sign=cab8447c0d21a6e7e5a16503492ed6d9&type=album")
        bot.send_message(message.chat.id, 'я тебя понимаю')
    elif message.text == 'Статус':
        bot.send_message(message.chat.id, f'Ваш уровень: {user[1]}, \n Ваши очки: {user[2]}')


    if message.text == 'Перейти на новый уровень':
        markup_2 = btn(message)
        if user[2] > 0 and user[2] <= 10:
            cursor.execute(f"UPDATE users SET level = '{levels[1]}' WHERE id = {message.from_user.id} ")
            conn.commit()
            bot.send_message(message.chat.id, f'Ваш уровень: {levels[1]}', reply_markup=markup_2)
        elif user[2] > 10 and user[2] <= 20:
            cursor.execute(f"UPDATE users SET level = '{levels[2]}' WHERE id = {message.from_user.id} ")
            conn.commit()
            bot.send_message(message.chat.id, f'Ваш уровень: {levels[2]}', reply_markup=markup_2)
        elif user[2] > 20  and user[2] <= 30:
            cursor.execute(f"UPDATE users SET level = '{levels[3]}' WHERE id = {message.from_user.id} ")
            conn.commit()
            bot.send_message(message.chat.id, f'Ваш уровень: {levels[3]}', reply_markup=markup_2)
        elif user[2] > 30 and user[2] <= 50:
            cursor.execute(f"UPDATE users SET level = '{levels[4]}' WHERE id = {message.from_user.id} ")
            conn.commit()
            bot.send_message(message.chat.id, f'Ваш уровень: {levels[4]}', reply_markup=markup_2)
        else:
            bot.send_message(message.chat.id, 'Покормите его ещё')

bot.polling(none_stop=True, interval=0)