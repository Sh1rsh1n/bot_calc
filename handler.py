import config
import datetime
import telebot
from keyboards import kb
from models import rational_calc as rc
from models import complex_calc as cc


bot = telebot.TeleBot(config.token)
first_arg = ''
second_arg = ''
result = ''


# дата, для логирования
def date():
	d_t = datetime.datetime.now()
	return d_t.strftime('%d-%m-%Y, %H:%M')
	
# запуск бота
def bot_run():
	bot.send_message(chat_id=config.admin_id, text='Бот успешно запущен, \nдля начала работы нажмите /start')
	print('Бот запущен -', date())
	# сохранение состояния для register_next_step_handler()
	bot.enable_save_next_step_handlers(delay=2)
	bot.load_next_step_handlers()

	bot.infinity_polling()
	


# стартовое меню бота
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Основное меню', reply_markup=kb.start_menu)

######################################################################
######################################################################
# обработка нажатия кнопки 'рациональные числа'
@bot.callback_query_handler(func=lambda call: call.data == 'rat')
def show_rational_menu(call):
	bot.send_message(call.message.chat.id, "Вы выбрали рациональные числа")
	msg = bot.send_message(call.message.chat.id, 'Введите первое число')
	bot.register_next_step_handler(msg, first_num)

######## методы для обработки ввода значений в чате #################
def first_num(message):
	global first_arg
	first_arg = message.text
	msg = bot.send_message(message.chat.id, 'Введите второе число')
	bot.register_next_step_handler(msg, second_num)

def second_num(message):
	global second_arg
	second_arg = message.text
	bot.send_message(message.chat.id, 'Какое действие нужно выполнить?', reply_markup=kb.rat_menu)
######################################################################


# обработка нажатия кнопок выбора действий(сложение/вычитание/умножение/деление)
rat_list = ['sum', 'sub', 'mult', 'div', 'back_s']
@bot.callback_query_handler(func=lambda call: call.data in rat_list)
def rational_calc(call):
	global result, first_arg, second_arg
	
	# Проверка корректности ввода значения
	if not first_arg.isdigit() or not second_arg.isdigit():
			bot.send_message(call.message.chat.id, f'Вводить нужно только цифры. Попробуй еще раз.', reply_markup=kb.start_menu)
	else:
		if call.data == 'sum':
			result = rc.sum(first_arg, second_arg)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'sub':
			result = rc.sub(first_arg, second_arg)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'mult':
			result = rc.mult(first_arg, second_arg)
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		if call.data == 'div':
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.rat_div_menu)
		if call.data == 'back_s':
			first_arg = None
			second_arg = None
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.start_menu)
			


div_list = ['div_reg', 'div_rem', 'div_int', 'back_r']
@bot.callback_query_handler(func=lambda call: call.data in div_list)
def div_calc(call):
	global result, first_arg, second_arg
	if not int(second_arg):
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
			bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.rat_menu)
######################################################################
######################################################################

######################################################################
######################################################################

############## Комплексные числа ################
first_real = ''
first_imag = ''
second_real = ''
second_imag = ''

@bot.callback_query_handler(func=lambda call: call.data == 'comp')
def show_complex_menu(call):
	bot.send_message(call.message.chat.id, "Вы выбрали комплексные числа")
	msg = bot.send_message(call.message.chat.id, 'Введите первое действительное число')
	bot.register_next_step_handler(msg, real_num_first)


############## Обработка ввода комплексных чисел ##############
def real_num_first(message):
	global first_real
	first_real = message.text
	msg = bot.send_message(message.chat.id, 'Введите первое мнимое число')
	bot.register_next_step_handler(msg, imag_num_first)

def imag_num_first(message):
	global first_imag
	first_imag = message.text
	msg = bot.send_message(message.chat.id, 'Введите второе действительное число')
	bot.register_next_step_handler(msg, real_num_second)

def real_num_second(message):
	global second_real
	second_real = message.text
	msg = bot.send_message(message.chat.id, 'Введите второе мнимое число')
	bot.register_next_step_handler(msg, imag_num_second)

def imag_num_second(message):
	global second_imag
	second_imag = message.text
	bot.send_message(message.chat.id, 'Какое действие нужно выполнить?', reply_markup=kb.comp_menu)

######################################################################
cmd_list_c = ['sum_c', 'sub_c', 'mult_c', 'div_c', 'back_s']
@bot.callback_query_handler(func=lambda call: call.data in cmd_list_c)
def complex_calc(call):
	print('complex calc')
	global result, first_real, first_imag, second_real, second_imag
	
	
	print((first_real.isdigit and first_imag.isdigit and second_real.isdigit and second_imag.isdigit), first_real,
	first_imag, second_real, second_imag)
	
	
	if first_real.isdigit and first_imag.isdigit and second_real.isdigit and second_imag.isdigit:
		if call.data == 'sum_с':
			result = cc.cal_compl(first_real, first_imag, second_real, second_imag, '+')
			bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
			bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
		
	else:
		bot.send_message(call.message.chat.id, f'Вводить нужно только цифры. Попробуй еще раз.', reply_markup=kb.start_menu)
		
		
# просто эхо-ответ для всех остальных сообщений
@bot.message_handler(content_types=['text'])
def echo(message):
	bot.send_message(message.chat.id, message.message_id.text)
