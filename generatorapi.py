from random import choice, shuffle

def _template_gen(length, charset, equal_count, template, default_template_key):
    password_for_template = _gen(length, charset, equal_count)
    res = ''
    j = 0
    for template_key in template:
        if template_key == default_template_key:
            res += password_for_template[j]
            j += 1
        else:
            res += template_key
    return res

#функция, отвечающая за то, чтобы рандомизировать порядок символов в строке
def _remake(unsorted_password):
    char_list = list(unsorted_password)
    shuffle(char_list)
    unsorted_password = ''.join(char_list)
    return unsorted_password

#функция, необходимая для генерации пароля (на вход мы получаем длинну пароля, массив символов из которых состоит пароль и переменную, от которой зависит будет ли количество этих символов равно или нет)
def _gen(length, symbols, equal_count):
    if len(symbols) == 1: #если переменная equal_count была передана случайно, то мы убираем ее для оптимизации
        equal_count = False
    if equal_count: #если надо сделать равное количество различных символов
        count_of_symbols = len(symbols)
        res = ''
        j = 0
        #в этом цикле мы генерируем строку по образцу "c1, c2, c3, c1, c2...", где c - это символ а после "перемешиваем" ее
        for i in range(length):
            res += choice(symbols[j])
            j += 1
            if j >= count_of_symbols:
                j = 0
        return _remake(res)
    else: #если на количество разных символов без разницы
        symbols = ''.join(symbols)
        res = ''
        for i in range(length):
            res += choice(symbols)
        return res


def generate(length, numbers=True, lower_letters=True, upper_letters=True, schars=True, equal_count=False, user_chars='', default_template_key='x', template='', count=1):
    #проверка на то есть ли у нас символы из которых можно составить пароль
    if not (numbers or lower_letters or upper_letters or schars) and (user_chars == ''):
        return('no arguments')
    #проверка того правильно ли введены данные
    if (count < 1) or (length < 1) or (not isinstance(count, int)) or (not isinstance(length, int)):
        return('wrong argument')
    if (template != ''):
        if (default_template_key not in template):
            return('wrong template')
        template_key_count = template.count(default_template_key)
        if (template_key_count != length):
            length = template_key_count
    charset = []
    #создаем массив из которого потом будем брать символы для пароля
    if numbers:
        charset.append('1234567890')
    if lower_letters or upper_letters:
        letters_is_used = ''
        if lower_letters:
            letters_is_used += 'qwertyuiopasdfghjklzxcvbnm'
        if upper_letters:
            letters_is_used += 'QWERTYUIOPASDFGHJKLZXCVBNM'
        charset.append(letters_is_used)
    if schars:
        charset.append('!@#$%^&*()_+=-?:;№".,/|<>')
    if user_chars != '':
        charset.append(user_chars)
    #если нам необходимо сделать одну генерацию
    if count == 1:
        if template == '':
            return _gen(length, charset, equal_count)
        else:
            return _template_gen(length, charset, equal_count, template, default_template_key)
    #если необходимо сделать больше, чем одну генерацию
    elif count > 1:
        res_m = []
        if template == '':
            for j in range(count):
                res_m.append(_gen(length, charset, equal_count))
            return res_m
        else:
            for j in range(count):
                res_m.append(_template_gen(length, charset, equal_count, template, default_template_key))
            return res_m