import sqlite3 as sql
import csv
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
with open('Data/students.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=' ')
    for i in reader:
        if i['F'] and i['I'] and i['O'] and i['_group']:
            cur.execute('''insert into student (F,I,O,_group) values ((?),(?),(?),(?))''',(i['F'], i['I'], i['O'], i['_group']))

cur.execute('''create table if not exists _groups 
                     (
                     Id integer primary key autoincrement,
                     Number text
                     );''')
with open('Data/_groups.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=' ')
    for i in reader:
        if i['Number']:
            cur.execute('''insert into _groups (Number) values ((?))''', (i['Number'],))

con.commit()
print('Введите фамилию студента:')
user_input = input()


cur.execute('''select F,I,O,(select Number from _groups where Id = _group ) from student''')
result = cur.fetchall()
for i in result:
    if user_input in i[0]:
        print('Студент ' + i[0] + ' ' + i[1] + ' ' + i[2] + ' обучается в ' + i[3] + ' группе')
        break

