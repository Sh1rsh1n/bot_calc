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
sum_c = types.InlineKeyboardButton(text=f"Сложение", callback_data="sum_c")
sub_c = types.InlineKeyboardButton(text=f"Вычитание", callback_data="sub_c")
mult_c = types.InlineKeyboardButton(text=f"Умножение", callback_data="mult_c")
div_c = types.InlineKeyboardButton(text=f"Деление", callback_data="div_c")
div_reg_c = types.InlineKeyboardButton(text=f"Обычное деление", callback_data="div_reg_c")
div_rem_c = types.InlineKeyboardButton(text=f"Остаток", callback_data="div_rem_c")
div_int_c = types.InlineKeyboardButton(text=f"Целочисленное деление", callback_data="div_int_c")


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
comp_menu.add(sum_с, sub_с)
comp_menu.add(mult_с, div_с)
comp_menu.add(back_start_menu)
# меню деления
comp_div_menu = types.InlineKeyboardMarkup(row_width=2)
comp_div_menu.add(div_reg_с, div_rem_с, div_int_с)
comp_div_menu.add(back_comp_menu)
