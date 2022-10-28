from telebot import types

# кнопки выбора режима калькулятора
rat_nums = types.InlineKeyboardButton(text="Рациональные числа", callback_data="rat")
comp_nums = types.InlineKeyboardButton(text="Комплексные числа", callback_data="comp")

# кнопка возврата в предыдущее меню
back_start_menu = types.InlineKeyboardButton(text="назад", callback_data="back_s")
back_rat_menu = types.InlineKeyboardButton(text="назад", callback_data="back_r")
back_comp_menu = types.InlineKeyboardButton(text="назад", callback_data="back_c")

# кнопки выбора вычислений для рациональных чисел
sum = types.InlineKeyboardButton(text=f"Сложение", callback_data="sum")
sub = types.InlineKeyboardButton(text=f"Вычитание", callback_data="sub")
mult = types.InlineKeyboardButton(text=f"Умножение", callback_data="mult")
div = types.InlineKeyboardButton(text=f"Деление", callback_data="div")
div_reg = types.InlineKeyboardButton(text=f"Обычное деление", callback_data="div_reg")
div_rem = types.InlineKeyboardButton(text=f"Остаток", callback_data="div_rem")
div_int = types.InlineKeyboardButton(text=f"Целочисленное деление", callback_data="div_int")

# кнопки выбора вычислений для комплексных чисел
sum_co = types.InlineKeyboardButton(text=f"Сложение", callback_data="sum_co")
sub_co = types.InlineKeyboardButton(text=f"Вычитание", callback_data="sub_co")
mult_co = types.InlineKeyboardButton(text=f"Умножение", callback_data="mult_co")
div_co = types.InlineKeyboardButton(text=f"Деление", callback_data="div_co")

# стартовое меню
start_menu = types.InlineKeyboardMarkup(row_width=2)
start_menu.add(rat_nums, comp_nums)

# меню вычислений с рациональными числами
rat_menu = types.InlineKeyboardMarkup(row_width=2)
rat_menu.add(sum, sub)
rat_menu.add(mult, div)
rat_menu.add(back_start_menu)
# меню деления
rat_div_menu = types.InlineKeyboardMarkup(row_width=2)
rat_div_menu.add(div_reg, div_rem, div_int)
rat_div_menu.add(back_rat_menu)

# меню вычислений с комплексными чиселами
comp_menu = types.InlineKeyboardMarkup(row_width=2)
comp_menu.add(sum_co, sub_co)
comp_menu.add(mult_co, div_co)
comp_menu.add(back_comp_menu)
