import telebot
import sqlite3 as sql
import csv
TOKEN = '7187394462:AAF4UoOskarpbjt9ScAFrS4zecX5lSiO1TU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_message(message):
    con = sql.connect('ForName.db')
    cur = con.cursor()
    cur.execute('''create table if not exists student 
                     (
                     Id integer primary key autoincrement,
                     F text,
                     I text,
                     O text,
                     _group integer references _groups (Id)
                     );''')
    cur.execute('''create table if not exists _groups 
                     (
                     Id integer primary key autoincrement,
                     Number text
                     );''')

    with open('Data/students.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=' ')
        for i in reader:
            if i['F'] and i['I'] and i['O'] and i['_group']:
                cur.execute('''insert into student (F,I,O,_group) values ((?),(?),(?),(?))''',
                            (i['F'], i['I'], i['O'], i['_group']))
    with open('Data/_groups.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=' ')
        for i in reader:
            if i['Number']:
                cur.execute('''insert into _groups (Number) values ((?))''', (i['Number'],))
    #bot.send_message(message.from_user.id,'Введите фамилию студента:')
    cur.execute('''select F,I,O,(select Number from _groups where Id = _group ) from student''')
    result = cur.fetchall()
    F = 0
    f = ''
    I = ''
    o = ''
    group = ''
    for i in result:
        if message.text in i[0]:
            F = 1
            f = i[0]
            I = i[1]
            o = i[2]
            group = i[3]
            break

    if F == 1:
        bot.send_message(message.from_user.id,'Студент(ка) ' + f + ' ' + I + ' ' + o + ' обучается в ' + group + ' группе')
    else:
        bot.send_message(message.from_user.id,'Студента(ки) с фамилией ' + message.text + ' нет в списке')
    con.close()
bot.polling(none_stop=True, interval=0)


