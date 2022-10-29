import config
import datetime
import telebot
from keyboards import kb
from models import rational_calc as rc
from models import complex_calc as cc
from log import log


bot = telebot.TeleBot(config.token)
first_arg = ''
second_arg = ''
result = ''

	
# запуск бота
def bot_run():
	print('Бот запущен')
	# сохранение состояния для register_next_step_handler()
	bot.enable_save_next_step_handlers(delay=2)
	bot.load_next_step_handlers()

	bot.infinity_polling()
	


# стартовое меню бота
@bot.message_handler(commands=['start'])
def start(message):
	log.input_logger(message, 'Основное меню')	# запись в лог выбора меню
	bot.send_message(message.chat.id, 'Основное меню', reply_markup=kb.start_menu)

######################################################################
# обработка нажатия кнопки 'рациональные числа'
@bot.callback_query_handler(func=lambda call: call.data == 'rat')
def show_rational_menu(call):
	log.callback_logger(call, 'рациональные числа') # запись в лог нажатия кнопки
	bot.send_message(call.message.chat.id, "Вы выбрали рациональные числа")
	msg = bot.send_message(call.message.chat.id, 'Введите первое число')
	bot.register_next_step_handler(msg, first_num) # запрос ввода первого значения

######## методы для обработки ввода значений в чате #################
def first_num(message):
	log.input_logger(message, 'первое число')	# запись в лог первого значения
	global first_arg
	first_arg = message.text # присвоили глобальной переменной первое значение
	msg = bot.send_message(message.chat.id, 'Введите второе число')
	bot.register_next_step_handler(msg, second_num)	# запрос ввода второго значения

def second_num(message):
	log.input_logger(message, 'второе число')	# запись в лог первого значения
	global second_arg	
	second_arg = message.text	# присвоили глобальной переменной второе значение
	bot.send_message(message.chat.id, 'Какое действие нужно выполнить?', reply_markup=kb.rat_menu) # вызов меню действий с рациональными числами
######################################################################


# обработка нажатия кнопок выбора действий(сложение/вычитание/умножение/деление)
rat_list = ['sum', 'sub', 'mult', 'div', 'back_s']
@bot.callback_query_handler(func=lambda call: call.data in rat_list)
def rational_calc(call):
	log.callback_logger(call, 'меню выбора действий с рациональными числами')	# запись в лог нажатия кнопки
	global result, first_arg, second_arg
	
	# Проверка корректности ввода значения
	if not first_arg.isdigit() or not second_arg.isdigit():
		log.callback_logger(call, 'Ошибка ввода значений, некорректный ввод.') # запись в лог ошибки
		bot.send_message(call.message.chat.id, f'Вводить нужно только цифры. Попробуй еще раз.', reply_markup=kb.start_menu) # возврат в основное меню
	else:
		if call.data == 'sum':
			log.callback_logger(call, 'Выбрано дествие "Сложение"')
			result = rc.sum(first_arg, second_arg)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'sub':
			log.callback_logger(call, 'Выбрано дествие "Вычитание"')
			result = rc.sub(first_arg, second_arg)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'mult':
			log.callback_logger(call, 'Выбрано дествие "Умножение"')
			result = rc.mult(first_arg, second_arg)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'div':
			log.callback_logger(call, 'Выбрано дествие "Деление"')
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.rat_div_menu)
		if call.data == 'back_s':
			log.callback_logger(call, 'Выбрано дествие "Возврат в основное меню"')
			first_arg = None
			second_arg = None
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.start_menu)
			

# обработка нажатия кнопок выбора действий деления двух чисел
div_list = ['div_reg', 'div_rem', 'div_int', 'back_r']
@bot.callback_query_handler(func=lambda call: call.data in div_list)
def div_calc(call):
	log.callback_logger(call, 'меню выбора действий деления')	# запись в лог нажатия кнопки
	global result, first_arg, second_arg
	if not int(second_arg):
		log.callback_logger(call, 'Ошибка деления на ноль')	# запись в лог ошибки
		bot.send_message(call.message.chat.id, f'На ноль делить нельзя. Попробуй еще раз.', reply_markup=kb.start_menu)
	else:
		if call.data == 'div_reg':
			result = rc.div(first_arg, second_arg, 1)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'div_int':
			result = rc.div(first_arg, second_arg, 2)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'div_rem':
			result = rc.div(first_arg, second_arg, 3)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'back_r':
			log.callback_logger(call, 'Выбрано дествие "Возврат в меню выбор действий"')
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.rat_menu)
######################################################################

######################################################################

############## Комплексные числа ################
first_real = ''
first_imag = ''
second_real = ''
second_imag = ''

