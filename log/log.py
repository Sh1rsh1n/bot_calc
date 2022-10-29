from datetime import datetime as dt


# логирование ошибочного ввода данных пользователем
def input_logger(call, text):
	time = dt.now().strftime('%d-%m-%Y, %H:%M:%S')
	with open('log.txt', 'a', encoding='utf-8') as file:
		file.write(f'TIME: {time}, ID :{call.from_user.id}, FIRST NAME: {call.from_user.first_name}, LAST NAME: {call.from_user.last_name}, ACTION: {call.text} TEXT: {text} \n')
		

def callback_logger(call, text):
	time = dt.now().strftime('%d-%m-%Y, %H:%M:%S')
	with open('log.txt', 'a', encoding='utf-8') as file:
		file.write(f'TIME: {time}, ID :{call.from_user.id}, FIRST NAME: {call.from_user.first_name}, LAST NAME: {call.from_user.last_name}, ACTION: {call.data} TEXT: {text} \n')

'''
# логирование выбранной операции
def oper_logger(call):
	time = dt.now().strftime('%d-%m-%Y, %H:%M')
	with open('log.txt', 'a', encoding='utf-8') as file:
		file.write(f'{time} - Выбранная операция: {data})


#data(), "- id", call.from_user.id, call.from_user.first_name, call.from_user.last_name, "-", text'''
