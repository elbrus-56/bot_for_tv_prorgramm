import requests
import misc
import json
from search import *


token = misc.token
url = "https://api.telegram.org/bot" + token + "/"
LAST_UPDATE_ID = 0


def get_updates():
	return requests.get(url + "getUpdates").json()


def get_messages():
	data = get_updates()
	last_object = data["result"][-1]
	cur_update_id = last_object["update_id"]
	global LAST_UPDATE_ID
	if LAST_UPDATE_ID != cur_update_id:
		LAST_UPDATE_ID = cur_update_id
		chat_id = last_object["message"]["chat"]["id"]
		msg_txt = last_object["message"]["text"]
		message = {"chat_id": chat_id,
				"text": msg_txt }
		return message
	return None


def send_messages(chat_id, text="Вывести весь список ТВ каналов (Да/Нет): "):
	return requests.get(url + f"sendMessage?chat_id={chat_id}&text={text}")


def main():
    d = get_updates()
	# with open("get_updates.json", "w") as file:
		# json.dump(d, file, indent = 2, ensure_ascii=False)

    while True:
        answer = get_messages()
        data = get_updates()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer["text"]
            lst = list_channel()
            last_object = data["result"][-2]["message"]["text"]
        
            if text == "Да":
                send_messages(chat_id, lst)

            elif text in list_channel():
                send_messages(chat_id, text="Введите время")

            elif text:
                send_messages(chat_id, search_program(last_object, text))
            else:
                continue
		
	
if __name__ == "__main__":
	main()