# обработка нажатия кнопки 'комплексные числа'
@bot.callback_query_handler(func=lambda call: call.data == 'comp')
def show_complex_menu(call):
	log.callback_logger(call, 'меню выбора действий с комплексными числами')	# запись в лог нажатия кнопки
	bot.send_message(call.message.chat.id, "Вы выбрали комплексные числа")  
	msg = bot.send_message(call.message.chat.id, 'Введите первое действительное число')
	bot.register_next_step_handler(msg, real_num_first) # запрос ввода первого действительного значения 


############## Обработка ввода комплексных чисел ##############
def real_num_first(message):
	global first_real
	log.input_logger(message, 'первое действительное число')	# запись в лог первого действительное значения
	first_real = message.text	# присвоили глобальной переменной входящее значение 
	msg = bot.send_message(message.chat.id, 'Введите первое мнимое число')
	bot.register_next_step_handler(msg, imag_num_first)	# запрос ввода первого мнимого значения

def imag_num_first(message):
	log.input_logger(message, 'первое мнимое число')	# запись в лог первого мнимого значения
	global first_imag
	first_imag = message.text	# присвоили глобальной переменной входящее значение 
	msg = bot.send_message(message.chat.id, 'Введите второе действительное число')
	bot.register_next_step_handler(msg, real_num_second)	# запрос ввода второго действительного значения

def real_num_second(message):
	log.input_logger(message, 'второе действительное число')	# запись в лог второго действительного значения
	global second_real
	second_real = message.text	# присвоили глобальной переменной входящее значение 
	msg = bot.send_message(message.chat.id, 'Введите второе мнимое число')
	bot.register_next_step_handler(msg, imag_num_second)	# запрос ввода второго мнимого значения

def imag_num_second(message):
	log.input_logger(message, 'второе мнимое число')	# запись в лог виорого мнимого значения
	global second_imag
	second_imag = message.text	# присвоили глобальной переменной входящее значение 
	bot.send_message(message.chat.id, 'Какое действие нужно выполнить?', reply_markup=kb.comp_menu)
######################################################################

# обработка нажатия кнопок выбора действий(сложение/вычитание/умножение/деление)
comp_list = ['sum_co', 'sub_co', 'mult_co', 'div_co', 'back_c']
@bot.callback_query_handler(func=lambda call: call.data in comp_list)
def complex_calc(call):
	log.callback_logger(call, 'меню выбора действий с комплексными числами')	# запись в лог нажатия кнопки
	global result, first_real, first_imag, second_real, second_imag
	
	# Проверка корректности ввода значения
	if not first_real.isdigit or not first_imag.isdigit or not second_real.isdigit or not second_imag.isdigit:
		log.callback_logger(call, 'Ошибка ввода значений, некорректный ввод.') # запись в лог ошибки
		bot.send_message(call.message.chat.id, f'Вводить нужно только цифры. Попробуй еще раз.', reply_markup=kb.start_menu)
	else:
		if call.data == 'sum_co':
			log.callback_logger(call, 'Выбрано дествие "Сложение"')
			result = cc.cal_compl(first_real, first_imag, second_real, second_imag, '+')
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'sub_co':
			log.callback_logger(call, 'Выбрано дествие "Вычитание"')
			result = cc.cal_compl(first_real, first_imag, second_real, second_imag, '-')
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'mult_co':
			log.callback_logger(call, 'Выбрано дествие "Умножение"')
			result = cc.cal_compl(first_real, first_imag, second_real, second_imag, '*')
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'div_co':
			if not int(second_real) and not int(second_imag):
				log.callback_logger(call, 'Ошибка деления на ноль')	# запись в лог ошибки
				bot.send_message(call.message.chat.id, f'На ноль делить нельзя. Попробуй еще раз.',
								 reply_markup=kb.start_menu)
			else:
				log.callback_logger(call, 'Выбрано дествие "Деление"')
				result = cc.cal_compl(first_real, first_imag, second_real, second_imag, '/')
				bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
				bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'back_c':	# возврат в главное меню
			log.callback_logger(call, 'Выбрано дествие "Возврат в основное меню"')
			first_real = None
			first_imag = None
			second_real = None
			second_imag = None
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.start_menu)
	
		
			
				
					

	
	'''global result, first_real, first_imag, second_real, second_imag
	
	if first_real.isdigit and first_imag.isdigit and second_real.isdigit and second_imag.isdigit:
		if call.data == 'sum_с':
			result = cc.cal_compl(first_real, first_imag, second_real, second_imag, '+')
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		
	else:
		bot.send_message(call.message.chat.id, f'Вводить нужно только цифры. Попробуй еще раз.', reply_markup=kb.start_menu)'''
		
		
# просто эхо-ответ для всех остальных сообщений
@bot.message_handler(content_types=['text'])
def echo(message):
	bot.send_message(message.chat.id, message.message_id.text)
