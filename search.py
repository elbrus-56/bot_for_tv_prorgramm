import json
import datetime

with open('data.json', 'r') as fp:
    data = json.load(fp)

def list_channel():
    lch = []
    for key in data.keys():
        lch.append(key)
    return lch

def search_program(ch, t):
    new_t = datetime.datetime.strptime(t, '%H.%M').time()
    ch = ch.lower()
    mlist = []

    for k in data[ch]:
        mlist.append(k)

    i = 0
    while True:
        if datetime.datetime.strptime(mlist[i], '%H.%M').time() <= new_t < datetime.datetime.strptime(mlist[i+1], '%H.%M').time():
            return f"Сейчас в эфире: {data[ch][mlist[i]]}"

        elif new_t == datetime.datetime.strptime(mlist[i+1], '%H.%M').time():
            return f"Сейчас в эфире: {data[ch][mlist[i]]}"

        else:
            i += 1
            




