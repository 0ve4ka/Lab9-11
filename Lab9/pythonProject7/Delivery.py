import sqlite3 as sql3
import csv

con = sql3.connect('Test.db')

cur = con.cursor()

cur.execute('''create table if not exists Client (
Id_Client integer primary key autoincrement,
FIO text
);''')

with open('Data/DataClient.csv','r',encoding='utf-8',newline='') as file:
    Reader = csv.DictReader(file,delimiter=',')
    for i in Reader:
        if i['FIO']:
            cur.execute('''insert into Client (FIO) values ((?))''',(i['FIO'],))

with open('Export/Client.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['FIO'])
    for i in cur.execute('''select FIO from Client'''):
        writer.writerow(i)



print('Client')
cur.execute('''select * from Client''')
result_Select = cur.fetchall()
print(result_Select)

cur.execute('''create table if not exists Agent (
Id_Agent integer primary key autoincrement,
N integer,
FIO text
);''')

with open('Data/DataAgent.csv','r',encoding='utf-8',newline='') as file:
    Reader = csv.DictReader(file,delimiter=',')
    for i in Reader:
        if i['N'] and i['FIO']:
            cur.execute('''insert into Agent (N,FIO) values ((?),(?))''',(i['N'],i['FIO']))

with open('Export/Agent.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['N','FIO'])
    for i in cur.execute('''select N,FIO from Agent'''):
        writer.writerow(i)

print('Agent')
cur.execute('''select * from Agent''')
result_Select = cur.fetchall()
print(result_Select)

cur.execute('''create table if not exists Product (
Id_Product integer primary key autoincrement,
Name text,
Id_Agent integer references Agent(Id_Agent),
Count integer,
Id_Client integer references Client(Id_Client)
);''')

with open('Data/DataProduct.csv','r',encoding='utf-8',newline='') as file:
    Reader = csv.DictReader(file,delimiter=',')
    for i in Reader:
        if i['Name'] and i['Id_Agent'] and i['Count'] and i['Id_Client']:
            cur.execute('''insert into Product (Name,Id_Agent,Count,Id_Client) values ((?),(?),(?),(?))''',(i['Name'],i['Id_Agent'],i['Count'],i['Id_Client']))

with open('Export/Product.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Id_Agent','Count','Id_Client'])
    for i in cur.execute('''select Name,Id_Agent,Count,Id_Client from Product'''):
        writer.writerow(i)

print('Product')
cur.execute('''select * from Product''')
result_Select = cur.fetchall()
print(result_Select)

cur.execute('''create table if not exists Worker (
Id_Worker integer primary key autoincrement,
FIO text
);''')

with open('Data/DataWorker.csv','r',encoding='utf-8',newline='') as file:
    Reader = csv.DictReader(file,delimiter=',')
    for i in Reader:
        if i['FIO']:
            cur.execute('''insert into Worker (FIO) values ((?))''',(i['FIO'],))

with open('Export/Worker.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['FIO'])
    for i in cur.execute('''select FIO from Worker'''):
        writer.writerow(i)

print('Worker')
cur.execute('''select * from Worker''')
result_Select = cur.fetchall()
print(result_Select)

cur.execute('''create table if not exists Orders (
Id_Order integer primary key autoincrement,
Date_Time text,
Id_Agent integer references Agent(Id_Agent),
Id_Client integer references Client(Id_Client),
Count integer,
Id_Worker integer references Worker(Id_Worker)
);''')

with open('Data/DataOrders.csv','r',encoding='utf-8',newline='') as file:
    Reader = csv.DictReader(file,delimiter=',')
    for i in Reader:
        if i['Date_Time'] and i['Id_Agent'] and i['Id_Client'] and i['Count'] and i['Id_Worker']:
            cur.execute('''insert into Orders (Date_Time,Id_Agent,Id_Client,Count,Id_Worker) values ((?),(?),(?),(?),(?))''',(i['Date_Time'],i['Id_Agent'],i['Id_Client'],i['Count'],i['Id_Worker']))

with open('Export/Orders.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date_Time','Id_Agent','Id_Client','Count','Id_Worker'])
    for i in cur.execute('''select Date_Time,Id_Agent,Id_Client,Count,Id_Worker from Orders'''):
        writer.writerow(i)

print('Orders')
cur.execute('''select * from Orders''')
result_Select = cur.fetchall()
print(result_Select)


