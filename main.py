import json
import datetime

with open('data.json', 'r') as fp:
    data = json.load(fp)


# Выводим список всех ТВ каналов
lch = input("Вывести весь список ТВ каналов (Да/Нет): ")
def list_channel(lch):
    lch = lch.lower()
    if lch == "да":
        for key in data.keys():
            yield key
    else:
        None
for k in list_channel(lch):
    print(k.title())

# Функция, которая ищет ТВ программу, по заданному времени
ch = input("Введите название ТВ канала: ")
t = input("Введите время показа: ")

def search_programm(ch, t):
    new_t = datetime.datetime.strptime(t, '%H.%M').time()
    ch = ch.lower()
    mlist = []

    for k in data[ch]:
        mlist.append(k)

    i = 0
    while True:
        if datetime.datetime.strptime(mlist[i], '%H.%M').time() <= new_t < datetime.datetime.strptime(mlist[i+1], '%H.%M').time():
            return data[ch][mlist[i]]

        elif new_t == datetime.datetime.strptime(mlist[i+1], '%H.%M').time():
            return print(data[ch][mlist[i+1]])

        else:
            i += 1
    
print(search_programm(ch, t))
