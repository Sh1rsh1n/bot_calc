from telebot import types

# кнопки выбора режима калькулятора
rat_nums = types.InlineKeyboardButton(text="Рациональные числа", callback_data="rat")
comp_nums = types.InlineKeyboardButton(text="Комплексные числа", callback_data="comp")

# кнопки выбора вычислений
sum = types.InlineKeyboardButton(text="+", callback_data="sum")
sub = types.InlineKeyboardButton(text="-", callback_data="sub")
mult = types.InlineKeyboardButton(text="*", callback_data="mult")
exp = types.InlineKeyboardButton(text="^", callback_data="div_reg")
div_reg = types.InlineKeyboardButton(text="/", callback_data="div_reg")
div_rem = types.InlineKeyboardButton(text="%", callback_data="div_rem")
div_int = types.InlineKeyboardButton(text="//", callback_data="div_int")

# стартовое меню
start_menu = types.InlineKeyboardMarkup(row_width=2)
start_menu.add(rat_nums, comp_nums)

# меню вычислений с рациональными числами
rat_menu = types.InlineKeyboardMarkup(row_width=5)
rat_menu.add(sum, sub)
rat_menu.add(mult, exp)
rat_menu.add(div_reg)
rat_menu.add(div_rem)
rat_menu.add(div_int)

# меню вычислений с комплексными чиселами
comp_menu = types.InlineKeyboardMarkup(row_width=5)
comp_menu.add(sum, sub)
comp_menu.add(mult, exp)
comp_menu.add(div_reg)
comp_menu.add(div_rem)
comp_menu.add(div_int)
