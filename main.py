import json

with open('data.json', 'r') as fp:
    data = json.load(fp)

lch = input("Вывести весь список ТВ программ(Да/Нет): ")
def list_channel(lch):
    lch = lch.lower()
    if lch == "да":
        for key in data.keys():
            yield key
        return None
for k in list_channel(lch):
    print(k.title())

ch = input("Введите название ТВ канала: ")
t = input("Введите время показа: ")
def tv_program(ch, t):
    channel = data[ch]
    time = channel[t]
    return time

print(tv_program(ch,t))