from bs4 import BeautifulSoup
import re
import json

# передаем объект открытого файла
with open("tv.html", 'r') as fp:
    doc = fp.read()
    # Редактируем для удобства работы, добавляем div ко всем <p id="">
    pt = r'<p id="'
    add_div = re.sub(pt, '</div><div class="channel"><p id="', doc)
    soup = BeautifulSoup(add_div, 'html5lib')


# Ищем div, которые добавил выше
all_channel = soup.find_all("div", class_="channel")
# print(all_channel)

json_tv_channel = {}


# Ищем назавание каналов <p> для заголовков и расписание программ <li>
for item in all_channel:
    names_channel = item.find_all("p", {"id": re.compile(r"(\d+.*)")})
    dirty_list_tv_show = item.find_all("li")
    dic = {}

    # Чистим строки, делим их на 2 части: "время показа : название программы"
    for p in dirty_list_tv_show:
        search_time = re.findall(r"(\d\d\.\d\d)\s", p.text)
        name_tv_show_1 = re.sub(r"(\d\d\.\d\d)\s", "", p.text)
        name_tv_show = re.sub(r"(Фильм)[\.\s]|(Фильм)", "Фильм. ", name_tv_show_1).rstrip("\n")
        
    # обрабатываем ошибку "List out range", с чем связана непонятно
        try:
            dic[search_time[0]] = name_tv_show # Добавляем значения во временный словарь dict
        except IndexError:
            "wrong"

    # Добавляем значения в конечный словарь json_tv
    for channel in names_channel:
        # print(channel.text.lower())
        json_tv_channel[channel.text.lower()] = dic
# print(json_tv)

# передаем данные в json файл
# with open('data.json', 'w') as fp:
    # json.dump(json_tv_channel, fp, indent=2, ensure_ascii=False)





    
    
    








