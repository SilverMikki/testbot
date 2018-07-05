import requests
import misc
import json


token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()

def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
		
	message = { 'chat_id': chat_id,
				'text': message_text }
	
	return message

def send_message(chat_id, text = 'Wait a second, please. . .'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)
	
def main():
	answer = get_message()
	chat_id = answer['chat_id']
	text = answer['text']
	
	if 'Привет' in text:
		send_message(chat_id, 'Здарова')
	#d = get_updates()
	
	#with open('updates.json', 'w') as file:
	#	json.dump(d, file, indent = 2, ensure_ascii = False)

if __name__ == '__main__':
	main()
	
