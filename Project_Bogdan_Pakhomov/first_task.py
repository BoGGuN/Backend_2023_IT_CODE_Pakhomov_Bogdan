def function_1(day, month, year):
    """Принимает 3 числа и выводит формат ДД+ММ'а/я'+ГГ 'года'"""
    month_name = 'Декабря'
    if month == 1:
        month_name = 'Января'
    elif month == 2:
        month_name = 'Февраля'
    elif month == 3:
        month_name = 'Марта'
    elif month == 4:
        month_name = 'Апреля'
    elif month == 5:
        month_name = 'Мая'
    elif month == 6:
        month_name = 'Июня'
    elif month == 7:
        month_name = 'Июля'
    elif month == 8:
        month_name = 'Августа'
    elif month == 9:
        month_name = 'Сентября'
    elif month == 10:
        month_name = 'Октября'
    elif month == 11:
        month_name = 'Ноября'
    return f'{day} {month_name.lower()} {year} года'


print('-----------Первая задача-----------')
print(function_1(2, 12, 2023))


def function_2(tupler):
    """Принимает кортеж имён и должна вернуть словарь
    с именем и количеством этого имени в кортеже"""
    name_dict = {}
    for i in tupler:
        if name_dict.get(i) is None:
            name_dict[i] = 1
        else:
            name_dict[i] += 1
    return name_dict


print('-----------Вторая задача-----------')
print(function_2(('Олег', 'Оля', 'Вася', 'Олег', 'Олег', 'Вася', 'Коля')))


def function_3(dicter):
    """Проверяет все 4 кейса, которые выводят что-то, если нет,
    то в конце выводится Нет данных"""
    if 'first_name' in dicter and 'last_name' in dicter and 'middle_name' in dicter:
        return f'{dicter["last_name"]} {dicter["first_name"]} {dicter["middle_name"]}'
    elif 'first_name' in dicter and 'last_name' not in dicter and 'middle_name' in dicter:
        return f'{dicter["first_name"]} {dicter["middle_name"]}'
    elif 'first_name' in dicter and 'last_name' in dicter and 'middle_name' not in dicter:
        return f'{dicter["last_name"]} {dicter["first_name"]}'
    elif 'first_name' not in dicter and 'last_name' in dicter and 'middle_name' in dicter:
        return f'{dicter["last_name"]}'
    else:
        return 'Нет данных'


print('-----------Третья задача-----------')
print(function_3({'middle_name': 'Дмитриевич', 'last_name': 'Пахомов', 'first_name': 'Богдан'}))
print(function_3({'last_name': 'Пахомов', 'first_name': 'Богдан'}))
print(function_3({'middle_name': 'Дмитриевич', 'last_name': 'Пахомов'}))
print(function_3({'middle_name': 'Дмитриевич', 'first_name': 'Богдан'}))
print(function_3({'first_name': 'Богдан'}))
print(function_3({'middle_name': 'Дмитриевич'}))
print(function_3({'last_name': 'Пахомов'}))


def function_4(number):
    """Аргумент переводится в модуль и
    переменная is_complex определяет, сложное ли число,
    сначала проверяется равно ли число 0 или 1, эти числа сложные
    потом если нет, то выполняется цикл от 0 до аргумента,
    если i=0 или 1, то итерация пропускается, дальше проверяется,
     делится ли каждое число на number без остатка"""
    number = abs(number)
    is_complex = False
    if number == 0 or number == 1:
        is_complex = True
    else:
        for i in range(number):
            if i == 0 or i == 1:
                continue
            elif number % i == 0:
                is_complex = True
    return not is_complex


print('-----------Четвёртая задача-----------')
print(f'Простое число {12}? - {function_4(12)}')
print(f'Простое число {7}? - {function_4(7)}')
print(f'Простое число {2029}? - {function_4(2029)}')
print(f'Простое число {0}? - {function_4(0)}')
print(f'Простое число {1}? - {function_4(1)}')
print(f'Простое число {2}? - {function_4(2)}')
print(f'Простое число {-1}? - {function_4(-1)}')


def function_5(*args):
    """Создаётся лист аргументов, добавляются аргументы,
    которые целые и с плавающей точной, и не являющиеся True(1) и False(0),
    которые являются по сути числами, потом массив изменяется сортировкой,
    в отличие от .sort(), которое только возвращает значение, но не изменяет"""
    arg_list = []
    for i in args:
        if isinstance(i, (int, float)) and not isinstance(i, bool):
            arg_list.append(i)
    return sorted(arg_list)


print('-----------Пятая задача-----------')
print(function_5(1, 'text', 2, 15, 3, False, (1, 3, True), [1, False, 2]))
