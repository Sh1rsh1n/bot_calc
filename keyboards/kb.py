from telebot import types

# кнопки выбора режима калькулятора
rat_nums = types.InlineKeyboardButton(text="Рациональные числа", callback_data="rat")
comp_nums = types.InlineKeyboardButton(text="Комплексные числа", callback_data="comp")

# кнопки выбора вычислений
sum = types.InlineKeyboardButton(text=f"Сложение", callback_data="sum")
sub = types.InlineKeyboardButton(text=f"Вычитание", callback_data="sub")
mult = types.InlineKeyboardButton(text=f"Умножение", callback_data="mult")
div_reg = types.InlineKeyboardButton(text=f"Обычное деление", callback_data="div_reg")
div_rem = types.InlineKeyboardButton(text=f"Остаток", callback_data="div_rem")
div_int = types.InlineKeyboardButton(text=f"Целочисленное деление", callback_data="div_int")

# стартовое меню
start_menu = types.InlineKeyboardMarkup(row_width=2)
start_menu.add(rat_nums, comp_nums)

# меню вычислений с рациональными числами
rat_menu = types.InlineKeyboardMarkup(row_width=3)
rat_menu.add(sum, sub)
rat_menu.add(mult, div_reg)
rat_menu.add(div_rem, div_int)

# меню вычислений с комплексными чиселами
comp_menu = types.InlineKeyboardMarkup(row_width=3)
comp_menu.add(sum, sub)
comp_menu.add(mult, div_reg)
comp_menu.add(div_rem, div_int)