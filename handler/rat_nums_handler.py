import config
import datetime
import telebot
from keyboards import kb
from models import rational_calc as rc
import bot_ctrl as bc

bot = telebot.TeleBot(config.token)

def first_num(message):
	global bc.first_arg
	bc.first_arg = message.text
	msg = bot.send_message(message.chat.id, 'Введите второе число')
	bot.register_next_step_handler(msg, second_num)

def second_num(message):
	global bc.second_arg
	bc.second_arg = message.text
	bot.send_message(message.chat.id, 'Какое действие нужно выполнить?', reply_markup=kb.rat_menu)
