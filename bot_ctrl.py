import config
import datetime
import telebot
from keyboards import kb

bot = telebot.TeleBot(config.token)


def date():
	d_t = datetime.datetime.now()
	return d_t.strftime('%d-%m-%Y, %H:%M')
	

def bot_run():
	bot.send_message(chat_id=config.admin_id, text='Бот успешно запущен, \nдля начала работы нажмите /start')
	print('Бот запущен -', date())
	bot.infinity_polling()
	

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Основное меню', reply_markup=kb.start_menu)

calc_result = ''
@bot.callback_query_handler(func=lambda call: call.data == 'rat')
def rational_calc(call):
	print(call)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Рациональные числа")
	#bot.edit_message_text(call.message.message_id, 'Рациональные числа')
	bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.rat_menu)
	#if call.data == 
