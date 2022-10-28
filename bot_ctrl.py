import config
import datetime
import telebot
from keyboards import kb
from models import model_sum, model_div, model_sub, model_mult

bot = telebot.TeleBot(config.token)


def date():
	d_t = datetime.datetime.now()
	return d_t.strftime('%d-%m-%Y, %H:%M')
	

def bot_run():
	bot.send_message(chat_id=config.admin_id, text='Бот успешно запущен, \nдля начала работы нажмите /start')
	print('Бот запущен -', date())
	bot.enable_save_next_step_handlers(delay=2)
	bot.load_next_step_handlers()
	bot.infinity_polling()
	

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Основное меню', reply_markup=kb.start_menu)

first_arg = None
second_arg = None
result = None

@bot.callback_query_handler(func=lambda call: call.data == 'rat')
def show_rational_menu(call):
	bot.send_message(call.message.chat.id, "Вы выбрали рациональные числа")
	msg = bot.send_message(call.message.chat.id, 'Введите первое число')
	bot.register_next_step_handler(msg, first_num)

def first_num(message):
	global first_arg
	first_arg = message.text
	msg = bot.send_message(message.chat.id, 'Введите второе число')
	bot.register_next_step_handler(msg, second_num)

def second_num(message):
	global second_arg
	second_arg = message.text
	bot.send_message(message.chat.id, 'Какое действие нужно выполнить?', reply_markup=kb.rat_menu)


cmd_list = ['sum', 'sub', 'mult', 'div_reg', 'div_rem', 'div_int']
@bot.callback_query_handler(func=lambda call: call.data in cmd_list)
def rational_calc(call):
	global result, first_arg, second_arg
	if call.data == 'sum':
		result = model_sum.get_sum(first_arg, second_arg)
		bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
		bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
	if call.data == 'sub':
		result = model_sub.get_sub(first_arg, second_arg)
		bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
		bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
	if call.data == 'mult':
		result = model_mult.get_mult(first_arg, second_arg)
		bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
		bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
	if call.data == 'div_reg':
		result = model_div.get_div(first_arg, second_arg, 1)
		bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
		bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
	if call.data == 'div_int':
		result = model_div.get_div(first_arg, second_arg, 2)
		bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
		bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)
	if call.data == 'div_rem':
		result = model_div.get_div(first_arg, second_arg, 3)
		bot.send_message(call.message.chat.id, f'Результат вычислений = {result}')
		bot.send_message(call.message.chat.id, f'Что еще счетаем?', reply_markup=kb.start_menu)

